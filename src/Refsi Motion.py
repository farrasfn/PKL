#! /usr/bin/env python

from __future__ import print_function

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

import numpy as np


class AllJoints:
    def __init__(self, joint_name_lst):
        rospy.loginfo('Waiting for joint trajectory Publisher')
        self.jtp = rospy.Publisher('/plen/joint_trajectory_controller/command',
                                   JointTrajectory,
                                   queue_size=1)
        rospy.loginfo('Found joint trajectory Publisher!')
        self.joint_name_lst = joint_name_lst
        self.jtp_zeros = np.zeros(len(joint_name_lst))

    def move_jtp(self, pos, howLong):
        jtp_msg = JointTrajectory()
        jtp_msg.joint_names = self.joint_name_lst
        point = JointTrajectoryPoint()
        point.positions = pos
        point.velocities = self.jtp_zeros
        point.accelerations = self.jtp_zeros
        point.effort = self.jtp_zeros
        point.time_from_start = rospy.Duration(howLong)  # rospy.Duration(1.0 / 60.0) #Edit howlong
        jtp_msg.points.append(point)
        self.jtp.publish(jtp_msg)

    def reset_move_jtp(self, pos):
        jtp_msg = JointTrajectory()
        self.jtp.publish(jtp_msg)
        jtp_msg = JointTrajectory()
        jtp_msg.joint_names = self.joint_name_lst
        point = JointTrajectoryPoint()
        point.positions = pos
        point.velocities = self.jtp_zeros
        point.accelerations = self.jtp_zeros
        point.effort = self.jtp_zeros
        point.time_from_start = rospy.Duration(0.0001)
        jtp_msg.points.append(point)
        self.jtp.publish(jtp_msg)


class PlenEnvironment:
    def __init__(self):
        rospy.init_node('joint_position_node')
        self.link_name_lst = [
            'plen::base_footprint', 'plen::l_shoulder', 'plen::ls_servo',
            'plen::l_elbow', 'plen::l_hip', 'plen::l_thigh', 'plen::l_knee',
            'plen::l_shin', 'plen::l_ankle', 'plen::l_foot',
            'plen::r_shoulder', 'plen::rs_servo', 'plen::r_elbow',
            'plen::r_hip', 'plen::r_thigh', 'plen::r_knee', 'plen::r_shin',
            'plen::r_ankle', 'plen::r_foot'
        ]

        self.joint_name_lst = [
            'rb_servo_r_hip', 'r_hip_r_thigh', 'r_thigh_r_knee',
            'r_knee_r_shin', 'r_shin_r_ankle', 'r_ankle_r_foot',
            'lb_servo_l_hip', 'l_hip_l_thigh', 'l_thigh_l_knee',
            'l_knee_l_shin', 'l_shin_l_ankle', 'l_ankle_l_foot',
            'torso_r_shoulder', 'r_shoulder_rs_servo', 're_servo_r_elbow',
            'torso_l_shoulder', 'l_shoulder_ls_servo', 'le_servo_l_elbow'
        ]
        self.all_joints = AllJoints(self.joint_name_lst)
        self.starting_pos = self.all_joints.jtp_zeros

    def reset(self):
        self.joint_pos = self.starting_pos
        print('RESET:', self.joint_pos)
        self.all_joints.reset_move_jtp(self.starting_pos)

    def step(self, action, howLong):
        print('STEP:', action)
        self.joint_pos = action
        self.all_joints.move_jtp(self.joint_pos,howLong) #Edit howlong


if __name__ == '__main__':
    plen = PlenEnvironment()

    plen.reset()

    joint_val=np.zeros(18)
    #print("Moving Joint 0 to Min")
    #joint_val[0]= 1.7
    #joint_val[1]= 1.7
    plen.step(joint_val, 0.1)     #for some fucking reason, the dumbass robot doesn't want to move
    rospy.sleep(1)        #before we do this stupid ass shit
    
    for i in range(2):
#=====Movement Below=================================================
    # Motion 1
    	joint_val[0] = 0
    	joint_val[1] = -0.24
    	joint_val[2] = 0 
    	joint_val[3] = 0 
    	joint_val[4] = 0 
    	joint_val[5] = -0.24
    	joint_val[6] = 0 
    	joint_val[7] = -0.24 
    	joint_val[8] = 0 
    	joint_val[9] = 0 
    	joint_val[10] = 0 
    	joint_val[11] = -0.24
    	joint_val[12] = 0 
    	joint_val[13] = 0.19
    	joint_val[14] = 0.2
    	joint_val[15] = 0.17 
    	joint_val[16] = -0.19
    	joint_val[17] = -0.2 
    	plen.step(joint_val, 1)     #for some fucking reason, the dumbass robot doesn't want to move
    	rospy.sleep(1)

# Motion 2
    	joint_val[0] = 0
    	joint_val[1] = -0.24
    	joint_val[2] = 0.7
    	joint_val[3] = -1.4  
    	joint_val[4] = -0.25 
    	joint_val[5] = -0.05
    	joint_val[6] = 0 
    	joint_val[7] = -0.2 
    	joint_val[8] = 0 
    	joint_val[9] = 0 
    	joint_val[10] = 0 
    	joint_val[11] = -0.2
    	joint_val[12] = 0 
    	joint_val[13] = 0.19
    	joint_val[14] = 0.2
    	joint_val[15] = 0.17 
    	joint_val[16] = -0.19
    	joint_val[17] = -0.2 
    	plen.step(joint_val, 1)     #for some fucking reason, the dumbass robot doesn't want to move
    	rospy.sleep(1)

