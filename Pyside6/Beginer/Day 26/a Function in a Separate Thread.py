import sys
import time
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class Worker(QThread):
    finished = Signal(str)

    def run(self):
        time.sleep(5)
        self.finished.emit("Task Completed!")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Running task...", self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.run_task()

    def run_task(self):
        self.worker = Worker()
        self.worker.finished.connect(self.on_task_finished)
        self.worker.start()

    def on_task_finished(self, result):
        self.label.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
