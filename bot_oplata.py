
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.types.message import ContentTypes
import ayder_bot_inline as bot_inline
import tg_analytic 
import csv
import time
import datetime


PAYMENTS_TOKEN = ("401643678:TEST:2283fbba-f75a-4006-8484-bf4fc7043493")
Token = ("6187755099:AAELA-olgaVVeGoCR9ZZLj-HR9t2ouUJr04")

bot = Bot(token=Token)
dp = Dispatcher(bot)
PRICE = types.LabeledPrice(label="Неограниченная подписка", amount=500*100)  


a = "Выберите способ оплаты. Перед оплатой сливов ознакомьтесь с информацией в разделе «О нас»."
b = "Добро пожаловать в наш бот автопродаж  2023-2024!❤️\nЗдесь вы можете получить реальные СЛИВЫ НА ИТОГОВОЕ СОЧИНЕНИЕ и ответы на ОГЭ и ЕГЭ 2023-2024⚠️\n\nТакже мы предоставляем ответы на устное собеседование и итоговое сочинение❤️\n\n🍭Что умеет бот?\n\n💙В разделе 'О нас' вы найдете подробную информацию о наших сливах и наш тг канал ✅\n\n💛В разделе 'Оплата' вы можете приобрести сливы сочинения и ответы на ОГЭ/ ЕГЭ.\n\n💚В разделе 'Отзывы' вы можете оценить нашу работу📚\n\n💜 Если у вас остались вопросы или возникла проблема с оплатой, кликайте на 'Поддержку'"
c = "😋Здесь вы можете почитать отзывы довольных клиентов: https://t.me/o0tzyv2023"
d = "👨‍💻Менеджер по ответам на все вопросы - @o23tvet2023\n\n❗️Внимание , писать все свои вопросы и скрины платежей  в одно сообщение , быть вежливым и не спамить!Вам обязательно ответят в порядке очереди🟢"
e = "😊Наша команда работает в данной деятельности уже на протяжении 2-х лет.Это наш не первый проект, с каждым годом создаём новые каналы и улучшаем работу бота и каналов! Перед покупкой , вы можете ознакомиться с отзывами! После оплаты наш администратор незамедлительно пришлет вам ссылку - приглашения в VIP канал ❤️\n\nhttps://t.me/o0tvet_2023\n- наш основной канал ⚜️"
k = "Перед оплатой сливов ознакомьтесь с информацией в разделе «О нас»."
i = "Тут вы можете оплатить доступ к сливам на итоговое сочинение, а также ответам на ЕГЭ и ОГЭ 2023-2024❤️\nВы платите один раз 490 рублей и получаете доступ к ответам по всем предметам на любой регион, включая итоговое сочинение или устное собеседование.\nПосле оплаты вы получите доступ к  VIP - специальному каналу для наших покупателей, куда мы и будем отсылать все сливы😊\nЕсли хотите получить доступ, жмите «Согласен(-на)»"
j = "⭐️Друзья! У нас доступен очень крутой бонус🍭! Выполнив его вы можете получить БЕСПЛАТНЫЙ пропуск в 👑VIP канал.🟢Условия :\n\n🥰1.Написать отзыв(его можно найти в боте)\n\n👀2.Пригласить 10 человек в наш основной канал.\n\n👸3.Пригласить 3 человека в VIP\n\n📌ПОСЛЕ ВЫПОЛНЕНИЯ ВСЕХ УСЛОВИЙ НАПИШИТЕ НАШЕМУ МЕНЕДЖЕРУ 🧑‍💻 @o23tvet2023"


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    tg_analytic.statistics(message.chat.id, command=message.text)
    file2 = open("photo otvets\photo_2023-03-19_21-11-56.jpg", "rb")
    user = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Оплата💵")
    btn2 = types.KeyboardButton("Отзывы📌")
    btn3 = types.KeyboardButton("Поддержка🟢")
    btn4 = types.KeyboardButton("О нас ❤️")
    btn5 = types.KeyboardButton("Акции🎁")
    btn6 = types.KeyboardButton("Статистика")
    user.insert(btn1)
    user.insert(btn2)
    user.insert(btn3)
    user.insert(btn4)
    user.insert(btn5)
    if message.from_user.id == 652309932 or message.from_user.id == 1337316590:
        user.insert(btn6)
    await bot.send_photo(message.chat.id, file2, b, reply_markup=user)


    
