from telebot import types
# Оскільки loader - це тепер папка з __init__.py, імпорт виглядає так само
from loader import bot
# Імпортуємо модуль database з папки database
from database import database
# Імпортуємо keyboards з папки keyboards
from keyboards import keyboards


# --- Допоміжна функція ---
def check_cancel(message):
    if message.text == '❌ Скасувати':
        bot.send_message(message.chat.id, "Дію скасовано.", reply_markup=keyboards.main_menu())
        return True
    return False


# --- START ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        f"Привіт, {message.from_user.first_name}! Обирай дію:",
        reply_markup=keyboards.main_menu()
    )


# --- ТРЕНУВАННЯ ---
@bot.message_handler(func=lambda m: m.text == '🏋️ Додати тренування')
def workout_start(message):
    msg = bot.send_message(message.chat.id, "Яке тренування? (Біг, Зал, Йога)", reply_markup=keyboards.cancel_menu())
    bot.register_next_step_handler(msg, process_w_type)


def process_w_type(message):
    if check_cancel(message): return
    w_type = message.text
    msg = bot.send_message(message.chat.id, "Скільки хвилин?", reply_markup=keyboards.cancel_menu())
    bot.register_next_step_handler(msg, process_w_duration, w_type)


def process_w_duration(message, w_type):
    if check_cancel(message): return
    if not message.text.isdigit():
        msg = bot.send_message(message.chat.id, "❌ Введи тільки цифри:")
        bot.register_next_step_handler(msg, process_w_duration, w_type)
        return

    database.add_workout(message.chat.id, w_type, int(message.text))
    bot.send_message(message.chat.id, "✅ Тренування збережено!", reply_markup=keyboards.main_menu())


# --- ЇЖА ---
@bot.message_handler(func=lambda m: m.text == '🍎 Додати їжу')
def meal_start(message):
    msg = bot.send_message(message.chat.id, "Що ти з'їв?", reply_markup=keyboards.cancel_menu())
    bot.register_next_step_handler(msg, process_food_name)


def process_food_name(message):
    if check_cancel(message): return
    food = message.text
    msg = bot.send_message(message.chat.id, "Скільки калорій?", reply_markup=keyboards.cancel_menu())
    bot.register_next_step_handler(msg, process_food_cal, food)


def process_food_cal(message, food):
    if check_cancel(message): return
    if not message.text.isdigit():
        msg = bot.send_message(message.chat.id, "❌ Тільки цифри:")
        bot.register_next_step_handler(msg, process_food_cal, food)
        return

    database.add_meal(message.chat.id, food, int(message.text))
    bot.send_message(message.chat.id, f"✅ {food} додано!", reply_markup=keyboards.main_menu())


# --- ЦІЛЬ ---
@bot.message_handler(func=lambda m: m.text == '🎯 Змінити ціль')
def goal_start(message):
    msg = bot.send_message(message.chat.id, "Напиши нову ціль:", reply_markup=keyboards.cancel_menu())
    bot.register_next_step_handler(msg, process_goal)


def process_goal(message):
    if check_cancel(message): return
    database.set_goal(message.chat.id, message.text)
    bot.send_message(message.chat.id, "✅ Ціль оновлено!", reply_markup=keyboards.main_menu())


# --- СТАТИСТИКА ---
@bot.message_handler(func=lambda m: m.text == '📊 Статистика')
def show_stats(message):
    goal, w_count, w_dur, c_total = database.get_today_stats(message.chat.id)
    text = (f"📅 **Сьогодні:**\n🎯 Ціль: {goal}\n"
            f"🏋️ Тренувань: {w_count} ({w_dur} хв)\n🍎 Калорій: {c_total}")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=keyboards.main_menu())