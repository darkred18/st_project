from pyzbar.pyzbar import decode
from PIL import Image, ImageOps
from pprint import pprint
import re, glob,time


def get_number_qr(code):
    try:
        nums = re.split('[m,q]',code.split('=')[1])
        round = nums.pop(0)
        for n in range(len(nums)):
            tn = nums[n]
            nums[n] = [int(tn[i:i+2]) for i in range(0, 12, 2)]
        return round, nums
    except:
        print('except  : qr_reader.py 14번줄')
        return None,None


def get_number_from_image(imgs:list):
    res = []
    for img in imgs:
        decoded = decode(img)
        if decoded == []:
            continue
        res_img = []
        for dc in decoded:
            d_data = dc.data.decode('utf-8')
            # d_type = dc.type
            # print('======================')
            # print('d_data : ', d_data)
            round, nums = get_number_qr(d_data)
            # print('회차 : ', round)
            # pprint(nums)
            # print('----------------------')
            if round is not None:
                res_img.append((round,nums))
        res.append(res_img)
    return res

def image_resize(f_imgs):
    stime = time.time()
    #이미지가 자동으로 회전되는 현상을 막아줌.
    #ImageOps.exif_transpose(image)
    imgs = [ImageOps.exif_transpose(Image.open(f)) for f in f_imgs]
    print('image open : %f'%(time.time()-stime))
    

    stime = time.time()
    for i in range(len(imgs)):
        w,h = imgs[i].size
        img_width = 640 if w > h else 480
        if w <= img_width: continue
        img_ratio = img_width/float(w)
        img_height = int((h * img_ratio)) 
        rimg = imgs[i].resize((img_width,img_height))
        imgs[i] = rimg
    print('image_resize : %f'%(time.time()-stime))
    return imgs

if __name__ == '__main__':
    names = glob.glob('qr_images/rr/*.JPG')
    imgs = [Image.open(f) for f in names]

    get_number_from_image(imgs)
    # img = Image.open('/var/folders/h6/pr_bnk716lj2zw4dcly7cj700000gn/T/tmpw167sz_i/IMG_2369.JPG')
    # Image.show(img)
