# -*- coding:utf-8 -*-
import rospy
import time
from nav_msgs.msg import Odometry
import geometry_msgs.msg
from geometry_msgs.msg import Twist, Point, Quaternion
import tf
from math import radians, copysign, sqrt, pow, pi, atan2,fabs
from tf.transformations import euler_from_quaternion
import numpy as np
from simple_pid import PID

base_frame = 'base_link'
parent_frame = 'odom'

pose = None

dis_err = 0.05
ang_err = 0.1

max_linear_vel = 1.5 # 最大线速度
max_angular_vel = 1 # 最大角速度
min_linear_vel = 0.05 # 最小线速度
min_angular_vel = 0.05 # 最小角速度

dec_linear_timing = 0.2 # 距目标0.2m内开始减速
dec_angular_timing = 0.5 # 距目标0.5rad内开始减速

from math import pi, fmod, fabs


def diffAng(target_ang, source_ang):
    a = target_ang - source_ang
    #a = fmod(a + pi, 2*pi) - pi
    #return a+2*pi if a <= -pi else a
    a = fmod(a,2*pi)
    if a <= -pi:
      return a+2*pi
    elif a > pi:
      return a-2*pi
    return a


def calcRoute(from_ang, route_ang, to_ang):
    reverse_route_ang = route_ang + pi
    route_dist = fabs(diffAng(route_ang, from_ang)) + \
        fabs(diffAng(to_ang, route_ang))
    reverse_dist = fabs(diffAng(reverse_route_ang, from_ang)) + \
        fabs(diffAng(to_ang, reverse_route_ang))
    return diffAng(route_ang, from_ang) if route_dist <= reverse_dist else diffAng(reverse_route_ang, from_ang)

def getPoses():
  try:
    (trans, rot) = tf_listener.lookupTransform('/odom', '/base_link', rospy.Time(0)) # TODO: frame id !!!
    x, y, z = trans
    roll, pitch, yaw = tf.transformations.euler_from_quaternion(rot)
  except (tf.Exception, tf.ConnectivityException, tf.LookupException):
    rospy.loginfo("Cannot find transform between base_frame parent_frame")
    return None
  return [x,y,yaw]
def getPose():
    x, y = pose.position.x, pose.position.y
    quat = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
    roll, pitch, yaw = tf.transformations.euler_from_quaternion(quat)
    return [x, y, yaw]
def Position(odom_data):

    global pose
    #rospy.sleep(1)
    #curr_time = odom_data.header.stamp
    pose = odom_data.pose.pose #  the x,y,z pose and quaternion orientation
    #counter= counter+1
    #print counter, curr_time
    #print
    #print pose
def goto_pose():
    pass

if __name__ == '__main__':
    rospy.init_node('autonav')
    #rospy.on_shutdown(on_shutdown)
    tf_listener = tf.TransformListener()
    rospy.Subscriber('odom',Odometry,Position)
    
    time.sleep(0.5)
    cmd_vel = rospy.Publisher('cmd_vel', geometry_msgs.msg.Twist, queue_size=5) # TODO: topic namespace
    rate = rospy.Rate(60.0)
    p = getPose()
    print('pos', p)
    goal_a = 0
    goal_x = 0.8
    goal_y = 0
    goal_da = 0  
    goal_distance = 0.8
    pid = PID(1, 0.1, 0, setpoint=-1.8)
    pid.output_limits = (0, 1.1)
    
    while(abs(p[0]-goal_x) > 0.02):
        global p
        p = getPose()
        speed = pid(p[0])
        move_cmd = geometry_msgs.msg.Twist()
        move_cmd.linear.x = speed*10
        move_cmd.angular.z = 0
        print(p)
        print(move_cmd)
        cmd_vel.publish(move_cmd)
        rate.sleep()
    move_cmd = geometry_msgs.msg.Twist()
    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    print(move_cmd)
    cmd_vel.publish(move_cmd)    
#    while not rospy.is_shutdown():
#        while (goal_distance > dis_err) or (fabs(goal_da)>ang_err):
#          #print 'while',goal_distance,abs(goal_da)
#          p = getPose()
#          x_start = p[0]
#          y_start = p[1]
#          rotation = p[2]
#          goal_distance = sqrt(pow((goal_x - x_start), 2) + pow((goal_y - y_start), 2))
#          path_angle = atan2(goal_y - y_start, goal_x- x_start)
#          goal_da = diffAng(goal_a,rotation)
#          turn_da = 0
#          move_cmd = geometry_msgs.msg.Twist()
#          move_cmd.linear.x = 0
#          move_cmd.angular.z = 0
#          if goal_distance < dis_err:
#            turn_da = goal_da
#          else:
#            turn_da = calcRoute(rotation,path_angle,goal_a)
#            if(fabs(turn_da)<ang_err):
#              dir = -1
#              if fabs(diffAng(path_angle,rotation)) <= fabs(2*turn_da):
#                dir = 1
#              vel1 = min(max_linear_vel*goal_distance/dec_linear_timing, max_linear_vel)
#              move_cmd.linear.x = dir*max(vel1, min_linear_vel)
#          move_cmd.angular.z = max_angular_vel * turn_da/dec_angular_timing
#          if move_cmd.angular.z > 0:
#            vel2 = min(move_cmd.angular.z, max_angular_vel)
#            move_cmd.angular.z = max(vel2,min_angular_vel)
#          else:
#            vel3 = max(move_cmd.angular.z, -1*max_angular_vel)
#            move_cmd.angular.z = -min(vel3,-1*min_angular_vel)
#          move_cmd.angular.z = 0
#          print(move_cmd)
#          cmd_vel.publish(move_cmd)
#          rate.sleep()
    rospy.spin()
    