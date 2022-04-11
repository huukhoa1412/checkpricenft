import json
import time
import requests
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


def send_req(id,seial):
    url = 'https://www.binance.com/bapi/nft/v1/public/nft/market-mystery/mystery-list'
    pre_result = []
    req_data = {"page": 1,
                    "size": 16,
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
    chat_id = '2002320248'
    command = msg['text']

    print('Received: %s' % command)

    # markup = ReplyKeyboardMarkup(keyboard=[['Time', KeyboardButton(text='NewKey')],["File", "Audio"]])
    if command == '/p':
        items_the_s1 = send_req(3,109191979564517376)
        items_box_s1 = send_req(2,109191979564517376)
        items_the_s2 = send_req(3,155499473454738432)
        items_box_s2 = send_req(2,155499473454738432)
        items_the_s3 = send_req(3,180885755495849984)
        items_box_s3 = send_req(2,180885755495849984)
        price_the_s1 = items_the_s1[0]['amount']
        price_box_s1 = items_box_s1[0]['amount']
        price_the_s2 = items_the_s2[0]['amount']
        price_box_s2 = items_box_s2[0]['amount']
        price_the_s3 = items_the_s3[0]['amount']
        price_box_s3 = items_box_s3[0]['amount']
        telegram_bot.sendMessage (chat_id, f"S1: R {price_the_s1} | Box {price_box_s1} \nS2: R {price_the_s2} | Box {price_box_s2} \nS3: R {price_the_s3} | Box {price_box_s3} \n")
        print(f"S1: R {price_the_s1} | Box {price_box_s1}")
        print(f"S2: R {price_the_s2} | Box {price_box_s2}")
        print(f"S3: R {price_the_s3} | Box {price_box_s3}")

telegram_bot = telepot.Bot('5175449048:AAHAFfjb5fGV5p89MpDwmMNK6LdjSog3oUc')
print((telegram_bot.getMe()))

MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')

while 1:
    time.sleep(10)

