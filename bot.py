import os
import telegram
from telegram.ext import Updater, CommandHandler

# Get the bot token from environment variables
TOKEN = os.getenv('7323756627:AAFENf3dUVp8yTofDMSyRqmp-2Js4QCYdFk')


# Function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, World!")

# Main function to set up the bot
def main():
    # Create an Updater object with the bot token
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add a handler for the /start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Start polling for updates from Telegram
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
