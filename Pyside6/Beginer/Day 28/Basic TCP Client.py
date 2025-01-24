import sys
from PySide6.QtCore import QCoreApplication, QTimer, QIODevice
from PySide6.QtNetwork import QTcpSocket

def on_connected():
    print("Connected to the server.")
    client.write(b"Hello, Server!")

def on_ready_read():
    print("Message from server:", client.readAll().data().decode())

def on_disconnected():
    print("Disconnected from the server.")
    QCoreApplication.quit()

app = QCoreApplication(sys.argv)

client = QTcpSocket()
client.connected.connect(on_connected)
client.readyRead.connect(on_ready_read)
client.disconnected.connect(on_disconnected)

client.connectToHost("localhost", 12345)

QTimer.singleShot(5000, lambda: client.disconnectFromHost())

sys.exit(app.exec())
