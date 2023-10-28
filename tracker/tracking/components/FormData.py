import cv2
import io
import requests
import asyncio
import aiohttp

url = "https://msdocs-custom-container-tutorial.azurewebsites.net/tracker/lost"

async def postData(
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
    
    # files = {"img": byte_stream, "detect_img": byte_stream}
    
    data = aiohttp.FormData()
    data.add_field("user", user)
    data.add_field("room_id", str(room_id))
    data.add_field("camera_id", str(camera_id))
    data.add_field("label", label)
    data.add_field("valid", "True")
    data.add_field("img", byte_stream, filename="img.jpg", content_type="image/jpeg")
    data.add_field("detect_img", byte_stream2, filename="detect_img.jpg", content_type="image/jpeg")
    
    # Send the POST request
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            response_text = await response.text()
            return response_text 


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