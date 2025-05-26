from typing import Tuple
from google import genai
from typing import List
from pydantic import BaseModel
from data.prompt import get_prompt
from data.keys import AI_API_KEY
import json
class Skills(BaseModel):
    languages: List[str]
    technologies: List[str]
    tools: List[str]

class ResumeOutput(BaseModel):
    summary: str
    skills: Skills
    job_title: str


# Initialize the Gemini client once
client = genai.Client(api_key=AI_API_KEY)

def generate_resume_summary_and_skills(resume_data: str, job_description_data: str) -> dict[str, dict[str, List[str]]]:
    prompt = get_prompt(job_description_data, resume_data)

    # noinspection PyTypeChecker
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": ResumeOutput,
        },
    )
    print(response.text)
    return json.loads(response.text)



if __name__ == "__main__":
    from data.reume import rdata
    from data.jd import job_description
    summary, skills , job_title = generate_resume_summary_and_skills(rdata, job_description)
    print(summary)
    print(skills)



