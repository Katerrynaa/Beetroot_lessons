from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Bot
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",
                     user = "root",
                     password="rootroot11",
                     db="schema")


bot_token = "6614098638:AAEuEJRZzpKyGauOvYJkOxgDnuCNiFD235c"
channel_id = "-1001862246809"

updater = Updater(bot_token, use_context=True)
bot = Bot(token=bot_token)

def send_msg(message):
    bot.send_message(chat_id=channel_id, text=message)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot. Please press /start ")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you, you said '%s'" % update.message.text)

cursor = db.cursor()
cursor.execute("SELECT * FROM Schema.polls_message")
data = cursor.fetchall()

for row in data:
    msg = f"Data from Schema: {row}"
    send_msg(msg)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) 
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling()






