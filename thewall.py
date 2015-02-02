from flask import Flask, jsonify, request
from pymongo import Connection

db = Connection()['thewall']
app = Flask(__name__)


@app.route('/api/messages')
def list_messages():
    messages = db.messages.find()
    result = []
    for message in messages:
        result.append({
            'name': message.get('name'),
            'message': message.get('message'),
        })
    return jsonify(messages=result)


@app.route('/api/messages', methods=['POST'])
def post_message():
    data = {
        'name': request.form.get('name'),
        'message': request.form.get('message'),
    }
    db.messages.insert(data)
    del data['_id']
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
