def get_stylesheet():
    return """
        QWidget {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                              stop:0 #23272e, stop:1 #1c2128);
            color: #cdd9e5;
            font-size: 15px;
            font-family: 'Segoe UI', 'Roboto', 'Helvetica', sans-serif;
        }
        QMainWindow {
            border: 1px solid #333c4a;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        QTabWidget::pane {
            border: 1px solid #333c4a;
            border-radius: 8px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #23272e, stop:1 #222831);
        }
        QTabBar::tab {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                       stop:0 #23272e, stop:1 #222831);
            padding: 12px 25px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            font-weight: bold;
            color: #768390;
            margin-right: 2px;
            transition: background-color 0.3s, color 0.3s, border-bottom 0.3s;
        }
        QTabBar::tab:selected {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                       stop:0 #2d333b, stop:1 #23272e);
            color: #539bf5;
            border-bottom: 3px solid #539bf5;
        }
        QTabBar::tab:hover {
            background: #2d333b;
            color: #539bf5;
        }
        QGroupBox {
            font-weight: bold;
            border: 1px solid #333c4a;
            border-radius: 8px;
            margin-top: 1ex;
            font-size: 16px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #23272e, stop:1 #222831);
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0 12px;
        }
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                              stop:0 #238636, stop:1 #2ea043);
            color: white;
            border: none;
            padding: 12px;
            border-radius: 8px;
            font-weight: bold;
            transition: background-color 0.4s, color 0.3s;
            box-shadow: 0 2px 8px rgba(35,134,54,0.12);
        }
        QPushButton:hover {
            background-color: #2ea043;
            box-shadow: 0 4px 16px rgba(35,134,54,0.18);
        }
        QPushButton:pressed {
            background-color: #2da44e;
        }
        QPushButton:disabled {
            background-color: #555;
            color: #999;
            box-shadow: none;
        }
        QPushButton#DeleteButton {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                              stop:0 #da3633, stop:1 #c62828);
        }
        QPushButton#DeleteButton:hover {
            background-color: #f04747;
        }
        QLineEdit, QListWidget {
            background-color: #222831;
            border: 1px solid #333c4a;
            border-radius: 8px;
            padding: 8px;
            transition: border 0.3s;
        }
        QLineEdit:focus {
            border: 1.5px solid #539bf5;
            background-color: #23272e;
        }
        QListWidget::item:hover {
            background-color: #2d333b;
        }
        QListWidget::item:selected {
            background-color: #539bf5;
            color: #1c2128;
            border-radius: 6px;
        }
        QLabel#ImagePreview, QLabel#CameraView {
            background-color: black;
            border: 2px dashed #333c4a;
            border-radius: 8px;
        }
        QLabel#AboutTitle {
            font-size: 28px;
            font-weight: bold;
            color: #539bf5;
            letter-spacing: 1.2px;
            text-shadow: 0 2px 8px #222831;
        }
        QStatusBar {
            background-color: #222831;
            font-weight: bold;
            border-top: 1px solid #333c4a;
        }
        QMessageBox, QProgressDialog {
             background-color: #2d333b;
             border: 1px solid #539bf5;
             border-radius: 8px;
        }
        QProgressDialog QLabel {
            color: #cdd9e5;
        }
        QProgressDialog QPushButton {
            background-color: #da3633;
            border-radius: 8px;
        }
        QProgressDialog QPushButton:hover {
            background-color: #f04747;
        }
    """