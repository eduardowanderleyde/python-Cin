#! /usr/bin/python3

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from trajectory_msgs.msg import JointTrajectory,JointTrajectoryPoint
from tf.transformations import euler_from_quaternion
from control_msgs.msg import JointTrajectoryControllerState
from projeto_01.srv import cameraserv,cameraservRequest
class myRobot():

    def __init__(self):
        self.sub_odom = rospy.Subscriber("/mobile_base_controller/odom",Odometry,self.callback_odometria)
        self.sub_laser = rospy.Subscriber("/scan_raw",LaserScan,self.callback_laser)
        self.sub_state_head = rospy.Subscriber("/head_controller/state",JointTrajectoryControllerState,self.statecallback)
        self.camera_res = rospy.ServiceProxy('detect', cameraserv)
        self.pub_vel = rospy.Publisher("/mobile_base_controller/cmd_vel",Twist,queue_size=1)
        self.pub_head = rospy.Publisher("/head_controller/command",JointTrajectory,queue_size=1)
        self.pub_hand = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=1)
        
        self.tiago_odom = Odometry()
        self.orinetacao = 0.0
        self.head = JointTrajectoryControllerState()
        self.tiago_laser = []
        self.parede_frente = self.parede_esquerda = self.parede_direita = float('inf')
        self.res = None
    
    def statecallback(self,msg):
        self.head = msg.actual.positions[0]
    
    def callback_odometria(self, msg):
        self.tiago_odom = msg.pose.pose.orientation
        self.orinetacao = (euler_from_quaternion([self.tiago_odom.x,self.tiago_odom.y,self.tiago_odom.z,self.tiago_odom.w])[2])*180/3.1416

    def callback_laser(self, msg):
        self.parede_frente = min(msg.ranges[280:340])
        self.parede_esquerda = min(msg.ranges[540:560])
        self.parede_direita = min(msg.ranges[120:140])
                     
    def res_camera(self):
        rospy.wait_for_service("detect")
        rospy.sleep(2)
        try:
            request = cameraservRequest()
            self.res = self.camera_res(request)
            print(self.res)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def dar_xau(self):
        cmd = JointTrajectory()        
        cmd.joint_names.append("arm_1_joint")
        cmd.joint_names.append("arm_2_joint")
        cmd.joint_names.append("arm_3_joint")
        cmd.joint_names.append("arm_4_joint")
        cmd.joint_names.append("arm_5_joint")
        cmd.joint_names.append("arm_6_joint")
        cmd.joint_names.append("arm_7_joint")
        point = JointTrajectoryPoint()
        point.positions = [0] * 7
        point.velocities = [0] * 7
        point.time_from_start = rospy.Duration(1)
        cmd.points.append(point)
        rate = rospy.Rate(1)
        angle = 0.7
        while not rospy.is_shutdown():
            cmd.points[0].positions[1] = angle
            cmd.points[0].velocities[1] = 0.5
            cmd.points[0].time_from_start = rospy.Duration(1)

            self.pub_hand.publish(cmd)
            if angle > 0.7:
                angle -= 0.2
            elif angle < 1.3:
                angle += 0.2
            rate.sleep()

    def moveHead(self):
        while self.head < 1.2:
            cmd = JointTrajectory()
            cmd.joint_names.append("head_1_joint")
            cmd.joint_names.append("head_2_joint")

            point = JointTrajectoryPoint()
            point.positions = [0] * 2
            point.velocities = [0] * 2
            point.time_from_start = rospy.Duration(1)

            cmd.points.append(point)
            cmd.points[0].positions[0] = 1.25
            
            cmd.points[0].velocities[0] = 0.1
            self.pub_head.publish(cmd)
        self.res_camera()
        
        if self.res.detect == False:
            while self.head > -1.2:
                cmd = JointTrajectory()
                cmd.joint_names.append("head_1_joint")
                cmd.joint_names.append("head_2_joint")

                point = JointTrajectoryPoint()
                point.positions = [0] * 2
                point.velocities = [0] * 2
                point.time_from_start = rospy.Duration(1)

                cmd.points.append(point)
                cmd.points[0].positions[0] = -1.25
                
                cmd.points[0].velocities[0] = 0.1
                self.pub_head.publish(cmd)
        self.res_camera()

    def turn_right(self):
        if self.orinetacao > -10 and self.orinetacao < 10:
            while self.orinetacao > -87:
                vel = Twist()
                vel.angular.z = -0.15
                self.pub_vel.publish(vel)
        elif self.orinetacao > -93 and self.orinetacao < -87:
            while self.orinetacao > -178 and self.orinetacao < 0:
                vel = Twist()
                vel.angular.z = -0.15
                self.pub_vel.publish(vel)
        elif self.orinetacao > 87 and self.orinetacao < 93:
            while self.orinetacao > 0:
                vel = Twist()
                vel.angular.z = -0.15
                self.pub_vel.publish(vel)

        rospy.sleep(2)

    def turn_left(self):
        if self.orinetacao > -10 and self.orinetacao < 10:
            while self.orinetacao < 89:
                vel = Twist()
                vel.angular.z = 0.15
                self.pub_vel.publish(vel)
        elif self.orinetacao < 93 and self.orinetacao > 87:
            while self.orinetacao < 178 and self.orinetacao >0 :
                vel = Twist()
                vel.angular.z = 0.15
                self.pub_vel.publish(vel)
        elif self.orinetacao < -87 and self.orinetacao > -93:
            while self.orinetacao < 2:
                vel = Twist()
                vel.angular.z = 0.12
                self.pub_vel.publish(vel)
        else:
            while abs(self.orinetacao) > 90:
                vel = Twist()
                vel.angular.z = 0.15
                self.pub_vel.publish(vel)
        rospy.sleep(2)
                    
    def move(self):
       while self.parede_frente > 0.9 or self.parede_frente == 0.0:
            vel = Twist()
            vel.linear.x = self.parede_frente*0.5
            self.pub_vel.publish(vel)

    def decision(self):
        if self.parede_frente > 1.0:
            self.move()
        elif self.parede_direita < 1.4 and self.parede_esquerda > 1.0:
            self.turn_left()
        elif self.parede_direita > 1.0 and self.parede_esquerda < 1.4:
            self.turn_right()
        elif self.parede_direita > 1.2 and self.parede_esquerda > 1.2 and self.parede_frente < 1.0 and self.res == None:
            self.moveHead()
        elif self.parede_direita != float("inf") and self.parede_esquerda != float("inf") and self.res.detect == True and self.head > 0.0:
            self.turn_left()
        elif self.parede_direita != float("inf") and self.parede_esquerda != float("inf") and self.res.detect == True and self.head < 0.0:
            self.turn_right()
        elif self.parede_direita == float("inf") or self.parede_esquerda == float("inf"):
            tiago.dar_xau()
        elif self.res.detect == False:
            print("LOST")
            
if __name__ == '__main__':

    rospy.init_node('dupla_1')
    tiago = myRobot()
    rospy.sleep(5)
    while not rospy.is_shutdown():
        tiago.decision()
    rospy.spin()
