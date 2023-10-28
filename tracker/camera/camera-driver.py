# cv2のインポート前にカメラに関する設定を行う(起動速度低下対策)
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import datetime

class CamController():
    def __init__(self, cam_num:int) -> None:
        self.cap = cv2.VideoCapture(cam_num)

    def save_frame(self, dir):       # cam_num：0=内蔵カメラ, 1,2,...=外付けカメラ
        while True:
            ret, frame = self.cap.read()
            cv2.imshow('Window', frame)
            if cv2.waitKey(33) == 27:       # 30fpsなので33ms待機, ESCキーで終了
                break
            strdate=datetime.datetime.now().strftime('%Y%m%dT%H%M%S%f') # 撮影時刻の生成
            fname=dir + strdate + ".jpg"    # ファイル名の結合
            cv2.imwrite(fname, frame)
        # self.cap.release()                       # メモリの開放
        cv2.destroyAllWindows()             # 画面消去

    def release(self):
        self.cap.release()

cam = CamController(1)

cam.save_frame('tracker/camera/buffer/') 

print("1")

cam.save_frame('tracker/camera/buffer/') 
