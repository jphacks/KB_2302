import settings
import json
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
import datetime


flask_app = Flask(__name__)

cred = credentials.Certificate(json.loads(settings.FIREBASE_CREDENTIALS))
firebase_app = firebase_admin.initialize_app(cred)

db = firestore.client()

bucket = storage.bucket('jphacks-kb-2302.appspot.com', app=firebase_app)

"""
docs = db.collection('lost_objects').get()
print(docs)
for doc in docs:
    print(doc.to_dict())
"""

def upload_image(file, filename):
    blob = bucket.blob(f"images/{filename}")
    blob.upload_from_file(file, content_type="image/jpeg")
    blob.make_public()
    return blob.public_url

def upload_document(time, user, room_id, camera_id, label, image_url, detect_image_url, valid):
    field = {"time": time, "user": user, "room_id": room_id, "camera_id": camera_id, "label": label, "imgURL": image_url, "detectImgURL": detect_image_url, "valid": valid}
    update_time, doc_ref = db.collection('lost_objects').add(field)
    print(f"{update_time}: Added document with id {doc_ref.id}")


@flask_app.route("/tracker/lost", methods=["POST"])
def lost():
    time = firestore.SERVER_TIMESTAMP
    user = request.form.get("user")
    room_id = int(request.form.get("room_id"))
    camera_id = int(request.form.get("camera_id"))
    label = request.form.get("label")
    img = request.files.get("img")
    detect_img = request.files.get("detect_img")
    valid = request.form.get("valid")
    img_url = upload_image(img, img.filename)
    detect_img_url = upload_image(detect_img, detect_img.filename)
    upload_document(time, user, room_id, camera_id, label, img_url, detect_img_url, valid)
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    flask_app.run(debug=True, host="localhost", port=8000)
    """
    img = ""
    detect_img = ""
    with open("IMG_4231.jpg", 'rb') as image:
        img = upload_image(image, image.name)
    with open("IMG_4231detect.jpg", 'rb') as image:
        detect_img = upload_image(image, image.name)
    import datetime
    upload_document(datetime.datetime.now(), "Shin", 0, 1, "mouse", img, detect_img, True)
    """

