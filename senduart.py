import serial

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=2)

def write_read(x):
    arduino.write(x)
    print(arduino.readline())

try:
    write_read(b'1')
except:
    print("send esp error")
