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


def _calculate_reward(self, action, true_label, reason=""):
    # Handle dict action (for reasoning feature)
    if isinstance(action, dict):
        act = action.get("action", "")
        reason = action.get("reason", "")
    else:
        act = action

    # Base reward from task
    if self.level == 1:
        base = self.grade_spam(act, true_label)

    elif self.level == 2:
        base = self.grade_priority(act, true_label)

    elif self.level == 3:
        base = self.grade_full_task(act, true_label)

    else:
        base = 0.0

    # Reasoning score (your EDGE feature)
    reason_score = self._score_reason(reason, true_label)

    # Final reward (weighted)
    final_reward = 0.7 * base + 0.3 * reason_score

    return min(max(final_reward, 0.0), 1.0)
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
