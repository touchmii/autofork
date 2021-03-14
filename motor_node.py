WheelDiff = 0.59
WheelRadius = 0.16/15
WheelRatio = 15
LeftWheelCmd = 0
RightWheelCmd = 0


def cal_vel(vx, w):
    LeftWheelCmd = (vx - w*WheelDiff*0.5)/WheelRadios
    RightWheelCmd = (vx + w*WheelDiff*0.5)/WheelRadius
    
