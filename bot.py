from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN_BOT') 
print(TOKEN)

button_list = ['free python course 😉', 'javascript', 'random 1']

def startCommand(update: Update, context: CallbackContext):
  buttons = [
    [
      KeyboardButton('free python course 😉'),
      KeyboardButton('javascript course'),
      KeyboardButton('random 1')
    ],
    [
      KeyboardButton('free python course 😉'),
      KeyboardButton('javascript course'),
      KeyboardButton('random 1')
    ],
    [
      KeyboardButton('free python course 😉'),
      KeyboardButton('javascript course'),
      KeyboardButton('random 1')
    ],
    [KeyboardButton('random 1')]
  ]
  context.bot.send_message(
    chat_id=update.effective_chat.id, 
    text="welcom to telegram bot", 
    reply_markup=ReplyKeyboardMarkup(buttons)
  )

def messageHandler(update: Update, context: CallbackContext):
  for text in button_list:
    if text in update.message.text:
      context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    # else:
    #   context.bot.send_message(chat_id=update.effective_chat.id, text="no found commade")

def main():
  updater = Updater('2053876681:AAE3_lbzwXW7kJsrk80o9baoGopDbWEaGjk')
  dp = updater.dispatcher
  dp.add_handler(CommandHandler('start', startCommand))
  dp.add_handler(MessageHandler(Filters.text, messageHandler))
  updater.start_polling()


if __name__ == '__main__':
  main()