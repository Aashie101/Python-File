def print_info(**kwargs):
 for key, value in kwargs.items():
     print(f"{key}: {value}")

print("Variable length(kwargs)")
print_info(name="Alice", age=30, city="New York")
print("79. This code is written by Prabhjot Kaur; 0221BCA047")