import canopen

if __name__ == "__main__":
    network = canopen.Network()
    #network.connect(channel='can0', bustype='socketcan')
    network.connect(channel=0 , bustype='canalystii', bitrate=500000)
    #time.sleep(0.5)
    motor3 = network.add_node(1, 'KINCO-JDFD.EDS')
    #time.sleep(0.5)
    motor3.sdo['Controlword'].raw = 0xf
