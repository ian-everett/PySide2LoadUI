"""
Example of Qt PySide2 with a native Qt application loading the Ui file
"""
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QWidget


class MainWindow(QWidget):
    """
    Subclass QWidget and create a widget reading
    from a given ui file
    """
    def __init__(self, ui_file_name):
        super().__init__()

        # Open ui file
        file = QFile(ui_file_name)
        file.open(QFile.ReadOnly)

        # Load the ui
        loader = QUiLoader()
        ui = loader.load(file, self)
        file.close()

        # Assign the ui controls to some refrences so can be used through class
        self.label = ui.label
        self.label.setText('')

        # Connect buttons to the clicked slot
        # pylint: disable=E1101
        ui.btn1.clicked.connect(lambda x: self.btn_clicked(0))
        ui.btn2.clicked.connect(lambda x: self.btn_clicked(1))
        ui.btn3.clicked.connect(lambda x: self.btn_clicked(2))
        ui.btn4.clicked.connect(lambda x: self.btn_clicked(3))


    def btn_clicked(self, button):
        """
        Update text label with which button was pressed
        """
        print(button)
        self.label.setText(str(button + 1))
        self.label.repaint()

def main():
    """
    Entry point into program
    """
    app = QApplication([])

    # Create main window from a ui file and show it
    window = MainWindow('frame.ui')
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
