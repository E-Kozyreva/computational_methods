import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


from design.app import Design as design
from design.buttons import Buttons as buttons
from design.data_input import DataInput as data_input


class BeetExperimentApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle('Эксперимент со свеклой')
        self.left, self.top, self.width, self.height = 1100, 100, 800, 500
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #ffffff;")

        self.time = QLabel(self)
        self.time = design.time_label(self.time)

        self.name_app = QLabel(self)
        self.name_app = design.name_app_label(self.name_app)
        
        self.end_app = QLabel(self)
        self.end_app = design.end_app_label(self.end_app)

        self.button_widget = QWidget(self)
        self.button_layout = QVBoxLayout(self.button_widget)
        self.button_widget = design.button_widget(self.button_widget)

        # создаем текст с вводом количества партий свеклы
        self.num_parties_input = QLineEdit(self)
        data_input.num_parties_input(self.num_parties_input)
        self.button_layout.addWidget(self.num_parties_input)

        # создаем текст с вводом интервала стартовой сахаристости
        self.start_sugar_interval_input = QLineEdit(self)
        data_input.start_sugar_interval_input(self.start_sugar_interval_input)
        self.button_layout.addWidget(self.start_sugar_interval_input)

        # создаем текст с вводом интервала коэффициентов деградации
        self.degradation_coeff_interval_input = QLineEdit(self)
        data_input.degradation_coeff_interval_input(self.degradation_coeff_interval_input)
        self.button_layout.addWidget(self.degradation_coeff_interval_input)

        # создаем чекбокс с поломкой оборудования
        self.breakdown_checkbox = QCheckBox('Поломка оборудования', self)
        self.button_layout.addWidget(self.breakdown_checkbox)

        # создаем чекбокс с выводом подробной информации в файл
        self.details_checkbox = QCheckBox('Вывести подробную информацию в файл', self)
        self.button_layout.addWidget(self.details_checkbox)


        
"""
        # Создаем виджеты
        self.num_parties_input = QLineEdit(self)
        self.start_sugar_interval_input = QLineEdit(self)
        self.degradation_coeff_interval_input = QLineEdit(self)
        self.breakdown_checkbox = QCheckBox('Поломка оборудования', self)
        self.details_checkbox = QCheckBox('Вывести подробную информацию в файл', self)
        self.output_text = QTextEdit(self)
        calculate_button = buttons.calculate_button(self)

        
        # Устанавливаем макет
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('Количество партий свеклы:', self))
        layout.addWidget(self.num_parties_input)
        layout.addWidget(QLabel('Интервал стартовой сахаристости (0-1):', self))
        layout.addWidget(self.start_sugar_interval_input)
        layout.addWidget(QLabel('Интервал коэффициентов деградации (0-1):', self))
        layout.addWidget(self.degradation_coeff_interval_input)
        layout.addWidget(self.breakdown_checkbox)
        layout.addWidget(self.details_checkbox)
        layout.addWidget(calculate_button)
        layout.addWidget(QLabel('Результат эксперимента:', self))
        layout.addWidget(self.output_text)

        # Связываем кнопку с функцией проведения эксперимента
        calculate_button.clicked.connect(self.run_experiment)

        self.setWindowTitle('Эксперимент со свеклой')
        self.setGeometry(300, 300, 400, 400)

    def run_experiment(self):
        try:
            # Получаем введенные пользователем значения
            num_parties = int(self.num_parties_input.text())
            start_sugar_interval = tuple(map(float, self.start_sugar_interval_input.text().split(',')))
            degradation_coeff_interval = tuple(map(float, self.degradation_coeff_interval_input.text().split()))
            breakdown_enabled = self.breakdown_checkbox.isChecked()
            details_enabled = self.details_checkbox.isChecked()

            # Выполняем эксперимент (здесь можно добавить свою логику)
            experiment_result = f"Эксперимент успешно выполнен для {num_parties} партий свеклы."

            # Выводим результат
            self.output_text.setPlainText(experiment_result)

            # Проверяем, нужно ли записать подробную информацию в файл
            if details_enabled:
                pass

        except ValueError:
            self.output_text.setPlainText('Ошибка ввода. Проверьте введенные данные.')
            """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    beet_app = BeetExperimentApp()
    beet_app.show()
    sys.exit(app.exec())
