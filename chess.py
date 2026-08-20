import sys
import random
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

board = np.full((8, 8), None, dtype=object)


class Piece:

    def __init__(self, color, position):
        self.color = color 
        self.position = position
    
    def movement(self, x, y):
        pass


class Rook(Piece):

    def movement(self, x, y):
        x = input('')
        y = input('')

class Pawn(Piece):

    def movement(self, x, y):
        x = input('')
        y = input('')

class King(Piece):

    def movement(self, x, y):
        x = input('')
        y = input('')

class Queen(Piece):

    def movement(self, x, y):
        x = input('')
        y = input('')

class Knight(Piece):

    def movement(self, x, y):
        x = input('')
        y = input('')



for i in range(8):
    board[6, i] = Pawn('White', [i, 0])
    board[1, i] = Pawn('Black', [i, 0])

for i in (0, 7):
    board[0, i] = Rook('Black', [0, i])
    board[7, i] = Rook('White', [7, i])

for i in (1, 6):
    board[0, i] = Knight('Black', [0, i])
    board[7, i] = Knight('White', [7, i])


print(board)

#print(isinstance(board[6, 0], Pawn))

layout = QGridLayout()
layout.setSpacing(0) 



if __name__ == "__main__":
    app = QApplication(sys.argv)


    for row in range(8):
        for col in range(8):
            cell_content = board[row, col]
            

            btn = QPushButton()
            btn.setFixedSize(60, 60) #quadrat buttons
            

            if cell_content is not None:

                btn.setText(cell_content.__class__.__name__)
                

            layout.addWidget(btn, row, col)


# Create a Qt widget, which will be our window.
    window = QWidget()
    window.setLayout(layout)
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()