import requests
"""
To change the password send /change newpassword
"""
print('Input username')
username = input()
print('Input password')
password = input()

while True:
    text = input()
    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={'username': username, 'password': password, 'text': text}
    )
    if response.status_code == 200:
        print('Message sent')
        print()
    if text.count('/change') != 0:
        start = text.find('/change') + 8
        password = text[start:len(text)]
