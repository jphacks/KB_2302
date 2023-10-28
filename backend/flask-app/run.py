import settings
import json
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate(json.loads(settings.FIREBASE_CREDENTIALS))
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection('test').get()
print(docs)
for doc in docs:
    print(doc.to_dict())



"""
app = Flask(__name__)

# Initialize Firestore and Storage clients
db = firestore.Client()
bucket = storage.Client().bucket('your-bucket-name')

@app.route('/api/documents', methods=['GET'])
def get_documents():
    # Get all documents from a Firestore collection
    docs = db.collection('your-collection-name').get()
    # Convert documents to a dictionary and return as JSON
    return jsonify({doc.id: doc.to_dict() for doc in docs})

@app.route('/api/upload', methods=['POST'])
def upload_file():
    # Get file from request
    file = request.files['file']
    # Upload file to Firebase Storage
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)
    # Return URL of uploaded file
    return jsonify({'url': blob.public_url})

if __name__ == '__main__':
    app.run()
"""