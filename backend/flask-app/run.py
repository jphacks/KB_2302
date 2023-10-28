import settings
import json
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage


cred = credentials.Certificate(json.loads(settings.FIREBASE_CREDENTIALS))
app = firebase_admin.initialize_app(cred)

db = firestore.client()

bucket = storage.bucket('jphacks-kb-2302.appspot.com', app=app)

docs = db.collection('lost_objects').get()
print(docs)
for doc in docs:
    print(doc.to_dict())

def upload_image(file, filename):
    blob = bucket.blob(f"images/{filename}")
    blob.upload_from_file(file, content_type="image/jpeg")
    blob.make_public()
    return blob.public_url

def upload_document(time, user, room_id, camera_id, label, image_url, detect_image_url, valid):
    field = {"time": time, "user": user, "room_id": room_id, "camera_id": camera_id, "label": label, "imgURL": image_url, "detectImgURL": detect_image_url, "valid": valid}
    update_time, doc_ref = db.collection('lost_objects').add(field)
    print(f"{update_time}: Added document with id {doc_ref.id}")

if __name__ == '__main__':
    img = ""
    detect_img = ""
    with open("IMG_4231.jpg", 'rb') as image:
        img = upload_image(image, image.name)
    with open("IMG_4231detect.jpg", 'rb') as image:
        detect_img = upload_image(image, image.name)
    import datetime
    upload_document(datetime.datetime.now(), "Shin", 0, 1, "mouse", img, detect_img, True)

