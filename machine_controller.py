import sorting_robot
import arduino_controller
from keras.models import load_model
import os, time
import cv2.cv2 as cv2
from datetime import date, datetime


class MachineController(object):
    def __init__(self):
        start_time = datetime.now()
        # Name of folder where to save data to
        self.IMG_SAVE_PATH = 'dataset/image_test'
        self.bolt_type_path = start_time.strftime("%Y%m%d_%H%M")
        self.machine = sorting_robot.SortingMachine()
        self.data = sorting_robot.Bolts()
        self.crop_dim = {
            "pos_x": 520,
            "pos_y": 200,
            "width": 640,
            "height": 640
        }
        self.model_img_size = (550, 550)

    def connect_arduino(self):
        try:
            self.arduino = arduino_controller.Arduino()
            return True
        except:
            print("arduinofalse")
            return False

    def connect_camera(self):
        try:
            self.camera = self.machine.set_camera()
            return True
        except:
            print("camerafalse")
            return False

    def connect_robot(self):
        try:
            self.rob = sorting_robot.Robot()
            return True
        except:
            print("robotfalse")
            return False

    def data_startup(self):
        self.count, _, self.IMG_CLASS_PATH = self.machine.save_pictures(self.IMG_SAVE_PATH, self.bolt_type_path, 0)
        self.REV_CLASS_MAP, self.file_path = self.data.bolts_in_model(sub_ass=1)
        self.model = load_model(self.file_path)

    def machine_startup(self):
        self.rob.startup(self.arduino)
        self.arduino.blocker_close()
        time.sleep(0.5)

    def belts_roll(self):
        self.arduino.all_forward()
        self.arduino.bin_open()
        self.arduino.bulk_feeder_start()

    def lightgate(self):
        return self.arduino.gate_state

    def img_stop(self):
        self.arduino.bulk_feeder_stop()
        self.arduino.bin_closed()
        self.arduino.all_stop()
        time.sleep(2)

    def img_capture(self):
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        return ret, self.frame

    def img_processing(self, frame):
        crop_img = self.crop(frame, self.crop_dim['pos_x'], self.crop_dim['pos_y'], self.crop_dim['width'], self.crop_dim['height'])
        return crop_img

    def crop(self, img, x=100, y=200, width=600, height=600, ):
        return img[y:y + height, x:x + width]

    def img_save(self, frame):
        filename = '{}.jpg'.format(self.count + 1)
        save_path = os.path.join(self.IMG_CLASS_PATH, filename)
        cv2.imwrite(save_path, frame)

    def img_classify(self, frame):
        bolt_type, pred, bolt_code = self.machine.test_img(frame, self.model, self.REV_CLASS_MAP, size=self.model_img_size)
        self.count += 1
        bolt_count = self.machine.bolt_counter(bolt_type)
        return bolt_type, pred, bolt_code, bolt_count

    def exit_classified_bolt(self):
        self.arduino.blocker_open()
        time.sleep(0.5)
        self.arduino.all_forward()
        time.sleep(0.4)  # wait until object is gone (don't go lower)
        self.arduino.blocker_close()  # close gate
        time.sleep(0.4)  # bolt goes into robot/output
        self.arduino.all_stop()

    def robot_drop(self, bolt_type):
        self.rob.drop(self.arduino, bolt_type)
        print("Dropped: ", bolt_type)

    def machine_stop(self):
        self.arduino.bulk_feeder_stop()
        self.arduino.all_stop()



if __name__ == "__main__":
    machine = MachineController()
    machine.connect_camera()
    machine.connect_arduino()
    machine.connect_robot()
    machine.data_startup()