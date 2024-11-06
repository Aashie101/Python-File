# Write a python program to determine whether the given String is a palindrome or not

def main():
    user_string = input("Enter String: ")
    if user_string == user_string[::-1]:
        print("User entered string is palindrome")
    else:
        print("User entered strign is not a palindrome")

if __name__ == "__main__":
    main()
print("44.This code is written by Prabhjot Kaur ERP:0221BCA047 ")