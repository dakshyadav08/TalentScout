# utils.py
import re

def is_valid_name(text):
    invalid = ["hi", "hello", "hey"]
    return text.lower().strip() not in invalid and len(text.split()) >= 2

def is_valid_email(text):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, text) is not None

def is_valid_phone(text):
    return text.isdigit() and 10 <= len(text) <= 13

def analyze_sentiment(text):
    positive = ["confident", "happy", "excited", "comfortable", "experienced"]
    negative = ["nervous", "confused", "worried", "unsure", "stressed"]

    score = 0
    for w in positive:
        if w in text.lower():
            score += 1
    for w in negative:
        if w in text.lower():
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"
