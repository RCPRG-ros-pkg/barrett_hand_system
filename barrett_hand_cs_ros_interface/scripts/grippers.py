#!/usr/bin/env python
import roslib; roslib.load_manifest('barrett_hand_cs_ros_interface')

import sys
import rospy
import math
import copy
import tf

import PyKDL

from velma_common.barrett_hand_interface import *

if __name__ == "__main__":

    rospy.init_node('grippers_test', anonymous=True)

    prefix = "right"

    rospy.sleep(1)

    print "initializing interface..."
    bh = BarrettHandInterface()
    print "waiting for init..."

    bh.waitForInit()
    print "init ok"

    print "reset"
    bh.resetHand()
    bh.waitForHand()

    print "move right"
    bh.moveHand([0,0,0,0], [1,1,1,1], [2000,2000,2000,2000], 1000, hold=False)
    bh.waitForHand()

    print "move right"
    bh.moveHand([90.0/180.0*math.pi,110.0/180.0*math.pi,100.0/180.0*math.pi,0], [1,1,1,1], [2000,2000,2000,2000], 1000, hold=False)
    bh.waitForHand()

    print "move right"
    bh.moveHand([0,0,0,0], [1,1,1,1], [2000,2000,2000,2000], 1000, hold=False)
    bh.waitForHand()

    print "move right 90"
    bh.moveHand([0,0,0,90.0/180.0*math.pi], [1,1,1,1], [2000,2000,2000,2000], 1000, hold=False)
    bh.waitForHand()

    print "move right"
    bh.moveHand([0,0,0,0], [1,1,1,1], [2000,2000,2000,2000], 1000, hold=False)
    bh.waitForHand()

