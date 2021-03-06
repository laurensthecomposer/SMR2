# ===========================================================================#
#                                                                           #
#  Copyright (C) 2006 - 2018                                                #
#  IDS Imaging Development Systems GmbH                                     #
#  Dimbacher Str. 6-8                                                       #
#  D-74182 Obersulm, Germany                                                #
#                                                                           #
#  The information in this document is subject to change without notice     #
#  and should not be construed as a commitment by IDS Imaging Development   #
#  Systems GmbH. IDS Imaging Development Systems GmbH does not assume any   #
#  responsibility for any errors that may appear in this document.          #
#                                                                           #
#  This document, or source code, is provided solely as an example          #
#  of how to utilize IDS software libraries in a sample application.        #
#  IDS Imaging Development Systems GmbH does not assume any responsibility  #
#  for the use or reliability of any portion of this document or the        #
#  described software.                                                      #
#                                                                           #
#  General permission to copy or modify, but not for profit, is hereby      #
#  granted, provided that the above copyright notice is included and        #
#  reference made to the fact that reproduction privileges were granted     #
#  by IDS Imaging Development Systems GmbH.                                 #
#                                                                           #
#  IDS Imaging Development Systems GmbH cannot assume any responsibility    #
#  for the use or misuse of any portion of this software for other than     #
#  its intended diagnostic purpose in calibrating and testing IDS           #
#  manufactured cameras and software.                                       #
#                                                                           #
# ===========================================================================#

# Developer Note: I tried to let it as simple as possible.
# Therefore there are no functions asking for the newest driver software or freeing memory beforehand, etc.
# The sole purpose of this program is to show one of the simplest ways to interact with an IDS camera via the uEye API.
# (XS cameras are not supported)
# ---------------------------------------------------------------------------------------------------------------------------------------

# Libraries
from pyueye import ueye
import numpy as np
from cv2 import cv2
import sys


# ---------------------------------------------------------------------------------------------------------------------------------------

