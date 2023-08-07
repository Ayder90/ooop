from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1)
Button = InlineKeyboardButton(text="VIP ОГЭ 9 класс CLASSIC 590р😌", callback_data="button_name")
Button1 = InlineKeyboardButton(text="VIP ОГЭ 9 класс PREMIUM 990р👑", callback_data="button_name1")

menu1 = InlineKeyboardMarkup(row_width=1 )
Button2_1 = InlineKeyboardButton(text = "ОПЛАТИТЬ", callback_data="button_name_2")


menu2 = InlineKeyboardMarkup(row_width=1)
Button3_1 = InlineKeyboardButton(text="VIP ЕГЭ 11 класс CRAZY 29900р👑", callback_data="button_name_3")
Button3_2 = InlineKeyboardButton(text="VIP ЕГЭ 11 класс ROYL 12900р🍭", callback_data="button_name_4")
Button3_3 = InlineKeyboardButton(text="VIP ЕГЭ 11 класс EASY 4900р☺️", callback_data="button_name_5")




# menu.insert(ap)
menu.insert(Button)
menu.insert(Button1)
menu1.insert(Button2_1)
menu2.insert(Button3_1)
menu2.insert(Button3_2)
menu2.insert(Button3_3)


