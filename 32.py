print("Part i")
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("Part ii")
for i in range(1,5+1):
    for j in range(1,i + 1): 
        print(j , end='')
    print()
print("Part iii")
for i in range(1,5+1):
    for j in range(1,i + 1): 
        print(i , end='')
    print() 
print("Part iv")
for i in range(5, 0, -1):
    for j in range(1,i + 1): 
        print("*" , end='')
    print()  
print("Part v")
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(i, end='')
    print()
print("Part vi")
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end='')
    print() 
print("Part vii")
for i in range(0,5):
    for j in range(5,i,-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()
print("Part viii")
size = 5
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
print("Part ix")
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
print("Code executed by Prabhjot Kaur ERP:0221BCA047")
