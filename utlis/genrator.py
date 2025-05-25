from typing import Tuple
from pydantic import BaseModel
from google import genai
from typing import List
import data
from data.prompt import get_prompt
import json

class Skills(BaseModel):
    languages: List[str]
    technologies: List[str]
    tools: List[str]

class ResumeOutput(BaseModel):
    summary: str
    skills: Skills

# Initialize the Gemini client once
client = genai.Client(api_key=data.keys.AI_API_KEY)

def generate_resume_summary_and_skills(resume_data: str, job_description_data: str) -> dict[str, dict[str, List[str]]]:
    prompt = get_prompt(job_description_data, resume_data)

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": ResumeOutput,
        },
    )

    return json.loads(response.text)



if __name__ == "__main__":
    from data.reume import rdata
    from data.jd import job_description
    summary, skills = generate_resume_summary_and_skills(rdata, job_description)
    print(summary)
    print(skills)



