from telegram import InlineKeyboardButton


INITIAL_KEYBOARD = [
    [
        InlineKeyboardButton("Interactive CV"),
        InlineKeyboardButton("Default CV (PDF-File)"),
    ],
    [
        InlineKeyboardButton("Bot Source Code"),
    ],
]

REDIRECT_SOURCE_CODE_KEYBOARD = [
    [
        InlineKeyboardButton(
            "Source Code", url="https://github.com/mykhailokukol/telegram-cv"
        ),
    ]
]
