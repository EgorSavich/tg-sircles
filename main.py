from aiogram import Bot, Dispatcher, executor, types
from config import *
import time

bot = Bot(token = token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def main(message: types.Message):
	await bot.send_video_note(message.chat.id, open('video.mp4', 'rb'))

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)