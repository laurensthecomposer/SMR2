# source https://medium.com/fnplus/blue-or-green-screen-effect-with-open-cv-chroma-keying-94d4a6ab2743
from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np

# sample_image = 6
# file_name = 'img/sample_' + str(sample_image) + '.jpg'
# image = cv2.imread(file_name)
#
# print('Image type: ', type(image),
#       'Image Dimensions : ', image.shape)
#
# # option 1
# lower_blue = np.array([0, 100, 0])     #  [B value, G value, R value]
# upper_blue = np.array([120, 255, 100])
#
# mask = cv2.inRange(image, lower_blue, upper_blue)
# cv2.imshow('mask', mask)
#
# cv2.imshow('image', image)
# cv2.waitKey(100)

# option 2


def mask(image, threshold=35, imshow=False):
      # https://codereview.stackexchange.com/questions/184044/processing-an-image-to-extract-green-screen-mask/184059#184059
      img = image
      empty_img = np.zeros_like( img )
      red, green, blue = (2, 1, 0)

      reds = img[:, :, red]
      greens = img[:, :, green]
      blues = img[:, :, blue]

      mask = (greens < threshold) | (reds > greens) | (blues > greens)

      # result = np.where(mask, 255, 0)
      empty_img[mask] = (255, 255, 255)
      if imshow:
            cv2.imshow( 'image', image )
            cv2.imshow( 'mask2', empty_img )

      return empty_img
