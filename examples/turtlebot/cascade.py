import rospy
from threading import Thread
import numpy as np
import time
import sys
import signal
import cv2
import time
import freenect
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from math import radians, degrees
from geometry_msgs.msg import *
from geometry_msgs.msg import Twist
import subprocess

def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

def robot_infront():
   
#    self.vel3_pub = rospy.Publisher('/robot2/mobile_base/commands/velocity', Twist, queue_size=5)

    print ('Start robot det')
    robot_cascade = cv2.CascadeClassifier('robot_front.xml')
    #cap = get_video()

    while 1:
        img = get_video()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        robot = robot_cascade.detectMultiScale(gray, 1.1, 1) #detect robot
        if robot == ():
#           print('no robot')
           font = cv2.FONT_HERSHEY_SIMPLEX
           cv2.putText(img,'no robot',(20,30), font, 1,(0,255,255),2,cv2.LINE_AA)
        else:
           print('robot infront')
           font = cv2.FONT_HERSHEY_SIMPLEX
           cv2.putText(img,'robot infront',(20,30), font, 1,(0,0,255),2,cv2.LINE_AA)
#           global p 
#           p.terminate()

        for (x,y,w,h) in robot:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
#            print('w= %s, h= %s') % (w,h)
#            if (w>=50 and h>=50):
#               print('done') 
#               global p 
#               p.terminate()
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

if __name__=='__main__':
    # detect robot_infront 
    thread_robot = Thread(target=robot_infront)
    thread_robot.start()

    global p
    p=subprocess.Popen(['python3', 'test2.py'])
