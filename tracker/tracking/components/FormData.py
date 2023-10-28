import cv2
import io
import requests
import asyncio
import aiohttp

url = "https://kb2302-jphack-471e16480034.herokuapp.com/tracker/lost"

def postData(
        label:str,
        rawimg,
        detectimg,
        user:str = "SSSRC",
        room_id:int = 1,
        camera_id:int = 1,
    ):
    
    asyncio.run(
        __postData(
            label=label,
            rawimg=rawimg,
            detectimg=detectimg,
            user=user,
            room_id=room_id,
            camera_id=camera_id,
            )
        )

async def __postData(
        label:str,
        rawimg,
        detectimg,
        user:str = "SSSRC",
        room_id:int = 1,
        camera_id:int = 1,
    ):
    """
    DBに渡す形
    
    Parameters
    ----------
    Usr : str
        username
    room_id : int
        room number
    camera_id : int
        camera number
    Label : str
        label name
    RawImg : 
        カメラから取得した画像データ
    DetectImg : 
        RawImgを処理した画像データ
    """
    data = {
        "user": user,
        "room_id": room_id,
        "camera_id": camera_id,
        "label": label
    }
    files = {"img": rawimg, "detect_img": rawimg}
    
    # Send the POST request
    response = requests.post(url, data=data, files=files)
    

if __name__ == "__main__":
    # テスト用
    url = "http://127.0.0.1:5000/tracker/lost"
    
    img = open("../zidane.jpg" ,"rb")
    detectimg = open("../zidane.jpg", "rb")
    
    # Encode the image as a JPEG byte stream
    byte_stream = io.BytesIO(img.read())
    
    postData(
        "pen case", 
        img, 
        img
    )