class Point2i:
    """
    画像平面内での座標を定義するクラス\n
    座標系は(OpenCVと統一するために)画像の左上端点を原点として，Xを右向き正，Yを下向き正とする．
    
    Parameters
    ----------
    X : int
        X方向位置
    Y : int
        Y方向位置
    """
    def __init__(self, x:int, y:int):
        self.X = x
        self.Y = y