import arduino_controller
import time

controller = arduino_controller.Arduino()

controller.forward()

time.sleep(2)

controller.stop()

time.sleep(2)

controller.backwards()

time.sleep(2)

controller.stop()

time.sleep(1)

gate = controller.gate_state

print(gate)

