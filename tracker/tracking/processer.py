from ultralytics import YOLO
from components.ItemResult import ItemResult
from components.Point2i import Point2i
from components.Rectangle import Rectangle
from typing import List

class Processer():
    def __init__(self):
        self.__conf=0.3
        self.__iou=0.5
        self.__showflag=True
        self.itemresult:List[ItemResult] = []

    def Execute(self,path):
        model = YOLO("tracker/tracking/yolov8n.pt")
        results = model.track(
        source=path,
        conf=self.__conf, 
        iou=self.__iou, 
        show=self.__showflag
        )
        for i in range(len(results[0].boxes)):
            is_track=results[0].boxes[i].is_track
            coordinates=results[0].boxes[i]
            leftcoordinatex=results[0].boxes[i].xyxy[0][0]
            leftcoordinatey=results[0].boxes[i].xyxy[0][1]
            rightcoordinatex=results[0].boxes[i].xyxy[0][2]
            rightcoordinatey=results[0].boxes[i].xyxy[0][3]
            rect=RectangleFactory(leftcoordinatex,leftcoordinatey,rightcoordinatex,rightcoordinatey)
            item=ItemResult("",is_track,rect)
            self.itemresult.append(item)
            #print(coordinates)
            #print(coordinates[0])
            #print(results[0].boxes[0])
        return self.itemresult

def RectangleFactory(leftx,lefty,rightx,righty):
    coordinate=Point2i(leftx,lefty)
    width=rightx-leftx
    height=righty-lefty
    rect=Rectangle(coordinate,width,height)
    return rect
