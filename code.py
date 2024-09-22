import re
def password_strength(password):
    """
    This function checks the strength of a password.
    
    A strong password should have:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    
    Returns:
    - "Strong" if the password meets all the criteria
    - "Weak" if the password does not meet all the criteria
    """
    if len(password) < 8:
        return "Weak"
    
    if not re.search("[a-z]", password):
        return "Weak"
    
    if not re.search("[A-Z]", password):
        return "Weak"
    
    if not re.search("[0-9]", password):
        return "Weak"
    
    if not re.search("[_@$]", password):
        return "Weak"
    
    return "Strong"

# Example usage:
password = input("Enter a password: ")
print(password_strength(password))
