from ultralytics import YOLO
from components.ItemResult import ItemResult
from components.Point2i import Point2i
from components.Rectangle import Rectangle
from typing import List
from components.TargetLabel import GetTargetLabel

class Processer():
    def __init__(self):
        self.__conf=0.3
        self.__iou=0.5
        self.__showflag=True
        self.itemresult:List[ItemResult] = []
        self.__dict={}

    def Execute(self,frame):
        model = YOLO("tracker/tracking/yolov8n.pt")
        results = model.track(
        frame,
        conf=self.__conf, 
        iou=self.__iou, 
        show=self.__showflag
        )
        for i in range(len(results[0].boxes)):
            is_track=results[0].boxes[i].is_track
            labelid=int(results[0].boxes[i].cls[0])
            label=results[0].names[labelid]
            
            # targetにないラベルは無視する
            if label not in GetTargetLabel():
                continue
            
            elif(label not in self.__dict):
                self.__dict[label]=1
            else:
                init=self.__dict[label]
                self.__dict[label]=init+1
                
            label=label+str(self.__dict[label])
            leftcoordinatex=int(results[0].boxes[i].xyxy[0][0])
            leftcoordinatey=int(results[0].boxes[i].xyxy[0][1])
            rightcoordinatex=int(results[0].boxes[i].xyxy[0][2])
            rightcoordinatey=int(results[0].boxes[i].xyxy[0][3])
            print(type(leftcoordinatex))
            rect=RectangleFactory(leftcoordinatex,leftcoordinatey,rightcoordinatex,rightcoordinatey)
            item=ItemResult(label,is_track,rect)
            self.itemresult.append(item)
        return self.itemresult

def RectangleFactory(leftx,lefty,rightx,righty):
    coordinate=Point2i(leftx,lefty)
    width=rightx-leftx
    height=righty-lefty
    rect=Rectangle(coordinate,width,height)
    return rect
