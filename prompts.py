# prompts.py

def system_prompt(language):
    return f"""
You are TalentScout, a professional AI Hiring Assistant.
Conduct the conversation in {language}.
Use a formal, recruiter-like tone.
Ask only one question at a time.
"""

INFO_PROMPTS = {
    "email": "Thank you. Please provide your **email address**.",
    "phone": "Please share your **phone number**.",
    "experience": "How many **years of professional experience** do you have?",
    "position": "Which **position(s)** are you applying for?",
    "location": "What is your **current location**?"
}

TECH_STACK_PROMPT = (
    "Please list your **technical skills**, including programming languages, "
    "frameworks, databases, and tools.\n"
    "Example: Python, Django, PostgreSQL, Git"
)

TECH_QUESTION_PROMPT = """
Candidate Tech Stack:
{tech_stack}

Generate 3 to 5 technical interview questions.
- Directly related to the technologies
- Mix conceptual and practical
- Do NOT include answers
- Number the questions
"""

END_PROMPT = (
    "Thank you for completing the initial screening.\n\n"
    "Our recruitment team will review your profile and contact you if your "
    "skills match our requirements.\n\n"
    "Have a great day!"
)
