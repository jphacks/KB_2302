from flask import Flask, request

app = Flask(__name__)

@app.route('/tracker/lost', methods=['POST'])
def receive_post():
    data = request.form
    files = request.files
    print("Received data:", data)
    print("Received files:", files)
    return "OK"

app.run(debug=True)