from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from transliterate import to_cyrillic, to_latin

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} botimizga\n"
                         f"xush kelibsiz. Ixtiyoriy text kiriting.")



@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def UserText(message:types.Message):
    user_message=message.text 
    if user_message.isascii():
        await message.answer(to_cyrillic(user_message))
    
    else:
        await message.answer(to_latin(user_message))



    

    




