import time
import requests
from bs4 import BeautifulSoup
import ccxt,json
import pandas as pd
import test, utils

# #get dollar value
# url = 'https://coinmarketcap.com/ko/currencies/tether'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# select = soup.select('#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.eMxKgr.container > div.n78udj-0.jskEGI > div > div.sc-16r8icm-0.kjciSH.priceSection > div.sc-16r8icm-0.kjciSH.priceTitle > div > span')
# Tether_krw = float(str(select[0]).split('₩')[1].split('<')[0].replace(',',''))

# #get bitcoin price
# binance = ccxt.binance()
# upbit = ccxt.upbit()
# binance_today_USDT_BTC = binance.fetchTicker('BTC/USDT').get('last')
# upbit_today_KRW_BTC = upbit.fetchTicker('BTC/KRW').get('last')
# upbit_today_USDT_BTC = upbit_today_KRW_BTC/Tether_krw

# #get kimchi premium
# kimchi_premium_BTC = str(round((round(upbit_today_USDT_BTC/binance_today_USDT_BTC,4) - 1 )*100, 4)) + '%'
# print(kimchi_premium_BTC)


import pprint


bnc = ccxt.binance()

# # takes a long time line
# markets = bnc.fetch_tickers()
# market = bnc.fetch_ticker('BTC/USDT')

# # 바이낸스 코인 종류 
# coin_names = [m for m in markets if 'USDT' in m]
# # print(coin_names)
# # print(len(coin_names))


# # json 파일 쓰기
# with open('coin_names.json', 'w') as f:
#     json.dump({'coin_names':coin_names}, f)

# # json 파일 읽기
# stime = time.time()
# with open('coin_names.json','r') as f:
#     temp = json.load(f)
# print(temp)
# print("json 읽기 : ", time.time()-stime)

# # text 파일 읽기
# stime = time.time()
# with open('coin_names.txt','r') as f:
#     temp = f.readline()
# print(temp)
# print("text 읽기 : ", time.time()-stime)







# symbol의 과거 이력
def load_trading_data(symbol):
    # btc_ohlcv = bnc.fetch_ohlcv(symbol, timeframe='1d')
    btc_ohlcv = bnc.fetch_ohlcv(symbol, limit=10)
    trading_df = pd.DataFrame(
        btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    trading_df['datetime'] = pd.to_datetime(
        trading_df['datetime'], unit='ms')
    trading_df.set_index('datetime', inplace=True)
    return trading_df

# symbol의 현개 가격(달러)
def get_current_price(symbol, trading_df=None):
    if trading_df is None:
        trading_df = load_trading_data(symbol)
    current_price = trading_df.iloc[-1,3]
    # current_price = trading_df['close'][-1]
    return current_price

df = load_trading_data('BTC/USDT')
print(df)

# # 비트코인 시세 csv 저장 
# df.to_csv('btc_usdt.csv')




# usd_krw = utils.get_usd_krw()
# print('현재 환율 : ',usd_krw)

# btc_krw = float(test.get_current_price('BTC'))
# print("BTC 현재가 : ", btc_krw)

# btc_usd = get_current_price('BTC/USDT')
# print('BTC current prict : ',btc_usd)

# chng_krw = btc_usd * usd_krw
# print('변환 현재가 : ', chng_krw)

# kimchi_p = btc_krw / chng_krw
# print('김치 프리미엄 : ',kimchi_p)

