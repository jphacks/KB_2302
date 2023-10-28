from components.TimeSeriesData import TimeSeriesData
from typing import List
from components.testcomponents.TestLable import TestLabel
from components.Rectangle import Rectangle
from components.Point2i import Point2i
from components.FrameResult import FrameResult
import numpy

class TestDatabaseCreator():
    def __init__(self, length:int):
        self.dbList:List[TimeSeriesData] = []
        self.testLabel = TestLabel(length)
        for i in range(length):
            item = FrameResult(i, Point2i(i, i), 0, numpy.zeros(8), numpy.zeros(8))
            self.dbList.append(TimeSeriesData(self.testLabel.LabelList[i], item))
            # self.dbList.append(ItemResult(self.testLabel[i], True, Rectangle(Point2i(i, i), 10*i, 11*i)))