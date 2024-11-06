#perfect number 
num=int(input("Enter Number:"))
if num<1:
    print("Enter number greater than 0")
else:
    multiples=[]
    for i in range(1,num//2+1):
        if num%i==0:
            multiples.append(i)
    sum_list= sum(multiples)
    if sum_list==num:
        print(num,"is Perfect number")
    else:
        print(num,"not a perfect number")
print("Code executed by Prabhjot Kaur ERP:0221BCA047")