num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

if num2>num1:
    mn = num1 
else:
    mn = num2

for i in range(1, mn+1):
    if num1%i == 0 and num2%i == 0:
        hcf = i

print("THE GCD of these two numbers :", hcf)               