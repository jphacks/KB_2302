# cv2のインポート前にカメラに関する設定を行う(起動速度低下対策)
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import datetime

class CamController():
    def __init__(self, cam_num:int) -> None:
        self.cap = cv2.VideoCapture(cam_num)

    def GetFrame(self):       # cam_num：0=内蔵カメラ, 1,2,...=外付けカメラ
        ret, frame = self.cap.read()
        return datetime.datetime.now(), frame

    def release(self):
        self.cap.release()
"""
if __name__ == "__main__":
    cam = CamController(1)
    date, frame = cam.GetFrame()
    cv2.imshow("result", frame)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
"""