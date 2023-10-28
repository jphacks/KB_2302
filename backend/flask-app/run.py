import settings
import json
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage


cred = credentials.Certificate(json.loads(settings.FIREBASE_CREDENTIALS))
firebase_app = firebase_admin.initialize_app(cred)

db = firestore.client()

bucket = storage.bucket('jphacks-kb-2302.appspot.com', app=firebase_app)

origins = [
    "https://kb-2302.vercel.app/",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def upload_image(file, filename):
    blob = bucket.blob(f"images/{filename}")
    blob.upload_from_file(file, content_type="image/jpeg")
    blob.make_public()
    return blob.public_url


def upload_document(time, user, room_id, camera_id, label, image_url, detect_image_url, valid):
    field = {"time": time, "user": user, "room_id": room_id, "camera_id": camera_id, "label": label, "imgURL": image_url, "detectImgURL": detect_image_url, "valid": valid}
    update_time, doc_ref =  db.collection('lost_objects').add(field)
    print(f"{update_time}: Added document with id {doc_ref.id}")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/tracker/lost")
def lost(user: str = Form(), room_id: int = Form(), camera_id: int = Form(), label: str = Form(), img: UploadFile = File(), detect_img: UploadFile = File(), valid: bool = Form()):
    time = firestore.SERVER_TIMESTAMP
    img_url = upload_image(img.file, img.filename)
    detect_img_url = upload_image(detect_img.file, detect_img.filename)
    upload_document(time, user, room_id, camera_id, label, img_url, detect_img_url, valid)
    return {"status": "ok"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
