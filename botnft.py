import json
import time
import requests
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


def send_req(seial,loai):
    url = 'https://www.binance.com/bapi/nft/v1/public/nft/market-mystery/mystery-list'
    pre_result = []

    for i in range(1, 2):

        req_data = {"page": i,
                    "size": 16,
                    "params":
                        {
                            "keyword": "topgoal",
                            "nftType": "3",
                            "orderBy": "amount_sort",
                            "orderType": "1",
                            "rarity": loai,
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
    time.sleep(0.5)    
    result = []
    for i in pre_result:
        for j in i:
            result.append(j)
    return result  

def send_req_box(seial):
    url = 'https://www.binance.com/bapi/nft/v1/public/nft/market-mystery/mystery-list'
    pre_result = []

    for i in range(1, 2):

        req_data = {"page": i,
                    "size": 16,
                    "params":
                        {
                            "keyword": "topgoal",
                            "nftType": "2",
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
    if command == '/n' or command == '/n@xabang_bot' or command == '/nft' or command == '/nfts':
        items_box_s1 = send_req_box(109191979564517376)
        price_box_s1 = items_box_s1[0]['amount']
        #R1
        items_the_s1 = send_req(109191979564517376,2)
        price_the_r1 = items_the_s1[0]['amount']
        #SR1
        items_the_sr1 = send_req(109191979564517376,1)
        price_the_sr1 = items_the_sr1[0]['amount']
        #SSR1
        items_the_ssr1 = send_req(109191979564517376,0)
        price_the_ssr1 = items_the_ssr1[0]['amount']
        
        #Box 2
        items_box_s2 = send_req_box(155499473454738432)
        price_box_s2 = items_box_s2[0]['amount']
        #R1
        items_the_s2 = send_req(155499473454738432,2)
        price_the_r2 = items_the_s2[0]['amount']
        #SR1
        items_the_sr2 = send_req(155499473454738432,1)
        price_the_sr2 = items_the_sr2[0]['amount']
        #SSR1
        items_the_ssr2 = send_req(155499473454738432,0)
        price_the_ssr2 = items_the_ssr2[0]['amount']
        
        #Box 3
        items_box_s3 = send_req_box(180885755495849984)
        price_box_s3 = items_box_s3[0]['amount']
        #R1
        items_the_s3 = send_req(180885755495849984,2)
        price_the_r3 = items_the_s3[0]['amount']
        #SR1
        items_the_sr3 = send_req(180885755495849984,1)
        price_the_sr3 = items_the_sr3[0]['amount']
        #SSR1
        items_the_ssr3 = send_req(180885755495849984,0)
        price_the_ssr3 = items_the_ssr3[0]['amount']
        
        #print(f'{total_s1} - {total_sr1} - {total_ssr1}')
        #print(f"S1: R {price_the_r1} | SR {price_the_sr1} | SSR {price_the_ssr1} | Box {price_box_s1} ")
        #print(f'{total_s2} - {total_sr2} - {total_ssr2}')
        #print(f"S2: R {price_the_r2} | SR {price_the_sr2} | SSR {price_the_ssr2} | Box {price_box_s2} ")
        #print(f'{total_s3} - {total_sr3} - {total_ssr3}')
        #print(f"S3: R {price_the_r3} | SR {price_the_sr3} | SSR {price_the_ssr3} | Box {price_box_s3} ")
          
        print("OK")
        #elegram_bot.sendMessage (chat_id, f"S1: R {price_the_r1} {donvi_the_r1}| SR {price_the_sr1} {donvi_the_sr1}| SSR {price_the_ssr1} {donvi_the_ssr1}| Box {price_box_s1} {donvi_box_r1} \nS2: R {price_the_r2} {donvi_the_r2}| SR {price_the_sr2} {donvi_the_sr2}| SSR {price_the_ssr2} {donvi_the_ssr2}| Box {price_box_s2} {donvi_box_r2} \nS3: R {price_the_r3} {donvi_the_r3}| SR {price_the_sr3} {donvi_the_sr3}| SSR {price_the_ssr3} {donvi_the_ssr3}| Box {price_box_s3} {donvi_box_r3}\n")
        telegram_bot.sendMessage (chat_id, f"S1: R {price_the_r1} | SR {price_the_sr1} | SSR {price_the_ssr1} | Box {price_box_s1} \nS2: R {price_the_r2} | SR {price_the_sr2} | SSR {price_the_ssr2} | Box {price_box_s2} \nS3: R {price_the_r3} | SR {price_the_sr3} | SSR {price_the_ssr3} | Box {price_box_s3}\n")

telegram_bot = telepot.Bot('5395216210:AAEKJynIsSMMXuike2rdaKjLdDyQMFkJ_ig')
print((telegram_bot.getMe()))

MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')

while 1:
    time.sleep(0)
