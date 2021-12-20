import parsing_2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont, QIcon
# from PyQt5 import QtGui, QtWidgets
from matplotlib import pyplot as plt


Time_2019 = [r'17/1/2019', r'19/2/2019', r'18/3/2019', r'22/4/2019', r'20/5/2019', r'19/6/2019', r'19/7/2019',
        r'19/8/2019', r'19/9/2019', r'21/10/2019', r'19/11/2019', r'19/12/2019']
Time_2020 = [r'17/1/2020', r'19/2/2020', r'18/3/2020', r'22/4/2020', r'20/5/2020', r'19/6/2020', r'20/7/2020',
        r'19/8/2020', r'21/9/2020', r'19/10/2020', r'19/11/2020', r'18/12/2020']
list_of_year = ['2019', '2020']


class Ticker:
    def __init__(self):
        self.value = ''.upper()
        self.price_index = -1
        self.year = '2020'

    def update_textbox(self, message):
        global textbox
        textbox.append(message)

    def get_ticker_from_text(self):
        textbox_value = str(textbox.toPlainText())
        textbox_value = textbox_value.replace(u'Введите тикер: ', u'')
        self.value = textbox_value
        return textbox_value

    def get_year_from_text(self):
        textbox_value_year = str(textbox.toPlainText())
        textbox_value_year = textbox_value_year.replace(u'Введите год: ', u'')
        return textbox_value_year

    def check_input_year(self):
        textbox_value_year = self.get_year_from_text()
        if textbox_value_year in list_of_year:
            self.year = textbox_value_year
        else:
            self.update_textbox('Данных для этого года еще нет в системе. Посмортите для 2020.')

    def check_input(self):
        textbox_value = self.get_ticker_from_text()
        t = str(textbox_value).upper()
        if t in parsing_2.list_of_tickers:
            self.price_index = parsing_2.list_of_tickers.index(t)
            self.update_textbox('Цена одной акции {} : {}'.format(t, parsing_2.list_of_price[self.price_index]))

    def draw_graph(self):
        # df_variability = parsing_2.price_variability(self.price_index)
        if self.year == 2019:
            x = Time_2019
            df_variability = parsing_2.price_variability_2019(self.price_index)
            y = df_variability.tolist()
        else:
            x = Time_2020
            df_variability = parsing_2.price_variability_2020(self.price_index)
            y = df_variability.tolist()

        # y = df_variability.tolist()

        for i in range(len(y)):
            y[i] = y[i].replace(u'\xa0$', u'')
            y[i] = y[i].replace(u',', u'.')
            y[i] = float(y[i])

        fig = plt.figure(figsize=(30, 5))
        plt.ylabel('Цена в $')
        plt.xlabel('Дата')
        plt.title('Изменение цены')
        plt.plot(x, y, color='green', linestyle='-', marker='x', linewidth=1, markersize=4)
        plt.show()

    def re_enter(self):
        self.price_index = -1
        self.value = ''
        textbox.setText('Введите тикер: ')
        self.check_input()

    def robot(self):
        self.check_input_year()
        dict_of_deals = {}
        for i in range(1, 12):
            if self.year == 2019:
                df_variability = parsing_2.price_variability_2019(self.price_index)
                list_of_price = df_variability.tolist()
            else:
                df_variability = parsing_2.price_variability_2020(self.price_index)
                list_of_price = df_variability.tolist()
            for k in range(len(list_of_price)):
                list_of_price[k] = list_of_price[k].replace(u'\xa0$', u'')
                list_of_price[k] = list_of_price[k].replace(u',', u'.')
                list_of_price[k] = float(list_of_price[k])

            if list_of_price[i] < sum(list_of_price[0:i])/i:
                dict_of_deals[i] = 'купили, потому что дешевле, чем в среднем за предыдущий период'
            elif i % 2 == 0:
                dict_of_deals[i] = 'купили, потому что регулярное пополнение'
            else:
                dict_of_deals[i] = 'ничего не покупали'
        self.update_textbox('Список сделок:')
        for j in dict_of_deals.items():
            self.update_textbox('{}'.format(j))


    def extra_button(self):
        window.setWindowTitle('Дополнительные возможности')

        button_graph = QPushButton('График цены за год')
        button_graph.setFixedSize(160, 120)
        button_graph.clicked.connect(self.draw_graph)

        button_robot = QPushButton('Робот')
        button_robot.setFixedSize(160, 120)
        button_robot.clicked.connect(self.robot)

        textbox.setText('Введите год: ')

        layout.addWidget(button_robot, 1, 1, 1, 1)
        layout.addWidget(button_graph, 1, 0, 1, 1)

        window.setLayout(layout)
        window.show()




if __name__ == '__main__':

    T = Ticker()

    app = QApplication([])
    app.setStyle('Fusion')

    # button_graph = QPushButton('График цены за 5 лет')
    # button_graph.setFixedSize(160, 120)
    # button_graph.clicked.connect(T.draw_graph)

    button_price = QPushButton('Текущая цена')
    button_price.setFixedSize(160, 120)
    button_price.clicked.connect(T.check_input)

    button_re_enter = QPushButton('Повторить ввод тикера')
    button_re_enter.setFixedSize(160, 120)
    button_re_enter.clicked.connect(T.re_enter)

    button_extra = QPushButton('Дополнительно')
    button_extra.setFixedSize(160, 120)
    button_extra.clicked.connect(T.extra_button)

    # button_robot = QPushButton('Робот')
    # button_robot.setFixedSize(160, 120)
    # button_robot.clicked.connect(T.robot)

    textbox = QTextEdit()
    textbox.setFont(QFont('Times New Roman', 16))
    textbox.setText('Введите тикер: ')

    window = QWidget()
    window.setWindowTitle('Биржевые торги')
    window.resize(640, 400)

    layout = QGridLayout()
    layout.addWidget(textbox, 0, 0, 1, 4)
    layout.addWidget(button_price, 1, 0, 1, 1)
    # layout.addWidget(button_graph, 1, 1, 1, 1)
    layout.addWidget(button_re_enter, 1, 1, 1, 1)
    # layout.addWidget(button_robot, 1, 2, 1, 1)
    layout.addWidget(button_extra,1, 2, 1, 1)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

