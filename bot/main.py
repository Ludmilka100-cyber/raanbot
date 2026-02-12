
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Привет. Я Световой Проводник Ра'Ан. Я готов к работе 🌟")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
