from env import EmailTriageEnv

if __name__ == "__main__":
    try:
        env = EmailTriageEnv()
        state = env.reset()
        print("Environment loaded successfully")
        print("Initial state:", state)
    except Exception as e:
        print("Error:", e)
