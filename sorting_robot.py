import urx
import time
import copy
import math
import os
import cv2
import arduino_controller
import numpy as np
import ueye_camera

class Robot(urx.Robot):
    def __init__(self, host="192.168.0.1", use_rt=True):
        super().__init__(host, use_rt)

        self.cal_points = []
        self.tcp = (0, 0, 0, 0, 0, 0)
        self.set_payload(0.5, (0, 0, 0))  # Set payload for joints
        time.sleep(0.2)  # leave some time to robot to process the setup commands
        drop_loc = [-0.36631595075034457, 0.010530619638235254, 0.11319565764023887, -1.1743545255671206, 2.873501497878966, -0.07976037840156265]
        self.movel(drop_loc, 0.01, 0.1)
        self.arduino = arduino_controller.Arduino()

    def move_joint(self, joint_index, degrees, acc=0.05, vel=0.5):
        # print(degrees)
        a = super().getj()
        a[joint_index] = math.radians(degrees)
        super().movej(a, acc, vel)

    def drop(self, bolt_type="", acc=0.02, vel=0.2):
        # drop locations
        m5955710 = [-0.32504072318747923, -0.39318955109641723, 0.18666989850907775, 2.8428185625446596, -1.1824626229075792, -2.5769697464202658e-05]
        m5955716 = [-0.2165225007215927, -0.4138486562860415, 0.17576298309224656, 2.824796585196249, -1.207647475705301, 0.015021960712533795]
        m5955720 = [-0.10993090065718465, -0.4309448612226831, 0.17729723522705876, 2.8510017180308793, -1.2150903983710595, 0.00971518144614266]
        nas180236 = [0.002485337885411759, -0.4343911332681018, 0.17670454590399137, 2.7795082292067805, -1.2833729676687562, 0.03907367436333244]
        nas180237 = [0.10368461913264634, -0.41910400865342645, 0.17504201241174677, 2.821992003142949, -1.2006505178949993, 0.04880091835975134]
        nas180238 = [0.21373253774954487, -0.4200046412105078, 0.17663094755183514, 2.7903322259286925, -1.1977460588503168, 0.035940343958805104]
        nas180239 = [0.3261977351011792, -0.4123818946764718, 0.1769937211004541, 2.7805945533844567, -1.281916726945966, 0.024615157235468428]
        nas630510 = [0.42736483713993145, -0.44216356313850436, 0.17314271705077852, 2.826655293962752, -1.2877285048654983, -0.00042725699011751547]
        nas1802407 = [0.5392318000332552, -0.4397002263695111, 0.19157130563521024, -2.747049558982466, 1.3176412440538665, 0.05347415800508491]
        v647p23b = [0.6462556060133496, -0.4330175053314038, 0.18483470601765029, -2.735340404844916, 1.3487650976441188, 0.053448079692322]

        safe_pos = [0.11773670017317478, -0.3851208207084043, 0.28093635899363284, 2.8320877914484157, -1.2109140693593983, 0.027290517942945874]

        drop_loc = [-0.36631595075034457, 0.010530619638235254, 0.11319565764023887, -1.1743545255671206, 2.873501497878966, -0.07976037840156265]


        # dropping
        self.movel(safe_pos, acc, vel)
        if bolt_type == "m59557-10":
            self.movel(m5955710,acc,vel)
        elif bolt_type == "m59557-16":
            self.movel(m5955716,acc,vel)
        elif bolt_type == "m59557-20":
            self.movel(m5955720,acc,vel)
        elif bolt_type == "nas1802-3-6":
            self.movel(nas180236, acc,vel)
        elif bolt_type == "nas1802-3-7":
            self.movel(nas180237,acc,vel)
        elif bolt_type == "nas1802-3-8":
            self.movel(nas180238, acc, vel)
        elif bolt_type == "nas1802-3-9":
            self.movel(nas180239, acc, vel)
        elif bolt_type == "nas6305-10":
            self.movel(nas630510, acc, vel)
        elif bolt_type == "nas1802-4-07":
            self.movel(nas1802407, acc, vel)
        elif bolt_type == "v647p23b":
            self.movel(v647p23b, acc, vel)
        self.arduino.bin_open()
        time.sleep(0.5)
        self.arduino.bin_closed()
        self.movel(safe_pos, acc, vel)
        self.movel(drop_loc, acc, vel)

class SortingMachine():
    def save_pictures(self, IMG_SAVE_PATH, bolt_type, num_samples):
        IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, bolt_type)
        try:
            os.mkdir(IMG_CLASS_PATH)
            count = 0
        except FileExistsError:
            # Find location of directory
            currentfolderpath = os.getcwd()
            # print(currentfolderpath)
            path = ''.join([currentfolderpath, "/", IMG_SAVE_PATH, "/", bolt_type])
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

    def test_img(self, img, model, REV_CLASS_MAP=[], size=(227, 227)):
        # prepare the image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, size)
        cv2.imshow("test", img)

        # predict the picture
        pred = model.predict(np.array([img]))

        # sets print of arrays to 2 decimal places
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

        pic_code = np.argmax(pred[0])
        # print(pic_code)
        pic_name = REV_CLASS_MAP[pic_code]

        return pic_name, pred, pic_code

    def set_camera(self):
        cap = ueye_camera.UeyeCameraCapture(1)
        return cap

    # # Todo LAURENS PART 1
    # def mapper(self, val, REV_CLASS_MAP):
    #     return REV_CLASS_MAP[val]

class Bolts():
    def bolts_in_model(self, sub_ass):
        if sub_ass == 1:
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
                9: "v647p23b"
            }
            # best model till 9-1-2020
            model_folder = "models"
            model_name = "blue_light_moreV1_sq550_e472_tb20_vb20_aug-hor-briran0_8;1_2.h5"
            # model_name = "blue_light_split2_sq550_e520_tb20_vb20_aug-hor-briran0_8;1_2.h5"
            # model_name = "image_data_blue_light_split_sq350_e72_tb20_vb20_aug-hor-rotran20-briran0_8;1_2).h5"
            # model_name = "new_camera_cleaned_v1_350px.h5"
            file_path = os.path.join(model_folder, model_name)


            # model_name = "more_pictures_cleaned_v1_350px.h5"
            return REV_CLASS_MAP, file_path

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
