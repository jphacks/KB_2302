from tabnanny import verbose
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
        self.__persist = True
        self.itemresult:List[ItemResult] = []
        self.DetectedItemDict={}
        self._model = YOLO("yolov8n.pt")

    def Execute(self,frame):
        self.itemresult.clear()
        self.results = self._model.track(
            frame,
            conf=self.__conf, 
            iou=self.__iou, 
            persist=self.__persist,
            show=self.__showflag,
            verbose=False,
        )
        for i in range(len(self.results[0].boxes)):
            self.is_track=self.results[0].boxes[i].is_track
            self.labelid=int(self.results[0].boxes[i].cls[0])
            self.label=self.results[0].names[self.labelid]
            
            # targetにないラベルは無視する
            if self.label not in GetTargetLabel():
                continue
            
            elif(self.label not in self.DetectedItemDict):
                self.DetectedItemDict[self.label]=1
            else:
                self.init=self.DetectedItemDict[self.label]
                self.DetectedItemDict[self.label]=self.init+1
                
            #self.label=self.label+str(self.DetectedItemDict[self.label])
            self.leftcoordinatex=int(self.results[0].boxes[i].xyxy[0][0])
            self.leftcoordinatey=int(self.results[0].boxes[i].xyxy[0][1])
            self.rightcoordinatex=int(self.results[0].boxes[i].xyxy[0][2])
            self.rightcoordinatey=int(self.results[0].boxes[i].xyxy[0][3])
            self.rect=RectangleFactory(self.leftcoordinatex,self.leftcoordinatey,self.rightcoordinatex,self.rightcoordinatey)
            self.item=ItemResult(self.label,self.is_track,self.rect)
            self.itemresult.append(self.item)

        return self.itemresult

def RectangleFactory(leftx,lefty,rightx,righty):
    coordinate=Point2i(leftx,lefty)
    width=rightx-leftx
    height=righty-lefty
    rect=Rectangle(coordinate,width,height)
    return rect
