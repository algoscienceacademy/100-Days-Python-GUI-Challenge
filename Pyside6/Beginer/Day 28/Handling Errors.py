import sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtNetwork import QTcpSocket, QAbstractSocket

def on_connected():
    print("Connected to the server.")

def on_error(error):
    print(f"Connection error: {error}")

app = QCoreApplication(sys.argv)

client = QTcpSocket()
client.connected.connect(on_connected)
client.errorOccurred.connect(on_error)

client.connectToHost("localhost", 12345)

sys.exit(app.exec())
