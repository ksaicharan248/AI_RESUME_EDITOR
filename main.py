import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from data.keys import eTELEGRAM_API_KEY
from data.reume import rdata
from utlis.genrator import generate_resume_summary_and_skills
from utlis.docgenrator import doc_generator

logging.basicConfig(level=logging.INFO)

bot = Bot(token=eTELEGRAM_API_KEY)
dp = Dispatcher()

# 👋 /start and /help
@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: types.Message):
    await message.reply("👋 Send me a job description (JD) using /jd command, and I’ll generate a tailored resume for you.")

@dp.message(Command(commands=["jd"]))
async def handle_jd(message: types.Message):
    jd_text = message.text.replace('/jd', '').strip()

    if not jd_text:
        await message.reply("⚠️ Please provide a job description after /jd")
        return
    working_msg = await message.answer("⚙️ Working on your tailored resume...")

    try:
        # 2. Generate resume content
        tailored_data = generate_resume_summary_and_skills(rdata, jd_text)
        title_name  = tailored_data["job_title"]
        title_name : str = title_name.replace(" ", "_")
        if doc_generator(tailored_data ,title_name):
            await working_msg.delete()
            print(title_name)
            resume = FSInputFile(rf"./docs/K_Sai_Charan_{title_name}.docx")
            await message.answer_document(document=resume, caption="✅ Here's your tailored resume!")
            #if sent successfully, delete the reume it storage
            try:
                os.remove(rf"./docs/K_Sai_Charan_{title_name}.docx")
            except Exception as e:
                logging.error(e)
                await working_msg.edit_text("⚠️ Something went wrong while processing the job description.")
        else:
            await working_msg.edit_text("❌ Failed to generate the resume document.")
    except Exception as e:
        logging.error(e)
        await working_msg.edit_text("⚠️ Something went wrong while processing the job description.")


# 📄 /resume or /df — Send default resume
@dp.message(Command(commands=["resume", "df"]))
async def handle_resume(message: types.Message):
    resume = FSInputFile(r"./docs/default_doc/K SAI CHARAN_Fresher.pdf")
    await message.answer_document(document=resume, caption="📄 Here's the default resume.")

# 🟢 Main entry
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
