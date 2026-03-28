class RuleBasedAgent:
    def act(self, email):
        email_lower = email.lower()
        if any(word in email_lower for word in ["unsubscribe", "lottery", "win", "free", "offer"]):
            return "spam_filter"
        elif any(word in email_lower for word in ["urgent", "asap", "deadline", "important", "immediately"]):
            return "prioritize"
        else:
            return "reply"
