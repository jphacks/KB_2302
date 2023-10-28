from components.Point2i import Point2i

class Rectangle():
    def __init__(self, upperLeftPoint:Point2i, width:float, height:float):
        self.UpperLeftPoint:Point2i = upperLeftPoint
        self.Width:float = width
        self.Height:float = height