from pyzbar.pyzbar import decode
from PIL import Image
from pprint import pprint
import re, glob

# test = 'http://m.dhlottery.co.kr/?v=0969m061113313241m041025273842m020819293445m011119293841q0205232531411998386727'

# t = re.split('[m,q]',test.split('=')[1])
# print(t)




# img = Image.open('qr_images/rr/IMG_2369.JPG')
# img.show()

def get_number_qr(code):
    # s = 'http://m.dhlottery.co.kr/?v=1003m010429394345m010429394345m010429394345m010429394345m0104293943451989'
    # http://m.dhlottery.co.kr/?v=0969m061113313241m041025273842m020819293445m011119293841q0205232531411998386727
    # t = code.split('=')[1]

    try:
        nums = re.split('[m,q]',code.split('=')[1])

    except:
        print('except  : qr_reader.py 14번줄')

    round = nums.pop(0)
    for n in range(len(nums)):
        tn = nums[n]
        nums[n] = [int(tn[i:i+2]) for i in range(0, 12, 2)]
    return round, nums

def get_number_from_image(imgs:list):
    res = []
    for img in imgs:
        decoded = decode(img)
        res_img = []
        for dc in decoded:
            d_data = dc.data.decode('utf-8')
            # d_type = dc.type
            print('======================')
            # print('d_data : ', d_data)
            round, nums = get_number_qr(d_data)
            print('회차 : ', round)
            pprint(nums)
            print('----------------------')
            res_img.append((round,nums))
        res.append(res_img)
    return res


if __name__ == '__main__':
    names = glob.glob('qr_images/rr/*.JPG')
    imgs = [Image.open(f) for f in names]

    get_number_from_image(imgs)
    # img = Image.open('/var/folders/h6/pr_bnk716lj2zw4dcly7cj700000gn/T/tmpw167sz_i/IMG_2369.JPG')
    # Image.show(img)
