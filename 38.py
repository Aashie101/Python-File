# try except else
try:
    num=int(input("Enter number:"))
    result=10//num
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error:Invalid input")
else:
    print("result is:",result)
print("Code executed by Prabhjot Kaur")