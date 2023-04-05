#! /usr/bin/python3

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from projeto_01.srv import cameraserv,cameraservResponse
import numpy as np


class myCamera():

    def __init__(self):
        print('init camera') 
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/xtion/rgb/image_color",Image,self.imageCallBack)

        self.service = rospy.Service('detect', cameraserv, self.callback_ServiceCamera)
        self.achei = False   
    def callback_ServiceCamera(self, request):
        self.res = cameraservResponse()
        self.res = self.achei
        return self.res
    def imageCallBack(self, msg):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            print(e)
        
        verm = self.cv_image[:,:,2]<20
        verde= self.cv_image[:,:,1]>60
        azul = self.cv_image[:,:,0]<20
        
        mascara = np.logical_and.reduce((verm,verde,azul))
        self.achei = np.any(mascara)
if __name__ == '__main__':

    rospy.init_node('camera_1')
    tiago_camera = myCamera()
    rospy.spin()