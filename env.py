from models import Observation, Action, Reward

"""
LEVELS:
1 → Spam Detection
2 → Urgency Handling
3 → Full Email Triage
"""

class EmailTriageEnv:
    def __init__(self, level=1):
        self.level = level

        self.inbox = [
            {"subject": "Win a lottery!", "body": "Claim your prize", "label": "spam"},
            {"subject": "Project deadline tomorrow", "body": "Submit report", "label": "urgent"},
            {"subject": "Lunch plans?", "body": "Want to meet at 1 PM?", "label": "normal"},
        ]

        self.current_index = 0

    def reset(self) -> Observation:
        self.current_index = 0
        email = self.inbox[self.current_index]

        return Observation(
            subject=email["subject"],
            body=email["body"]
        )

    def step(self, action: str):
        email = self.inbox[self.current_index]

        reward_value = self._calculate_reward(action, email["label"])

        self.current_index += 1
        done = self.current_index >= len(self.inbox)

        next_obs = None
        if not done:
            next_email = self.inbox[self.current_index]
            next_obs = Observation(
                subject=next_email["subject"],
                body=next_email["body"]
            )

        return next_obs, Reward(value=reward_value), done, {}

    def state(self) -> Observation:
        email = self.inbox[self.current_index]

        return Observation(
            subject=email["subject"],
            body=email["body"]
        )

    def _calculate_reward(self, action, true_label):
        # -------------------------------
        # LEVEL 1: Spam Detection
        # -------------------------------
        if self.level == 1:
            if true_label == "spam":
                return 1.0 if action == "spam_filter" else -1.0
            else:
                return 1.0 if action != "spam_filter" else -1.0

        # -------------------------------
        # LEVEL 2: Urgency Handling
        # -------------------------------
        elif self.level == 2:
            if true_label == "urgent":
                return 1.5 if action == "prioritize" else -1.0
            elif true_label == "normal":
                return 1.0 if action == "reply" else -0.5
            elif true_label == "spam":
                return 1.0 if action == "spam_filter" else -1.0

        # -------------------------------
        # LEVEL 3: Full Email Triage
        # -------------------------------
        elif self.level == 3:
            if true_label == "spam" and action == "spam_filter":
                return 2.0
            elif true_label == "urgent" and action == "prioritize":
                return 2.0
            elif true_label == "normal" and action == "reply":
                return 1.5
            else:
                return -1.5

        return 0.0
