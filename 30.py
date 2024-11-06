def sum_digit(num):
    total=0
    while num>0:
        x=num%10
        total=total+x
        num=num//10
    return total

def discount_calc(bill):
    if bill<10000:
        discount=sum_digit(bill)/2
    else:
        discount=sum_digit(bill)
    amount=(discount/100)*bill
    final_bill=bill-amount
    return discount, amount, final_bill

bill1=int(input("enter bill:"))
discount, amount, final_bill=discount_calc(bill1)
print(f"Total Amount:Rs.{bill1}")
print(f"Discount:{discount}%")
print(f"Discount amount:Rs.{amount}")
print(f"Final bill:Rs.{final_bill}")
print("Code executed by Prabhjot Kaur ERP:0221BCA047")