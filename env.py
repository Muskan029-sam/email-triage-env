class EmailTriageEnv:

    def __init__(self):
        self.level = 1
        self.current_index = 0
        self.action_history = []
        self.emails = [...]  


    def reset(self):
        self.current_index = 0
        self.action_history = []
        return self.emails[self.current_index]


    
    def step(self, action):
        email = self.emails[self.current_index]

        reward = self._calculate_reward(action, email["label"])

        self.current_index += 1

        done = self.current_index >= len(self.emails)

        if not done:
            observation = self.emails[self.current_index]
        else:
            observation = None

        info = {}

        return observation, reward, done, info


    # --- GRADERS BELOW ---

    def grade_spam(self, action, true_label):
        if true_label == "spam":
            return 1.0 if action == "spam_filter" else 0.0
        else:
            return 1.0 if action != "spam_filter" else 0.0


    def grade_priority(self, action, true_label):
        if true_label == "urgent":
            return 1.0 if action == "prioritize" else 0.0
        elif true_label == "normal":
            return 1.0 if action == "reply" else 0.3
        elif true_label == "spam":
            return 1.0 if action == "spam_filter" else 0.0


    def grade_full_task(self, action, true_label):
        if true_label == "spam" and action == "spam_filter":
            return 1.0
        elif true_label == "urgent" and action == "prioritize":
            return 1.0
        elif true_label == "normal" and action == "reply":
            return 1.0
        else:
            return 0.0


    def _score_reason(self, reason, true_label):
        if not reason:
            return 0.0

        if len(reason) < 10:
            return 0.2

        keywords = {
            "spam": ["offer", "win", "free", "lottery"],
            "urgent": ["meeting", "deadline", "asap"],
            "normal": ["update", "hello", "info"]
        }

        score = 0
        for word in keywords.get(true_label, []):
            if word in reason.lower():
                score += 0.3

        return min(score, 1.0)


    def _consistency_score(self):
        if len(self.action_history) < 2:
            return 1.0

        penalty = 0
        for i in range(1, len(self.action_history)):
            if self.action_history[i] != self.action_history[i - 1]:
                penalty += 0.1

        return max(0.0, 1.0 - penalty)


    def _calculate_reward(self, action, true_label, reason=""):
        if isinstance(action, dict):
            act = action.get("action", "")
            reason = action.get("reason", "")
        else:
            act = action

        if self.level == 1:
            base = self.grade_spam(act, true_label)
        elif self.level == 2:
            base = self.grade_priority(act, true_label)
        elif self.level == 3:
            base = self.grade_full_task(act, true_label)
        else:
            base = 0.0

        reason_score = self._score_reason(reason, true_label)

        self.action_history.append(act)

        consistency = self._consistency_score()

        final_reward = 0.6 * base + 0.2 * reason_score + 0.2 * consistency

        return min(max(final_reward, 0.0), 1.0)
