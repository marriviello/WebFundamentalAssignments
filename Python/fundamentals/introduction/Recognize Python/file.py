#primitive: numbers
#variable declaration
num1 = 42
num2 = 2.3

#primitive: boolean
boolean = True

#primitive: string
string = 'Hello World'

#composite: initialize list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

#composite: initialize dictionary 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

#composite: initialize tuples
fruit = ('blueberry', 'strawberry', 'banana')

print(type(fruit)) #type check
print(pizza_toppings[1]) #list: access value
pizza_toppings.append('Mushrooms') #list: add value
print(person['name']) #dictionary: access value
person['name'] = 'George' #dictionary: change value
person['eye_color'] = 'blue' #dictionary: add value
print(fruit[2]) #tuples: access value

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")


if len(string) < 5: #length check #conditional: if
    print("It's a short word!")
elif len(string) > 15: #conditional: else if
    print("It's a long word!")
else: #conditional: else
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):#for loop: start & end
    print(x)
for x in range(2,10,3): #for loop: increment
    print(x)
x = 0 #while loop: start
while(x < 5): #while loop: stop
    print(x)
    x += 1 #while loop: increment

pizza_toppings.pop() #list: delete value
pizza_toppings.pop(1) 

print(person) #log statement
person.pop('eye_color')#dictionary: delete value
print(person)

for topping in pizza_toppings: #for loop: sequence
    if topping == 'Pepperoni':
        continue #for loop: continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #for loop: break


def print_hello_ten_times():
    for num in range(10):
        print('Hello') #function: return

print_hello_ten_times()

def print_hello_x_times(x): #function: parameter
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #function: argument

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

#comment: multiline
"""
Bonus section
"""

#comment: single line

# print(num3) #NameError
# num3 = 72
# fruit[0] = 'cranberry' #tuples: change value #TypeError
# print(person['favorite_team']) #KeyError
# print(pizza_toppings[7]) #IndexError
#   print(boolean) #IndentationError
# fruit.append('raspberry') #tuples: add value #AttributeError
# fruit.pop(1) #tuples: delete value #AttributeError


