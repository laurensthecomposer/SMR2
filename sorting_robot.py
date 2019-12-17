import urx
import time
import copy
import math

class Robot( urx.Robot ):
    def __init__(self, host="192.168.0.1", use_rt=True):
        super().__init__( host, use_rt )

        self.cal_points = []
        self.tcp = (0, 0, 0, 0, 0, 0)
        self.set_payload(0.5, (0, 0, 0))  # Set payload for joints
        time.sleep(0.2)  # leave some time to robot to process the setup commands

    def get_waypoints(self):
        pickup_point = self.getl()
        safe_pos = pickup_point.copy()
        x_offset = -pickup_point[1]-0.3
        safe_pos[1] += x_offset
        table_clear = safe_pos.copy()
        z_offset = -table_clear[2] + 0.4
        table_clear[2] += z_offset
        pre_drop = table_clear.copy()
        y_offset = -pre_drop[0] + 0.3
        pre_drop[0] += y_offset
        zy_train = pickup_point.copy()
        z_offset = -zy_train[2]+0.20
        zy_train[2] += z_offset
        zy_train[0] += 0.45
        x_train = zy_train.copy()
        x_train[1] -= 0.15
        x_train[2] -= 0.10
        return pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train

    def move_joint(self, joint_index, degrees, acc=0.05, vel=0.5):
        # print(degrees)
        a = super().getj()
        a[joint_index] = math.radians( degrees )
        super().movej( a, acc, vel )

    # def train_pathing(self, pickup_point, zy_train, xy_train, dropping, acc = 0.05, vel = 0,5):
    #     if dropping:
    #         self.movel(zy_train, acc, vel)
    #         self.movel(xy_train, acc ,vel)
    #     elif dropping == False:
    #         self.movel(zy_train, acc, vel)
    #         self.movel(pickup_point, acc, vel)

    def drop_pathing(self, pickup_point, safe_pos, table_clear,  pre_drop, dropping):
        if dropping == True:
            self.movel(safe_pos, acc, vel)
            self.movel(table_clear, acc, vel)
            self.movel(pre_drop, acc, vel)
        elif dropping == False:
            self.movel(pre_drop, acc, vel)
            self.movel(table_clear, acc, vel)
            self.movel(safe_pos, acc, vel)
            self.movel(pickup_point, acc, vel)



    def drop(self, bolt_type="", pickup_point=[], safe_pos=[], table_clear=[], pre_drop=[], zy_train=[], x_train=[], train=False, acc=0.02,vel=0.2):
        # drop locations
        nas180236 = [0.31, 0.20, 0.23, 1.0945, 2.88, -0.167]
        nas180237 = [0.43, 0.20, 0.23, 1.0945, 2.88, -0.167]
        nas180238 = [0.55, 0.20, 0.23, 1.0945, 2.88, -0.167]
        nas180239 = [0.67, 0.20, 0.23, 1.0945, 2.88, -0.167]

        # dropping
        self.drop_pathing(pickup_point, safe_pos, table_clear,  pre_drop, dropping=True, acc=0.05, vel=0.5)
        if train:
            self.train_pathing(zy_train, x_train,dropping=True)
            self.move_joint(3, -120)
            self.move_joint(3, -180)
            self.train_pathing(zy_train, x_train,dropping=False)
        elif bolt_type == "None":
            print("Cant drop nothing!")
        elif bolt_type == "nas1802-3-6":
            self.movel(nas180236, acc, vel)
            self.move_joint(4, -160)
            self.movel(nas180236, acc, vel)
            self.move_joint(5, 0)
        elif bolt_type == "nas1802-3-7":
            self.movel(nas180237, acc, vel)
            self.move_joint(4, -160)
            self.movel(nas180237, acc, vel)
            self.move_joint(5, 0)
        elif bolt_type == "nas1802-3-8":
            self.movel(nas180238, acc, vel)
            self.move_joint(4, -160)
            self.movel(nas180238, acc, vel)
            self.move_joint(5, 0)
        elif bolt_type == "nas1802-3-9":
            self.movel(nas180239, acc, vel)
            self.move_joint(4, -160)
            self.movel(nas180239, acc, vel)
            self.move_joint(5, 0)

        self.drop_pathing(pickup_point, safe_pos, table_clear,  pre_drop, dropping=False, acc=0.05, vel=0.5)



# #
# grab_pos = rob.getl()
# # rob.movel(grab_pos,a,v)
# offset = -grab_pos[1]-0.3
# rob.movel([0,offset,0,0,0,0],a,v,relative=True)
# safe_pos = rob.getl()
# rob.movel([0,0,0.4,0,0,0],a,v,relative=True)
# table_clear = rob.getl()
# rob.movel([0.6,0,0,0,0,0],a,v,relative=True)
# pre_drop = rob.getl()
# rob.movel(nas180236,0.02,0.2)
# rob.move_joint(4, -145)
# rob.movel(pre_drop,0.02,0.2)
# rob.movel(table_clear,a,v)
# rob.movel(safe_pos,a,v)
# rob.movel(grab_pos,a,v)


safe_pos = [0.09971948282828372, -0.28262633013908556, 0.18818396760195247, 2.8671851248843883, -1.1966115425973087, -0.06471721693152228]
predown_pos = [-0.4463722236754941, -0.29059048689795197, 0.15793967714281765, 2.828433668932312, -1.0557416698825994, 0.06735982734772203]
down_pos = [-0.4463722236754941, 0.015021497883424577, -0.25072682093612597, 2.5889324276558927, -1.0855968486533858, 0.1880735394550927]

# nas180236 = [0.3305719576326038, 0.178241525633243, 0.12187782402836271, 1.0945296614329365, 2.888786561159549, -0.16719136219750047]
# nas180237 = [0.45188696797825134, 0.17824359582040053, 0.12185134879187386, 1.0945477029007147, 2.888844200528327, -0.1672353426870481]
# nas180238 = [0.45188696797825134, 0.17824359582040053, 0.12185134879187386, 1.0945477029007147, 2.888844200528327, -0.1672353426870481]
# nas180239 = [0.6786258534848617, 0.1782441194658825, 0.12184786196087888, 1.0945302905363183, 2.888806706098612, -0.1672289811290121]

# rob.movel(grab_pos, a, v)
# rob.movel([0,0.5,0,])
# rob.movel(predown_pos)
# rob.movel
# rob.movel
# pos_start = rob.getl()
# rob.movel(pos_start, a, v)
#
# rob.getl()
#


# delta_x = 0.100  # distance in meters
# delta_z = 0.100  # distance in meters
# radius = 0.02
#
# robot = van_robot.Robot
#
# rob.draw_square(delta_x, delta_z, radius)

# van_robot.Robot.draw_rectangle()
