#!/usr/bin/python
# -*- coding: utf-8 -*-

import cachet
import telebot
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

BOT_TOKEN = os.getenv('BOT_TOKEN')


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hi, i am Bot!')


@bot.message_handler(commands=['incidents'])
def show_incidents(message):
    incidents = cachet.get_incidents()
    bot.send_message(message.chat.id, 'На данный момент в системе зарегистрированы следующие инциденты:')
    for item in incidents:
        if item['status'] < 4:
            answer = '- %s (%s)' % (item['name'], item['human_status'])

            if item['component'] is not None:
                answer += '\n  Затронут сервис: % s' % item['component']['name']

            bot.send_message(message.chat.id, answer)


print('Bot started')

bot.polling()
