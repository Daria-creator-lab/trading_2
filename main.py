import parsing_2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont, QIcon
from matplotlib import pyplot as plt


Time = [r'17/1/2019', r'19/2/2019', r'18/3/2019', r'22/4/2019', r'20/5/2019', r'19/6/2019', r'19/7/2019',
        r'19/8/2019', r'19/9/2019', r'21/10/2019', r'19/11/2019', r'19/12/2019']


def draw_graph(df):

    x = Time
    y = df.tolist()

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


def check_input():
    textbox_value = get_ticker_from_text()
    t = str(textbox_value).upper()
    if t in parsing_2.list_of_tickers:
        price_index = parsing_2.list_of_tickers.index(t)
        update_textbox('Цена одной акции {} : {}'.format(t, parsing_2.list_of_price[price_index]))

        # df_variability = parsing_2.price_variability(price_index)
        # draw_graph(df_variability)


def get_ticker_from_text():
    textbox_value = str(textbox.toPlainText())
    textbox_value = textbox_value.replace(u'Введите тикер: ', u'')
    return textbox_value


def update_textbox(message):
    global textbox
    textbox.append(message)



if __name__ == '__main__':

    # t = input('Введите тикер: ').upper()

    # if t in parsing_2.list_of_tickers:
    #     price_index = parsing_2.list_of_tickers.index(t)
    #     print('Цена одной акции {} : {}'.format(t, parsing_2.list_of_price[price_index]))
    #
    #     df_variability = parsing_2.price_variability(price_index)
    #     # draw_graph(df_variability)

    app = QApplication([])
    app.setStyle('Fusion')

    button_graph = QPushButton('График цены за 5 лет')
    button_graph.setFixedSize(190, 120)
    # button_graph.clicked.connect(draw_graph(df_variability))
    button_price = QPushButton('Текущая цена')
    button_price.setFixedSize(190, 120)
    button_price.clicked.connect(check_input)

    textbox = QTextEdit()
    textbox.setFont(QFont('Times New Roman', 16))
    textbox.setText('Введите тикер: ')
    # textbox_value = textbox.toPlainText()

    # check_input(textbox_value)
    # textbox.setReadOnly(True)

    window = QWidget()
    window.setWindowTitle('Биржевые торги')
    # window.setWindowIcon()
    window.resize(640, 400)

    layout = QGridLayout()
    layout.addWidget(textbox, 0, 0, 1, 4)
    layout.addWidget(button_price, 1, 0, 1, 1)
    layout.addWidget(button_graph, 1, 1, 1, 1)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

    # button_diagram =
    # button_favorites =


