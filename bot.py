import logging
from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, filters, ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="""Bienvenue sur mon bot. Envoyez moi des instructions ou des messages. /youtube - Pour ma chaîne youtube 
    /linkedin - Pour mon profile Linkedin 
    /gmail - Pour m/'envoyer des mails sympa
    /geeks - Un URL extra""")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""Commande disponible :- 
    /youtube - Pour ma chaîne youtube 
    /linkedin - Pour mon profile Linkedin 
    /gmail - Pour m/'envoyer des mails sympa
    /geeks - Un URL extra""")


async def gmail_url(update: Update, context: CallbackContext):
    await update.message.reply_text("akambinabil@outlook.com")


async def youtube_url(update: Update, context: CallbackContext):
    await update.message.reply_text("https://www.youtube.com/@biloud")


async def linkedIn_url(update: Update, context: CallbackContext):
    await update.message.reply_text("https://www.linkedin.com/in/akambi-nabil-lawani-a2847a1b3/")


async def geeks_url(update: Update, context: CallbackContext):
    await update.message.reply_text("GeeksforGeeks url here")


async def unknown_text(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Désolé je ne comprends pas '%s'" % update.message.text)


async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Désolé '%s' Je n'ai aucune action configurée pour cette commande" % update.message.text)


if __name__ == '__main__':
    application = ApplicationBuilder().token('your telegram token').build()
    start_handler = CommandHandler('start', start)
    youtube_handler = CommandHandler('youtube', youtube_url)
    linkedin_handler = CommandHandler('linkedin', linkedIn_url)
    gmail_handler = CommandHandler('gmail', gmail_url)
    geeks_handler = CommandHandler('geeks', geeks_url)
    echo_handler = MessageHandler(filters.TEXT, unknown_text)
    command_handler = MessageHandler(filters.COMMAND, unknown)
    help_handler = CommandHandler('help', help)

    application.add_handler(start_handler)
    application.add_handler(youtube_handler)
    application.add_handler(linkedin_handler)
    application.add_handler(gmail_handler)
    application.add_handler(geeks_handler)
    application.add_handler(echo_handler)
    application.add_handler(command_handler)
    application.add_handler(help_handler)

    application.run_polling()
