from ultralytics import YOLO

class Processer():
    def __init__(self):
        self.__conf=0.3
        self.__iou=0.5
        self.__showflag=True
        self.__model = YOLO('yolov8n.pt')

    def Execute(self,path):
        results = self.__model.track(
        source=path,
        conf=self.__conf, 
        iou=self.__iou, 
        show=self.__showflag
        )

        results.show()