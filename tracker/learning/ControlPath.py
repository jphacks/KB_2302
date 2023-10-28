import os

# このファイルの実行位置を取得
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# yolov8n.ptをロード
YOLO_ORI_FILE  = os.path.join(CURRENT_FOLDER, "yolov8n.pt")

BEST_FILE  = os.path.join(CURRENT_FOLDER, "best.pt")
