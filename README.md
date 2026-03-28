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

Email Triage Environment
# Email Triage Environment  

 [![OpenEnv Compliant](https://img.shields.io/badge/OpenEnv-Compliant-blue)](https://openenv.org)
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-lightblue)](https://www.docker.com/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-yellow)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](./LICENSE)
 

docker run -p 8000:8000 email-triage-env
Baseline Scores
Rule-based agent: baseline accuracy for spam filtering and prioritization.

LLM baseline: tested with GPT-style models for reply suggestion.


# Build the Docker image
docker build -t email-triage-env .

# Run the container
docker run -p 8000:8000 email-triage-env

# Run tests locally
python -m unittest discover tests

Quickstart Example  
Show a tiny demo of the environment + agent working together:

python env.py

Current email: Win a lottery!
Agent action: spam_filter
Reward: 1

Architecture Diagram
A simple flowchart in the README showing:
Email → Environment → Agent → Action → Reward

Baseline Scores Section  
Add a short table comparing rule-based agent vs. LLM baseline (even if LLM is “future work”):

Contribution Guide
A short section like:

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss.


A simple flowchart in the README showing:

python demo.py

output:

Current email: Win a lottery!
Agent action: spam_filter
Reward: 1

