🤖 TalentScout: AI Hiring Assistant
TalentScout is a specialized recruitment chatbot built to streamline the initial screening process for technology roles. Leveraging the power of Large Language Models (LLMs), it gathers candidate information, validates data in real-time, and generates custom technical screening questions based on a candidate's specific tech stack.

🚀 Features
State-Driven Conversation: Uses a robust state machine to guide candidates through a logical sequence (Info Gathering → Tech Screening → Wrap-up).

Intelligent Validation: Employs Regex and heuristic logic to ensure names, emails, and phone numbers are valid before proceeding.

Custom Technical Screening: Dynamically generates 3–5 technical questions tailored to the candidate's specific skills using Llama 3.

Multilingual Support: Adjustable interface to accommodate candidates in English, Hindi, Spanish, and French.

Professional UX: Built with Streamlit for a clean, intuitive, and responsive web interface.

🛠️ Technical Stack
Frontend: Streamlit

LLM Integration: Ollama (Running Llama 3)

Language: Python 3.10+

Libraries: requests, python-dotenv, re

📂 Project Structure

```bash

├── app.py              # Main Streamlit application and State Machine logic
├── llm.py              # Interface for local Ollama/Llama 3 API calls
├── utils.py            # Validation logic (Regex, Sentiment Analysis)
├── prompts.py          # System and Dynamic Prompt templates
├── .env                # Environment variables (API Configuration)
└── README.md           # Project documentation

```

🧠 Prompt Engineering Decisions
System Persona: The "System Prompt" defines TalentScout as a professional recruiter. It is strictly instructed to ignore off-topic queries (e.g., weather, trivia) to maintain the integrity of the interview.

Context Awareness: The TECH_QUESTION_PROMPT utilizes the candidate's input to generate questions that mix conceptual knowledge with practical application, ensuring a comprehensive skill assessment.

Constraint Injection: Prompts are engineered to explicitly forbid the LLM from providing answers, preventing candidates from seeing the solutions during the screening phase.

🛡️ Data Handling & Privacy
Session Management: Candidate data is stored in Session State, meaning it persists only for the duration of the browser session and is not saved to a persistent database.

Validation: Inputs are cleaned and stripped of PII (Personally Identifiable Information) before being processed by the LLM where applicable.

Compliance: The workflow is designed to align with GDPR principles of "Data Minimization" by only requesting essential hiring information.

🚧 Challenges & Solutions
The "Off-by-One" Lag: Streamlit's rerun behavior initially caused the bot to respond one step behind. Solution: Implemented st.rerun() after every state transition to force immediate UI updates.

Local LLM Latency: Local models can be slow. Solution: Added st.spinner to provide visual feedback to the user during processing.

Tech Stack Verification: Preventing the bot from asking technical questions about "nonsense" inputs. Solution: Improved prompt instructions to validate tech inputs before generating questions.
