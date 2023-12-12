from PyQt6.QtGui import QFont


class DataInput(object):

    def num_parties_input(widget):
        widget.setFixedSize(300, 40)
        widget.setFont(QFont("Arial", 15))
        widget.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        return widget
    

    def start_sugar_interval_input(widget):
        widget.setFixedSize(300, 40)
        widget.setFont(QFont("Arial", 15))
        widget.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        return widget
    
    
    def degradation_coeff_interval_input(widget):
        widget.setFixedSize(300, 40)
        widget.setFont(QFont("Arial", 15))
        widget.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        return widget
