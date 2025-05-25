import data
from utlis.genrator import generate_resume_summary_and_skills
from data.reume import rdata
from utlis.docgenrator import doc_generator
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from data.keys import eTELEGRAM_API_KEY
API_TOKEN = eTELEGRAM_API_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: types.Message):
    # await message.answer("Hi! I'm a Telegram bot that generates tailored summaries and skills for resumes based on job descriptions.")
    await message.reply("Send me a job description (JD), and I'll generate a tailored summary and skills for you!")


@dp.message(Command(commands=["jd"]))
async def handle_jd(message: types.Message):
    jd_text = message.text.strip('/jd')
    tailored_data = generate_resume_summary_and_skills(rdata, jd_text)
    if doc_generator(tailored_data) :
        #send the document
        resume = FSInputFile(r"./docs/Tailored_Resume.docx")
        await message.answer_document(document=resume)

@dp.message(Command(commands=["resume" , "df"]))
async def handle_resume(message: types.Message):
    resume = FSInputFile(r"./docs/default_doc/K SAI CHARAN_Fresher.pdf")
    await message.answer_document(document=resume)


# Main entry point
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
