from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

cred = credentials.Certificate(".secret.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/search/word/v1")
def search_keyword_v1(q: Optional[str] = None):
    return {"q": q}

@app.get("/search/label/v1")
def search_label_v1(q: Optional[str] = None):
    collection = db.collection(u'lost_objects')
    docs = collection.stream()
    retdocs = []
    for doc in docs:
        aobject = doc.to_dict()
        if aobject['label'] == q:
            aobject['time'] = datetime.datetime.fromtimestamp(aobject['time'].timestamp()).strftime('%Y-%m-%d %H:%M:%S')
            retdocs.append(aobject)    
    return JSONResponse(content={"count": len(retdocs), "contents": retdocs})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)