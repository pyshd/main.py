import kb
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text= "НАЧАТЬ")]],
                           resize_keyboard=True,
                           input_field_placeholder="Начните викторину......",)





catalog = InlineKeyboardMarkup(inline_keyboard=[


    [InlineKeyboardButton(text="LIGHT", callback_data="LIGHT")],
    [InlineKeyboardButton(text="MEDIUM", callback_data="MEDIUM")],
    [InlineKeyboardButton(text="HARD", callback_data="HARD")]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text= "stop")]],
                                 resize_keyboard=True)




