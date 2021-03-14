# coding: utf-8
import canopen
network = canopen.Network()
network.connect(channel='can0', bustype='socketcan')
node = network.add_node(5, 'KINCO-JDFD.eds')
node = network.add_node(5, 'KINCO-JDFD.EDS')
node.nmt.state = 'OPERATIONAL'
node.sdo['Mode of operation'].raw = 0x01
node.sdo['Modes_of_operation'].raw = 0x01
node1 = network.add_node(1, 'KINCO-JDFD.EDS')
node1.nmt.state = 'OPERATIONAL'
node1.sdo['Modes_of_operation'].raw = 0x01
node1.sdo['Modes_of_operation'].raw = 0x03
node1.sdo['Target_velocity'].raw = 0xFF
node1.sdo['Target_velocity'].raw = 0xFFF
node1.sdo['Target_velocity'].raw = 0xFFFF
node1.sdo['Controlword'].raw = 0xF
node1.sdo['Target_velocity'].raw = 0xFFFFF
node2 = network.add_node(2, 'KINCO-JDFD.EDS')
node2.nmt.state = 'OPERATIONAL'
node2.sdo['Modes_of_operation'].raw = 0x03
node2.sdo['Target_velocity'].raw = 0xFFFFF
node2.sdo['Controlword'].raw = 0xF
node2.tpdo.read()
node2.rpdo.read()
node2.sdo['Controlword']
s = node2.sdo['Controlword']
s
s.data
s.raw
node2.sdo['Target_velocity'].raw
get_ipython().magic('save motor.py')
get_ipython().magic('save motor.py ~0/')
node2.sdo['Statusword'].raw
node2.sdo['Statusword'].bit
node2.sdo['Statusword'].data
node2.sdo['Statusword'].bits
s.get_data
node2.sdo['Statusword'].bits
node2.sdo['Velocity_actual_value'].data
node2.sdo['Velocity_actual_value'].raw
node2.sdo['Max_current'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Current_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo['Position_actual_value'].raw
node2.sdo[0x6079].raw
node2.sdo[0x1000].raw
node2.sdo[0x1003].raw
node2.sdo['Statusword'].desc
node2.sdo['Statusword'].phys
node2.nmt.state = 'PRE-OPERATIONAL'
node2.tpd[4].clear()
node2.tpdo[4].clear()
node2.tpdo[4].add_variable('Position_actual_value')
node2.tpdo[4].add_variable('Velocity_actual_value')
node2.tpdo[4].trans_type = 254
node2.tpdo[4].even_timer = 10
node2.tpdo[4].enable = True
node.tpdo.save()
node2.tpdo.read()
node2.tpd[4].clear()
node2.tpdo[4].clear()
node2.tpdo[4].add_variable('Position_actual_value')
node2.tpdo[4].add_variable('Velocity_actual_value')
node2.tpdo[4].trans_type = 254
node2.tpdo[4].even_timer = 10
node2.tpdo[4].enable = True
node2.tpdo.save()
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = noe2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}').format(speed, velocity)
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}').format(speed, velocity)
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
node2.nmt.state = 'OPERATIONAL'
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('speed: {}, velocity: {}'.format(speed, velocity))
    
for i in range(50):
    node2.tpdo[4].wait_for_reception()
    speed = node2.tpdo['Position_actual_value'].raw
    velocity = node2.tpdo['Velocity_actual_value'].raw
    print('position: {}, velocity: {}'.format(speed, velocity))
    
get_ipython().magic('save motor.py ~0/')
