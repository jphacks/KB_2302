from typing import List
from components.TimeSeriesData import TimeSeriesData
from components.ItemResult import ItemResult

class ItemExplorer():
    def __init__(self):
        pass

    def FindFromLabelInResDB(self, inputList:List[TimeSeriesData], keyLabel:str):
        return list(map(lambda x:x.Label, inputList)).index(keyLabel)
    
    def FindFromLabelInProcRes(self, inputList:List[ItemResult], keyLabel:str):
        return list(map(lambda x:x.Label, inputList)).index(keyLabel)