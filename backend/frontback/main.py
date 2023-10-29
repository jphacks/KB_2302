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
if True:
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

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/getlist/v1")
def get_objectlist_v1():
    collection = db.collection(u'lost_objects')
    query = collection.order_by(u'time', direction=firestore.Query.DESCENDING)
    docs = query.get()
    retdocs = []
    labelset = set()
    for doc in docs:
        aobject = doc.to_dict()
        if aobject['label'] in labelset:
            pass
        else:
            labelset.add(aobject['label'])
            try:
                dt = datetime.datetime.fromtimestamp(aobject['time'].timestamp())+datetime.timedelta(hours=9)
                aobject['time'] = dt.strftime('%Y/%m/%d %H:%M:%S')
            except:
                aobject['time'] = "Unknown"
            retdocs.append(aobject)
    return JSONResponse(content={"count": len(retdocs), "contents": retdocs})



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

@app.get("/search/word/v2")
def search_keyword_v2(q: Optional[str] = None):
    collection = db.collection(u'lost_objects')
    query = collection.order_by(u'time', direction=firestore.Query.DESCENDING).limit(100)
    docs = query.get()
    retdocs = []
    searchedlabel = set()
    matchedlabel = set()
    for doc in docs:
        aobject = doc.to_dict()
        if aobject['label'] in searchedlabel:
            if aobject['label'] in matchedlabel:
                # 検索済みで、一致している
                try:
                    dt = datetime.datetime.fromtimestamp(aobject['time'].timestamp())+datetime.timedelta(hours=9)
                    aobject['time'] = dt.strftime('%Y/%m/%d %H:%M:%S')
                except:
                    aobject['time'] = "Unknown"
                retdocs.append(aobject)
            else:
                # 検索済みだが、一致していない
                pass
        else:
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
                matchedlabel.add(aobject['label'])
                searchedlabel.add(aobject['label'])
            else:
                searchedlabel.add(aobject['label'])
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
                dt = datetime.datetime.fromtimestamp(aobject['time'].timestamp())+datetime.timedelta(hours=9)
                aobject['time'] = dt.strftime('%Y/%m/%d %H:%M:%S')
            except:
                aobject['time'] = "Unknown"
            retdocs.append(aobject)
    return JSONResponse(content={"count": len(retdocs), "contents": retdocs})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
