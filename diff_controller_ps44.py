import canopen

from controller_ps4 import *

class f124():
    def __init__(self, net, node, eds):
        self.rpm_scale = 5120000/1875
        self.motor_mode_dict = {'pulse':-1,'immediate speed':-3, 'torque':4, 'localtion':1, 'speed':3, 'home':6, 'interpolation':7, 'ecan_location':8, 'ecan_speed':9, 'ecan_torque':10}
        self.motor_status_list = ['Ready_on', 'Switched_on', 'Operatetion_enable', 'Fault', 'Voltage_enable', 'Quick_stop', 'Switchon_disable', 'Warning', 'Manunfacture0', 'Remote', 'Target_reached', 'Intlim_active', 'Setpoint_Ack', 'Fllowing_Error', 'Commutation_found', 'Reference_Found']
        self.motor_control_dict = {'enable_speed':0x0F, 'enable_localtion':0x2F, 'disable':0x06, 'reset':'0x86'}

        self.node = net.add_node(node, eds)
    def set_node_status(self, state):
        self.node.state = state
    def set_motor_mode(self, mode):
        self.node.sdo['Modes_of_operation'].raw = self.motor_mode_dict[mode]
    def set_motor_speed(self, speed):
        self.node.sdo['Target_velocity'].raw = speed*self.rpm_scale
    def get_motor_speed(self):
        return self.node.sdo['Velocity_actual_value'].raw/self.rpm_scale
    def set_motor_control(self, state):
        self.node.sdo['Controlword'].raw = self.motor_control_dict[state]
    def get_motor_state(self):
        return self.node.sdo['Statusword'].raw
    def set_motor_direct(self, dir=0):
        self.node.sdo['Polarity'].raw = dir

async def motion_control(q):
    network = canopen.Network()
    network.connect(channel='can0', bustype='socketcan')
#    network.connect(channel=0 , bustype='canalystii', bitrate=500000)
    motor1 = f124(network, 1, 'KINCO-JDFD.EDS')
    motor2 = f124(network, 2, 'KINCO-JDFD.EDS')

    motor1.node.sdo['Controlword'].raw = 0x86
    motor2.node.sdo['Controlword'].raw = 0x86
#    time.sleep(0.5)
#    motor2.set_motor_control('disable')
#    motor2.set_motor_control('reset')
    motor1.set_motor_direct(1)
    motor1.set_motor_mode('speed')
    #motor1.set_motor_direct(1)
    motor2.set_motor_mode('speed')
    motor1.node.sdo['Profile_acceleration'].raw = 163.84*40
    motor1.node.sdo['Profile_deceleration'].raw = 163.84*40
    motor2.node.sdo['Profile_acceleration'].raw = 163.84*40
    motor2.node.sdo['Profile_deceleration'].raw = 163.84*40
    motor1.set_motor_speed(0)
    motor2.set_motor_speed(0)
    motor1.set_motor_control('enable_speed')
    motor2.set_motor_control('enable_speed')
    print('motor init ok')
    while True:
        command = await q.get()
        print('left_motor_speed: {}, right_motor_speed: {}'.format(command[0],command[1]))
        motor1.set_motor_speed(command[0])
        motor2.set_motor_speed(command[1])
        await asyncio.sleep(0.005)

async def joystick_control(event_queue, command_q):
    motor1_speed = 0
    motor2_speed = 0
    diff = 0
    event_q = event_queue
    speed_up = 1
    while True:
        event = await event_q.get()
        #event_q.task_done()
        #print(event)

        if(event[0] == 3):
            if(event[1] == 1):
                motor1_speed = 127-event[2]
            elif(event[1] == 5):
                motor2_speed = 127-event[2]
            elif(event[1] == 2):
                diff = event[2]-127
            command_q.put_nowait([(motor1_speed*10+diff*abs(motor1_speed)/31.75+3*diff)*speed_up, (motor1_speed*10-diff*abs(motor1_speed)/31.75-3*diff)*speed_up])
        elif(event[0] == 1):
            if(event[1] == 0x127):
                speed_up = event[2]*1.36+1
            #elif(event[1] == 0x126):
            #    speed_up = speed_up + (speed_up-2)event[2]*1.18
            #print(motor1_speed, motor2_speed)
            command_q.put_nowait([(motor1_speed*10+diff*abs(motor1_speed)/31.75+3*diff)*speed_up, (motor1_speed*10-diff*abs(motor1_speed)/31.75-3*diff)*speed_up])
            #print('command_q size: {}'.format(command_q.qsize()))
        #await asyncio.sleep(0.01)
if __name__ == "__main__":
    dev = find_device()
    q = asyncio.Queue()
    command_q = asyncio.Queue()
    loop = asyncio.get_event_loop()
    tasks = [asyncio.Task(read_event(dev, q)), asyncio.Task(motion_control(command_q)), asyncio.Task(joystick_control(q, command_q))]
    #tasks = [asyncio.Task(read_event(dev, q)), asyncio.Task(joystick_control(q, command_q))]
    loop.run_until_complete(asyncio.wait(tasks))

