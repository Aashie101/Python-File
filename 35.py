#armstrong in a range
def armstrong(num):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp=temp//10
    if sum==num:
        return num
range1=int(input("Enter lower range:"))
range2=int(input("Enter upper range:"))
counter=0
for i in range(range1,range2):
    if armstrong(i):
        print(i)
        counter=counter+1
print("Counter:",counter)
print("Code executed by Prabhjot Kaur ERP:0221BCA047")