import logging

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot.config import settings
from bot.general import start, send_cv_file, send_bot_source


logging.basicConfig(
    format="%(levelname)s | %(name)s | %(asctime)s | %(message)s", level=logging.INFO
)
log = logging.getLogger(__name__)


def main() -> None:
    app = Application.builder().token(settings.TG_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex("^Bot Source Code$"), send_bot_source))
    app.add_handler(
        MessageHandler(filters.Regex("^Default CV \(PDF-File\)$"), send_cv_file)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
