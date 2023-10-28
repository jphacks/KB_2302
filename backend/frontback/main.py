from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import firebase_admin
from firebase_admin import credentials, firestore
import datetime
from fastapi.middleware.cors import CORSMiddleware

cred = credentials.Certificate(".secret.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

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
            try:
                aobject['time'] = datetime.datetime.fromtimestamp(aobject['time'].timestamp()).strftime('%Y-%m-%d %H:%M:%S')
            except:
                aobject['time'] = "Unknown"
            retdocs.append(aobject)    
    return JSONResponse(content={"count": len(retdocs), "contents": retdocs})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)