# import sorting_robot
# import arduino_controller
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
        print("self.machine = sorting_robot.SortingMachine()")
        print("self.data = sorting_robot.Bolts()")
        self.crop_dim = {
            "pos_x": 520,
            "pos_y": 200,
            "width": 640,
            "height": 640
        }
        self.model_img_size = (550, 550)
        self.count = 0

    def connect_arduino(self):
        print("connected arduino")
        return True

    def connect_camera(self):
        print("connected camera")
        return True

    def connect_robot(self):
        print("connected robot")
        return True

    def data_startup(self):
        # self.count, _, self.IMG_CLASS_PATH = self.machine.save_pictures(self.IMG_SAVE_PATH, self.bolt_type_path, 0)
        # self.REV_CLASS_MAP, self.file_path = self.data.bolts_in_model(sub_ass=1)
        # self.model = load_model(self.file_path)
        print("Loaded model")

    def machine_startup(self):
        print("rob.startup(arduino)")
        print("arduino.blocker_close()")
        time.sleep(0.5)

    def belts_roll(self):
        print("arduino.all_forward() / arduino.bulk_feeder_start()")

    def lightgate(self):
        time.sleep(1)
        print("bolt found")
        return True

    def img_stop(self):
        print("arduino.bulk_feeder_stop() / arduino.all_stop()")
        time.sleep(2)

    def img_capture(self):
        self.frame = cv2.imread("dataset/image_data_better_camera_more_split/train/m59557-16/4.jpg")
        return True, self.frame

    def img_processing(self, frame):
        crop_img = self.crop(frame, self.crop_dim['pos_x'], self.crop_dim['pos_y'], self.crop_dim['width'], self.crop_dim['height'])
        print("Image Cropped")
        return crop_img

    def crop(self, img, x=100, y=200, width=600, height=600, ):
        return img[y:y + height, x:x + width]

    def img_save(self, frame):
        # filename = '{}.jpg'.format(self.count + 1)
        # save_path = os.path.join(self.IMG_CLASS_PATH, filename)
        # cv2.imwrite(save_path, frame)
        time.sleep(0.1)
        print("Image Saved")

    def img_classify(self, frame):
        # bolt_type, pred, bolt_code = self.machine.test_img(frame, self.model, self.REV_CLASS_MAP, size=self.model_img_size)
        self.count += 1
        # bolt_counts = self.machine.bolt_counter(bolt_type)
        bolt_type, pred, bolt_code, bolt_counts = "nas1802-3-6", [[0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0]], 4, [1,2,3,4,5,6,7,8,9,self.count]
        return bolt_type, pred, bolt_code, bolt_counts

    def exit_classified_bolt(self):
        print("Bolt thrown out")

    def robot_drop(self, bolt_type):
        print("Dropped: ", bolt_type)

    def machine_stop(self):
        print("Machine stopped")



if __name__ == "__main__":
    machine = MachineController()
    machine.connect_camera()
    machine.connect_arduino()
    machine.connect_robot()
    machine.data_startup()