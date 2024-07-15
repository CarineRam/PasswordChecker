import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    common_passwords = ["password", "123456", "123456789", "qwerty", "abc123", "azerty"]
    common_password_criteria = password.lower() not in common_passwords
    
    criteria = [length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria, common_password_criteria]
    
    score = sum(criteria)
    strength = ["Very weak", "Weak", "Average", "Strong", "Very strong", "Excellent"]
    
    if score >= len(strength):
        score = len(strength) - 1

    feedback = []
    if not length_criteria:
        feedback.append("Password must have 8 characters or plus")
    if not uppercase_criteria:
        feedback.append("Add uppercase")
    if not lowercase_criteria:
        feedback.append("Add lowercase")
    if not digit_criteria:
        feedback.append("Add number")
    if not special_char_criteria:
        feedback.append("Add special characters")
    if not common_password_criteria:
        feedback.append("Avoid common passwords")

    return strength[score], feedback


word = "Pass1." #You can change put your password here
print(f"Password strength is : {check_password_strength(word)}")