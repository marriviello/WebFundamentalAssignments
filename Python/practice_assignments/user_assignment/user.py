class User:
    def __init__(self, name, last, email, age):
        self.first_name = name
        self.last_name = last
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self
    
    def enroll(self):
        # if self.is_rewards_member == False:
        self.is_rewards_member = True
        self.gold_card_points = self.gold_card_points + 200
        # else:
        #     print("already a member!")
        return self
    
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("funds not available!")
        return self

user_maria = User("Maria", "Arriviello", "maria@gmail.com", 28)
user_maria.display_info().enroll().spend_points(50).display_info
print(user_maria.gold_card_points)

# user_maria.display_info().enroll().spend_points(50).display_info()
# print(user_maria.gold_card_points)

#first user spend 50 points
# user_maria.enroll()
# user_maria.spend_points(50)
# print(user_maria.gold_card_points)

user_harry = User("Harry", "Chang", "harry@gmail.com", 39)
user_harry.display_info().enroll().spend_points(80).display_info
print(user_harry.gold_card_points)

#enroll second user & spend 80 points
# user_harry.enroll()
# user_harry.spend_points(80)
# print(user_harry.gold_card_points)













