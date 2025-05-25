from typing import List
from pydantic import BaseModel
from google import genai
from data.jd import job_description
from data.reume import rdata

# Define the nested structure properly
class Skills(BaseModel):
    languages: List[str]
    technologies: List[str]
    tools: List[str]

class ResumeOutput(BaseModel):
    summary: str
    skills: Skills  # ✅ Typed, nested model

# Setup job description and resume data


# Gemini setup
client = genai.Client(api_key="AIzaSyAwLnOXUclNGmO33OY6Jlx_rzY19S_gyco")

# Prompt to send
prompt = f"""
   SYSTEM:
You are an expert AI résumé specialist. Given:
  • resume_data: the full text of a candidate’s résumé  
  • job_description_data: the full text of a target job description  

Produce **only** a JSON object (no markdown, no extra text) with these two keys:

1. "summary":  
   - 100–120 words  
   - Positions the candidate as the *perfect fit* for the JD  
   - Cites two specific “supported statements” drawn verbatim from resume_data  
   - Mentions only skills and experiences required by the JD  
   - Excludes any hardware, IoT, electronics, or embedded-system details  

2. "skills":  
   A dict with exactly three lists. **In each list, place all JD-required skills first (in the order they appear in the job_description_data), then append the candidate’s other relevant skills from resume_data.**  
   - "languages": programming/scripting languages  
   - "technologies": platforms, frameworks, methodologies, cloud or big-data stacks  
   - "tools": libraries, APIs, version control, testing or automation tools  

USER:
Here is the candidate’s résumé (resume_data):
{rdata}

Here is the job description (job_description_data):
{job_description}

TASK:
Return the JSON object as specified.


    {{
      "summary": "…tailored summary here…",
      "skills": {{
        "languages": [...],
        "technologies": [...],
        "tools": [...]
      }}
    }}
    """

# Call Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    contents=prompt,
    config={ "response_mime_type": "application/json",
        "response_schema": ResumeOutput,
    },
)

# Output result
print(response.text)

# Optional: Access structured result
result: ResumeOutput = response.parsed
print(result.summary)
print(result.skills)
