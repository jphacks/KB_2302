from ultralytics import YOLO

class Processer():
    def __init__(self):
        self.__conf=0.3
        self.__iou=0.5
        self.__showflag=True

    def Execute(self,path):
        model = YOLO('yolov8n.pt')
        results = model.track(
        source=path,
        conf=self.__conf, 
        iou=self.__iou, 
        show=self.__showflag
        )