num=int(input ("Enter number:"))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp=temp//10
print("Sum of numbers:", sum)
if sum==num:
    print(num,"is armstrong")
else:
    print(num,"not armstrong")
print("Code executed by Prabhjot Kaur ERP:0221BCA047")