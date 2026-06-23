import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton

class Calculator_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator")
        self.setFixedSize(300, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setPlaceholderText("0")

        layout.addWidget(self.display)

        buttons_layout = QGridLayout()
        layout.addLayout(buttons_layout)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]

        for row_index, row in enumerate(buttons):
            for col_index, text in enumerate(row):
                button = QPushButton(text)
                button.clicked.connect(lambda checked, value=text: self.on_button_click(value))
                buttons_layout.addWidget(button, row_index, col_index)

    def on_button_click(self, value):
        current_text = self.display.text()

        if value == "C":
            self.display.clear()

        elif value == "=":
            try:
                result = eval(current_text)
                self.display.setText(str(result))
            except:
                self.display.setText("Błąd")
        
        else:
            self.display.setText(current_text + value)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator_window()
    window.show()
    sys.exit(app.exec())