import cv2
import io
import requests
import asyncio
import aiohttp

url = "https://jphacks-kb2302.azurewebsites.net/tracker/lost"

async def postData(
    label:str,
    rawimg,
    detectimg,
    user:str = "SSSRC",
    room_id:int = 1,
    camera_id:int = 1,
):
    await __postData(
        label=label,
        rawimg=rawimg,
        detectimg=detectimg,
        user=user,
        room_id=room_id,
        camera_id=camera_id
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
            return await response.text()


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