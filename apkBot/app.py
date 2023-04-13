from cgitb import text
import logging
from telegram import *
from telegram.ext import *
from flask import Flask, request
from link_extracter import get_simple_apps_games,keyboard_options,paid_mod_games
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger=logging.getLogger(__name__)

#Token provided by botfather
TOKEN="5578005923:AAHp-lp8WzUfXj-uo8g9H7KGqbw1htBhf4U"
door=None

#make and app object of flask
app=Flask(__name__)
@app.route('/')
def index():
    return "Hello!"

@app.route(f'/{TOKEN}',methods=['GET','POST'])
def webhook():
    # Request contains all thge usefull info of a particular update or response
    #we recieve updates in the form of json from telegram server 
    #the above step will convert json to a Update object for dispatcher
    update=Update.de_json(request.get_json(),bot)

    #after we got Update object we will pass it to the dispatcher
    dp.process_update(update)
    return  "ok"





def start(update:Update,context:CallbackContext):
    # print(update)
    author=update.message.from_user.first_name
    reply1=f"Hello! {author} welcome to Appy!"
    update.message.reply_text(text=reply1)
    reply2=f"""***IMPORTANT THING***\n If you do not know working of the bot please refer (/help)"""
    update.message.reply_text(text=reply2)


def _help_(update:Update,context:CallbackContext):
    help_txt="1- Using /category command select the category you want.\n2- Simply type the name of the app you want. But make sure name must be same as name of the app on Playstore.\n3- For example: candy crush saga, Minecraft-pocket edition."
    update.message.reply_text(text=help_txt)


def reply_text(update:Update,context:CallbackContext):
    # print(update.message.text)
    # intent,reply=get_reply(update.message.text,update.message.chat_id)
    
    if(update.message.text=="Apps and Games"):
        door=1
        update.message.reply_voice(voice=open("apps_and_games.mp3",'rb'),quote=True)
    elif(update.message.text=="Paid games"):
        door=2
        update.message.reply_voice(voice=open("Paid_and_Mod_games.mp3","rb"),quote=True)


    elif(update.message.text!="Apps and Games" and update.message.text!="Paid games"):
        app_link=get_simple_apps_games(update.message.text)
        if(app_link==Exception):
            app_link1,title=paid_mod_games(update.message.text)
            if(update.message.text.lower() in title and app_link1!=Exception):
                text=f"Dear, {update.message.from_user.first_name} here is your app link ENJOY!!!"
                update.message.reply_text(text=text+'\n'+app_link1)
            elif(update.message.text not in title):
                # update.message.reply_text(f"Sorry, mod of this app is not available!")
                update.message.reply_text(f"Sorry, either the spelling of the app is wrong or app might not be available!")
        elif(app_link!=Exception):
            text=f"Dear, {update.message.from_user.first_name} here is your app link ENJOY!!!"
            update.message.reply_text(text=text+'\n'+app_link)

        else:
            update.message.reply_text(f"Sorry, either the spelling of the app is wrong or app might not be available!")
    # elif(door==2 and update.message.text!="Apps and Games" and update.message.text!="Paid and Mod games"):
    #     app_link,title=paid_mod_games(update.message.text)
    #     if(update.message.text.lower() in title and app_link!=Exception):
    #         text=f"Dear, {update.message.from_user.first_name} here is your app link ENJOY!!!"
    #         update.message.reply_text(text=text+'\n'+app_link)
    #     elif(update.message.text not in title):
    #         update.message.reply_text(f"Sorry, mod of this app is not available!")



def echo_stickers(update:Update,context:CallbackContext):
    update.message.reply_sticker(sticker=update.message.sticker.file_id)



def show_category(update:Update,context:CallbackContext):
    update.message.reply_text(text="Please, select a Category", reply_markup=ReplyKeyboardMarkup(keyboard=keyboard_options,one_time_keyboard=True))


# def error(update:Update,context: CallbackContext):
#         logger.error(f"{update} has caused {update.err}")



#Representing a bot object
bot=Bot(TOKEN)
#setting webhook for telegram bot
bot.set_webhook("https://apkbot646.herokuapp.com/" + TOKEN)
#dispatcher object to handle and dispatch all kind of updates
dp=Dispatcher(bot,None)
dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("help",_help_))
dp.add_handler(CommandHandler("category",show_category))
dp.add_handler(MessageHandler(Filters.text,reply_text))
dp.add_handler(MessageHandler(Filters.sticker,echo_stickers))
# dp.add_error_handler(error)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT',5000)))

