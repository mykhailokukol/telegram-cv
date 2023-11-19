from telegram import ReplyKeyboardMarkup, Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot.config import settings
from bot.keyboards import INITIAL_KEYBOARD, REDIRECT_SOURCE_CODE_KEYBOARD


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    markup = ReplyKeyboardMarkup(INITIAL_KEYBOARD)
    await update.message.reply_text(
        "Hey!\nWelcome to my CV bot!\nCheck out the keyboard below 👇",
        reply_markup=markup,
    )


async def send_cv_file(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    markup = ReplyKeyboardMarkup(INITIAL_KEYBOARD)
    with open(settings.BASE_DIR / "static/Mykhailo Kukol CV.pdf", "rb") as file:
        await update.message.reply_document(
            file,
            reply_markup=markup,
            caption="Here is my CV ⬆️",
        )


async def send_bot_source(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    markup = InlineKeyboardMarkup(REDIRECT_SOURCE_CODE_KEYBOARD)
    await update.message.reply_text(
        "The next button leads to third-party service (github.com).\nIf you are sure click/tap on it",
        reply_markup=markup,
    )
