# pyqt-polygon-window
PyQt polygon window

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-polygon-window.git --upgrade```

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_polygon_window import PolygonWindow


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    pw = PolygonWindow()
    pw.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/149039804-c080d8fc-379e-4ba5-87c2-c64d53308f99.png)


