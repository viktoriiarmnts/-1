import sqlite3
import config
from datetime import datetime


# Оскільки ми запускаємо main.py з кореня, шлях до БД буде від кореня
def connect():
    return sqlite3.connect(config.DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS workouts 
                      (id INTEGER PRIMARY KEY, user_id INTEGER, type TEXT, duration INTEGER, date TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS meals 
                      (id INTEGER PRIMARY KEY, user_id INTEGER, food_name TEXT, calories INTEGER, date TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS goals 
                      (user_id INTEGER PRIMARY KEY, goal_text TEXT)''')

    conn.commit()
    conn.close()


def add_workout(user_id, w_type, duration):
    conn = connect()
    cursor = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO workouts (user_id, type, duration, date) VALUES (?, ?, ?, ?)",
                   (user_id, w_type, duration, today))
    conn.commit()
    conn.close()


def add_meal(user_id, food_name, calories):
    conn = connect()
    cursor = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO meals (user_id, food_name, calories, date) VALUES (?, ?, ?, ?)",
                   (user_id, food_name, calories, today))
    conn.commit()
    conn.close()


def set_goal(user_id, goal_text):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO goals (user_id, goal_text) VALUES (?, ?)",
                   (user_id, goal_text))
    conn.commit()
    conn.close()


def get_today_stats(user_id):
    conn = connect()
    cursor = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("SELECT goal_text FROM goals WHERE user_id = ?", (user_id,))
    goal_res = cursor.fetchone()
    goal = goal_res[0] if goal_res else "Не встановлено"

    cursor.execute("SELECT COUNT(*), SUM(duration) FROM workouts WHERE user_id = ? AND date = ?", (user_id, today))
    w_stats = cursor.fetchone()
    w_count = w_stats[0] if w_stats[0] else 0
    w_dur = w_stats[1] if w_stats[1] else 0

    cursor.execute("SELECT SUM(calories) FROM meals WHERE user_id = ? AND date = ?", (user_id, today))
    c_stats = cursor.fetchone()
    c_total = c_stats[0] if c_stats[0] else 0

    conn.close()
    return goal, w_count, w_dur, c_total