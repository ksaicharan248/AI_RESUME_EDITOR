import os
import asyncio
import logging
import requests
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

@dp.message(Command(commands=["add"]))
async def handle_add(message: types.Message):
    msg = (
        "First Name : \n"
        "`Sai`\n\n"
        "Middle Name : \n"
        "`Charan`\n\n"
        "Last Name : \n"
        "`K`\n\n"
        "Email : \n"
        "`saicharanreddy141458@gmail.com`\n\n"
        "Mobile Number : \n"
        "`+91 9014145839`\n\n"
        "Address line1 : \n"
        "`25, THRIDHAMNE, JAI BHUNESHWARI LAYOUT,`\n\n"
        "Address line2 : \n"
        "`Vidya Nagar, Krishnarajapuram, Bengaluru`\n\n"
        "Address line3 : \n"
        "`Near Cambridge institute of technology, Karnataka - 560036`\n\n"
        "Pin Code : \n"
        "`560036`\n\n"
        "City : \n"
        "`Bengaluru`\n\n"
        "State : \n"
        "`Karnataka`\n\n"
        "Country : \n"
        "`India`"
    )
    await message.answer(msg, parse_mode="MarkdownV2")

@dp.message(Command(commands=["edu"]))
async def handle_edu(message: types.Message):
    msg = ("`Bachlor of Technology in Electronics and Communication Engineering`\n\n"
           "`Sreenivasa Institute of Technology and Management Studies`\n\n"
           "`2020 - 2024`\n\n"
           "`CGPA: 8.24/10`\n\n"
           "`Intermediate`]\n\n"
           "`State Board`\n\n"
           "`Sri Chaitanya Junior College`\n\n"
           "`CGPA: 9.01/10`\n\n"
           "`Class 10th`\n\n"
           "`Sri Chaitanya Techno School`\n\n"
           "`CGPA: 9.7/10`")
    await message.answer(msg, parse_mode="MarkdownV2")

@dp.message(Command(commands=["block"]))
async def handle_block(message:types.Message):
    if message:
        response = requests.get("https://trigger.macrodroid.com/75b4c80d-729e-4b11-9f5c-22646225ef32/call")
        if response.status_code == 200 and response.text == "OK":
            await message.answer("🟢 Successfully blocked")
        else:
            await message.answer("🔴 Failed to block")



@dp.message(Command(commands=["unblock"]))
async def handle_unblock(message:types.Message):
    if message:
        response = requests.get("https://trigger.macrodroid.com/75b4c80d-729e-4b11-9f5c-22646225ef32/disable")
        if response.status_code == 200 and response.text == "OK":
            await message.answer("🟢 Successfully unblocked")
        else:
            await message.answer("🔴 Failed to unblock")


@dp.message(Command(commands=["link"]))
async def handle_link(message:types.Message):
    if message:
        await message.answer("https://sai-charan-portfolio.vercel.app/")



# 🟢 Main entry
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
