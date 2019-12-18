import sorting_robot

rob = sorting_robot.Robot()
pickup_point, safe_pos, table_clear, pre_drop, z_train, xy_train = rob.get_waypoints()


bolt_type = "nas1802-3-6"

rob.drop(bolt_type, pickup_point, safe_pos, table_clear, pre_drop)
print("Dropped: ", bolt_type)


