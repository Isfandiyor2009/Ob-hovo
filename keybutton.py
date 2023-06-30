from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

def registratsiya():

    markub = ReplyKeyboardMarkup(resize_keyboard=True)


    markub.add(
        KeyboardButton(text='®️Registratsiyadan otish')
    )

    return markub

def back_button():

    bos = ReplyKeyboardMarkup(resize_keyboard=True)

    bos.add(
        KeyboardButton(text='🔙Orqaga')
    )

    return bos

def ob_hovo():
    obhovo = ReplyKeyboardMarkup(resize_keyboard=True)

    obhovo.add(
        KeyboardButton(text='🌤️Ob-hovo')
    )

    return obhovo