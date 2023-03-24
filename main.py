import os
import openai
import telebot
from settings import *

openai.api_key = openai_API_KEY

bot = telebot.TeleBot(telegram_API_KEY)

def verify(msg):
    return True

@bot.message_handler(func=verify)
def responder(msg):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "user", "content": msg.text}
  ]
)
    bot.reply_to(msg, completion.choices[0].message.content)


bot.polling()


