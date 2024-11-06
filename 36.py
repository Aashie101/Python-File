def armstrong(num):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp=temp//10
    if sum==num:
        return True
    return False
range1=int(input("Enter lower range"))
number=int(input("Enter numbers you want:"))
counter=0
while counter<number:
    range1+=1
    if armstrong(range1):
        print(range1)
        counter+=1
print ("Counter:",counter)
print("Code executed by Prabhjot Kaur")