# Variables
class UeyeCameraCapture( object ):
    def __init__(self, index):
        self.hCam = ueye.HIDS( index )  # 0: first available camera;  1-254: The camera with the specified camera ID
        self.sInfo = ueye.SENSORINFO()
        self.cInfo = ueye.CAMINFO()
        self.pcImageMemory = ueye.c_mem_p()
        self.MemID = ueye.int()
        self.rectAOI = ueye.IS_RECT()
        self.pitch = ueye.INT()
        self.nBitsPerPixel = ueye.INT( 24 )  # 24: bits per pixel for color mode; take 8 bits per pixel for monochrome
        channels = 3  # 3: channels for color mode(RGB); take 1 channel for monochrome
        self.m_nColorMode = ueye.INT()  # Y8/RGB16/RGB24/REG32
        self.bytes_per_pixel = int( self.nBitsPerPixel / 8 )
        # ---------------------------------------------------------------------------------------------------------------------------------------
        # print( "START" )
        # print()

        # Starts the driver and establishes the connection to the camera
        self.nRet = ueye.is_InitCamera( self.hCam, None )
        if self.nRet != ueye.IS_SUCCESS:
            raise Exception( "is_InitCamera ERROR" )

        # Reads out the data hard-coded in the non-volatile camera memory and writes it to the data structure that self.cInfo
        # points to
        self.nRet = ueye.is_GetCameraInfo( self.hCam, self.cInfo )
        if self.nRet != ueye.IS_SUCCESS:
            raise Exception( "is_GetCameraInfo ERROR" )

        # You can query additional information about the sensor type used in the camera
        self.nRet = ueye.is_GetSensorInfo( self.hCam, self.sInfo )
        if self.nRet != ueye.IS_SUCCESS:
            raise Exception( "is_GetSensorInfo ERROR" )

        self.nRet = ueye.is_ResetToDefault( self.hCam )
        if self.nRet != ueye.IS_SUCCESS:
            raise Exception( "is_ResetToDefault ERROR" )

        # Set display mode to DIB
        self.nRet = ueye.is_SetDisplayMode( self.hCam, ueye.IS_SET_DM_DIB )

        # Set the right color mode
        if int.from_bytes( self.sInfo.nColorMode.value, byteorder='big' ) == ueye.IS_COLORMODE_BAYER:
            # setup the color depth to the current windows setting
            ueye.is_GetColorDepth( self.hCam, self.nBitsPerPixel, self.m_nColorMode )
            self.bytes_per_pixel = int( self.nBitsPerPixel / 8 )
            print( "IS_COLORMODE_BAYER: ", )
            print( "\tm_nColorMode: \t\t", self.m_nColorMode )
            print( "\tnBitsPerPixel: \t\t", self.nBitsPerPixel )
            print( "\tbytes_per_pixel: \t\t", self.bytes_per_pixel )
            print()

        elif int.from_bytes( self.sInfo.nColorMode.value, byteorder='big' ) == ueye.IS_COLORMODE_CBYCRY:
            # for color camera models use RGB32 mode
            self.m_nColorMode = ueye.IS_CM_BGRA8_PACKED
            self.nBitsPerPixel = ueye.INT( 32 )
            self.bytes_per_pixel = int( self.nBitsPerPixel / 8 )
            print( "IS_COLORMODE_CBYCRY: ", )
            print( "\tm_nColorMode: \t\t", self.m_nColorMode )
            print( "\tnBitsPerPixel: \t\t", self.nBitsPerPixel )
            print( "\tbytes_per_pixel: \t\t", self.bytes_per_pixel )
            print()

        elif int.from_bytes( self.sInfo.nColorMode.value, byteorder='big' ) == ueye.IS_COLORMODE_MONOCHROME:
            # for color camera models use RGB32 mode
            self.m_nColorMode = ueye.IS_CM_MONO8
            self.nBitsPerPixel = ueye.INT( 8 )
            self.bytes_per_pixel = int( self.nBitsPerPixel / 8 )
            print( "IS_COLORMODE_MONOCHROME: ", )
            print( "\tm_nColorMode: \t\t", self.m_nColorMode )
            print( "\tnBitsPerPixel: \t\t", self.nBitsPerPixel )
            print( "\tbytes_per_pixel: \t\t", self.bytes_per_pixel )
            print()

        else:
            # for monochrome camera models use Y8 mode
            self.m_nColorMode = ueye.IS_CM_MONO8
            self.nBitsPerPixel = ueye.INT( 8 )
            self.bytes_per_pixel = int( self.nBitsPerPixel / 8 )
            print( "else" )

        # Can be used to set the size and position of an "area of interest"(AOI) within an image
        self.nRet = ueye.is_AOI( self.hCam, ueye.IS_AOI_IMAGE_GET_AOI, self.rectAOI, ueye.sizeof( self.rectAOI ) )
        if self.nRet != ueye.IS_SUCCESS:
            raise Exception( "is_AOI ERROR" )

        self.width = self.rectAOI.s32Width
        self.height = self.rectAOI.s32Height

        # Prints out some information about the camera and the sensor
        print( "Camera model:\t\t", self.sInfo.strSensorName.decode( 'utf-8' ) )
        print( "Camera serial no.:\t", self.cInfo.SerNo.decode( 'utf-8' ) )
        print( "Maximum image width:\t", self.width )
        print( "Maximum image height:\t", self.height )
        print()

        # ---------------------------------------------------------------------------------------------------------------------------------------

        # Allocates an image memory for an image having its dimensions defined by width and height and its color depth
        # defined by nBitsPerPixel
        self.nRet = ueye.is_AllocImageMem( self.hCam, self.width, self.height, self.nBitsPerPixel, self.pcImageMemory, self.MemID )
        if self.nRet != ueye.IS_SUCCESS:
            raise Exception( "is_AllocImageMem ERROR" )
        else:
            # Makes the specified image memory the active memory
            self.nRet = ueye.is_SetImageMem( self.hCam, self.pcImageMemory, self.MemID )
            if self.nRet != ueye.IS_SUCCESS:
                raise Exception( "is_SetImageMem ERROR" )
            else:
                # Set the desired color mode
                self.nRet = ueye.is_SetColorMode( self.hCam, self.m_nColorMode )

        # Activates the camera's live video mode (free run mode)
        self.nRet = ueye.is_CaptureVideo( self.hCam, ueye.IS_DONT_WAIT )
        if self.nRet != ueye.IS_SUCCESS:
            raise Exception("is_CaptureVideo ERROR" )

        # Enables the queue mode for existing image memory sequences
        self.nRet = ueye.is_InquireImageMem( self.hCam, self.pcImageMemory, self.MemID, self.width, self.height, self.nBitsPerPixel, self.pitch )
        if self.nRet != ueye.IS_SUCCESS:
            raise Exception("is_InquireImageMem ERROR" )
        else:
            print( "Camera Connection success")
        # ---------------------------------------------------------------------------------------------------------------------------------------

    def read(self):
        # Continuous image display
        if self.nRet == ueye.IS_SUCCESS:

            # In order to display the image in an OpenCV window we need to...
            # ...extract the data of our image memory
            array = ueye.get_data( self.pcImageMemory, self.width, self.height, self.nBitsPerPixel, self.pitch, copy=False )

            # self.bytes_per_pixel = int(self.nBitsPerPixel / 8)

            # ...reshape it in an numpy array...
            frame = np.reshape( array, (self.height.value, self.width.value, self.bytes_per_pixel) )

            # ...resize the image by a half
            # frame = cv2.resize( frame, (0, 0), fx=0.5, fy=0.5 )
            return True, frame
        else:
            return False, None

    def release(self):
        # Releases an image memory that was allocated using is_AllocImageMem() and removes it from the driver management
        ueye.is_FreeImageMem( self.hCam, self.pcImageMemory, self.MemID )

        # Disables the hCam camera handle and releases the data structures and memory areas taken up by the uEye camera
        ueye.is_ExitCamera( self.hCam )

        print('Camera connection closed')

    def __del__(self):
        print('destructor called')
        self.release()

if __name__ == "__main__":

    cam = UeyeCameraCapture(1)
    import time
    time.sleep( 1 )

    while True:
        ret, frame = cam.read()
        cv2.imshow('hi', frame)
        cv2.waitKey(1)



    # Destroys the OpenCv windows
    cv2.destroyAllWindows()
    # automatically closes connection
