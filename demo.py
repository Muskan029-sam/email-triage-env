from env import EmailTriageEnv
from baseline_agent import RuleBasedAgent

if __name__ == "__main__":
    env = EmailTriageEnv()
    agent = RuleBasedAgent()

    email = env.reset()
    print("Current email:", email.subject)

    action = agent.act(email.subject)

    state, reward, done, _ = env.step(action)

    print("Agent action:", action)
    print("Reward:", reward)
