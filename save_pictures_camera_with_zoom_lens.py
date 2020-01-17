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
import sorting_robot
import os
# ---------------------------------------------------------------------------------------------------------------------------------------

IMG_SAVE_PATH = 'dataset/image_data_better_camera'
REV_CLASS_MAP = {
    0: "m59557-10",
    1: "m59557-16",
    2: "m59557-20",
    3: "nas1802-3-6",
    4: "nas1802-3-7",
    5: "nas1802-3-8",
    6: "nas1802-3-9",
    7: "nas1802-4-07",
    8: "nas6305-10",
    9: "v647p23b",
    10: "none"
}
bolt_type = REV_CLASS_MAP[1]
num_samples = 100
count = 0
# Connect to robot & machine
# rob = sorting_robot.Robot()
machine = sorting_robot.SortingMachine()

# Calculate robot coordinates
# pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train = rob.get_waypoints()

# Set save path
count, num_samples, IMG_CLASS_PATH = machine.save_pictures(IMG_SAVE_PATH, bolt_type, num_samples)

# Variables
hCam = ueye.HIDS( 1 )           # 0: first available camera;  1-254: The camera with the specified camera ID
sInfo = ueye.SENSORINFO()
cInfo = ueye.CAMINFO()
pcImageMemory = ueye.c_mem_p()
MemID = ueye.int()
rectAOI = ueye.IS_RECT()
pitch = ueye.INT()
nBitsPerPixel = ueye.INT( 24 )  # 24: bits per pixel for color mode; take 8 bits per pixel for monochrome
channels = 3                    # 3: channels for color mode(RGB); take 1 channel for monochrome
m_nColorMode = ueye.INT()       # Y8/RGB16/RGB24/REG32
bytes_per_pixel = int( nBitsPerPixel / 8 )
# ---------------------------------------------------------------------------------------------------------------------------------------
print( "START" )
print()

# Starts the driver and establishes the connection to the camera
nRet = ueye.is_InitCamera( hCam, None )
if nRet != ueye.IS_SUCCESS:
    print( "is_InitCamera ERROR" )

# Reads out the data hard-coded in the non-volatile camera memory and writes it to the data structure that cInfo
# points to
nRet = ueye.is_GetCameraInfo( hCam, cInfo )
if nRet != ueye.IS_SUCCESS:
    print( "is_GetCameraInfo ERROR" )

# You can query additional information about the sensor type used in the camera
nRet = ueye.is_GetSensorInfo( hCam, sInfo )
if nRet != ueye.IS_SUCCESS:
    print( "is_GetSensorInfo ERROR" )

nRet = ueye.is_ResetToDefault( hCam )
if nRet != ueye.IS_SUCCESS:
    print( "is_ResetToDefault ERROR" )

# Set display mode to DIB
nRet = ueye.is_SetDisplayMode( hCam, ueye.IS_SET_DM_DIB )

# Set the right color mode
if int.from_bytes( sInfo.nColorMode.value, byteorder='big' ) == ueye.IS_COLORMODE_BAYER:
    # setup the color depth to the current windows setting
    ueye.is_GetColorDepth( hCam, nBitsPerPixel, m_nColorMode )
    bytes_per_pixel = int( nBitsPerPixel / 8 )
    print( "IS_COLORMODE_BAYER: ", )
    print( "\tm_nColorMode: \t\t", m_nColorMode )
    print( "\tnBitsPerPixel: \t\t", nBitsPerPixel )
    print( "\tbytes_per_pixel: \t\t", bytes_per_pixel )
    print()

elif int.from_bytes( sInfo.nColorMode.value, byteorder='big' ) == ueye.IS_COLORMODE_CBYCRY:
    # for color camera models use RGB32 mode
    m_nColorMode = ueye.IS_CM_BGRA8_PACKED
    nBitsPerPixel = ueye.INT( 32 )
    bytes_per_pixel = int( nBitsPerPixel / 8 )
    print( "IS_COLORMODE_CBYCRY: ", )
    print( "\tm_nColorMode: \t\t", m_nColorMode )
    print( "\tnBitsPerPixel: \t\t", nBitsPerPixel )
    print( "\tbytes_per_pixel: \t\t", bytes_per_pixel )
    print()

