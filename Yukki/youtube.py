import telebot
import requests
tok = input("Token : ")
bot = telebot.TeleBot(tok)
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id,"This bot can help you get  videos. It works automatically,  Simply send  url from youtube  by @MROAN8")
@bot.message_handler(content_types=['text'])    
def photo(message):
    if message.text:
            get = requests.get(f"https://iuytiuyt.000webhostapp.com/tiktok/s.php?url={message.text}").json()
            bot.send_video(message.chat.id,get,caption=f"<strong>Done Download Video. </strong>",parse_mode="html")
bot.polling()

#-> by @MROAN8   &&CH @PHP88