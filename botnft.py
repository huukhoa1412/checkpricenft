import json
import os
import time
import requests



# https://www.binance.com/en/nft/search-result?serialNo=109191979564517376&nftType=3&tradeType=0&rarity=2&tab=mystery-box&keyword=topgoal&order=amount_sort%401

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
    
def main():
    while True:
        #Box S1
        items_box_s1 = send_req_box(109191979564517376)
        try:
            price_box_s1 = items_box_s1[0]['amount']
        except IndexError:
            price_box_s1 = 0
        #R1
        items_the_s1 = send_req(109191979564517376,2)
        try:
            price_the_r1 = items_the_s1[0]['amount']
        except IndexError:
            price_the_r1 = 0
        #SR1
        items_the_sr1 = send_req(109191979564517376,1)
        try:
            price_the_sr1 = items_the_sr1[0]['amount']
        except IndexError:
            price_the_sr1 = 0
        #SSR1
        items_the_ssr1 = send_req(109191979564517376,0)
        try:
            price_the_ssr1 = items_the_ssr1[0]['amount']
        except IndexError:
            price_the_ssr1 = 0
        
        #Box 2
        items_box_s2 = send_req_box(155499473454738432)
        try:
            price_box_s2 = items_box_s2[0]['amount']
        except IndexError:
            price_box_s2 = 0
        #R2
        items_the_s2 = send_req(155499473454738432,2)
        try:
            price_the_r2 = items_the_s2[0]['amount']
        except IndexError:
            price_the_r2 = 0
        #SR2
        items_the_sr2 = send_req(155499473454738432,1)
        try:
            price_the_sr2 = items_the_sr2[0]['amount']
        except IndexError:
            price_the_sr2 = 0
        #SSR2
        items_the_ssr2 = send_req(155499473454738432,0)
        try:
            price_the_ssr2 = items_the_ssr2[0]['amount']
        except IndexError:
            price_the_ssr2 = 0
            
        #Box 3
        items_box_s3 = send_req_box(180885755495849984)
        try:
            price_box_s3 = items_box_s3[0]['amount']
        except IndexError:
            price_box_s3 = 0
        #R3
        items_the_s3 = send_req(180885755495849984,2)
        try:
            price_the_r3 = items_the_s3[0]['amount']
        except IndexError:
            price_the_r3 = 0
        #SR3
        items_the_sr3 = send_req(180885755495849984,1)
        try:
            price_the_sr3 = items_the_sr3[0]['amount']
        except IndexError:
            price_the_sr3 = 0
        #SSR3
        items_the_ssr3 = send_req(180885755495849984,0)
        try:
            price_the_ssr3 = items_the_ssr3[0]['amount']
        except IndexError:
            price_the_ssr3 = 0
            
        #print(f'{total_s1} - {total_sr1} - {total_ssr1}')
        print(f"S1: R {price_the_r1} | SR {price_the_sr1} | SSR {price_the_ssr1} | Box {price_box_s1} ")
        #print(f'{total_s2} - {total_sr2} - {total_ssr2}')
        print(f"S2: R {price_the_r2} | SR {price_the_sr2} | SSR {price_the_ssr2} | Box {price_box_s2} ")
        #print(f'{total_s3} - {total_sr3} - {total_ssr3}')
        print(f"S3: R {price_the_r3} | SR {price_the_sr3} | SSR {price_the_ssr3} | Box {price_box_s3} ")


if __name__ == '__main__':
    main()
