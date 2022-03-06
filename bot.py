from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '2053876681:AAE3_lbzwXW7kJsrk80o9baoGopDbWEaGjk'


def start(update, context):
  update.message.reply_text("""
    Bienvenu sur le bot officiel de @alone, le bot te permet de partage des messages aux menbre des groupes de discutions,
    les commandes disponibles sont:
    - /start
    - /sendmessage
    - /addcanal
    - /addgroup
    - /viewhistory
    - /sendmassivemessage
    - /viewadd
    - /subscribe
    - /login
    - /logout
    - /buyadd
    - /contactme
    enjoy sur telegram
  """)

def main():
  updater = Updater('2053876681:AAE3_lbzwXW7kJsrk80o9baoGopDbWEaGjk')

  dp = updater.dispatcher
  dp.add_handler(CommandHandler('start', start))

  updater.start_polling()


if __name__ == '__main__':
  main()