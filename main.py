import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8302071173:AAHa8rRRK2MdKJyWokvAVd8DszlvWtlUvXM"  

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("👋 Привет! Я echo-бот.\nОтправь мне любое сообщение — я его повторю.")

@dp.message()
async def echo(message: Message):
    logger.info(f"Получено сообщение от {message.from_user.id}")
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception as e:
        logger.error(f"Ошибка при отправке: {e}")
        await message.answer("Не смог повторить сообщение 😔")

async def main():
    logger.info("🚀 Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())