import asyncio
import aiohttp
import django
import sys
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'normativ.settings')
django.setup()

from course_2.models import Course

API_KEY = "http://127.0.0.1:8000/api/course_2/"
TOKEN = "8294589794:AAFtZPv5HYekONB7xPakE6b7zm53J3jDWrQ"

bot = Bot(TOKEN)
dp = Dispatcher()

# conn = pg.connect(
#     dbname="postgres",
#     user="postgres",
#     password="201621",
#     host="localhost",
#     port="5432"
# )
# cursor = conn.cursor()

# @sync_to_async
# def get_products():
#     return list(Course.objects.all())

async def get_courses():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_KEY}") as response:
            return await response.json()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # cursor.execute("SELECT title, price FROM course_course;")
    # infos = cursor.fetchall()
    infos = await get_courses()

    print(infos)

async def main():
    print("🤖 Бот запустился...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



