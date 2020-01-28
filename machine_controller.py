import sorting_robot
import arduino_controller

class MachineController(object):
    def __init__(self):
        # Name of folder where to save data to
        self.IMG_SAVE_PATH = 'dataset/image_test'
        self.bolt_type_path = "test_bolts"
        self.machine = sorting_robot.SortingMachine()

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

if __name__ == "__main__":
    machine = MachineController()
    machine.connect_camera()
    machine.connect_arduino()
    machine.connect_robot()