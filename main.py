import parsing_2

if __name__ == '__main__':

    t = input('Введите тикер: ')

    if t in parsing_2.list_of_tickers:
        price_index = parsing_2.list_of_tickers.index(t)
        print(parsing_2.list_of_price[price_index])
