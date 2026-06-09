import re

suspicious_words = [
    "urgent",
    "verify",
    "password",
    "bank",
    "account",
    "click",
    "login",
    "winner",
    "lottery",
    "claim",
    "update",
    "suspended",
    "immediately"
]

def detect_phishing(email_text):

    score = 0
    found_keywords = []

    # Check suspicious keywords
    for word in suspicious_words:
        if word in email_text.lower():
            score += 1
            found_keywords.append(word)

    # Check URLs
    urls = re.findall(r'https?://\S+|www\.\S+', email_text)

    if urls:
        score += 2

    # Final Decision
    if score >= 3:
        result = "PHISHING EMAIL"
    else:
        result = "LEGITIMATE EMAIL"

    return result, score, found_keywords


while True:

    email = input("\nEnter Email Text: ")

    if email.lower() == "quit":
        break

    result, score, keywords = detect_phishing(email)

    print("\nRisk Score:", score)
    print("Result:", result)

    if keywords:
        print("Suspicious Keywords:", keywords)
