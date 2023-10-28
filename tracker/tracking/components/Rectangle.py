from components.Point2i import Point2i

class Rectangle():
    def __init__(self, upperLeftPoint:Point2i, width:int, height:int):
        self.UpperLeftPoint:Point2i = upperLeftPoint
        self.Width:int = width
        self.Height:int = height