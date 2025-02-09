string = "This is my first python project"
freq = {}
for char in string:
    if char in freq:
        freq[char] +=1
    else:
         freq[char] = 1
print(freq)
     


