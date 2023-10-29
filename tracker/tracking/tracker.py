import time
from turtle import pos
import numpy
import asyncio
from typing import List
from components.TimeSeriesData import TimeSeriesData
from components.FrameResult import FrameResult
from components.Point2i import Point2i
from processer import Processer
from components.camera.CameraDriverReturn import CamController
from components.ItemResult import ItemResult
from components.Rectangle import Rectangle
from components.ItemFinder import ItemExplorer
from components.ResultImgCreator import ResultImgCreator
from components.FormData import postData
import cv2
import datetime

# 単体テスト用のimport
from components.testcomponents.processorForTest import ProcessorForTest
from components.testcomponents.TestDatabaseCreator import TestDatabaseCreator
from components.testcomponents.TestLable import TestLabel

class Tracker():
    def __init__(self, studiedData):
        self._roopCounter:int = 0
        self._studiedData = studiedData
        self._resDB:List[TimeSeriesData] = []
        self._itemCount:int = 0
        self._threshListCount = 10 # 保存するフレーム数
        self._cam:CamController = CamController(0)
        self._itemExp:ItemExplorer = ItemExplorer()
        self._resImgCreator:ResultImgCreator = ResultImgCreator([0, 255, 0], [211, 0, 148])
        #self._proc = ProcessorForTest(10)
        self._proc = Processer()
        self._nowKeysList = []
        self._formerKeysList = []
        
    
    def InitResDB(self, procResult:List[ItemResult], frame:numpy, time:datetime):
        for i in range(len(procResult)):
            res = FrameResult(0, procResult[i].Box,  time, frame, frame)
            self._resImgCreator.CreateImg(res, procResult[i].Label)
            self._resDB.append(TimeSeriesData(procResult[i].Label, res))


    def Execute(self):
        # TODO 1. もっさの画像処理部分を統合する
        self.snapdate, self.RawImg = self._cam.GetFrame()
        # TODO 2. YOLOv5で物体検出部分を実装する
        self.ProcResult = self._proc.Execute(self.RawImg)

        # TODO 3. 今回のループで検出した物体の総数 > 前回のループの総数のとき，新たに物体をDBに登録する
        # TODO 2.で検出した物体数を"0"の部分に代入する．
        if (self._roopCounter > 0):
            self._nowKeysList = list(self._proc.DetectedItemDict.keys())
            self._formerKeysList = list(self._formerDetectedItemDic.keys())
            if (len(self.ProcResult) > self._itemCount):
                for i in range(len(self._nowKeysList)):
                    self._isMakeRegist:bool = False
                    if(self._nowKeysList[i] not in self._formerKeysList):
                        self._isMakeRegist = True
                    if(self._isMakeRegist == False):
                        if(self._proc.DetectedItemDict[self._nowKeysList[i]] > self._formerDetectedItemDic[self._nowKeysList[i]]):
                            self._isMakeRegist = True
                    if(self._isMakeRegist):
                        self.addedProcRes = FrameResult(self._roopCounter, self.ProcResult[i].Box, self.snapdate,\
                                                        self.RawImg, self.RawImg) # 結局位置データは使わないことになってるので，一旦ProcResultの整合性は横に置く
                        self._resImgCreator.CreateImg(self.addedProcRes, self._nowKeysList[i])
                        self.addedItem = TimeSeriesData(self._nowKeysList[i], self.addedProcRes)
                        self._resDB.append(self.addedItem)
                        print(f"[ADD  ] : {self._nowKeysList[i]}")
        else:
            self.InitResDB(self.ProcResult, self.RawImg, self.snapdate)
        
        # 追跡中の物体の各々について，データベースを更新する．
        for i in range(len(self.ProcResult)):
            # TODO このフレームの画像処理結果をデータベースに保存する．
            self._framaRes = FrameResult(self._roopCounter, self.ProcResult[i].Box, self.snapdate, self.RawImg, numpy.zeros(8))
            self._resImgCreator.CreateImg(self._framaRes, self.ProcResult[i].Label)
            self._foundDBIdx:int = self._itemExp.FindFromLabelInResDB(self._resDB, self.ProcResult[i].Label)
            self._resDB[self._foundDBIdx].Result.append(self._framaRes)
            
            # 一番古いデータを削除する．
            if(len(self._resDB[self._foundDBIdx].Result) >  self._threshListCount):
                del(self._resDB[self._foundDBIdx].Result[0])
        
        # TODO 物体が消えた場合の処理を追加する
        if (len(self.ProcResult) < self._itemCount):
            if(len(self._nowKeysList)==0):
                self._isDeleteRegist:bool = True
                self._removeIdx = 0
                postData(
                    label = self._formerKeysList[self._removeIdx],
                    rawimg=self.RawImg,
                    detectimg=self.RawImg
                )
                del self._resDB[self._removeIdx]
                print(f"[ALL REMOVE]")
            else:
                for i in range(len(self._nowKeysList)):
                    self._isDeleteRegist:bool = False
                    if(self._nowKeysList[i] not in self._formerDetectedItemDic):
                        self._isDeleteRegist = True
                    if(self._isDeleteRegist == False):
                        if(self._proc.DetectedItemDict[self._nowKeysList[i]] < self._formerDetectedItemDic[self._nowKeysList[i]]):
                            self._isDeleteRegist = True
                    if(self._isDeleteRegist):
                        self._removeIdx = self._itemExp.FindFromLabelInResDB(self._resDB, self._nowKeysList[i])
                        postData(
                            label = self._nowKeysList[i],
                            rawimg=self.RawImg,
                            detectimg=self.RawImg
                        )
                        del self._resDB[self._removeIdx]
                        print(f"[REMOVE] : {self._nowKeysList[i]}")
            # 消えた場合は，フロント側のデータベースに情報を受け渡す
            # 消えていなければ，pass
        
        # 次ループに向けた後処理
        self._roopCounter = self._roopCounter + 1
        self._itemCount = len(self.ProcResult)
        # ディクショナリーのコピー
        self._formerDetectedItemDic = self._proc.DetectedItemDict.copy()
        self._proc.DetectedItemDict = {}

if __name__ == "__main__":
    app=Tracker("trial")
    elapsedSec = 100
    startTime = time.time()
    while True:
        app.Execute()
        #cv2.imshow("result", app._resDB[0].Result[-1].ResultImg)
        #cv2.waitKey(33)
        #if((time.time() - startTime) > elapsedSec):
        #    break
    #dataCount = 10
    #initExp = ItemExplorer()
    #proc = ProcessorForTest(dataCount)
    #procResult = proc.Execute()
    #database = TestDatabaseCreator(dataCount)
    #testLabel = TestLabel(dataCount)
    #for i in range(dataCount):
    #    dbCount = initExp.FindFromLabelInProcRes(procResult, testLabel.LabelList[i])
    #    resCount = initExp.FindFromLabelInResDB(database.dbList, testLabel.LabelList[i])
    #    print(f"Label: {testLabel.LabelList[i]}, db: {dbCount}, res: {resCount}")



