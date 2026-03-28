# email-triage-env
Email Triage Environment is a real-world simulation built on the OpenEnv specification. It models the everyday task of managing emails — classifying, prioritizing, and responding — so that AI agents can learn to handle productivity workflows effectively. 
📖 Overview
Email Triage Environment is a real-world simulation built on the OpenEnv specification. It models the everyday task of managing emails – classifying, prioritizing, and responding – so that AI agents can learn to handle productivity workflows effectively.

🔑 Tasks
Spam Filtering (Easy): Identify whether an email is spam or not.

Urgency Prioritization (Medium): Distinguish urgent emails from normal ones and rank them.

Reply Suggestion (Hard): Generate appropriate responses for urgent emails based on context.

⚙️ Action & Observation Spaces
Observation: Email metadata (sender, subject, body, timestamp).

Actions: Classify, prioritize, or generate a reply.

🎯 Reward Function
Partial credit for correct classification or prioritization.

Full credit for correct triage and appropriate responses.

Penalties for irrelevant or incorrect actions.

🚀 Setup
# Clone the repo
git clone https://github.com/<your-username>/email-triage-env.git
cd email-triage-env

# Build Docker image
docker build -t email-triage-env .

# Run container
docker run -p 8000:8000 email-triage-env
Baseline Scores
Rule-based agent: baseline accuracy for spam filtering and prioritization.

LLM baseline: tested with GPT-style models for reply suggestion.
