from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from bot.config import settings
from bot.keyboards import INITIAL_KEYBOARD


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
    print(settings.BASE_DIR / "static/Mykhailo Kukol CV.pdf")
    with open(settings.BASE_DIR / "static/Mykhailo Kukol CV.pdf", "rb") as file:
        await update.message.reply_document(
            file,
            reply_markup=markup,
            caption="Here is my CV ⬆️",
        )
