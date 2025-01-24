from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtPositioning import QGeoPositionInfoSource

def method_changed():
    print("Positioning method changed")

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

label = QLabel("Positioning Methods Example")
layout.addWidget(label)

position_source = QGeoPositionInfoSource.createDefaultSource(window)

if position_source is not None:
    position_source.supportedPositioningMethodsChanged.connect(method_changed)
    position_source.updateInterval.connect(lambda: print("Update timeout occurred"))

window.setLayout(layout)
window.show()

app.exec()
