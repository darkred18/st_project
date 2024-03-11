# import pybithumb
# import time
# tickets = pybithumb.get_tickers()[:10]


# for t in tickets:
#     price = pybithumb.get_current_price(t)
#     print( price)
#     # time.sleep(1)


import requests
import json
import pandas as pd

# dict key change
# dict((head_names_data[key], value) for (key, value) in data.items())

head_names_data = {
    'opening_price':        '시가',
    'closing_price':        '종가', 
    'min_price':            '저가', 
    'max_price':            '고가', 
    'units_traded':         '거래량', 
    'acc_trade_value':      '거래금액',
    'prev_closing_price':   '전일종가', 
    'units_traded_24H':     '최근거래량', 
    'acc_trade_value_24H':  '최근거래금액',
    'fluctate_24H':         '최근변동가',
    'fluctate_rate_24H':    '최근변동률'

}

# n_index = ['시가','종가','저가','고가','거래량','거래금액','전일종가','최근거래량','최근거래금액','최근변동가','최근변동률']

# url = "https://api.bithumb.com/public/ticker/ALL_KRW"

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)
# # print(response.text)

# data = json.loads(response.text)['data']
# df = pd.DataFrame(data)
# df.index = n_index
# # print(df)



def get_test_data():
    url = "https://api.bithumb.com/public/ticker/ALL_KRW"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    # print(response.text)

    data = json.loads(response.text)['data']
    return data
    # df = pd.DataFrame(data)
    # df.index = n_index
    # return df.transpose()

def test_dataframe():
    data = get_test_data()
    df = pd.DataFrame(data).transpose()
    return df

def get_current_price(order):
    data = get_test_data()
    return data[order]['closing_price']

# print(get_current_price('BTC'))

# tickets = list(data.keys())[:10]

# dict_data = head_names_data.copy()
# for key in dict_data:
#     dict_data[key] = []



# for tk in tickets:
#     print(tk)
#     print(data[tk])
#     tk_data = data[tk]
#     for key in tk_data:
#         val = tk_data[key]
#         dict_data[tk][key].append(val)
#     break

# print(dict_data)

