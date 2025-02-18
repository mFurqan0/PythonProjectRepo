class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_stock(self, sold_quantity):
        self.quantity -= sold_quantity
    
    def get_total_value(self):
        return self.price * self.quantity
    
    def display(self):
        print(f"{self.name} - Price: ${self.price}, Stock: {self.quantity}")

# Test Case:
p1 = Product("Iphone14", 350, 56)
p1.update_stock(12)
p1.display()
print("Total Inventory Value:", p1.get_total_value())