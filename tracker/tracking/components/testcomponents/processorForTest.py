import sys
sys.path.append("~/tracking")

from components.ItemResult import ItemResult
from components.Rectangle import Rectangle
from components.Point2i import Point2i
from typing import List
from components.testcomponents.TestLable import TestLabel

class ProcessorForTest():
    def __init__(self, listLength:int):
        self.ReturnList:List[ItemResult] = []
        self.label = TestLabel(listLength)
        # テスト用の仮の結果リストを作成, 要素数listLength
        for i in range(listLength):
            rect = Rectangle(Point2i(i, i), i * 10, i * 11)
            self.ReturnList.append(ItemResult(self.label.LabelList[i], True, rect))
    
    def Execute(self) -> List[ItemResult]:
        return self.ReturnList