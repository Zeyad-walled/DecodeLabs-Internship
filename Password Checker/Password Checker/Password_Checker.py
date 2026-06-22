import string
print("============== Welcome to the Password Strength Checker! ==============")
print("Strong password must contain upeercase & lowercase & Numbers & Symbols")

password = input("Enter a password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if any(char.isupper() for char in password):
    score += 1

# Lowercase check
if any(char.islower() for char in password):
    score += 1

# Number check
if any(char.isdigit() for char in password):
    score += 1

# Symbol check
if any(char in string.punctuation for char in password):
    score += 1
    
# Strength evaluation
if score <= 2:
    print("Password Strength: Weak")
    print("Please Try again!")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
