import pytest
from PySide6.QtWidgets import QApplication
from packaging101.gui.main_window import MainWindow
from PySide6.QtCore import Qt

@pytest.fixture
def app(qtbot):
    app = QApplication.instance()
    if app is None:  # No QApplication exists yet, so create one
        app = QApplication([])

    main_window = MainWindow()
    qtbot.addWidget(main_window)
    return main_window, qtbot

def test_slow_factorial(app):
    main_window, qtbot = app
    qtbot.keyClicks(main_window.slow_input, '5')
    qtbot.mouseClick(main_window.slow_button, Qt.LeftButton)

    assert main_window.slow_result.text() == "Slow Result: 120", "Slow factorial calculation failed"

def test_fast_factorial(app):
    main_window, qtbot = app
    qtbot.keyClicks(main_window.fast_input, '5')
    qtbot.mouseClick(main_window.fast_button, Qt.LeftButton)

    assert main_window.fast_result.text() == "Fast Result: 120", "Fast factorial calculation failed"
