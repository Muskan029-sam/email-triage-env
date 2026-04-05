import os
from openai import OpenAI
from env import EmailTriageEnv

# ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("OPENAI_API_KEY")

TASK_NAME = "email-triage"
BENCHMARK = "openenv"

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

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip(), None
    except Exception as e:
        return "reply", str(e)   # fallback action


def run():
    env = EmailTriageEnv()
    state = env.reset()

    done = False
    step_count = 0
    rewards = []
    success = False

    print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}")

    try:
        while not done:
            step_count += 1

            email_text = f"{state['subject']} {state['body']}"

            action, error = get_llm_action(email_text)

            state, reward, done, _ = env.step(action)

            reward_val = float(reward)

            rewards.append(reward_val)

            error_msg = error if error else "null"

            print(
                f"[STEP] step={step_count} action={action} "
                f"reward={reward_val:.2f} done={str(done).lower()} error={error_msg}"
            )

        success = True

    except Exception as e:
        error_msg = str(e)

    # FINAL SCORE (normalize 0–1)
    score = sum(rewards) / len(rewards) if rewards else 0

    rewards_str = ",".join([f"{r:.2f}" for r in rewards])

    print(
        f"[END] success={str(success).lower()} steps={step_count} "
        f"score={score:.2f} rewards={rewards_str}"
    )


if __name__ == "__main__":
    run()
