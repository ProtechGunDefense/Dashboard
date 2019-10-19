from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


# Create a class - inherit from QMainWindow (take all of the properties it has and use them
# in myWindow and modify them slightly(=)
class MyWindow(QMainWindow):
    # Constructor - run for each instance
    def __init__(self):
        # Calling the parent constructor of myWindow, so everything gets set up properly
        super(MyWindow, self).__init__()

        # Set size and title of window and position on it form the screen
        # setGeometry takes 4 args - x pos (where on screen you want it to show up), y pos, width, height
        # x and y pos are offsets from right top of screen
        self.setGeometry(200, 200, 300, 300)

        # Window title - what will show up on the top of the screen
        self.setWindowTitle("Test UI")

        # Call initUi - cleaning up code (all things going into window goes into initUi)
        self.initUi()

    def initUi(self):
        # ----- LABEL -----
        # Create Label - where we want the label to show up
        # Create instance of mywindow, add widget to self because the object is the actual window
        self.label = QtWidgets.QLabel(self)

        # Sets the text of the label (what the label actually says)
        self.label.setText("A Label?")

        # Moves the label to an x and y position (relative)
        self.label.move(50, 50)
        # ----- /LABEL -----

        # ----- BUTTON -----
        # Create button - where we want the button to show up
        self.b1 = QtWidgets.QPushButton(self)

        # Set the text of the button
        self.b1.setText("Click Me")

        # Map the button press to the clicked function
        # Clicked - function, connecting the button click event to the clicked function (called signals)
        self.b1.clicked.connect(self.clicked)
        # ----- /BUTTON -----

    # We need to map the button click to an event - what happens when we click the button
    # Create a function that we will trigger when the button is clicked
    def clicked(self):
        # Change the text of the label
        self.label.setText("You Pressed the Button!")

        # Update the size of the label
        self.update()

        # Common bug on MacOS - refresh the window
        self.repaint()

    # The label has a set width - the width is set to the width of the first text value it is set to
    # As soon as you click the button, and the width is greater than the width it has,
    # it cuts off, it doesn't show the rest of the text.
    # We need to add a way to update the width of the text.
    # Every time we click the button, we need to call the update method
    def update(self):
        # Automatically adjust the size of the label to hold the text is assigned to it
        self.label.adjustSize()


# We need to map the button click to an event - what happens when we click the button
# Create a function that we will trigger when the button is clicked

# Function that finds application
def window():
    # Giving config setting for system ( what os, how to display window)
    app = QApplication(sys.argv)

    # Create a window (widget) that we show in the application (QWidget or QMainWindow)
    win = MyWindow()

    # To show our window
    win.show()

    # Makes sure window shows up nicely and exits (clean exit) when click x button
    # Means waiting for application to exit, and when happens, exit and close application
    sys.exit(app.exec())


# Need to call function if we want anything to show up
window()
