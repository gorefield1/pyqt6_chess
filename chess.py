import sys
import random
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget

board = np.full((8, 8), None, dtype=object)


a = None


class Piece:

    def __init__(self, color, position):
        self.color = color 
        self.position = position
    
    def movement(self, x, y):
        pass


class Pawn(Piece):

    def movement(self, x, y):
        x = input('')
        y = input('')
    

for i in range(8):
    print(i)
    board[6, i] = Pawn('White', [i, 0])
    board[1, i] = Pawn('Black', [i, 0])

print('hi')

print(range(1, 5))

print(board)

if __name__ == "__main__":
    app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
    window = QWidget()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()