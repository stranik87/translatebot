from deep_translator import GoogleTranslator
from aiogram import Bot,Dispatcher,types
import os
from aiogram.utils import executor
TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)





def tarjimon(text):
    tarjima = GoogleTranslator(source='auto',target='en').translate(text)
    return tarjima

@dp.message_handler(commands='start')

async def start_com(message:types.Message):
    await message.answer('Welcome to our telegram bot "English translator"')
    

@dp.message_handler(content_types='text')

async def send_message(message:types.Message):
    text = message.text
    tarjima = tarjimon(text=text)
    
    await message.answer(tarjima)
    
if __name__=='__main__':
    executor.start_polling(dispatcher=dp)