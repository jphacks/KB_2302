from components.TimeSeriesData import TimeSeriesData
from components.FrameResult import FrameResult
from components.Point2i import Point2i
from typing import List
import time
import numpy

class Tracker:
    def __init__(self, studiedData):
        self._studiedData = studiedData
        self._resDB:List[TimeSeriesData] = []
        self._itemCount:int = 0
        self._threshListCount = 10 # 保存するフレーム数

    def Execute(self):
        # TODO 1. もっさの画像処理部分を統合する

        # TODO 2. YOLOv5で物体検出部分を実装する

        # 検出された物体が新たに増えたかどうか判定
        # TODO 2.で検出した物体数を"0"の部分に代入する．
        if( 0 < self._itemCount):
            self._resDB.append(TimeSeriesData("適当なラベル名"))
        
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



