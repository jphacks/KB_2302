import cv2
import io
import requests
import asyncio
import aiohttp
import threading

url = "https://jphacks-kb2302.azurewebsites.net/tracker/lost"

def postData(
        label:str,
        rawimg,
        detectimg,
        user:str = "SSSRC",
        room_id:int = 1,
        camera_id:int = 1,
    ):
    thread = threading.Thread(
            target=__postData, 
            args=(
                label, 
                rawimg, 
                detectimg,
                user,
                room_id,
                camera_id
            )
        )
    thread.start()

def __postData(
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
    
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    
    # Encode the image as a JPEG byte stream
    ret, buffer = cv2.imencode(".jpg", rawimg, encode_param)
    byte_stream = io.BytesIO(buffer)
    
    ret, buffer2 = cv2.imencode(".jpg", rawimg, encode_param)
    byte_stream2 = io.BytesIO(buffer2)
    
    
    data = {
        "user": user,
        "room_id": str(room_id),
        "camera_id": str(camera_id),
        "label": label,
        "valid": True,
    }
    files = {
        "img": byte_stream,
        "detect_img": byte_stream2
    }

    # Send the POST request
    response = requests.post(url, data=data, files=files)

if __name__ == "__main__":
    # テスト用
    url = "http://127.0.0.1:5000/tracker/lost"
    
    img = cv2.imread("../zidane.jpg")
    detectimg = cv2.imread("../zidane.jpg")
    
    # Encode the image as a JPEG byte stream

    asyncio.run(postData(
        "pen case", 
        img, 
        img
    ))