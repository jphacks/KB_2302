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
        self._cam:CamController = CamController(1)
        #self._proc = ProcessorForTest(10)
        self._proc = Processer()
    
    def InitResDB(self, procResult:List[ItemResult], frame:numpy, time:datetime):
        for i in range(len(procResult)):
            res = FrameResult(0, procResult[i].Box.UpperLeftPoint,  time, frame, frame)
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
                self._resDB.append(TimeSeriesData("適当なラベル名"))
        else:
            self.InitResDB(self.ProcResult, self.RawImg, self.snapdate)
        
        # 追跡中の物体の各々について，データベースを更新する．
        for i in range(len(self._resDB)):
            # TODO このフレームの画像処理結果をデータベースに保存する．
            self._resDB[i].Result.append(FrameResult(0, Point2i(0,0), time.time(), numpy.zeros(), numpy.zeros()))
        
            # 一番古いデータを削除する．
            if(len(self._resDB[i].Result) <  self._threshListCount):
                del(self._resDB[i].Result[0])
        
            # TODO 物体が消えた場合の処理を追加する
                # 消えた場合は，フロント側のデータベースに情報を受け渡す
                # 消えていなければ，pass
        self._roopCounter = self._roopCounter + 1

if __name__ == "__main__":
    app=Tracker("trial")
    app.Execute()
    dataCount = 10
    initExp = ItemExplorer()
    proc = ProcessorForTest(dataCount)
    procResult = proc.Execute()
    database = TestDatabaseCreator(dataCount)
    testLabel = TestLabel(dataCount)
    for i in range(dataCount):
        dbCount = initExp.FindFromLabelInProcRes(procResult, testLabel.LabelList[i])
        resCount = initExp.FindFromLabelInResDB(database.dbList, testLabel.LabelList[i])
        print(f"Label: {testLabel.LabelList[i]}, db: {dbCount}, res: {resCount}")



