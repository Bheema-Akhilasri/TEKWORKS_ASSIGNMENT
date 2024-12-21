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

#Factorial 
def factorial(num):
    result=1
    for i in range(1,num+1):
        result*= i
    return result
fact=int(input('Enter number:'))
print(f"Factorial of {fact} is",factorial(fact))

#Prime Number
def prime(num):
    count=0
    if num==0 or num==1:
        return "neither prime nor composite"
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count>2:
        return "not prime"
    else:
        return "prime"
number=int(input('Enter number:'))
print(f"The number {number} is",prime(number))


#Leap Year
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "leap year"
    else:
        return "not a leap year"
year=int(input('Enter year:'))
print(f"The year {year} is",leap_year(year))

#
