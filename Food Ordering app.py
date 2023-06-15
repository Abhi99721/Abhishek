
class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = len(self.food_items) + 1
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                break

    def view_food_items(self):
        for food_item in self.food_items:
            print(f"FoodID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print()

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                break

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_order(self, food_items):
        order = []
        for food_id in food_items:
            for food_item in admin.food_items:
                if food_item.food_id == food_id:
                    order.append(food_item)
                    break
        self.order_history.append(order)

    def view_order_history(self):
        for order in self.order_history:
            print("Order:")
            for food_item in order:
                print(f"Name: {food_item.name}")
                print(f"Quantity: {food_item.quantity}")
                print(f"Price: {food_item.price}")
                print(f"Discount: {food_item.discount}")
                print()
            print()

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

# Creating an instance of Admin
admin = Admin()

# Creating food items
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
admin.add_food_item("Vegan Burger", "1 piece", 320, 0, 15)
admin.add_food_item("Truffle Cake", "500gm", 900, 0, 5)

# Creating an instance of User
user = User("John Doe", "1234567890", "johndoe@example.com", "123 Main St", "password")

# Placing a new order
user.place_order([2, 3])

# Viewing order history
user.view_order_history()

# Updating profile
user.update_profile("John Smith", "0987654321", "johnsmith@example.com", "456 Elm St", "newpassword")
