from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import re
import json 
import os
import time
import asyncio 
import subprocess

print("start...")


  # معرف المجموعة المستهدفة
group_id = '-1001833380321'
file_path = 'cards.json'
api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']
session_string = os.environ['TELETHON_SESSION']


async def process_messages():
	def convert_year(year):
	   year_str = str(year)
	   if len(year_str) == 4:
	   	return year_str[-2:]
	   return year_str
    
def extract_fields_v1(text):
    match = re.search(r'(\d{16})\|(\d{2})\|(\d{2})\|(\d{3,4})', text)
    if match:
        return match.groups()
    return None

def extract_fields_v2(text):
    match = re.search(r'(\d{16})\|(\d{2}/\d{2})\|(\d{3,4})', text)
    if match:
        parts = match.groups()
        num, month_year, code = parts
        month, year = month_year.split('/')
        return num, month, year, code
    return None

def extract_fields_v3(text):
    match = re.search(r'(\d{16})\|(\d{2})\|(\d{2})\r\n(\d{3,4})', text)
    if match:
        num, month, year, code = match.groups()
        return num, month, year, code
    return None

def extract_fields_v4(text):
    match = re.search(r'(\d{16})\r?\n(\d{2})\|(\d{2})\r?\n(\d{3,4})', text)
    if match:
        return match.groups()
    return None


def extract_fields_v5(text):
   # print("فحص النمط 5...")
    match = re.search(r'Card:\s*(\d{16})\|(\d{2})\|(\d{4})\|(\d{3,4})', text)
    if match:
       # print("تم التعرف على النمط 5.")
        parts = match.groups()
        num, month, year, code = parts
        return num, month, year, code
    return None
    
def extract_fields_v6(text):
    
    match = re.search(r'(d{16})|(d{2})|(d{4})|(d{3,4})', text)
    if match:
        return match.groups()
    return None

def contains_more_than_16_digits(text):
    digits = re.findall(r'\d+', text)
    total_digits = sum(len(d) for d in digits)
    return total_digits > 16

#client = TelegramClient('session_name', api_id, api_hash)
#with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def run_process_cards():
		process = await asyncio.create_subprocess_exec('python','process_cards.py')
		await process.wait()
		@client.on(events.NewMessage(chats=int(group_id)))
		async def handler(event):
			message_text = event.message.text
			if contains_more_than_16_digits(message_text):
				fields = (extract_fields_v1(message_text) or 
                  extract_fields_v2(message_text) or 
                  extract_fields_v3(message_text) or 
                  extract_fields_v4(message_text) or extract_fields_v5(message_text) or extract_fields_v6(text))
				if fields:
					num, month, year, code = fields
					data = {"num": num, "month": month, "year": year, "code": code}
					with open(file_path, 'w') as file:
						json.dump(data, file)
						await client.send_message('me', f"تم العثور على بيانات معنونة: {data}")
						await run_process_cards()
				else:
					await client.send_message('me', f"تم العثور على رسالة تحتوي على أكثر من 16 رقم، لكن لم يتم التعرف على النمط: {message_text}")
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
	await event.respond('Begin...')

client.start()
client.run_until_disconnected()
