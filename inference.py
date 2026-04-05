import os
from openai import OpenAI
from env import EmailTriageEnv

# ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("OPENAI_API_KEY")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

def get_llm_action(email_text):
    prompt = f"""
Classify this email into:
- spam_filter
- prioritize
- reply

Email:
{email_text}

Answer ONLY one word.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()


def run():
    print("[START] Email Triage Inference")

    env = EmailTriageEnv()
    state = env.reset()

    done = False
    total_score = 0
    steps = 0

    while not done:
        email_text = f"{state['subject']} {state['body']}"

        action = get_llm_action(email_text)

        state, reward, done, _ = env.step(action)

        print(f"[STEP] action={action} reward={reward}")

        total_score += reward
        steps += 1

    final_score = total_score / steps if steps > 0 else 0

    print(f"[END] final_score={final_score}")


if __name__ == "__main__":
    run()
