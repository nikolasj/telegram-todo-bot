from aiogram.types import (Message)

import db
from load_all import dp

db = db.DBCommands()


@dp.message_handler()
async def other_echo(message: Message):
    await message.answer(message.text)
