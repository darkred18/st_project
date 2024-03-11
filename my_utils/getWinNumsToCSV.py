import requests
from stqdm import stqdm
import pandas as pd

# def get_lastRound_data(path):
#     model = pd.read_csv(path)
#     return int(model["회차"].to_list()[-1])

def crawlingLottoData(fullPath, update = True):

    model = pd.read_csv(fullPath)
    round_num = model["회차"].to_list()[-1]
    date = model["추첨일"].to_list()[-1]

    
    if update:
        round_num, date =  update_lotto_db(fullPath, round_num+1)

    print("round_num : ", round_num)
    dbInfo = "회차 : " + str(round_num) + ", 추첨일 : " + date
    return dbInfo, round_num

#=========  TO DO   ================
#   progress bar 구현
#-----------------------------------

# 로또 복권 데이터 크롤링
def getLottoWinInfo(startRound, endRound):
    
    drwtNo1 = [] 
    drwtNo2 = [] 
    drwtNo3 = [] 
    drwtNo4 = [] 
    drwtNo5 = [] 
    drwtNo6 = [] 
    bnusNo = [] 
    totSellamnt = [] 
    drwNoDate = [] 
    firstAccumamnt = [] 
    firstPrzwnerCo = [] 
    firstWinamnt = [] 
    roundNo = []
    
    for i in stqdm(range(startRound, endRound+1, 1)): 
        
        # i = 1
        
        req_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(i)
        
        req_lotto = requests.get(req_url) 

        # print("=====    lottoNo   +++++")
        # print(req_lotto)
        
        lottoNo = req_lotto.json() 
        if lottoNo['returnValue'] == 'fail':
            print(" 더 찾을수 없습니다.")
            if drwtNo1: break
            else:return None, None

        drwtNo1.append(lottoNo['drwtNo1']) 
        drwtNo2.append(lottoNo['drwtNo2']) 
        drwtNo3.append(lottoNo['drwtNo3']) 
        drwtNo4.append(lottoNo['drwtNo4']) 
        drwtNo5.append(lottoNo['drwtNo5']) 
        drwtNo6.append(lottoNo['drwtNo6']) 
        bnusNo.append(lottoNo['bnusNo']) 

        roundNo.append(i)
        totSellamnt.append(lottoNo['totSellamnt']) 
        drwNoDate.append(lottoNo['drwNoDate']) 
        firstAccumamnt.append(lottoNo['firstAccumamnt']) 
        firstPrzwnerCo.append(lottoNo['firstPrzwnerCo']) 
        firstWinamnt.append(lottoNo['firstWinamnt']) 
        
    lotto_dict = {"회차":roundNo,
                    "No.1":drwtNo1, "No.2":drwtNo2,
                    "No.3":drwtNo3, "No.4":drwtNo4, "No.5":drwtNo5, 
                    "No.6":drwtNo6, "보너스":bnusNo,
                    "추첨일":drwNoDate, 
                    "총판매금액":totSellamnt,
                    "총1등당첨금":firstAccumamnt,
                    "1등당첨인원":firstPrzwnerCo,
                    "1등수령액":firstWinamnt}
    lotto_df = pd.DataFrame(lotto_dict)
    return lotto_dict, lotto_df

def update_lotto_db(path, idx):
    drwtNo1 = [] 
    drwtNo2 = [] 
    drwtNo3 = [] 
    drwtNo4 = [] 
    drwtNo5 = [] 
    drwtNo6 = [] 
    bnusNo = [] 
    totSellamnt = [] 
    drwNoDate = [] 
    firstAccumamnt = [] 
    firstPrzwnerCo = [] 
    firstWinamnt = [] 
    roundNo = []

    while(True):
        req_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(idx)
        req_lotto = requests.get(req_url)
        lottoNo = req_lotto.json()

        if lottoNo['returnValue'] == 'fail':
            break
        
        drwtNo1.append(lottoNo['drwtNo1']) 
        drwtNo2.append(lottoNo['drwtNo2']) 
        drwtNo3.append(lottoNo['drwtNo3']) 
        drwtNo4.append(lottoNo['drwtNo4']) 
        drwtNo5.append(lottoNo['drwtNo5']) 
        drwtNo6.append(lottoNo['drwtNo6']) 
        bnusNo.append(lottoNo['bnusNo']) 

        roundNo.append(idx)
        totSellamnt.append(lottoNo['totSellamnt']) 
        drwNoDate.append(lottoNo['drwNoDate']) 
        firstAccumamnt.append(lottoNo['firstAccumamnt']) 
        firstPrzwnerCo.append(lottoNo['firstPrzwnerCo']) 
        firstWinamnt.append(lottoNo['firstWinamnt']) 
        idx += 1

    lotto_dict = {  "회차":roundNo,
                    "No.1":drwtNo1, "No.2":drwtNo2,
                    "No.3":drwtNo3, "No.4":drwtNo4, "No.5":drwtNo5, 
                    "No.6":drwtNo6, "보너스":bnusNo,
                    "추첨일":drwNoDate, 
                    "총판매금액":totSellamnt,
                    "총1등당첨금":firstAccumamnt,
                    "1등당첨인원":firstPrzwnerCo,
                    "1등수령액":firstWinamnt}
    lotto_df = pd.DataFrame(lotto_dict)
    lotto_df.to_csv(path, index=False, mode='a', header=False, encoding='utf-8-sig')

    return (roundNo[-1], drwNoDate[-1])

# 연금 복권
def getPensionWinInfo(startRound, endRound):
    roundNo = []
    cho = []
    rankClass = []
    bnusNo =[]
    drwNoDate = [] 

    for i in range(startRound, endRound):
        url = "https://www.dhlottery.co.kr/common.do?method=get720Number&drwNo=" + str(i)
        req_lotto = requests.get(url) 
        pensionNums = req_lotto.json()

        roundNo.append(int(pensionNums['rows1'][0]['round_num']))
        drwNoDate.append(int(pensionNums['rows1'][0]['pensionDrawDate']))
        rankClass.append(pensionNums['rows1'][0]['rankClass'])
        bnusNo.append(pensionNums['rows1'][0]['rankNo'])
        cho.append(pensionNums['rows2'][0]['rankClass'])

    lotto_dict = {"회차":roundNo, "조" : cho, "당첨번호":rankClass, "보너스번호":bnusNo, "추첨일":drwNoDate} 

    return pd.DataFrame(lotto_dict)

