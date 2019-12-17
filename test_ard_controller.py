import arduino_controller
import time

controller = arduino_controller.Arduino()

controller.belts[0].forward()
time.sleep(2)

controller.belts[0].stop()

time.sleep(2)

controller.belts[0].backwards()

time.sleep(2)

controller.belts[0].stop()

time.sleep(1)

controller.all_backwards()

time.sleep(2)

controller.all_stop()

time.sleep(1)

gate = controller.gate_state

print(gate)

