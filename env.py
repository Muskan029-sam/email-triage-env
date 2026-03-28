from models import Observation, Action, Reward

class EmailTriageEnv:
    def __init__(self):
        self.inbox = [
            {"subject": "Win a lottery!", "body": "Claim your prize", "label": "spam"},
            {"subject": "Project deadline tomorrow", "body": "Submit report", "label": "urgent"},
            {"subject": "Lunch plans?", "body": "Want to meet at 1 PM?", "label": "normal"}
        ]
        self.current_index = 0

    def reset(self) -> Observation:
        self.current_index = 0
        email = self.inbox[self.current_index]
        return Observation(subject=email["subject"], body=email["body"])

    def step(self, action: str):
        email = self.inbox[self.current_index]
        reward_value = self._calculate_reward(action, email["label"])
        self.current_index += 1
        done = self.current_index >= len(self.inbox)
        return Observation(subject=email["subject"], body=email["body"]), Reward(value=reward_value), done

    def state(self) -> Observation:
        email = self.inbox[self.current_index]
        return Observation(subject=email["subject"], body=email["body"])

    def _calculate_reward(self, action, true_label):
        if true_label == "spam" and action == "spam_filter":
            return 1.0
        elif true_label == "urgent" and action == "prioritize":
            return 0.8
        elif true_label == "normal" and action == "reply":
            return 0.9
        else:
            return 0.0

