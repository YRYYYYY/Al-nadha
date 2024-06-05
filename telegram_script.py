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
api_id = '26127417'
api_hash = '829adb8b07fc99aac2d3bb8061372a6d'
session_string = os.environ.get('1BJWap1sBuy-_9YzAYfCVPGO9jtjQtAxcznNqzl0NgiceDx-3AqUfS-dP0QEIzvx-q2OFHTXF_9p3-7FJrstf4YmI8Y1560W6A374A_Rm16-l4_ptzqe37bU8bPDprEdz5IFbswgo2s5LoGMehhKeUMr1ezLm2im172lVqA21gHSW-Uxz5hCGcbrOgAQYoxnNjwSNF7JZiTxsAnQYF6fKqanRahh_KnKqYuJTMQLMFk93jQNc5NzfwaAivwF-VZh1xC8gaMR5cRVvfP4xdU9c9l52X0QEGLmM5gp74Q3qONp-ulFfeeaQRwSyXwgROBXSZwPOyWHkRwTYj_LMXGjF_VwwO6exE2o=')

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

client = TelegramClient(StringSession(session_string), api_id, api_hash)

is_bot_active = True

async def run_process_cards():

    process = await asyncio.create_subprocess_exec('python','process_cards.py')

    await process.wait()

@client.on(events.NewMessage(chats=int(group_id)))
async def handler(event):
    message_text = event.message.text
    fields = None
    if is_bot_active:
                  if contains_more_than_16_digits(message_text):
                  	fields = (extract_fields_v1(message_text) or 
                  extract_fields_v2(message_text) or 
                  extract_fields_v3(message_text) or 
                  extract_fields_v4(message_text) or extract_fields_v5(message_text) or extract_fields_v6(message_text))
                  if fields:
                  	num, month, year, code = fields
                  	data = {"num": num, "month":
                  	month, "year": year, "code":code}
                  	with open(file_path, 'w') as file:
                  				json.dump(data, file)
                  	await client.send_message('me', f"تم العثور على بيانات معنونة: {data}")
                  	await run_process_cards()
                  else:
                  		await client.send_message('me', f"تم العثور على رسالة تحتوي على أكثر من 16 رقم، لكن لم يتم التعرف على النمط: {message_text}")
                  		pass  
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    global is_bot_active
    is_bot_active = True  
    await event.respond('Bot is now active...')

@client.on(events.NewMessage(pattern='/stop'))
async def stop_handler(event):
    global is_bot_active
    is_bot_active = False  
    await event.respond('Bot is now inactive...')

client.start()
while True:
	client.run_until_disconnected()