# Motion 3
    	joint_val[0] = 0
    	joint_val[1] = -0.24
    	joint_val[2] = 0.9
    	joint_val[3] = -1.4  
    	joint_val[4] = -0.25 
    	joint_val[5] = -0.05
    	joint_val[6] = 0 
    	joint_val[7] = -0.2 
    	joint_val[8] = 0 
    	joint_val[9] = 0 
    	joint_val[10] = 0 
    	joint_val[11] = -0.2
    	joint_val[12] = 0 
    	joint_val[13] = 0.19
    	joint_val[14] = 0.2
    	joint_val[15] = 0.17 
    	joint_val[16] = -0.19
    	joint_val[17] = -0.2 
    	plen.step(joint_val, 1)     #for some fucking reason, the dumbass robot doesn't want to move
    	rospy.sleep(1)

# Motion 4
    	joint_val[0] = 0
    	joint_val[1] = 0.24
    	joint_val[2] = 1.1
    	joint_val[3] = -1.4  
    	joint_val[4] = -0.3 
    	joint_val[5] = 0.24
    	joint_val[6] = 0 
    	joint_val[7] = 0.22 
    	joint_val[8] = -0.4 
    	joint_val[9] = 0.2 
    	joint_val[10] = 0 
    	joint_val[11] = 0.22
    	joint_val[12] = 0 
    	joint_val[13] = 0.19
    	joint_val[14] = 0.2
    	joint_val[15] = 0.17 
    	joint_val[16] = -0.19
    	joint_val[17] = -0.2 
    	plen.step(joint_val, 1)     #for some fucking reason, the dumbass robot doesn't want to move
    	rospy.sleep(1)

# Motion 5
    	joint_val[0] = 0
    	joint_val[1] = 0.24
    	joint_val[2] = 0
    	joint_val[3] = 0  
    	joint_val[4] = 0
    	joint_val[5] = 0.24
    	joint_val[6] = 0 
    	joint_val[7] = 0.24 
    	joint_val[8] = -0.6 
    	joint_val[9] = 0.8 
    	joint_val[10] = 0.2 
    	joint_val[11] = 0.22
    	joint_val[12] = 0 
    	joint_val[13] = 0.19
    	joint_val[14] = 0.2
    	joint_val[15] = 0.17 
    	joint_val[16] = -0.19
    	joint_val[17] = -0.2 
    	plen.step(joint_val, 1)     #for some fucking reason, the dumbass robot doesn't want to move
    	rospy.sleep(1)

# Motion 6
    	joint_val[0] = 0
    	joint_val[1] = 0.24
    	joint_val[2] = 0
    	joint_val[3] = 0  
    	joint_val[4] = 0
    	joint_val[5] = 0.24
    	joint_val[6] = 0 
    	joint_val[7] = 1
    	joint_val[8] = -0.8 
    	joint_val[9] = 1 
    	joint_val[10] = 0.2 
    	joint_val[11] = 0
    	joint_val[12] = 0 
    	joint_val[13] = 0.19
    	joint_val[14] = 0.2
    	joint_val[15] = 0.17 
    	joint_val[16] = -0.19
    	joint_val[17] = -0.2 
    	plen.step(joint_val, 1)     #for some fucking reason, the dumbass robot doesn't want to move
    	rospy.sleep(1)

# Motion 7
    	joint_val[0] = 0
    	joint_val[1] = -0.3
    	joint_val[2] = 0
    	joint_val[3] = 0  
    	joint_val[4] = 0
    	joint_val[5] = -0.3
    	joint_val[6] = 0 
    	joint_val[7] = 1
    	joint_val[8] = -0.3 
    	joint_val[9] = 0.87 
    	joint_val[10] = 0.4 
    	joint_val[11] = -0.15
    	joint_val[12] = 0 
    	joint_val[13] = 0.19
    	joint_val[14] = 0.2
    	joint_val[15] = 0.17 
    	joint_val[16] = -0.19
    	joint_val[17] = -0.2 
    	plen.step(joint_val, 1)     #for some fucking reason, the dumbass robot doesn't want to move
    	rospy.sleep(1)

# Motion 7
    	joint_val[0] = 0
    	joint_val[1] = 0
    	joint_val[2] = 0
    	joint_val[3] = 0  
    	joint_val[4] = 0
    	joint_val[5] = 0
    	joint_val[6] = 0 
    	joint_val[7] = 1
    	joint_val[8] = -0.15 
    	joint_val[9] = 0.6 
    	joint_val[10] = 0.4 
    	joint_val[11] = -0.15
    	joint_val[12] = 0 
    	joint_val[13] = 0.19
    	joint_val[14] = 0.2
    	joint_val[15] = 0.17 
    	joint_val[16] = -0.19
    	joint_val[17] = -0.2 
    	plen.step(joint_val, 1)     #for some fucking reason, the dumbass robot doesn't want to move
    	rospy.sleep(1)

    	plen.reset()
    	rospy.sleep(1)