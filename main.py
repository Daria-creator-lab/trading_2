import parsing_2
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
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

    print(type(y[0]))
    print(y)

    fig = plt.figure(figsize=(30, 5))
    plt.ylabel('Цена в $')
    plt.xlabel('Дата')
    plt.title('Изменение цены')
    # plt.plot(df.index, df[0:12])
    plt.plot(x, y, color='green', linestyle='-', marker='x', linewidth=1, markersize=4)
    plt.show()


if __name__ == '__main__':

    t = input('Введите тикер: ').upper()

    if t in parsing_2.list_of_tickers:
        price_index = parsing_2.list_of_tickers.index(t)
        print('Цена одной акции {} : {}'.format(t, parsing_2.list_of_price[price_index]))

        # print(parsing_2.import_file.loc[price_index, r'17/1/2019': r'19/12/2019'])

        df_variability = parsing_2.price_variability(price_index)

        # df_variability = df_variability.sort_values()
        # print(df_variability)
        draw_graph(df_variability)

    # app = QApplication([])
    # app.setStyle('Fusion')
    #
    # button_graph = QPushButton('График цены за 5 лет')
    # button_graph.setFixedSize(90, 20)
    # button_graph.clicked.connect(draw_graph)


    # button_diagram =
    # button_favorites =


