import pandas as pd

path = r'/Users/dary/Desktop/stocks_c.csv'
import_file = pd.read_csv(path, sep=';', engine='python', encoding='utf-8-sig',
                          error_bad_lines=False)

# headers = pd.read_csv(r'/Users/dary/Desktop/stocks_c.csv', nrows=0).columns.tolist()
columns_t = 'Ticker'
columns_p = 'Price'

list_of_tickers = import_file[columns_t].tolist()
list_of_price = import_file[columns_p].tolist()
# list_of_year_price = import_file.loc[]



def price_variability(index):
    list_price_variability = []





# tickers_t = pd.read_csv(r'/Users/dary/Desktop/stocks_c.csv', usecols=columns_t, sep=';')
# # print(type(tickers_t))
# list_of_tickers = []
# for row in tickers_t.itertuples():
#     list_of_tickers.append(row)
#
# tickers_p = pd.read_csv(path, usecols=columns_p, sep=';')
# # print(type(tickers_p))
# list_of_price = []
# for row in tickers_p.itertuples():
#     list_of_price.append(row)
# #
# # print(list_of_tickers)
# # print(list_of_price)
# # print(tickers_p.loc[0])
# # print(str(tickers_p.loc[0]).split('\n')[0])

