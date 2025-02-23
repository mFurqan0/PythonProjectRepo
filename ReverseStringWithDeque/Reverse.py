from collections import deque
store = input("Enter a string:")
de = deque(store)
s = ""
while de:
    s += de.pop()
print(s)    


