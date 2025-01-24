import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

def square(n):
    return n * n

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Calculating squares...", self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        numbers = [1, 2, 3, 4, 5]
        self.run_task(numbers)

    def run_task(self, numbers):
        results = list(map(square, numbers))
        self.on_task_finished(results)

    def on_task_finished(self, results):
        self.label.setText(f"Squares: {results}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())