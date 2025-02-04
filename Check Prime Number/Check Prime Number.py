n = int(input("enter a number:"))
if n == 1:
    print("please enter a greater number than 1")
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not prime number")
            break
    else:
        print(n,"is a prime number")        
