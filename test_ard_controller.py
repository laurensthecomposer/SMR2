import arduino_controller
import time

# connect to Arduino
controller = arduino_controller.Arduino(com= '/dev/cu.usbmodem14101')
# test the belts
for i in range(0, 3): # loop through 0, 1, 2
    print(i)
    controller.belts[i].forward()
    time.sleep(2)

    controller.belts[i].stop()
    time.sleep(2)

    controller.belts[i].backwards()
    time.sleep(2)

    controller.belts[0].stop()
    time.sleep(1)

controller.all_backwards()
time.sleep(2)
controller.all_stop()
time.sleep(1)

controller.all_forward()
time.sleep(2)
controller.all_stop()
time.sleep(1)

controller.all_forward()
time.sleep(0.2)
controller.all_backwards()
time.sleep(0.2)
controller.all_stop()

# test the blocker gate
controller.blocker_open()
time.sleep(0.5)
controller.blocker_close()
time.sleep(0.5)
controller.blocker_open()
time.sleep(1)

# test the bulk feeder
controller.bulk_feeder_start()
time.sleep(3)
controller.bulk_feeder_stop()
time.sleep(1)

gate = controller.gate_state

print(gate)

