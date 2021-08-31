#Banking System

class User():

    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def user_details(self):
        print("-"*20)
        print("USER DETAILS..")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance+=amount
        print("Deposit Done\nNew Balance: $", self.balance)
    
    def withdraw(self, amount):
        if (amount > self.balance):
            print("Not Enough Balance")
            return
        else: 
            self.balance -= amount
            print("Withdraw Done\nBalance Left: $", self.balance)

    def bank_details(self):
        print("\n\nAccount Details...")

        self.user_details()
        print("Account Balance: $",self.balance)



def main():
    u1 = User("Maaz", 21, "Male")
    u1.user_details()

    b1 = Bank("Maaz", 20, "Male")
    b1.deposit(150)
    b1.withdraw(200)
    b1.bank_details()

if __name__ == "__main__":
    main()
