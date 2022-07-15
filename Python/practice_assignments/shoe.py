
# class User:
#     def __init__(self):
#         self.first_name = "maria"
#         self.last_name = "arriviello"
#         self.age = "28"

# print("Hello")

# user_maria = User()
# print(user_maria.first_name)

# user_2 = User()
# print(user_2.first_name)


# Instance attributes are defined in the constructor, 
# that special __init__ method, which is called when a new object is instantiated, 
# in this case, when a new type of shoes is added to inventory.

# declare a class and give it name Shoe
class Shoe:
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
        self.price = 69.99
        self.in_stock = True

skater_shoe = Shoe()
dress_shoe = Shoe()
# Accessing the instance's attributes
print(skater_shoe.type) # Classic Sk8-Hi
print(dress_shoe.type)	# Classic Sk8-Hi

skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)
# output: Low-top Trainers
dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)
# output: Ballet Flats

#Passing an argument 
class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True

    def on_sale_by_percent(self, percent):
        self.price = self.price * (1- percent)

skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats
print(skater_shoe.price)

skater_shoe.on_sale_by_percent(0.3)
print(skater_shoe.price)

dress_shoe.on_sale_by_percent(0.5)
print(dress_shoe.price)

#The skater shoes go on sale by 20%
skater_shoe.price = (1 - 0.2) * skater_shoe.price

#The dress shoes go on sale by 10% reduction
dress_shoe.price = (1-0.1) * dress_shoe.price

#The skater shoes go on sale AGAIN by another 10%
skater_shoe.price = (1-0.1) * skater_shoe.price 








