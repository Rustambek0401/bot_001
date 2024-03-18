from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from Postgres import Data_Basa
menyu = ReplyKeyboardMarkup([
    [KeyboardButton(" 🇺🇿 O'zbekcha 🇺🇿"), KeyboardButton(" 🇷🇺 Ruscha 🇷🇺 ")]
],resize_keyboard=True)

ovqat = ReplyKeyboardMarkup([
    [KeyboardButton("🍨 Taomlar 🍨"), KeyboardButton("🥦 Salatlar 🥦" )],
    [ KeyboardButton(" 🥂 Ichimliklar 🥂 "), KeyboardButton("🍱 Asartelar 🍱")],
    [KeyboardButton("🧁 Desert 🧁"), KeyboardButton("⬅️ Chiqish ⬅️")],
    [KeyboardButton("Afitsan isimlari")]
],resize_keyboard=True)

psql = ReplyKeyboardMarkup(resize_keyboard=True)
quer = f""" SELECT * FROM users;"""
for i in Data_Basa.data_basa(quer,'select'):
    # data = list
    # data = (i[0],i[1])
    psql.add(KeyboardButton(i[1]))
