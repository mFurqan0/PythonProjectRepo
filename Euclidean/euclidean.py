import math

def main():
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))
    
    distance = math.sqrt(x * x + y * y)
    
    print("Euclidean distance between X and Y is:", distance)

if __name__ == "__main__":
    main()

    