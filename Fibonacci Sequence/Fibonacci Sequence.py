n =(int(input("ENTER THE NUMBER FOR THE NO.OF TERMS OF FIBONACCI SEQUENCE:")))
num1 = 0
num2 = 1
sum = 0
if n<= 0:
    print("please enter a greater number than Zero!")
else:
    for i in range(0,n):
        print(sum)
        num1 = num2
        num2 = sum
        sum = num1+num2
