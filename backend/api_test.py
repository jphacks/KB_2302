import requests
import datetime

url = 'http://localhost:8000/tracker/lost'

time = datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
user = "test_user"
room_id = 0
camera_id = 1
label = "mouse"
image = open("IMG_4232.jpg", 'rb')
detect_image = open("IMG_4232detect.jpg", 'rb')
valid = True

data = {"user": user,
        "room_id": room_id,
        "camera_id": camera_id,
        "label": label,
        "valid": valid
        }
files = {"img": image, "detect_img": detect_image}

# Send the POST request
response = requests.post(url, data=data, files=files)

# Print the response from the server
print(response.json())

image.close()
detect_image.close()
