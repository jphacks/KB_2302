# cv2のインポート前にカメラに関する設定を行う(起動速度低下対策)
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import datetime

def save_frame(cam_num, dir):       # cam_num：0=内蔵カメラ, 1,2,...=外付けカメラ
    cap = cv2.VideoCapture(cam_num)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Window', frame)
        if cv2.waitKey(33) == 27:       # 30fpsなので33ms待機, ESCキーで終了
            break
        strdate=datetime.datetime.now().strftime('%Y%m%dT%H%M%S%f') # 撮影時刻の生成
        fname=dir + strdate + ".jpg"    # ファイル名の結合
        cv2.imwrite(fname, frame)
    cap.release()                       # メモリの開放
    cv2.destroyAllWindows()             # 画面消去

save_frame(1, 'tracker/camera/buffer/') 