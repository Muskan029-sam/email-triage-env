class EmailTriageEnv:
    def __init__(self):
        self.inbox = []
        self.current_email = None

    def reset(self):
        # Example inbox with labeled emails
        self.inbox = [
            {"subject": "Win a lottery!", "label": "spam"},
            {"subject": "Project deadline tomorrow", "label": "urgent"},
            {"subject": "Lunch plans?", "label": "normal"}
        ]
        self.current_email = self.inbox[0]
        return self.current_email

    def step(self, action):
        # Compare agent action with true label
        reward = self._calculate_reward(action, self.current_email["label"])
        done = True  # one email per step for now
        return self.current_email, reward, done

    def _calculate_reward(self, action, true_label):
        if true_label == "spam" and action == "spam_filter":
            return 1
        elif true_label == "urgent" and action == "prioritize":
            return 2
        elif true_label == "normal" and action == "reply":
            return 3
        return 0
