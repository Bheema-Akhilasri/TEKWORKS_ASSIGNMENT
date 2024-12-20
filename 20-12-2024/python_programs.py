#Validate password
def check_password_strength(password):
    if len(password)<10 and len(password)>15:
        return "Password length should be between 10-15"
    elif not any(char.isupper() for char in password):
        return "Moderate: Use at least 1 uppercase letter."
    elif not any(char.islower() for char in password):
        return "Moderate: Use at least 1 lowercase letter."
    elif not any(char.isdigit() for char in password):
        return "Moderate: Use at least 1 digit."
    elif not any(char in "!@#$%^&*()-_=+[{]};:'\",<.>/?`~" for char in password):
        return "Password should include at least one special character."
    elif " " in password:
        return "Password should not contain white space"
    elif password[-1]=='.' or password[-1]=='@':
        return "Password should not end with '.' or '@'"
password=input('Enter your password : ')
print(check_password_strength(password))

#
