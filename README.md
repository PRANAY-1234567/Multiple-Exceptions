📘 Python Program: Exception Handling (Division with Error Handling)


📌 Overview

This Python program demonstrates exception handling using try-except blocks.
It takes a number as input and performs division (10 / num) while handling possible errors like:

Division by zero
Invalid (non-numeric) input
⚙️ Source Code
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input (not a number)")
    
🧠 How It Works
1️⃣ Try Block
try:
Contains code that may cause an error.
Python attempts to execute this block.
2️⃣ User Input
num = int(input("Enter number: "))
Takes input from the user.
Converts it to an integer.
If input is not a number → ValueError
3️⃣ Division Operation
result = 10 / num
Divides 10 by the input number.
If num = 0 → ZeroDivisionError
4️⃣ Print Result
print(result)
Displays the result if no error occurs.
5️⃣ Handle ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
Executes when user enters 0.
6️⃣ Handle ValueError
except ValueError:
    print("Invalid input (not a number)")
Executes when user enters text or invalid input.
▶️ Example Execution
✅ Valid Input
Enter number: 2
5.0
❌ Division by Zero
Enter number: 0
Cannot divide by zero
❌ Invalid Input
Enter number: abc
Invalid input (not a number)
🔑 Key Concepts Used
Exception Handling (try-except)
Multiple Exceptions
User Input
Type Conversion (int())
Arithmetic Operations
⏱️ Time Complexity

O(1) — Constant time execution.

🚀 Possible Improvement (Using finally)
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Program execution completed")
📚 Learning Outcome

After understanding this program, you will learn:

How to handle runtime errors
How to use multiple except blocks
How to write safe and user-friendly programs

<img width="631" height="805" alt="image" src="https://github.com/user-attachments/assets/2548f0a1-96f2-45e9-b38e-75f7d2025404" />

