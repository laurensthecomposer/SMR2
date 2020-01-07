import green_screen
from crop_single_file import crop
from cv2 import cv2

for i in range(1, 50):
    img = cv2.imread('image_data_green/nas6305-10/' + str(i) + '.jpg')

    img_crop = crop(img, 0, 200, 1600, 600)
    crop_square = crop(img_crop, 700, 0, 500, 500)
    mask = green_screen.mask(img, threshold=100, imshow=True)

    cv2.imshow('img_crop', img_crop)
    cv2.imshow('crop_square', crop_square)
    cv2.waitKey(0)