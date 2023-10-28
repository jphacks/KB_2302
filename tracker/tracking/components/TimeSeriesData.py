from typing import List
from FrameResult import FrameResult

class TimeSeriesData:
    """
    ある物体における検出結果の時系列データ
    
    Parameters
    ----------
    label : str
        検出物体の名称(検索時のキーワード)
    Result : list[FrameResult]
        検出結果の時系列データ
    """
    def __init__(self, label:str):
        self.Label:str = label
        self.Result:List[FrameResult] = []