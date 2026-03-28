"""
Inference Script for EmailTriageEnv
===================================
MANDATORY for Hackathon Submission

- Reads API_BASE_URL, MODEL_NAME, HF_TOKEN from environment variables
- Uses OpenAI client to run baseline inference
- Produces reproducible scores on all tasks
"""

import os
from openai import OpenAI
from env import EmailTriageEnv
from models import Observation, Reward

# Load environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_inference():
    env = EmailTriageEnv()
    obs = env.reset()
    total_score = 0
    num_tasks = 0

    while True:
        # Ask the model what action to take
        prompt = f"Email subject: {obs.subject}\nEmail body: {obs.body}\nDecide: spam_filter / prioritize / reply"
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "system", "content": "You are an email triage agent."},
                      {"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=50
        )

        action = response.choices[0].message.content.strip()
        obs, reward, done = env.step(action)

        print(f"Email: {obs.subject}")
        print(f"Model action: {action}")
        print(f"Reward: {reward.value}\n")

        total_score += reward.value
        num_tasks += 1

        if done:
            break

    avg_score = total_score / num_tasks if num_tasks > 0 else 0
    print(f"Baseline average score: {avg_score:.2f}")

if __name__ == "__main__":
    run_inference()
