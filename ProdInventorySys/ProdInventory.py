class Product:
    def __init__(self, name, price, quantity):
<<<<<<< HEAD
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
=======
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
>>>>>>> ec5ad5aa70dd1fd5c6bc622741e7e69fddc63da5
