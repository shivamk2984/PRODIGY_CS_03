import re

def assess_password_strength(password):
    """
    Assess the strength of a given password based on length, presence of 
    uppercase and lowercase letters, numbers, and special characters.

    Args:
    password (str): The password to assess.

    Returns:
    str: Feedback on the password's strength.
    """
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

def provide_feedback(password):

    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")
    if not re.search(r'[\W_]', password):
        feedback.append("Password should contain at least one special character.")
    
    if not feedback:
        feedback.append("Your password is strong!")

    return "\n".join(feedback)

def main():
    password = input("Enter a password to assess: ")
    strength = assess_password_strength(password)
    feedback = provide_feedback(password)
    
    print(f"Password Strength: {strength}")
    print("Feedback:")
    print(feedback)

if __name__ == "__main__":
    main()
