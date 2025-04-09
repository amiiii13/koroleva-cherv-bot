
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = 'PASTE_YOUR_BOT_TOKEN_HERE'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📖 Читать книгу"),
    KeyboardButton("✨ Случайное послание"),
    KeyboardButton("🤍 Поддержать"),
    KeyboardButton("... Тишина")
)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет. Ты здесь — значит, что-то почувствовал. Это 'Королева'. Здесь нет шума, только дыхание.",
        reply_markup=main_menu
    )

@dp.message_handler(lambda message: message.text == "📖 Читать книгу")
async def send_books(message: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Русская", url="https://sandbox.openai.com/mnt/data/Королева_червей_Та_что_смогла_РУ_для_планшета.pdf"),
        InlineKeyboardButton("Українська", url="https://sandbox.openai.com/mnt/data/Королева_червей_Та_що_змогла_UA_для_планшета.pdf"),
        InlineKeyboardButton("Особисто", url="https://sandbox.openai.com/mnt/data/Королева_червей_Та_що_змогла_Особиста_для_Ані.pdf")
    )
    await message.answer("Выбери язык, в котором хочешь услышать её.", reply_markup=markup)

@dp.message_handler(lambda message: message.text == "✨ Случайное послание")
async def send_whisper(message: types.Message):
    import random
    quotes = [
        "Ты не сломана. Ты всё ещё здесь. И это победа.",
        "Мир не узнал бы тебя — если бы ты не написала.",
        "Твоя тишина говорит громче, чем крик других.",
        "Королева не кричит. Она смотрит — и тебя понимают.",
        "Если ты выжил — значит, в тебе есть текст."
    ]
    await message.answer(random.choice(quotes))

@dp.message_handler(lambda message: message.text == "🤍 Поддержать")
async def support(message: types.Message):
    await message.answer("Если хочешь поддержать ту, что создала это — ты можешь найти её здесь: @giftsfarming")

@dp.message_handler(lambda message: message.text == "... Тишина")
async def silence(message: types.Message):
    await message.answer("Ты можешь остаться здесь. Молча. Без ответов. Я всё равно рядом.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
