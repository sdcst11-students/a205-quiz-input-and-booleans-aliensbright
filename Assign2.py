"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
print('I will calculate the missing side length of a right triangle.')
a=float(input('Input one of the side lengths==>'))
b=float(input('Input the other known side length==>'))
if a>b:
    large=a
    small=b
else:
    large=b
    small=a
q=str(input('Is one of the known side lengths the hypotenuse. Y/N==>'))
if q=="Y":
    hyp=large
    missing = (hyp**2-small**2)**0.5
    missing = float(missing)
    missing = round(missing,1)
    if missing<small:
        large=small
        small=missing
    else:
        large=missing
else:
    hyp=(large**2+small**2)**0.5
    hyp = round(hyp,1)
    print(hyp)
print(f"The 3 side lengths would be {small}, {large}, and {hyp}")
