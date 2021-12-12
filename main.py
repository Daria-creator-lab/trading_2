import parsing_2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont, QIcon
from matplotlib import pyplot as plt


Time = [r'17/1/2019', r'19/2/2019', r'18/3/2019', r'22/4/2019', r'20/5/2019', r'19/6/2019', r'19/7/2019',
        r'19/8/2019', r'19/9/2019', r'21/10/2019', r'19/11/2019', r'19/12/2019']


class Ticker:
    def __init__(self):
        self.value = ''.upper()
        self.price_index = -1

    def update_textbox(self, message):
        global textbox
        textbox.append(message)

    def get_ticker_from_text(self):
        textbox_value = str(textbox.toPlainText())
        textbox_value = textbox_value.replace(u'Введите тикер: ', u'')
        self.value = textbox_value
        return textbox_value

    def check_input(self):
        textbox_value = self.get_ticker_from_text()
        t = str(textbox_value).upper()
        if t in parsing_2.list_of_tickers:
            self.price_index = parsing_2.list_of_tickers.index(t)
            self.update_textbox('Цена одной акции {} : {}'.format(t, parsing_2.list_of_price[self.price_index]))

    def draw_graph(self):
        df_variability = parsing_2.price_variability(self.price_index)

        x = Time
        y = df_variability.tolist()

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



if __name__ == '__main__':

    T = Ticker()

    app = QApplication([])
    app.setStyle('Fusion')

    button_graph = QPushButton('График цены за 5 лет')
    button_graph.setFixedSize(211, 120)
    button_graph.clicked.connect(T.draw_graph)

    button_price = QPushButton('Текущая цена')
    button_price.setFixedSize(211, 120)
    button_price.clicked.connect(T.check_input)

    button_re_enter = QPushButton('Повторить ввод тикера')
    button_re_enter.setFixedSize(211, 120)
    button_re_enter.clicked.connect(T.re_enter)

    textbox = QTextEdit()
    textbox.setFont(QFont('Times New Roman', 16))
    textbox.setText('Введите тикер: ')

    window = QWidget()
    window.setWindowTitle('Биржевые торги')
    # window.setWindowIcon()
    window.resize(640, 400)

    layout = QGridLayout()
    layout.addWidget(textbox, 0, 0, 1, 4)
    layout.addWidget(button_price, 1, 0, 1, 1)
    layout.addWidget(button_graph, 1, 1, 1, 1)
    layout.addWidget(button_re_enter, 1, 2, 1, 1)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

    # button_diagram =
    # button_favorites =