elif int.from_bytes( sInfo.nColorMode.value, byteorder='big' ) == ueye.IS_COLORMODE_MONOCHROME:
    # for color camera models use RGB32 mode
    m_nColorMode = ueye.IS_CM_MONO8
    nBitsPerPixel = ueye.INT( 8 )
    bytes_per_pixel = int( nBitsPerPixel / 8 )
    print( "IS_COLORMODE_MONOCHROME: ", )
    print( "\tm_nColorMode: \t\t", m_nColorMode )
    print( "\tnBitsPerPixel: \t\t", nBitsPerPixel )
    print( "\tbytes_per_pixel: \t\t", bytes_per_pixel )
    print()

else:
    # for monochrome camera models use Y8 mode
    m_nColorMode = ueye.IS_CM_MONO8
    nBitsPerPixel = ueye.INT( 8 )
    bytes_per_pixel = int( nBitsPerPixel / 8 )
    print( "else" )

# Can be used to set the size and position of an "area of interest"(AOI) within an image
nRet = ueye.is_AOI( hCam, ueye.IS_AOI_IMAGE_GET_AOI, rectAOI, ueye.sizeof( rectAOI ) )
if nRet != ueye.IS_SUCCESS:
    print( "is_AOI ERROR" )

width = rectAOI.s32Width
height = rectAOI.s32Height

# Prints out some information about the camera and the sensor
print( "Camera model:\t\t", sInfo.strSensorName.decode( 'utf-8' ) )
print( "Camera serial no.:\t", cInfo.SerNo.decode( 'utf-8' ) )
print( "Maximum image width:\t", width )
print( "Maximum image height:\t", height )
print()

# ---------------------------------------------------------------------------------------------------------------------------------------

# Allocates an image memory for an image having its dimensions defined by width and height and its color depth
# defined by nBitsPerPixel
nRet = ueye.is_AllocImageMem( hCam, width, height, nBitsPerPixel, pcImageMemory, MemID )
if nRet != ueye.IS_SUCCESS:
    print( "is_AllocImageMem ERROR" )
else:
    # Makes the specified image memory the active memory
    nRet = ueye.is_SetImageMem( hCam, pcImageMemory, MemID )
    if nRet != ueye.IS_SUCCESS:
        print( "is_SetImageMem ERROR" )
    else:
        # Set the desired color mode
        nRet = ueye.is_SetColorMode( hCam, m_nColorMode )

# Activates the camera's live video mode (free run mode)
nRet = ueye.is_CaptureVideo( hCam, ueye.IS_DONT_WAIT )
if nRet != ueye.IS_SUCCESS:
    print( "is_CaptureVideo ERROR" )

# Enables the queue mode for existing image memory sequences
nRet = ueye.is_InquireImageMem( hCam, pcImageMemory, MemID, width, height, nBitsPerPixel, pitch )
if nRet != ueye.IS_SUCCESS:
    print( "is_InquireImageMem ERROR" )
else:
    print( "Press q to leave the programm" )

# ---------------------------------------------------------------------------------------------------------------------------------------

