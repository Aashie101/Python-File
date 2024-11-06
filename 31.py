#reverse a number
def reverse(num):
    reverseNum=0
    while num>0:
        x=num%10
        reverseNum= reverseNum*10+x
        num=num//10
    return reverseNum
number=int(input("Enter number:"))
print(f"Reverse Number:{reverse(number)}")
print("Code executed by Prabhjot Kaur ERP:0221BCA047")