@dp.message_handler(content_types=["text"])
async def ysvf(message: types.Message):
    tg_analytic.statistics(message.chat.id, command=message.text)
    file = open ("photo_2023-03-18_01-01-55.jpg", "rb")
    file1 = open("photo_2023-03-18_23-40-34.jpg", "rb")
    if message.text == 'Оплата💵':
        user = types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_btn1 = types.KeyboardButton("ОГЭ📝🟢")
        user_btn2 = types.KeyboardButton("ЕГЭ📝🔴")
        user.insert(user_btn1)
        user.insert(user_btn2)
        await bot.send_message(message.chat.id, "📚Выберите нужный вам экзамен : 👇", reply_markup=user)

    if message.text == "Статистика":
        if message.from_user.id == 652309932 or message.from_user.id == 1337316590:

            with open ("data.csv", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file, delimiter=";")
                info = ""
                users_id = []
                print(reader)
                for row in reader:
                    if row["data"] == str(datetime.date.today()):
                        info += f"{row['data']}, {row['id']}, {row['command']}\n"
                        users_id.append(row["id"])
                users_ynik = set(users_id)
                info += f"\nКоличество пользователей сегодня: {len(users_ynik)}"
            await bot.send_message(message.chat.id, info)


        
    if message.text == "ОГЭ📝🟢":
        await bot.send_photo(message.chat.id, file, reply_markup=bot_inline.menu)

    if message.text == "ЕГЭ📝🔴":
        await bot.send_photo(message.chat.id, file1 , reply_markup=bot_inline.menu2)

    if message.text == "Отзывы📌":
        user = types.ReplyKeyboardMarkup()
        await bot.send_message(message.chat.id, c, reply_markup=user)

    if message.text == "Поддержка🟢":
        user = types.ReplyKeyboardMarkup()
        await bot.send_message(message.chat.id, d, reply_markup=user)

    if message.text == "О нас ❤️":
         user = types.ReplyKeyboardMarkup()
         await bot.send_message(message.chat.id, e, reply_markup=user)
         
    if message.text == "Акции🎁":
        user = types.ReplyKeyboardMarkup()
        await bot.send_message(message.chat.id, j, reply_markup=user)

@dp.callback_query_handler(text=["button_name"])
async def knopka(message: types.Message):
    tg_analytic.statistics(message.from_user.id, command=["button_name"])
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Вы выбрали: VIP ОГЭ 9 класс CLASSIC 590р😌 ", reply_markup=bot_inline.menu1)

@dp.callback_query_handler(text=["button_name1"])
async def knopka(message: types.Message):
    tg_analytic.statistics(message.from_user.id, command=["button_name1"])
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Вы выбрали: VIP ОГЭ 9 класс PREMIUM 990р👑 ", reply_markup=bot_inline.menu1)

@dp.callback_query_handler(text=["button_name_3"])
async def knopka(message: types.Message):
    tg_analytic.statistics(message.from_user.id, command=["button_name_3"])
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Вы выбрали: VIP ЕГЭ 11 класс CRAZY 29900р👑 ", reply_markup=bot_inline.menu1)

@dp.callback_query_handler(text=["button_name_4"])
async def knopka(message: types.Message):
    tg_analytic.statistics(message.from_user.id, command=["button_name_4"])
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Вы выбрали: VIP ЕГЭ 11 класс ROYL 12900р🍭 ", reply_markup=bot_inline.menu1)

@dp.callback_query_handler(text=["button_name_5"])
async def knopka(message: types.Message):
    tg_analytic.statistics(message.from_user.id, command=["button_name_5"])
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Вы выбрали: VIP ЕГЭ 11 класс EASY 4900р☺️ ", reply_markup=bot_inline.menu1)

@dp.callback_query_handler(text=("button_name_2"))
async def button(message: types.Message):
    tg_analytic.statistics(message.from_user.id, command=["button_name_2"])
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text="Реквизиты для оплаты VIP 👑\n\n🟢  2200 7302 5180 2241\n\nПеревод должен быть осуществлен одним платежом!\nДля подтверждения оплаты - отправьте 👨‍💻администратору фото либо скриншот квитанции и название вашего VIP\n\n 🔹После подтверждения оплаты администратором,  ссылка на частный VIP канал будет выслана вам незамедлительно ! 🫅\n\n📌В нашем боте нажимаете на 'Поддержка' далее пишите администратору - @o23tvet2023")





@dp.message_handler(commands=["stop"])
async def messages(message):
    await bot.send_message(message.chat.id, "Спасибо за внимание!")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)