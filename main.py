
# import os
import time
from robot import Robot
import numpy as np

workspace_limits = np.asarray([[0.3, 0.748], [-0.224, 0.224], [-0.255, -0.1]])
robot= Robot(workspace_limits)
robot.move_to_position([0.15,0.25,0.2,0, 1,0,0])
print("robot move to position A:(0.15,0.25,0.2)")
time.sleep(0.5)

robot.move_to_position([-0.35,-0.11,0.1,0, 1,0,0])
print("robot move to position B:(-0.35,-0.11,0.1)")