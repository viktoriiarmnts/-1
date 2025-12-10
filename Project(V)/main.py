from loader import bot
from database import database
import handlers  # Цей рядок активує всі хендлери

if __name__ == '__main__':
    # Створюємо таблиці (звертаємось до модуля database, а в ньому до функції create_tables)
    database.create_tables()

    print("✅ Бот успішно запущено з новою структурою!")
    bot.infinity_polling()