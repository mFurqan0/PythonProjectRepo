status = input("Are you Single or Married: ").lower()
salary = int(input("Enter your Salary: $"))

if status == "single":
    if salary >= 372951:
        tax_rate = 35.0
    elif salary >= 171551:
        tax_rate = 30.0
    elif salary >= 82251:
        tax_rate = 25.0
    elif salary >= 33951:
        tax_rate = 20.0
    elif salary >= 8351:
        tax_rate = 15.0
    else:
        tax_rate = 10.0
elif status == "married":
    if salary >= 372951:
        tax_rate = 35.0
    elif salary >= 208851:
        tax_rate = 30.0
    elif salary >= 137051:
        tax_rate = 25.0
    elif salary >= 67901:
        tax_rate = 20.0
    elif salary >= 16701:
        tax_rate = 15.0
    else:
        tax_rate = 10.0
else:
    print("Invalid input! Please enter 'single' or 'married'")
    exit()

tax = salary * (tax_rate / 100)
take_home = salary - tax

print(f"\nMarginal Tax Rate: {tax_rate}%")
print(f"Tax Amount: ${tax:.2f}")
print(f"Take-home Salary: ${take_home:.2f}")