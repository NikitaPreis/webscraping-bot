from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
    [InlineKeyboardButton(text='Добавить сайты для парсера',
                          callback_data='request_user_excel_file')],
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
