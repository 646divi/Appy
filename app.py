from telegram import ForceReply, Update,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import dotenv_values
from linkExtracter import paid_mod_games


config = dotenv_values(".env")
# print(config)
TOKEN=config['TOKEN']

keyboard_options=[[InlineKeyboardButton("Apps and Games",callback_data="1")],
                  [InlineKeyboardButton("Paid games",callback_data="2")]
                  ]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    
    user=update.message.from_user.first_name
    reply1 = f"Hello! {user} welcome to TheProvider😈!"
    await update.message.reply_text(text=reply1)
    reply2 = """***IMPORTANT THING***\n If you do not know working of the bot please refer (/help)"""
    await update.message.reply_text(text=reply2)
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    help_txt = "1- Using /category command select the category you want.\n2- Simply type the name of the app you want. But make sure the name must be the same as the name of the app on Playstore.\n3- For example: candy crush saga, Minecraft-pocket edition."
    await update.message.reply_text(text=help_txt)

async def show_category(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text="Please, select a Category", reply_markup=InlineKeyboardMarkup(keyboard_options))


async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global door
    if update.message.text == "Apps and Games" or update.message.text == "Paid games":
        door = 1
        await update.message.reply_voice(voice=open("apps_and_games.mp3", 'rb'), quote=True)
    elif update.message.text == "Paid games":
        door = 2
        await update.message.reply_voice(voice=open("Paid_and_Mod_games.mp3", "rb"), quote=True)
    elif update.message.text != "Apps and Games" and update.message.text != "Paid games":
        app_link,title = paid_mod_games(update.message.text)
        
        if app_link != Exception:
            text = f"Dear, {update.message.from_user.first_name} here is your app link ENJOY!!!"
            await update.message.reply_text(text=title+'\n'+app_link)
        else:
            await update.message.reply_text(f"Sorry, either the spelling of the app is wrong or the app might not be available!")

def main() -> None:
    
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("category", show_category))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply_text))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)




if __name__ == "__main__":
    main()