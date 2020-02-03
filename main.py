import logging, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='912658745:AAEvvAGV-L5ajB_wkAW74eZq52K7rPtZSSM', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id,
							text='Hello, ' + update.message.chat.username + ' Use keyboard for getting information.', 
							reply_markup=start_menu())

def start_menu():
	button = KeyboardButton(text='Get information')
	return ReplyKeyboardMarkup([[button]], resize_keyboard=True)	

def send_information(update, context):
	context.bot.send_photo(chat_id=update.message.chat_id, photo=open('1.jpg', 'rb'))
	with open('t.txt') as f:
		for line in f.readlines():
			context.bot.send_message(chat_id=update.message.chat_id, text=line)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.regex('Get information'), send_information))
updater.start_polling()