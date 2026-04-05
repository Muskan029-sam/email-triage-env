from fastapi import FastAPI
from env import EmailTriageEnv

app = FastAPI()

env = EmailTriageEnv()


@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "subject": state.subject,
        "body": state.body
    }


@app.post("/step")
def step(action: str):
    state, reward, done, _ = env.step(action)
    return {
        "subject": state.subject,
        "body": state.body,
        "reward": reward.value,
        "done": done
    }


@app.get("/state")
def get_state():
    state = env.state
    return {
        "subject": state.subject,
        "body": state.body
    }
