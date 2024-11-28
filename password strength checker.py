import string

def check_password_strength(password):
    """
    Evaluates the strength of a password and provides suggestions to improve it.
    """
    # Initialize variables
    length_score = 0
    special_char_score = 0
    uppercase_score = 0
    lowercase_score = 0
    digit_score = 0

    # Check length
    if len(password) >= 8:
        length_score = 1

    # Check for special characters
    if any(char in string.punctuation for char in password):
        special_char_score = 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        uppercase_score = 1

    # Check for lowercase letters
    if any(char.islower() for char in password):
        lowercase_score = 1

    # Check for digits
    if any(char.isdigit() for char in password):
        digit_score = 1

    # Calculate total score
    total_score = length_score + special_char_score + uppercase_score + lowercase_score + digit_score

    # Evaluate strength based on score
    if total_score == 5:
        strength = "Strong"
    elif total_score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, {
        "length": length_score,
        "special_characters": special_char_score,
        "uppercase": uppercase_score,
        "lowercase": lowercase_score,
        "digits": digit_score,
    }


def suggest_improvements(password):
    """
    Provides suggestions for improving the password.
    """
    suggestions = []
    if len(password) < 8:
        suggestions.append("Increase the length to at least 8 characters.")
    if not any(char in string.punctuation for char in password):
        suggestions.append("Add special characters (e.g., @, #, $, etc.).")
    if not any(char.isupper() for char in password):
        suggestions.append("Include at least one uppercase letter.")
    if not any(char.islower() for char in password):
        suggestions.append("Include at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include at least one numeric digit.")

    return suggestions


# Main program
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")

    # Check strength
    strength, breakdown = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    print("Criteria breakdown:")
    for criteria, score in breakdown.items():
        print(f" - {criteria.replace('_', ' ').capitalize()}: {'✔️' if score else '❌'}")

    # Provide suggestions if needed
    if strength != "Strong":
        print("\nSuggestions to improve your password:")
        for suggestion in suggest_improvements(password):
            print(f" - {suggestion}")
    else:
        print("\nGreat! Your password is strong.")

