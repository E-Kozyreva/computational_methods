from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class Design(object):
    
    def time_label(time) -> QLabel:
        time.setFixedSize(140, 30)
        time.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        time.move(330, -7)
        return time


    def name_app_label(name_app) -> QLabel:
        name_app.setFixedSize(792, 80)
        name_app.move(4, 4)
        name_app.setText("Эксперименты")
        name_app.setFont(QFont("Arial", 25, QFont.Weight.Bold))
        name_app.setStyleSheet("background-color: #262626; color: white; border-radius: 20px;")
        name_app.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_app.lower()
        return name_app


    def end_app_label(end_app) -> QLabel:
        end_app.setFixedSize(792, 80)
        end_app.move(4, 416)
        end_app.setStyleSheet("background-color: #262626; border-radius: 20px;")
        return end_app
    

    def button_widget(button_widget) -> QWidget:
        button_widget.setFixedSize(792, 400)
        button_widget.move(4, 50)
        button_widget.setStyleSheet("background-color: #353535;")
        button_widget.lower()
        return button_widget
    

    def black_button(button) -> QPushButton:
        button.setGeometry(150, 100, 200, 50)
        button.setFixedSize(240, 50)
        button.setFont(QFont("Arial", 20))
        button.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        return button
    

    def white_button(button) -> QPushButton:
        button.setGeometry(150, 100, 200, 50)
        button.setFixedSize(240, 50)
        button.setFont(QFont("Arial", 20))
        button.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        return button
