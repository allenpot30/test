#!/usr/bin/env python
# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json




from pprint import pprint

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def clean_cmd_str(cmd):
    if hasNumbers(cmd):
        return cmd.replace("_/","q").replace("$","").strip()
    else:
        return cmd.replace("_/","").replace("$","").strip()



def read_response_text(in_file,out_file):
    text_file = open(in_file)
    responses = text_file.read().split("\n$")
    response_dict = {}
    for response in responses:
        lines = response.split("\n")
        header = lines[0]
        head_split = header.split(":")
        cmd = clean_cmd_str(head_split[0])
        print(cmd)
        cmd_str = "" if len(head_split)< 2 else head_split[1]
        body = response.replace(header,"")
        resp_obj = {"cmd" : cmd, "str" : cmd_str, "body" : body}
        response_dict.update({cmd : resp_obj})

    json_file = open(out_file,'w')
    json.dump(response_dict,json_file)



read_response_text('raw_bot_response.txt','bot_response_dict.json')
bot_responses = json.load(open('bot_response_dict.json'))



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text(bot_responses['start']['body'])
def faq(bot, update):
    update.message.reply_text(bot_responses['faq']['body'])
def about(bot, update):
    update.message.reply_text(bot_responses['about']['body'])
def aboutICO(bot, update):
    update.message.reply_text(bot_responses['aboutICO']['body'])
def team(bot, update):
    update.message.reply_text(bot_responses['team']['body'])
def whitepaper(bot, update):
    update.message.reply_text(bot_responses['whitepaper']['body'])
def dates(bot, update):
    update.message.reply_text(bot_responses['dates']['body'])
def now(bot, update):
    update.message.reply_text(bot_responses['now']['body'])
def bounty(bot, update):
    update.message.reply_text(bot_responses['bounty']['body'])
def q01(bot, update):
    update.message.reply_text(bot_responses['q01']['body'])
def q02(bot, update):
    update.message.reply_text(bot_responses['q02']['body'])
def q03(bot, update):
    update.message.reply_text(bot_responses['q03']['body'])
def q04(bot, update):
    update.message.reply_text(bot_responses['q04']['body'])    
def q05(bot, update):
    update.message.reply_text(bot_responses['q05']['body'])
def q06(bot, update):
    update.message.reply_text(bot_responses['q06']['body'])
def q07(bot, update):
    update.message.reply_text(bot_responses['q07']['body'])
def q08(bot, update):
    update.message.reply_text(bot_responses['q08']['body'])
def q09(bot, update):
    update.message.reply_text(bot_responses['q09']['body'])
def q010(bot, update):
    update.message.reply_text(bot_responses['q010']['body'])

def q1(bot, update):
    update.message.reply_text(bot_responses['q1']['body'])
def q2(bot, update):
    update.message.reply_text(bot_responses['q2']['body'])
def q3(bot, update):
    update.message.reply_text(bot_responses['q3']['body'])
def q4(bot, update):
    update.message.reply_text(bot_responses['q4']['body'])    
def q5(bot, update):
    update.message.reply_text(bot_responses['q5']['body'])
def q6(bot, update):
    update.message.reply_text(bot_responses['q6']['body'])
def q7(bot, update):
    update.message.reply_text(bot_responses['q7']['body'])
def q8(bot, update):
    update.message.reply_text(bot_responses['q8']['body'])    
def q9(bot, update):
    update.message.reply_text(bot_responses['q9']['body'])
def q10(bot, update):
    update.message.reply_text(bot_responses['q10']['body'])
def q11(bot, update):
    update.message.reply_text(bot_responses['q11']['body'])

    
    
def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def log_message(bot, update):
    logger.debug(update.message.text)
    # logger.debug(update.channel_post.text)

def log_gmessage(bot, update):
    logger.debug("hey there")
    # logger.debug(update.channel_post.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.


    updater = Updater("590668272:AAFyhJhA_2NkjbduhzDmvcqFav3S3KSamt8")  




    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram-+
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("faq", faq))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("aboutICO", aboutICO))
    dp.add_handler(CommandHandler("team", team))
    dp.add_handler(CommandHandler("whitepaper", whitepaper))
    dp.add_handler(CommandHandler("dates", dates))
    dp.add_handler(CommandHandler("now", now))
    dp.add_handler(CommandHandler("bounty", bounty))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("01", q01))
    dp.add_handler(CommandHandler("02", q02))
    dp.add_handler(CommandHandler("03", q03))
    dp.add_handler(CommandHandler("04", q04))
    dp.add_handler(CommandHandler("05", q05))
    dp.add_handler(CommandHandler("06", q06))
    dp.add_handler(CommandHandler("07", q07))
    dp.add_handler(CommandHandler("08", q08))
    dp.add_handler(CommandHandler("09", q09))
    dp.add_handler(CommandHandler("010", q010))
    dp.add_handler(CommandHandler("1", q1))
    dp.add_handler(CommandHandler("2", q2))
    dp.add_handler(CommandHandler("3", q3))
    dp.add_handler(CommandHandler("4", q4))
    dp.add_handler(CommandHandler("5", q5))
    dp.add_handler(CommandHandler("6", q6))
    dp.add_handler(CommandHandler("7", q7))
    dp.add_handler(CommandHandler("8", q8))
    dp.add_handler(CommandHandler("9", q9))
    dp.add_handler(CommandHandler("10", q10))
    dp.add_handler(CommandHandler("11", q11))


    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, log_message))
    dp.add_handler(MessageHandler(Filters.group, log_gmessage))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
