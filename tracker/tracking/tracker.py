import time
import numpy
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
            if (len(self.ProcResult) > self._itemCount):
                pass
                #self._resDB.append(TimeSeriesData("適当なラベル名"))
        else:
            self.InitResDB(self.ProcResult, self.RawImg, self.snapdate)
        
        # 追跡中の物体の各々について，データベースを更新する．
        for i in range(len(self._resDB)):
            # TODO このフレームの画像処理結果をデータベースに保存する．
            self._framaRes = FrameResult(self._roopCounter, self.ProcResult[i].Box, self.snapdate, self.RawImg, numpy.zeros(8))
            self._resImgCreator.CreateImg(self._framaRes, self.ProcResult[i].Label)
            self._foundDBIdx:int = self._itemExp.FindFromLabelInResDB(self._resDB, self.ProcResult[i].Label)
            self._resDB[self._foundDBIdx].Result.append(self._framaRes)
        
            # 一番古いデータを削除する．
            if(len(self._resDB[self._foundDBIdx].Result) >  self._threshListCount):
                del(self._resDB[self._foundDBIdx].Result[0])
        
            # TODO 物体が消えた場合の処理を追加する
                # 消えた場合は，フロント側のデータベースに情報を受け渡す
                # 消えていなければ，pass
        
        # 次ループに向けた後処理
        self._roopCounter = self._roopCounter + 1
        self._itemCount = len(self.ProcResult)

if __name__ == "__main__":
    app=Tracker("trial")
    elapsedSec = 10
    startTime = time.time()
    while True:
        app.Execute()
        cv2.imshow("result", app._resDB[0].Result[-1].ResultImg)
        cv2.waitKey(33)
        if((time.time() - startTime) > elapsedSec):
            break
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



