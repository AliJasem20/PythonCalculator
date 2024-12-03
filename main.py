#python Calculator

operator = input("enter an operator (+,-,*, /): ")
Num1 = float(input("Enter the 1st number: "))
Num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = Num1 + Num2
    print(round(result,3))
elif operator == "-":
    result = Num1 - Num2
    print(round(result,3))
elif operator == "*":
    result = Num1 * Num2
    print(round(result,3))
elif operator == "/":
    result = Num1 / Num2
    print(round(result,3))
else:
    print(f"{operator} is not a valid operator")