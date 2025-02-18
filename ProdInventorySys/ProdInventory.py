class Product:
    def __init__(self, name, price, quantity):
        self.name  = name 
        self.price = price 
        self.quantity = quantity

    # Update stock quantity
    def update_stock(self, sold_quantity):
        self.quantity -= sold_quantity

        
    
    # Calculate total value of inventory
    def get_total_value(self):
        return self.price * self.quantity
    
    # Display product info
    def display(self):
        print(self.name,"|","Price:",self.price,"$","|","Quantity:",self.quantity)

# Test Case:
p1 = Product("Iphone14",350,56)
p1.update_stock(12)
p1.display()
print("Total value of Inventory:",p1.get_total_value())
