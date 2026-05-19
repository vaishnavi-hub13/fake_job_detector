def check_pattern(text):
    suspicious_words = ["urgent", "fee", "pay"]
    score = sum(word in text.lower() for word in suspicious_words)
    return score
