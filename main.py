import cv2
from pathlib import Path
import argparse
import time
import json
from src.lp_recognition import E2E
import serial

def read_json(path):
    with open(path) as f:
        return json.load(f)

license_plate_data = read_json('./data.json')

cap = cv2.VideoCapture(0)

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=2)

def write_read(x):
    arduino.write(x)

# read image
while True:
    ret, img = cap.read()
    if ret:
        # start
        # start = time.time()

        # load model
        model = E2E()

        # recognize license plate
        try:
            image, license_plate = model.predict(img)
            license_plate.replace('-', '')
            license_plate.replace(' ', '')
            license_plate.replace('.', '')
            if license_plate in license_plate_data:
                print("License Plate detected: {}".format(license_plate))
                try:
                    write_read(b'1')
                except:
                    print("send esp error")

        except:
            print("license recognize error")
        # # end
        # end = time.time()

        # print('Model process on %.2f s' % (end - start))

        # show image
        cv2.imshow('Nhan dien bang so', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
