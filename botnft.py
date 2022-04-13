import json
import time
import requests
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


def send_req(trang,id,seial):
    url = 'https://www.binance.com/bapi/nft/v1/public/nft/market-mystery/mystery-list'
    pre_result = []
    req_data = {"page": trang,
                    "size": 60,
                    "params":
                        {
                            "keyword": "",
                            "nftType": id,
                            "orderBy": "amount_sort",
                            "orderType": "1",
                            "serialNo": [seial],
                            "tradeType": "0"
                        }
                    }

    headers = {
            'Content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36'
    }
    r = requests.post(url, data=json.dumps(req_data), headers=headers)
    pre_result.append(r.json()['data']['data'])

    result = []
    for i in pre_result:
        for j in i:
            result.append(j)
    return result

def action(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text']

    print('Received: %s' % command)

    # markup = ReplyKeyboardMarkup(keyboard=[['Time', KeyboardButton(text='NewKey')],["File", "Audio"]])
    if command == '/n' or command == '/n@xabang_bot':
    #Box S1
        #R box S1
        items_the_r1 = send_req(1,3,109191979564517376)
        items_box_s1 = send_req(1,2,109191979564517376)
        #gia
        price_the_r1 = items_the_r1[0]['amount']
        #donvi
        donvi_the_r1 = items_the_r1[0]['currency']
        #gia
        price_box_s1 = items_box_s1[0]['amount']
        #donvi
        donvi_box_r1 = items_box_s1[0]['currency']
        #RS box S1
        items_the_sr1 = send_req(2,3,109191979564517376)
        loai_the_sr1 = 2
        i = 0
        while (loai_the_sr1 > 1):
            i = i + 1   
            loai_the_sr1= items_the_sr1[i]['rarity']
        #print(f"sr1 {i}")     
        donvi_the_sr1 = items_the_sr1[i]['currency']
        price_the_sr1 = items_the_sr1[i]['amount']
        #RSS box S1
        items_the_ssr1 = send_req(2,3,109191979564517376)
        loai_the_ssr1 = 1
        j = 20
        while (loai_the_ssr1 > 0):
            j = j + 1 
            loai_the_ssr1= items_the_ssr1[j]['rarity']
        #print(f"ssr1 {j}")     
        donvi_the_ssr1 = items_the_ssr1[j]['currency']
        price_the_ssr1 = items_the_ssr1[j]['amount']
        #SSR box S1            
    #Box S2
        #R box S2
        items_the_r2 = send_req(1,3,155499473454738432)
        items_box_s2 = send_req(1,2,155499473454738432)
        #gia
        price_the_r2 = items_the_r2[0]['amount']
        #donvi
        donvi_the_r2 = items_the_r2[0]['currency']
        #gia
        price_box_s2 = items_box_s2[0]['amount']
        #donvi
        donvi_box_r2 = items_box_s2[0]['currency']
        #RS box S2
        items_the_sr2 = send_req(2,3,155499473454738432)
        loai_the_sr2 = 2
        i = 0
        while (loai_the_sr2 > 1):
            i = i + 1 
            loai_the_sr2= items_the_sr2[i]['rarity']
        #print(f"sr2 {i}")    
        donvi_the_sr2 = items_the_sr2[i]['currency']
        price_the_sr2 = items_the_sr2[i]['amount']
        #RSS box S2
        items_the_ssr2 = send_req(2,3,155499473454738432)
        loai_the_ssr2 = 1
        j = 20
        while (loai_the_ssr2 > 0):
            j = j + 1
            loai_the_ssr2 = items_the_ssr2[j]['rarity']
        #print(f"ssr2 {j}")    
        donvi_the_ssr2 = items_the_ssr2[j]['currency']
        price_the_ssr2 = items_the_ssr2[j]['amount']
        #SSR box S2
      #Box S3
        #R box S2
        items_the_r3 = send_req(1,3,180885755495849984)
        items_box_s3 = send_req(1,2,180885755495849984)
        #gia
        price_the_r3 = items_the_r3[0]['amount']
        #donvi
        donvi_the_r3 = items_the_r3[0]['currency']
        #gia
        price_box_s3 = items_box_s3[0]['amount']
        #donvi
        donvi_box_r3 = items_box_s3[0]['currency']
        #RS box S2
        items_the_sr3 = send_req(4,3,180885755495849984)
        loai_the_sr3 = 2
        i = 0
        while (loai_the_sr3 > 1):
            i = i + 1
            loai_the_sr3 = items_the_sr3[i]['rarity']
        #print(f"sr3 {i}")    
        donvi_the_sr3 = items_the_sr3[i]['currency']
        price_the_sr3 = items_the_sr3[i]['amount']
        #RSS box S2
        items_the_ssr3 = send_req(4,3,180885755495849984)
        loai_the_ssr3 = 1
        j = 20
        while (loai_the_ssr3 > 0):
            j = j + 1    
            loai_the_ssr3= items_the_ssr3[j]['rarity']
        #print(f"ssr3 {j}")    
        donvi_the_ssr3 = items_the_ssr3[j]['currency']
        price_the_ssr3 = items_the_ssr3[j]['amount']
        #SSR box S2         
        print("OK")
        #elegram_bot.sendMessage (chat_id, f"S1: R {price_the_r1} {donvi_the_r1}| SR {price_the_sr1} {donvi_the_sr1}| SSR {price_the_ssr1} {donvi_the_ssr1}| Box {price_box_s1} {donvi_box_r1} \nS2: R {price_the_r2} {donvi_the_r2}| SR {price_the_sr2} {donvi_the_sr2}| SSR {price_the_ssr2} {donvi_the_ssr2}| Box {price_box_s2} {donvi_box_r2} \nS3: R {price_the_r3} {donvi_the_r3}| SR {price_the_sr3} {donvi_the_sr3}| SSR {price_the_ssr3} {donvi_the_ssr3}| Box {price_box_s3} {donvi_box_r3}\n")
        telegram_bot.sendMessage (chat_id, f"S1: R {price_the_r1}| SR {price_the_sr1}| SSR {price_the_ssr1}| Box {price_box_s1} \nS2: R {price_the_r2}| SR {price_the_sr2}| SSR {price_the_ssr2}| Box {price_box_s2} \nS3: R {price_the_r3}| SR {price_the_sr3}| SSR {price_the_ssr3}| Box {price_box_s3}\n")

telegram_bot = telepot.Bot('5235784128:AAEd5gY8AHcmNH1adsMCzM8QWFJZY2KUrAc')
print((telegram_bot.getMe()))

MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')

while 1:
    time.sleep(1)

