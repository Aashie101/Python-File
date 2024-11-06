def findFirstEven(numbers):
    for num in numbers:
        if num%2==0:
            return num
    return None 
list1=[1,5,9,7,3,6,8]
result=findFirstEven(list1)
print(result)

print("77. This code is written by Prabhjot Kaur; 0221BCA047")