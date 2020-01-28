import sorting_robot
import arduino_controller

# arduino = arduino_controller.Arduino()
rob = sorting_robot.Robot()


bolt_type = "nas1802-4-07"


print(rob.getl())
# rob.drop(arduino, bolt_type)
print("Dropped: ", bolt_type)


