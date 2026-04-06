try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input (not a number)")