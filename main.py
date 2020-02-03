import logging, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

REQUEST_KWARGS={
    'proxy_url': 'socks5://138.201.243.83:1080',
}

updater = Updater(token='token', use_context=True,  request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id,
							text='Hello. Choose your floor', 
							reply_markup=start_menu())

def start_menu():
	third_floor = KeyboardButton(text='3')
	forth_floor = KeyboardButton(text='4')

	return ReplyKeyboardMarkup(resize_keyboard=True, [ [f, h], [third_floor, forth_floor]])

def send_third_floor(update, context):
	context.bot.send_photo(chat_id=update.message.chat_id, photo=open('1.jpg', 'rb'), caption='Third floor')

def send_forth_floor(update, context):
	context.bot.send_photo(chat_id=update.message.chat_id, photo=open('2.jpg', 'rb'), caption="Forth floor")


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.regex('3'), send_third_floor))
dispatcher.add_handler(MessageHandler(Filters.regex('4'), send_forth_floor))
updater.start_polling()
