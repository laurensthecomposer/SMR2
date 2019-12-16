import arduino_controller
import time

controller = arduino_controller.Arduino()

controller.m2.forward()
time.sleep(2)

controller.m2.stop()

time.sleep(2)

controller.m2.backwards()

time.sleep(2)

controller.m2.stop()

time.sleep(1)

gate = controller.gate_state

print(gate)

