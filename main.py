import parsing_2
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
from PyQt5.QtGui import QFont, QIcon
from matplotlib import pyplot as plt

# def draw_graph():


if __name__ == '__main__':

    t = input('Введите тикер: ').upper()

    if t in parsing_2.list_of_tickers:
        price_index = parsing_2.list_of_tickers.index(t)
        print('Цена одной акции {} : {}'.format(t,parsing_2.list_of_price[price_index]))

        print(parsing_2.import_file.loc[price_index, r'17/1/2019': r'19/12/2019'])

    # app = QApplication([])
    # app.setStyle('Fusion')
    #
    # button_graph = QPushButton('График цены за 5 лет')
    # button_graph.setFixedSize(90, 20)
    # button_graph.clicked.connect(draw_graph)


    # button_diagram =
    # button_favorites =


