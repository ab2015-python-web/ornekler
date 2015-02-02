from flask import Flask, jsonify
from pymongo import Connection
app = Flask(__name__)

db=Connection()['thewall']
@app.route("/api/messages")
def hello():
    messages = db.messages.find()

    result = []

    for message in messages:
        result.append({
	       "name":message.get("name"),
	       "message":message.get("message"),
        })
    return jsonify(messages=result)

if __name__ == "__main__":
    app.run(debug=True)
