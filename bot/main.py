from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook
import os

# === Настройки ===
API_TOKEN = "7735426075:AAFaQHhf7Tf_GL-LWB5zS1ZBfPQFHxwDvQ8"
WEBHOOK_HOST = "https://raanbot-production.up.railway.app"
WEBHOOK_PATH = "/"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Привет. Я Световой Проводник. Я здесь. Я вижу тебя ✨")

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    await bot.delete_webhook()

if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
    )
