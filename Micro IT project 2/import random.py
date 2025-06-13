import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_specials=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    specials = string.punctuation if use_specials else ''
    
    all_chars = lower + upper + digits + specials
    if not all_chars:
        raise ValueError("At least one character set must be selected")

    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_specials:
        password.append(random.choice(specials))
    password.append(random.choice(lower))

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(length=16))