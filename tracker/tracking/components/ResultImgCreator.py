from typing import List
import cv2
import copy
from components.FrameResult import FrameResult

class ResultImgCreator():
    def __init__(self, rectangleColorBGR:List[int], strColorBGR:List[int]):
        self._rectangleBGR:List[int] = rectangleColorBGR
        self._strBGR:List[int] = strColorBGR

    def CreateImg(self, result:FrameResult, string:str):
        result.ResultImg = copy.deepcopy(result.RawImg)
        cv2.rectangle(result.ResultImg, (result.Rectangle.UpperLeftPoint.X, result.Rectangle.UpperLeftPoint.Y), \
                      (result.Rectangle.UpperLeftPoint.X + result.Rectangle.Width, result.Rectangle.UpperLeftPoint.Y + result.Rectangle.Height),\
                          (self._rectangleBGR[0], self._rectangleBGR[1], self._rectangleBGR[2]), 2)
        #cv2.putText(result.ResultImg, string, result.Rectangle.UpperLeftPoint, 0, 5.0, \
        #            (self._strBGR[0], self._strBGR[1], self._strBGR[2]))