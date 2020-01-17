import sorting_robot

rob = sorting_robot.Robot()
pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train = rob.get_waypoints()


bolt_type = "nas1802-3-6"

print(rob.getl())
rob.drop(bolt_type, pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train, train=True)
print("Dropped: ", bolt_type)


