from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentType.TEXT)
async def delete_links(message: types.Message):
    if message.chat.type not in ["group", "supergroup"]:
        return

    member = await message.chat.get_member(message.from_user.id)

    # agar ADMIN bo‘lsa — tegmaymiz
    if member.is_chat_admin():
        return

    text = message.text.lower()

    if "http" in text or "t.me" in text or "www." in text:
        try:
            await message.delete()
        except:
            pass

executor.start_polling(dp)
