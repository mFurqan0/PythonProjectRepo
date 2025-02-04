#def a recursive function in which pass a number as a parameter
def fact(n):

#After creating a function check if n = 0 or 1 
    if (n == 0 or n == 1):

#return 1
        return 1
    else:

#or return the factorial of the number by using stack call method
        return n * fact(n-1)

#assign a variable to your factorial you want to print 
print_factorial = fact(5)

#then print it 
print(print_factorial)
