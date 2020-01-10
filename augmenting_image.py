## Installing shapely
# pip install Shapely-1.6.4.post2-cp36-cpl36m-win_amd64 (error with installing)
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely


import imageio
import imgaug as ia
from imgaug import augmenters as iaa
import os
import cv2
import time

bolt = "nas1802-3-6"
images_augmented = 0
total_images = 0

currentfolderpath = os.getcwd()
path = ''.join( [currentfolderpath, "/images_nas18/", bolt, "/"])

names = os.listdir(path)

names = sorted(names, key=len )

total_images = ((len(names) )/9) - 1

print(total_images)
while images_augmented <= total_images:
    image_loc = ''.join([path, names[images_augmented]])

    image = cv2.imread(image_loc)
    img1 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)




    cv2.imwrite(os.path.join(path, names[images_augmented]), image)

    # cv2.imshow("test", image)
    # cv2.waitKey(1)
    i = 10
    while i<90:
        ia.seed(4)
        current_name = names[images_augmented]
        number_name = current_name.replace( ".jpg", "" )
        filename = ''.join([number_name, "_rotate_", str(i), ".jpg"])
        rotate = iaa.Affine(rotate=(i))
        image_aug = rotate.augment_image(image)

        img1 = cv2.cvtColor(image_aug, cv2.COLOR_RGB2GRAY)

        height, width = img1.shape

        h_centre = int(height / 2)
        w_centre = int(width / 2)

        thickness = 100

        cv2.circle(image_aug, (h_centre, w_centre), w_centre + int(thickness / 2), (0, 0, 0), thickness=thickness)

        # cv2.imshow(filename, image_aug)
        cv2.imwrite(os.path.join(path,filename), image_aug)
        # cv2.waitKey(1)
        # time.sleep(1)

        i = i + 10
        # print(i)
        # cv2.destroyAllWindows()
        # time.sleep(1)

    images_augmented += 1
    # print(images_augmented)

    # time.sleep(0.5)
    # cv2.destroyAllWindows()
    if cv2.waitKey(0) == ord('q'):
        break

print("All images rotated & saved.")