import sys
import random
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget

board = np.full((8, 8), None, dtype=object)

print(board)


class Piece:

    def __init__(self, color, position):
        self.color = color 
        self.position = position

#

if __name__ == "__main__":
    app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
    window = QWidget()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()