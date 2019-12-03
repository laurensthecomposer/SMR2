from __future__ import print_function
import sys
import cv2


def main(argv):
    # capture from camera at location 0
    camera_index = 1

    # cap = cv2.VideoCapture(camera_index)

    cap = cv2.VideoCapture( camera_index, cv2.CAP_DSHOW )
    # TODO: Remember to put size!
    # cap.set( cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc( 'M', 'J', 'P', 'G' ) )
    cap.set( cv2.CAP_PROP_FRAME_WIDTH, 1920 )
    cap.set( cv2.CAP_PROP_FRAME_HEIGHT, 1080 )
    cap.set( cv2.CAP_PROP_AUTOFOCUS, 0 )  # turn the autofocus off
    cap.set( cv2.CAP_PROP_FOCUS, 5) # set the focus of camera
    print(cap.get(cv2.CAP_PROP_FOCUS))


    # Change the camera setting using the set() function
    # cap.set(cv2.CAP_PROP_EXPOSURE, -6.0)
    # cap.set(cv2.CAP_PROP_GAIN, 4.0)
    # cap.set(cv2.CAP_PROP_BRIGHTNESS, 144.0)
    # cap.set(cv2.CAP_PROP_CONTRAST, 27.0)
    # cap.set(cv2.CAP_PROP_HUE, 13) # 13.0
    # cap.set(cv2.CAP_PROP_SATURATION, 28.0)
    #
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 128.0)
    cap.set(cv2.CAP_PROP_CONTRAST, 128.0)
    cap.set(cv2.CAP_PROP_SATURATION, 128.0)
    cap.set(cv2.CAP_PROP_HUE, -1.0) # 13.0
    cap.set(cv2.CAP_PROP_GAIN, 4.0)
    cap.set(cv2.CAP_PROP_EXPOSURE, -7.0)
    # Read the current setting from the camera
    def print_props():
        test = cap.get(cv2.CAP_PROP_POS_MSEC)
        ratio = cap.get(cv2.CAP_PROP_POS_AVI_RATIO)
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS)
        contrast = cap.get(cv2.CAP_PROP_CONTRAST)
        saturation = cap.get(cv2.CAP_PROP_SATURATION)
        hue = cap.get(cv2.CAP_PROP_HUE)
        gain = cap.get(cv2.CAP_PROP_GAIN)
        exposure = cap.get(cv2.CAP_PROP_EXPOSURE)
        print("Test: ", test)
        print("Ratio: ", ratio)
        print("Frame Rate: ", frame_rate)
        print("Height: ", height)
        print("Width: ", width)
        print("Brightness: ", brightness)
        print("Contrast: ", contrast)
        print("Saturation: ", saturation)
        print("Hue: ", hue)
        print("Gain: ", gain)
        print("Exposure: ", exposure)

    print_props()

    while True:
        ret, img = cap.read()

        h, w = img.shape[:2]
        cv2.imshow( "World co-ordinate frame axes", img )

        k = cv2.waitKey( 10 )
        print_props()
        if k == ord( 'q' ):
            break

    cv2.destroyAllWindows()
    cv2.VideoCapture(camera_index).release()


#   0  CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
#   1  CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
#   2  CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
#   3  CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
#   4  CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
#   5  CV_CAP_PROP_FPS Frame rate.
#   6  CV_CAP_PROP_FOURCC 4-character code of codec.
#   7  CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
#   8  CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
#   9 CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
#   10 CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
#   11 CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
#   12 CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
#   13 CV_CAP_PROP_HUE Hue of the image (only for cameras).
#   14 CV_CAP_PROP_GAIN Gain of the image (only for cameras).
#   15 CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
#   16 CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
#   17 CV_CAP_PROP_WHITE_BALANCE Currently unsupported
#   18 CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)

if __name__ == '__main__':
    main(sys.argv)