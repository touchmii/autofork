#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import rospy
import numpy as np
from std_msgs.msg import String
from nav_msgs.msg import Odometry

import pyqtgraph as pg
# import pyqtgraph.opengl as gl
#from pyqtgraph.Qt import QtCore, QtGui ,QtWidgets, uic
from pyqtgraph.Qt import QtCore, QtGui, uic
#from Graphs.Surface3D_Graph import Surface3D_Graph
try:
   import queue
except ImportError:
   import Queue as queue
uifilename = 'robot_control.ui'
form_class = uic.loadUiType(uifilename)[0] #dirty reading of the ui file. better to convert it to a '.py'

class MyWindowClass(QtGui.QMainWindow, form_class):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pub = rospy.Publisher("pyqt_topic", String, queue_size=10)
        rospy.init_node('pylistener', anonymous = True)  # ros节点初始化
        rospy.Subscriber('pyqt_topic', String, self.callback)  # ros节点接收数据
        rospy.Subscriber('odom', Odometry, self.callback2)
        #rospy.init_node('pyqt_gui')
        self.my_signal = QtCore.pyqtSignal(int)

    	self.upButton.pressed.connect(lambda: self.ptz_go("up"))
        #self.x_fit = np.linspace(1,100, 100)
        #self.y_fit = [_x*2 for _x in self.x_fit]
        self.graphicsView.plot([0], [0],symbol='o',pen=None)
        self.graphicsView.setLabel('left',text='toto',units='')
        self.graphicsView.setLabel('top',text='tata',units='')

    def ptz_go(self, dir):
    	if dir == 'up':
    		print('upButton pressed')
    		self.pub.publish('upButton pressed')
    @QtCore.pyqtSlot(int)
    def draw_pose(self, odom):
        self.graphicsView.plot([odom], [odom], symbol='o', pen=None)


    def callback(self, str):
        rospy.loginfo('Listener: %s', str)
        print('Recive: {}'.format(str))
    def callback2(self, odom):
        #self.draw_pose(odom)
        self.my_signal.emit(5)
        #pass
        rospy.loginfo('Listener: %s', odom.pose.pose)

if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtGui.QApplication([])
        # app.setWindowIcon(QtGui.QIcon("./logo.ico")) 无效
        pg.setConfigOption('background', 'w')
        # loop = asyncio.get_event_loop()

        win = MyWindowClass()
        win.show()

        

        sys.exit(app.exec_())

        rospy.spin()
        #app.exec_()
        #sys.exit()
