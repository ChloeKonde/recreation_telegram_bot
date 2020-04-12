import logging, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup 


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



updater = Updater(token='', use_context=True)
dispatcher = updater.dispatcher
url = 'http://35.228.181.111/'
map_game = 'recreation_nsu_map'


def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id,
							text='Hello. Use keyboard for getting information.',
							reply_markup=start_menu())


def call_handler(update, context):
	context.bot.answerCallbackQuery(
								callback_query_id=update['callback_query']['id'],
								url=url)


def start_menu():
	interactive_map = KeyboardButton(text='Get interactive map')
	return ReplyKeyboardMarkup([[interactive_map]], resize_keyboard=True)	


def send_map(update, context):
	context.bot.send_game(chat_id=update.message.chat_id, game_short_name=map_game)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.regex('Get interactive map'), send_map))
dispatcher.add_handler(CallbackQueryHandler(call_handler))
updater.start_polling()

