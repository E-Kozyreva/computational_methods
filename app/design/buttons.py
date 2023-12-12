from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QSize, Qt

from design.app import Design


class Buttons(object):

    def calculate_button(self) -> QPushButton:
        calculate = QPushButton("Начать эксперимент")
        calculate = Design.black_button(calculate)
        return calculate
    
    
    def exit_button(self) -> QPushButton:
        exit_b = QPushButton("Выход")
        exit_b = Design.white_button(exit_b)
        return exit_b
