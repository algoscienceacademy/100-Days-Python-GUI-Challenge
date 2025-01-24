import sys
from PySide6.QtCore import QCoreApplication, QTimer
from PySide6.QtPositioning import QGeoPositionInfoSource

def position_updated(position):
    print(f"Latitude: {position.coordinate().latitude()}, Longitude: {position.coordinate().longitude()}")

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)

    # Create QGeoPositionInfoSource object
    position_source = QGeoPositionInfoSource.createDefaultSource(app)
    
    if position_source is not None:
        position_source.positionUpdated.connect(position_updated)
        position_source.startUpdates()
    else:
        print("Positioning source not available.")
    
    QTimer.singleShot(10000, app.quit)  # Run the app for 10 seconds
    sys.exit(app.exec())
