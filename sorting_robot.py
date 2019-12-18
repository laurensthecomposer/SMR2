import urx
import time
import copy
import math
import os
import cv2
import arduino_controller
import numpy as np

class Robot( urx.Robot ):
    def __init__(self, host="192.168.0.1", use_rt=True):
        super().__init__( host, use_rt )

        self.cal_points = []
        self.tcp = (0, 0, 0, 0, 0, 0)
        self.set_payload(0.5, (0, 0, 0))  # Set payload for joints
        time.sleep(0.2)  # leave some time to robot to process the setup commands

    def get_waypoints(self):
        pickup_point = self.getl()
        safe_pos = pickup_point.copy()
        x_offset = -pickup_point[1]-0.3
        safe_pos[1] += x_offset
        table_clear = safe_pos.copy()
        z_offset = -table_clear[2] + 0.4
        table_clear[2] += z_offset
        pre_drop = table_clear.copy()
        y_offset = -pre_drop[0] + 0.3
        pre_drop[0] += y_offset
        zy_train = pickup_point.copy()
        z_offset = -zy_train[2]+0.25
        zy_train[2] += z_offset
        zy_train[0] += 0.45
        x_train = zy_train.copy()
        x_train[1] -= 0.25
        x_train[2] -= 0.10
        return pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train

    def move_joint(self, joint_index, degrees, acc=0.05, vel=0.5):
        # print(degrees)
        a = super().getj()
        a[joint_index] = math.radians( degrees )
        super().movej( a, acc, vel )

    def train_pathing(self, pickup_point, zy_train, x_train, dropping=True, acc = 0.05, vel = 0.5):
        if dropping:
            self.movel(zy_train, acc, vel)
            self.movel(x_train, acc ,vel)
        elif dropping == False:
            self.movel(zy_train, acc, vel)
            self.movel(pickup_point, acc, vel)

    def drop_pathing(self, pickup_point, safe_pos, table_clear,  pre_drop, dropping=True,acc = 0.05, vel = 0.5):
        if dropping == True:
            self.movel(safe_pos, acc, vel)
            self.movel(table_clear, acc, vel)
            self.movel(pre_drop, acc, vel)
        elif dropping == False:
            self.movel(pre_drop, acc, vel)
            self.movel(table_clear, acc, vel)
            self.movel(safe_pos, acc, vel)
            self.movel(pickup_point, acc, vel)

    def drop(self, bolt_type="", pickup_point=[], safe_pos=[], table_clear=[], pre_drop=[], zy_train=[], x_train=[], train=False, acc=0.02,vel=0.2):
        # drop locations
        nas180236 = [0.31, 0.20, 0.23, 1.0945, 2.88, -0.167]
        nas180237 = [0.43, 0.20, 0.23, 1.0945, 2.88, -0.167]
        nas180238 = [0.55, 0.20, 0.23, 1.0945, 2.88, -0.167]
        nas180239 = [0.67, 0.20, 0.23, 1.0945, 2.88, -0.167]
        drop_loc = [-0.05926119038282123, -0.6900939148643027, 0.09265212533873536, -1.8691329331934325, 0.818416169672539, 0.63033805270759]
        # dropping
        if train == True:
            self.train_pathing(pickup_point, zy_train, x_train, dropping=True)
            self.movel(drop_loc, 0.05, 0.5)
            self.movel(x_train, 0.05, 0.5)
            self.train_pathing(pickup_point, zy_train, x_train,dropping=False)
        elif bolt_type == "None" and train == False:
            print("Cant drop nothing!")
        elif bolt_type == "nas1802-3-6" and train == False:
            self.drop_pathing(pickup_point, safe_pos, table_clear, pre_drop, dropping=True, acc=0.05, vel=0.5)
            self.movel(nas180236, acc, vel)
            self.move_joint(4, -160)
            self.movel(nas180236, acc, vel)
            self.move_joint(5, 0)
            self.drop_pathing(pickup_point, safe_pos, table_clear, pre_drop, dropping=False, acc=0.05, vel=0.5)
        elif bolt_type == "nas1802-3-7" and train == False:
            self.drop_pathing(pickup_point, safe_pos, table_clear, pre_drop, dropping=True, acc=0.05, vel=0.5)
            self.movel(nas180237, acc, vel)
            self.move_joint(4, -160)
            self.movel(nas180237, acc, vel)
            self.move_joint(5, 0)
            self.drop_pathing(pickup_point, safe_pos, table_clear, pre_drop, dropping=False, acc=0.05, vel=0.5)
        elif bolt_type == "nas1802-3-8" and train == False:
            self.drop_pathing(pickup_point, safe_pos, table_clear, pre_drop, dropping=True, acc=0.05, vel=0.5)
            self.movel(nas180238, acc, vel)
            self.move_joint(4, -160)
            self.movel(nas180238, acc, vel)
            self.move_joint(5, 0)
            self.drop_pathing(pickup_point, safe_pos, table_clear, pre_drop, dropping=False, acc=0.05, vel=0.5)
        elif bolt_type == "nas1802-3-9" and train == False:
            self.drop_pathing(pickup_point, safe_pos, table_clear, pre_drop, dropping=True, acc=0.05, vel=0.5)
            self.movel(nas180239, acc, vel)
            self.move_joint(4, -160)
            self.movel(nas180239, acc, vel)
            self.move_joint(5, 0)
            self.drop_pathing(pickup_point, safe_pos, table_clear, pre_drop, dropping=False, acc=0.05, vel=0.5)

