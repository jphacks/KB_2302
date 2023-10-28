import numpy
from components.Point2i import Point2i


class FrameResult():
    """
    ある時刻(フレーム)の結果データ
    
    Parameters
    ----------
    Index : int
        インデックス(輪番とする)
    Position : point2i
        フレームにおける検出物体の位置(座標系注意)
    time : float
        フレームの時刻(time.time()で取得した値を格納したい)
    RawImg : numpy
        カメラから取得した画像データそのもの
    ResultImg : numpy
        RawImgを処理し，物体検出結果を重ね合わせた画像データ
    """
    def __init__(self, index:int, position:Point2i, time:float, rawImg:numpy, resultImg:numpy):
        self.Index:int = index
        self.Position:Point2i = position
        self.Time:float = time
        self.RawImg:numpy = rawImg
        self.ResultImg:numpy = resultImg 