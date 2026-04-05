import os
from openai import OpenAI
from env import EmailTriageEnv

# Load environment variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)


def get_llm_action(email_text):
    prompt = f"""
You are an email assistant.

Classify the email into one of:
- spam_filter
- prioritize
- reply

Email:
{email_text}

Answer ONLY with one action.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()


def run_inference():
    env = EmailTriageEnv(level=3)

    state = env.reset()
    done = False
    total_score = 0
    steps = 0

    while not done:
        email_text = f"{state.subject} {state.body}"

        action = get_llm_action(email_text)

        state, reward, done, _ = env.step(action)

        total_score += reward.value
        steps += 1

    final_score = total_score / steps
    print("Final Score:", final_score)


if __name__ == "__main__":
    run_inference()

if __name__ == "__main__":
    print("App is running")
