from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = 'ВАШ_ТОКЕН_ОТ_BOTFATHER'
WEB_APP_URL = 'https://ваш-сайт-с-игрой.com'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Старт игры
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    web_app_button = types.InlineKeyboardButton(text="Играть в тапалку", web_app=types.WebAppInfo(url=WEB_APP_URL))
    keyboard.add(web_app_button)

    await message.reply("Нажмите на кнопку ниже, чтобы начать играть!", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