class sorting_machine ():
    def save_pictures(self, IMG_SAVE_PATH, bolt_type, num_samples):
        IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, bolt_type)
        try:
            os.mkdir(IMG_CLASS_PATH)
            count = 0
        except FileExistsError:
            # Find location of directory
            currentfolderpath = os.getcwd()
            print(currentfolderpath)
            path = ''.join([currentfolderpath, "/", IMG_SAVE_PATH,"/", bolt_type])
            available = os.listdir(str(path))  # Check the files in the directory

            if len(available):  # if there are already files in the folder
                available = sorted(available, key=len)  # Sort files by name lenght
                lastfile = available[-1]  # Select last file
                startnr = lastfile.replace(".jpg", "")  # Strip JPG from file name
                count = int(startnr)  # Start counting from selected number
                num_samples = count + num_samples
            else:
                count = 0

        return count, num_samples, IMG_CLASS_PATH

    def test_img(self, img, model, size=(227,227), REV_CLASS_MAP={}):
        # prepare the image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, size)
        cv2.imshow("test", img)

        # predict the picture
        pred = model.predict(np.array([img]))

        # sets print of arrays to 2 decimal places
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

        pic_code = np.argmax(pred[0])
        print(pic_code)
    # Todo Laurens part 1 (cant get right value from REV_CLASS_MAP) when putting in PIC code, so this prints 4 and sould then take the REV_CLASS_MAP value from class BOLTS
        #  pic_name = self.mapper(pic_code, REV_CLASS_MAP)
        return pic_name

    def set_camera(self):
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # turn the autofocus off
        cap.set(cv2.CAP_PROP_FOCUS, 20)  # set the focus of camera
        cap.set(cv2.CAP_PROP_AUTO_WB, 0)
        cap.set(cv2.CAP_PROP_XI_AUTO_WB, 0)
        cap.set(cv2.CAP_PROP_EXPOSUREPROGRAM, 0)
        cap.set(cv2.CAP_PROP_XI_AEAG, 0)
        cap.set(cv2.CAP_PROP_BRIGHTNESS, 128.0)
        cap.set(cv2.CAP_PROP_CONTRAST, 128.0)
        cap.set(cv2.CAP_PROP_SATURATION, 128.0)
        cap.set(cv2.CAP_PROP_HUE, -1.0)  # 13.0
        cap.set(cv2.CAP_PROP_GAIN, 5.0)
        cap.set(cv2.CAP_PROP_EXPOSURE, -5.0)
        cap.set(cv2.CAP_PROP_SPEED, 1)
        return cap
 # Todo LAURENS PART 1
    def mapper(self, val, REV_CLASS_MAP):
        return REV_CLASS_MAP[val]

class bolts():
    def bolts_in_model(sub_ass):
        if sub_ass == 1:
            REV_CLASS_MAP = {
                0:"m59557-10",
                1:"m59557-16",
                2:"m59557-20",
                3:"nas1802-3-6",
                4:"nas1802-3-7",
                5:"nas1802-3-8",
                6:"nas1802-3-9",
                7: "nas1802-4-07",
                8:"nas6305-10",
               9: "none"
            }
            return REV_CLASS_MAP
        elif sub_ass == 2:
            REV_CLASS_MAP = {
                0: "nas1802-3-6",
                1: "nas1802-3-7",
                2: "nas1802-3-8",
                3: "nas1802-3-9",
                4: "none"
            }
            model_name = "nas18.h5"
            return REV_CLASS_MAP, model_name


