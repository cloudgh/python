class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total = self.calculate_total()

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def display_order(self):
        print(f"Order for {self.customer.name}:")
        for item in self.items:
            print(f"{item['product'].name} - {item['quantity']} units")
        print(f"Total: ${self.total}")
        print("Thank you for shopping with us!")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def checkout(self, customer):
        order = Order(customer, self.items)
        order.display_order()


product1 = Product(1, "Laptop", 1200)
product2 = Product(2, "Smartphone", 800)
product3 = Product(3, "Headphones", 100)


customer = Customer(1, "John Doe")


cart = ShoppingCart()


cart.add_item(product1, 2)
cart.add_item(product2, 1)
cart.add_item(product3, 3)


cart.checkout(customer)
