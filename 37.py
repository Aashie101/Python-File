#try and except
try:
    num=int(input("Enter Number:"))
    result=10/num
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error:Invalid input")
print("Code executed by Prabhjot Kaur")