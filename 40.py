def evenOdd(num):
    if num%5==0:
        print(num,"is divisible by 5")
    elif num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")

def div5(num):
    if num%5==0:
        print(num,"divisible by 5")

num1=int(input("Enter lower range:"))
num2=int(input("Enter upper range:"))
if num1<=0:
    print("Enter number greater than 0")
else:
    for i in range(num1,num2+1):
        evenOdd(i)
        
print("Code executed by Prabhjot Kaur ERP:0221BCA047")
