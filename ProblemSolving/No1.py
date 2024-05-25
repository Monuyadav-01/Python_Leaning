def calAge(age):
    if age < 13:
        return "Children"
    elif 13 <= age <= 18:
        return "Teenager"
    elif 18 < age <= 60:
        return "Younger"
    elif age > 60:
        return "Senior citizen"
    else:
        return "very old"


age = int(input("Enter your age : "))
print(calAge(age))
