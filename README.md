# 📄 DocuBot AI – Smart Resume Tailoring Assistant

DocuBot AI is a Telegram-based intelligent bot that helps job seekers personalize their `.docx` resumes by analyzing job descriptions and tailoring resume content to match relevant roles. Powered by Google Gemini, the bot rewrites and updates resumes with optimized keywords, bullet points, and formatting—making them ATS-friendly and role-specific.

---

## 🚀 Features

- 🧠 **AI-Powered Resume Tailoring**  
  Uses Google Gemini LLM to analyze job descriptions and rewrite resumes accordingly.

- 📄 **DOCX Automation**  
  Edits `.docx` files using `python-docx` to add or modify content with precision.

- 💬 **Telegram Integration**  
  Interacts with users via Telegram Bot API for easy access—send a JD, get a resume.

- ☁️ **Cloud Deployment**  
  Deployed on AWS EC2 for 24/7 availability and fast response times.

---

## 🔧 Tech Stack

| Tool / Technology       | Purpose |
|--------------------------|---------|
| **Python**              | Backend logic, API integration, automation |
| **Google Gemini API**   | Natural Language Processing for content rewriting |
| **python-docx**         | Reading, editing, and writing `.docx` resume files |
| **Telegram Bot API**    | User interface through Telegram for sending/receiving files |
| **AWS EC2**             | Cloud server hosting the bot and services |

---

## 🛠 How It Works

1. User sends a **Job Description** via Telegram.
2. Bot processes the JD using **Google Gemini** to understand role-specific requirements.
3. Bot customizes the `.docx` resume accordingly using **python-docx**.
4. A tailored resume is returned to the user via the **Telegram chat**.

---
