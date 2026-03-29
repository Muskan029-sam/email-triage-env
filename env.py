def _calculate_reward(self, action, true_label):
    # LEVEL 1
    if self.level == 1:
        if true_label == "spam":
            return 1.0 if action == "spam_filter" else 0.0
        else:
            return 1.0 if action != "spam_filter" else 0.0

    # LEVEL 2
    elif self.level == 2:
        if true_label == "urgent":
            return 1.0 if action == "prioritize" else 0.0
        elif true_label == "normal":
            return 1.0 if action == "reply" else 0.3
        elif true_label == "spam":
            return 1.0 if action == "spam_filter" else 0.0

    # LEVEL 3
    elif self.level == 3:
        if true_label == "spam" and action == "spam_filter":
            return 1.0
        elif true_label == "urgent" and action == "prioritize":
            return 1.0
        elif true_label == "normal" and action == "reply":
            return 1.0
        else:
            return 0.0
