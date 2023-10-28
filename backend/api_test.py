import requests
import datetime

url = 'http://localhost:8000/tracker/lost'
url = "https://kb2302-jphack-471e16480034.herokuapp.com/tracker/lost"

time = datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
user = "heroku使ってみるよ"
room_id = 2
camera_id = 5
label = "pen case"
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
