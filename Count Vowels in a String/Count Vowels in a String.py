#take input of string
string = input("Enter a string:")

#make the uppercase letter of string into lowercase
string.lower()

#declare a variable that will check the count of vowels in string
count = 0 

# create a list in which give vowels letters
list = ["a","e","i","o","u"]

#search for characters in string 
for char in string:

#if chracter found in string 
    if char in list:

#increase the value of count by 1 
        count = count + 1

#after the total count of vowels in a string print the output along the count
print("no of vowels found in string is :", count)
