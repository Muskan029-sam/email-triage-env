from env import EmailTriageEnv
from baseline_agent import RuleBasedAgent

if __name__ == "__main__":
    env = EmailTriageEnv()
    agent = RuleBasedAgent()

    # Reset environment to get first email
    email = env.reset()
    print("Current email:", email["subject"])

    # Agent decides what to do
    action = agent.act(email["subject"])
    state, reward, done = env.step(action)

    # Show results
    print("Agent action:", action)
    print("Reward:", reward)
