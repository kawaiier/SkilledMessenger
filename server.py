import time
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

messages = [
    {'username': 'John', 'time': time.time(), 'text': 'Hello!'},
    {'username': 'Mary', 'time': time.time(), 'text': 'Hello, John!'},
]

password_storage = {
    'John': '12345',
    'Mary': '54321'
}


@app.route("/")
def hello_method():
    return "Hello, World!"


@app.route("/status")
def status_method():

    return {
        'status': True,
        'time': datetime.now(),
        'messages': len(messages),
        'users': len(password_storage)
    }


@app.route("/send", methods=['POST'])
def send_method():
    """
    JSON {"username": str, "password": str, "text":str}
    username, text - non-empty lines
    :return: {'ok': bool}
    """
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    #first attempt for password is always valid
    if username not in password_storage:
        password_storage[username] = password

    # validate data
    if not isinstance(username, str) or len(username) == 0:
        return {'ok': False}
    if not isinstance(text, str) or len(text) == 0:
        return {'ok': False}
    if password_storage[username] != password:
        return {'ok': False}

    if text.count('/status') != 0:
        messages.append({'username': username, 'time': time.time(), 'text': str(status_method())})
    elif text.count('/change') != 0:
        start = text.find('/change') + 8
        password_storage[username] = text[start:len(text)]
    else:
        messages.append({'username': username, 'time': time.time(), 'text': text})

    return {'ok': True}


@app.route("/messages")
def messages_method():
    """
    Param after -
    :return: {'messages': [
        {'username': str, 'time': float, 'text': str}
    ]}
    """

    after = float(request.args['after'])

    filtered_messages = [message for message in messages if message['time'] > after]

    return {'messages': filtered_messages}


app.run()




















