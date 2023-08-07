from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types.message import ContentType
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.chat_join_request import ChatJoinRequest
import csv
import time
import datetime

# from aiogram.utils.callback_data import CallbackData
from aiogram.utils.callback_answer import CallbackAnswer as CallbackData
from aiogram.types import ChatMember
import logging
import aiohttp
from db_narod_of import DataBase
from aiogram.client.session.aiohttp import AiohttpSession
import asyncio

Session = AiohttpSession(proxy="http://proxy.server:3128")


Token = ("6445419185:AAHLVCb18Xq_jcN594PsOOuxyV7se0sljZg")
bot = Bot(token=Token, session = Session, parse_mode="HTML")
dp = Dispatcher()
db = DataBase(db_file="USER_PODPS.db")

action = CallbackData("check", "data")

logging.basicConfig(level=logging.INFO)


#   ОСНОВНОЙ КОД БОТА # 

# markup = types.InlineKeyboardMarkup(True)
builder = InlineKeyboardBuilder()

link_keyboard1 = types.InlineKeyboardButton(text = "1-й канал", url = "https://t.me/+vzTyzvgBdC8wOWUy")
link_keyboard2 = types.InlineKeyboardButton(text = "2-й канал", url = "https://t.me/+8jQ_Jlu2YN43M2Qy")
link_keyboard3 = types.InlineKeyboardButton(text = "3-й канал", url = "https://t.me/+AaMLtLsF6sU5OWIy")
check_keybord_button = types.InlineKeyboardButton(text="Проверить подписку", callback_data="check")
builder.add(link_keyboard1)
builder.add(link_keyboard2)
builder.add(link_keyboard3)
builder.add(check_keybord_button)

# markup.insert(link_keyboard1)
# markup.insert(link_keyboard2)
# markup.insert(link_keyboard3)
# markup.insert(check_keybord_button)
markup = builder.as_markup()

@dp.message(Command("start"))
async def start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    await bot.send_message(chat_id, f"Привет, {first_name} \nПодпишись на канал", reply_markup=markup)

@dp.chat_join_request()
async def koop(message: types.ChatJoinRequest):
    await message.approve()
    await bot.send_message(message.from_user.id, "Спасибо за подписку!!")

@dp.callback_query()
async def check(call: types.CallbackQuery):
    await call.answer()
    k = await bot.get_chat_member(chat_id="-1001842719333", user_id=call.message.chat.id)
    o = await bot.get_chat_member(chat_id="-1001820407176", user_id=call.message.chat.id)
    p = await bot.get_chat_member(chat_id="-1001944152116", user_id=call.message.chat.id)
    if k.is_member and o.is_member() and p.is_member():
        await bot.send_message(call.message.chat.id, "Спасибо за подписку!")
    else:
        await bot.send_message(call.message.chat.id, "Подпишись на канал", reply_markup=markup)

########################




# ВНУТРЕННЯЯ БД ДЛЯ ВЫВОД ПОЛЬЗОВАТЕЛЕЙ #


@dp.message(Command("help"))
async def start(message: types.Message):
    if message.chat.type == "private":
        if not db.user_existist(message.from_user.id):
            db.add_user(message.from_user.id)
        po = db.cursor.execute("SELECT * FROM users")
        print(po.fetchall())
        await bot.send_message(message.from_user.id, "Приветствую")


#########################################

async def main():
    
    await dp.start_polling(bot)
    



if __name__ == "__main__":
    asyncio.run(main())

    








# status = ["Creator", "Admin", "Member"]
    # p = await bot.get_chat_member(chat_id="-1001898635045", user_id=call.message.chat.id)
    # await call.message.edit_text(p)