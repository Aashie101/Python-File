a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a==b or a==c or b==c:
    print("Number are same")
else:
    if a>b and a>c:
        print(a,"is greatest")
    elif b>c and b>a:
        print(b,"is greatest")
    else:
        print(c,"is greatest")
print("Code executed by Prabhjot Kaur ERP:0221BCA047")
