class FormData():
    """
    DBに渡す形
    
    Parameters
    ----------
    Usr : str
        username
    Roomid : int
        room number
    Cameraid : int
        camera number
    Label : str
        label name
    RawImg : 
        カメラから取得した画像データ
    DetectImg : 
        RawImgを処理した画像データ
    """
    def __init__(self,user:str,roomid:int,cameraid:int,label:str,rawimg,detectimg):
        self.User=user
        self.Roomid=roomid
        self.Cameraid=cameraid
        self.Label=label
        self.RawImg=rawimg
        self.DetectImg=detectimg
