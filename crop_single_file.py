import imageio
import cv2.cv2 as cv2

def crop(img, x=100, y=200, width=600, height=600, ):
    return img[y:y + height, x:x + width]
