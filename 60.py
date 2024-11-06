# Program to Use Generator with yield:

def countdown(n):
   while n > 0:
     yield n
     n -= 1
for number in countdown(5):
 print(number) # Outputs: 5, 4, 3, 2, 1
print("60.This code is written by Prabhjot Kaur ERP:0221BCA047")