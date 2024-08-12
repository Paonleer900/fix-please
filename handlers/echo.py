from config import bot,dp
from aiogram import types, Dispatcher


async def echo(message:types.Message):
    text=message.text
    if text.isdigit():
        await message.answer(int(text)**2)
    else:
        await message.answer(text)


def registr_echo(dp: Dispatcher):
    dp.register_message_handler(echo)