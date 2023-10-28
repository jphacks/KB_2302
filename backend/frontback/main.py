from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import firebase_admin
from firebase_admin import credentials, firestore
import datetime
from fastapi.middleware.cors import CORSMiddleware
import json
import requests
import os
# 環境変数を取得
if False:
    import dotenv
    dotenv.load_dotenv()
goo_api_key = os.environ["GOO_API_KEY"]

cred = credentials.Certificate(".secret.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# jsonの翻訳辞書を読み込んで辞書型にする
with open('translate.json', 'r', encoding="utf-8") as f:
    label_dict = json.load(f)


def goo_api(text1, text2):
    try:
        response = requests.post(
            "https://labs.goo.ne.jp/api/textpair",
            json={"app_id": goo_api_key, "text1": text1, "text2": text2})
        jsonData = response.json()
        if response.status_code == 200:
            return jsonData["score"]
        else:
            return 0.0
    except:
        return 0.0


origins = [
    "https://kb-2302.vercel.app/",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
]


origins = [
    "https://kb-2302.vercel.app",
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
<<<<<<< HEAD
=======

>>>>>>> master

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/search/word/v1")
def search_keyword_v1(q: Optional[str] = None):
    collection = db.collection(u'lost_objects')
    docs = collection.stream()
    retdocs = []
    for doc in docs:
        aobject = doc.to_dict()
        if aobject['label'] in label_dict.keys():
            useword = label_dict[aobject['label']]
        else:
            useword = aobject['label']
        if goo_api(q, useword) > 0.6:
            try:
                dt = datetime.datetime.fromtimestamp(aobject['time'].timestamp())+datetime.timedelta(hours=9)
                aobject['time'] = dt.strftime('%Y/%m/%d %H:%M:%S')
            except:
                aobject['time'] = "Unknown"
            retdocs.append(aobject)

    return JSONResponse(content={"count": len(retdocs), "contents": retdocs})


@app.get("/search/label/v1")
def search_label_v1(q: Optional[str] = None):
    collection = db.collection(u'lost_objects')
    docs = collection.stream()
    retdocs = []
    for doc in docs:
        aobject = doc.to_dict()
        if aobject['label'] == q:
            try:
<<<<<<< HEAD
                aobject['time'] = datetime.datetime.fromtimestamp(aobject['time'].timestamp()).strftime('%Y-%m-%d %H:%M:%S')
            except:
                aobject['time'] = "Unknown"
            retdocs.append(aobject)    
=======
                dt = datetime.datetime.fromtimestamp(aobject['time'].timestamp())+datetime.timedelta(hours=9)
                aobject['time'] = dt.strftime('%Y/%m/%d %H:%M:%S')
            except:
                aobject['time'] = "Unknown"
            retdocs.append(aobject)
>>>>>>> master
    return JSONResponse(content={"count": len(retdocs), "contents": retdocs})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
