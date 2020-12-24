n=int(input("Enter number of terms"))
start = 1
space = n-1
for i in range(1,n+1):
    start = i
    for j in range(1, space+1):
        print(" ", end=" ")
    space = space-1

    for j in range(1, i+1):
        print(start, end=" ")
        start = start+1
        
    start = start-2
    for j in range(1,i):
        print(start, end=" ")
        start = start-1
    print()
