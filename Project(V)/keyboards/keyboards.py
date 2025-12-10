from telebot import types

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('🏋️ Додати тренування')
    btn2 = types.KeyboardButton('🍎 Додати їжу')
    btn3 = types.KeyboardButton('📊 Статистика')
    btn4 = types.KeyboardButton('🎯 Змінити ціль')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def cancel_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('❌ Скасувати'))
    return markup