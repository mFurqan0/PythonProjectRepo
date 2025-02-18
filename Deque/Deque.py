from collections import deque  

def is_palindrome(s):  
    # Clean the string: lowercase and remove spaces  
    cleaned = s.lower().replace(" ", "")  
    dq = deque(cleaned)  

    while len(dq) > 1:  
        left = dq.popleft()  
        right = dq.pop()  
        if left != right:  
            return False  
    
    return True

print(is_palindrome("Racecar"))  
