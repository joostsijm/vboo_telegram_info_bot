"""Telegram bot"""

import re

import hyperlink
from telegram import ParseMode
from telegram.ext import MessageHandler, CommandHandler, Filters

from vboo_info_bot import TELEGRAM_UPDATER, api, functions


def cmd_start(update, context):
    """Start command"""
    update.message.reply_text(
        'Hi {}'.format(update.message.from_user.first_name))

def cmd_help(update, context):
    """Help command"""
    update.message.reply_text('**HELP**', parse_mode=ParseMode.MARKDOWN)

def text_handler(update, context):
    """Handle text"""
    urls = re.findall(r'(https?://\S+)', update.message.text)
    for url in urls:
        url = hyperlink.URL.from_text(url)
        if url.host == 'rivalregions.com' or url.host == 'm.rivalregions.com':
            if 'news/show/' in url.fragment:
                article_id = url.fragment.replace('news/show/', '')
                article = api.get_article(article_id)
                formatted_article = functions.telegram_format_article(article)
                update.message.reply_text(formatted_article, parse_mode=ParseMode.MARKDOWN)


def run():
    """run function"""
    dispatcher = TELEGRAM_UPDATER.dispatcher

    # general commands
    dispatcher.add_handler(CommandHandler('start', cmd_start))
    dispatcher.add_handler(CommandHandler('help', cmd_help))

    # translate
    dispatcher.add_handler(MessageHandler(Filters.text, text_handler))

    TELEGRAM_UPDATER.start_polling()
    TELEGRAM_UPDATER.idle()