# Continuous image display
while (nRet == ueye.IS_SUCCESS):

    # In order to display the image in an OpenCV window we need to...
    # ...extract the data of our image memory
    array = ueye.get_data( pcImageMemory, width, height, nBitsPerPixel, pitch, copy=False )

    # bytes_per_pixel = int(nBitsPerPixel / 8)

    # ...reshape it in an numpy array...
    frame = np.reshape( array, (height.value, width.value, bytes_per_pixel) )

    # ...resize the image by a half
    # frame = cv2.resize( frame, (0, 0), fx=0.5, fy=0.5 )

    # gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
    #
    # thresh1_L = 127
    # thresh1_H = 255
    # ret, thresh1 = cv2.threshold( gray, 127, 255, cv2.THRESH_BINARY )
    # thresh2 = cv2.threshold( gray, 127, 255, cv2.THRESH_BINARY_INV )
    # thresh3 = cv2.threshold( gray, 127, 255, cv2.THRESH_TRUNC )
    # thresh4 = cv2.threshold( gray, 127, 255, cv2.THRESH_TOZERO )
    # thresh5 = cv2.threshold( gray, 127, 255, cv2.THRESH_TOZERO_INV )
    # otsu = cv2.threshold( gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU )
    # th2 = cv2.adaptiveThreshold( gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
    #                              cv2.THRESH_BINARY, 11, 11 )
    # th3 = cv2.adaptiveThreshold( gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
    #                              cv2.THRESH_BINARY, 11, 5 )
    # kernel = np.ones( (2, 2), np.uint8 )
    # erosion = cv2.erode( th3, kernel, iterations=1 )
    # opening = cv2.morphologyEx( th3, cv2.MORPH_OPEN, kernel )
    # edges = cv2.Canny( th3, 100, 200 )

    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Include image data processing here

    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Saving images of different views
    # Remove comment for the the pictures you want to be saved

    # pathframe = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/frame'
    # paththresh1 = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Thresh1'
    # paththresh2 = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Thresh2'
    # paththresh3 = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Thresh3'
    # paththresh4 = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Thresh4'
    # paththresh5 = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Thresh5'
    # pathth2 = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Th2'
    # pathth3 = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Th3'
    # patherosion = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/erosion'
    # pathopening = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/opening'
    # pathedges = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/edges'
    # pathotsu = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Otsu'
    # pathth1 = 'D:/3D_BIN_PICKING_2D/3Dbin-picking-smr/Photos/Th1'

    # cv.imwrite(os.pathframe.join, 'Frame.jpeg', frame)
    # cv.imwrite(os.pathframe.join, 'Thresh1.jpeg', thresh1)
    # cv.imwrite(os.pathframe.join, 'Thresh2.jpeg', thresh2)
    # cv.imwrite(os.pathframe.join, 'Thresh3.jpeg', thresh3)
    # cv.imwrite(os.pathframe.join, 'Thresh4.jpeg', thresh4)
    # cv.imwrite(os.pathframe.join, 'Thresh5.jpeg', thresh5)
    # cv.imwrite(os.pathth2.join, 'Th2.jpeg', th2)
    # cv.imwrite(os.pathth3.join, 'Th3.jpeg', th3)
    # cv.imwrite(os.patherosion.join, 'Erosion.jpeg', erosion)
    # cv.imwrite(os.pathopening.join, 'Opening.jpeg', opening)
    # cv.imwrite(os.pathedges.join, 'Edges.jpeg', edges)
    # cv.imwrite(os.pathframe.join, 'Otsu.jpeg', otsu)
    # cv.imwrite(os.pathframe.join, 'Th1', th1)
    # cv.imwrite(os.pathframe.join, 'Th1', th1)

    # ...and finally display it
    cv2.imshow( "SimpleLive_Python_uEye_OpenCV", frame )
    # cv2.imshow( "SimpleLive_Python_uEye_OpenCV1", th2 )
    # cv2.imshow( "SimpleLive_Python_uEye_OpenCV2", th3 )
    # cv2.imshow( "SimpleLive_Python_uEye_OpenCV3", erosion )
    # cv2.imshow( "SimpleLive_Python_uEye_OpenCV4", opening )
    # cv2.imshow( "SimpleLive_Python_uEye_OpenCV5", edges )
    k = cv2.waitKey( 1 )
    # Press q if you want to end the loop

    if k & 0xFF == ord( 'q' ) or count >= num_samples:
        print(bytes(k))
        print('stop')
        break
    elif k & 0xFF == ord( 'a' ):
        save_path = os.path.join( IMG_CLASS_PATH, '{}.jpg'.format( count + 1 ) )
        cv2.imwrite( save_path, frame )
        print(save_path)
        count += 1

# ---------------------------------------------------------------------------------------------------------------------------------------

# Releases an image memory that was allocated using is_AllocImageMem() and removes it from the driver management
ueye.is_FreeImageMem( hCam, pcImageMemory, MemID )

# Disables the hCam camera handle and releases the data structures and memory areas taken up by the uEye camera
ueye.is_ExitCamera( hCam )

# Destroys the OpenCv windows
cv2.destroyAllWindows()

print()
print( "END" )
