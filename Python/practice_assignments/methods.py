class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def greeting(self):
        print(f"Hello, my name is {self.name}")

maria = User("Maria", "maria@gmail.com")
harry = User("harry", "harry@gmail.com")

maria.greeting()
harry.greeting()
print(harry.email)