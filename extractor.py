import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
import os

# You can get this information from https://my.telegram.org/ 
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
client = TelegramClient('TelegramDownloader', api_id, api_hash)

client.connect()

if not client.is_user_authorized():
    phone =input("phone number with country code: ")
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

# Username from which you want to retrieve media history
nick = input("Nick: ")

folder = "{}_Archive".format(str(nick))

os.mkdir(str(folder))
os.mkdir(str(folder)+"\Videos")
os.mkdir(str(folder)+"\Gifs")
os.mkdir(str(folder)+"\Photos")

async def main():
    async for message in client.iter_messages(nick):
        if message.video:
            path = await message.download_media(str(folder)+"\Videos")
            print('File saved to', path)
     
        if message.photo:
            path = await message.download_media(str(folder)+"\Photos")
            print('File saved to', path)
       
        if message.gif:
            path = await message.download_media(str(folder)+"\Gifs")
            print('File saved to', path)
        
with client:
    client.loop.run_until_complete(main())
    print("Completed!")
