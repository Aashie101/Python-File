my_string="Hello"
char_find=input("Enter character to find:")
position=[i for i, char in enumerate(my_string) if char==char_find]
if position:
    print("Character found at position:",position)
else:
    print("Character not found")
print("Code executed by Prabhjot Kaur")