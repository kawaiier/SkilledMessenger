import datetime
import time
import threading
from PyQt5 import QtWidgets
import design
import requests


class MessengerApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send)

        thread = threading.Thread(target=self.receive)
        thread.start()

    def send(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        text = self.textEdit.toPlainText()

        if not username or not password or not text:
            return

        try:
            requests.post(
                "http://127.0.0.1:5000/send",
                json={"username": username, "password": password, "text": text}
            )
        except:
            pass

        self.textEdit.setPlainText("")

    def receive(self):
        last_received = 0

        while True:
            response = requests.get(
                "http://127.0.0.1:5000/messages",
                params={"after": last_received}
            )
            if response.status_code == 200:
                messages = response.json()["messages"]
                for message in messages:
                    username = message["username"]
                    time_1 = datetime.datetime.fromtimestamp(message["time"])
                    time_text = time_1.strftime("%D %T")
                    text = message["text"]

                    self.textBrowser.append(f"{username} {time_text}")
                    self.textBrowser.append(text)
                    self.textBrowser.append("")
                    #self.textBrowser.repaint()

                    last_received = message["time"]
            time.sleep(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MessengerApp()
    window.show()
    app.exec_()
