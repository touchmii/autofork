import evdev
from queue import Queue
import asyncio
from evdev import InputDevice, categorize, ecodes
import logging
import warnings
#logging.basicConfig(level=logging.DEBUG)
device_path = ''

def find_device():
    global device_path
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)
        if( device.name == 'ShanWan PS3/PC Gamepad'):
            device_path = device.path
    if(device_path != ''):
        print('find Gamepad device: {}'.format(device_path))
        dev = evdev.InputDevice(device_path)
    return dev
async def read_event(dev, queue):
    async for ev in dev.async_read_loop():
        #print(ev.type == 3)
        if( ev.type == 3 or ev.type == 1):
            #print(repr(ev))
            ev_l = [ev.type, ev.code, ev.value]
            queue.put_nowait(ev_l)
            print(queue.qsize())
            e, v = detect_event(ev_l)
            print('Detect {} action {}'.format(e, v))

def detect_event(event):
    joystick_dict = {1:'LEFT_Y', 0:'LEFT_X', 2:'RIGHT_X', 5:'RIGHT_Y', 0x10:'UPDOWN', 0x11:'LEFTRIGHT'}
    button_dict = {0x123:'SQUARE', 0x120:'TRIANGLE', 0x121:'CIRCLE', 0x122:'CROSS', 0x124:'L1',0x125:'R1', 0x126:'L2', 0x127:'R2', 0x12A:'L_JOYSTICK', 0x12B:'R_JOYSTICK', 0x128:'SELECT', 0x129:'START'}
    e, v = '', None
    if(event[0] == 3):
        e = joystick_dict[event[1]]
        v = event[2]
    elif(event[0] == 1):
        e = button_dict[event[1]]
        v = event[2]
    else:
        pass
    return e, v

if __name__ == "__main__":
    dev = find_device()
    q = Queue()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(read_event(dev, q))
