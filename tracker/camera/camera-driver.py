#!/usr/bin/env python

import cv2

deviceid=0 # it depends on the order of USB connection. 
capture = cv2.VideoCapture(deviceid)

ret, frame = capture.read()
cv2.imwrite('test.jpg', frame)