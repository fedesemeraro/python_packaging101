from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QHBoxLayout
from packaging101 import fastfactorial, slowfactorial

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Factorial Calculator')

        # Layout for slowfactorial
        self.slow_input = QLineEdit()
        self.slow_button = QPushButton('Calculate Slow Factorial')
        self.slow_button.clicked.connect(self.on_slow_button_clicked)
        self.slow_result = QLabel('Result will be shown here')
        slow_layout = QHBoxLayout()
        slow_layout.addWidget(self.slow_input)
        slow_layout.addWidget(self.slow_button)

        # Layout for fastfactorial
        self.fast_input = QLineEdit()
        self.fast_button = QPushButton('Calculate Fast Factorial')
        self.fast_button.clicked.connect(self.on_fast_button_clicked)
        self.fast_result = QLabel('Result will be shown here')
        fast_layout = QHBoxLayout()
        fast_layout.addWidget(self.fast_input)
        fast_layout.addWidget(self.fast_button)

        # Main layout
        layout = QVBoxLayout(self)
        layout.addLayout(slow_layout)
        layout.addWidget(self.slow_result)
        layout.addLayout(fast_layout)
        layout.addWidget(self.fast_result)

    def on_slow_button_clicked(self):
        n = int(self.slow_input.text())
        result = slowfactorial(n)  # Assuming slowfactorial is implemented similarly
        self.slow_result.setText(f'Slow Result: {result}')

    def on_fast_button_clicked(self):
        n = int(self.fast_input.text())
        result = fastfactorial(n)  # This will call the C++ implemented fastfactorial
        self.fast_result.setText(f'Fast Result: {result}')
