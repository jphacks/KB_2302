from components.Rectangle import Rectangle

class ItemResult():
    def __init__(self, label:str, isDetected:bool, box:Rectangle):
        self.Label:str = label
        self.IsDetected:bool = isDetected
        self.Box:Rectangle = box