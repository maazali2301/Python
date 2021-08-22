#Basic Inventory Program for a Pet Shop

#For File Handling
import json
import os.path

class Manager:

    pets = {}

    def __init__(self):
        self.load()

    def add(self, key, qty):
        if key in self.pets:
            self.pets[key] += qty
        else:
            self.pets[key] = qty

        print("Addition Complete!")
        print("Key: {}, Total: {}".format(key, self.pets[key]) )
   
   
    def remove(self, key, qty):
        if key in self.pets:
            self.pets[key] -= qty
        
        if self.pets[key] < 0:
            self.pets[key] = 0

        print("Subtraction Complete!")
        print("Key: {}, Total: {}".format(key, self.pets[key]) )

    def details(self):
        print("*" * 20)
        print("Inventory Details")
        print("*" * 20)
        for key, value in self.pets.items():
            print(f'{key} = {value}')


    def save(self):
        print("\nSaving Inventory")

        filename = "inventory.txt"
        with open(filename, 'w') as f:
            json.dump(self.pets, f)

        print("Saving Complete\n")

    def load(self):
        print("\nLoading Inventory")

        filename = "inventory.txt"

        if not os.path.exists(filename):
            print("Nothing to Load!\n")
            return
        else:
            with open(filename, 'r') as f:
             self.pets = json.load(f)

        print("Loading Complete\n")
        

def main():
    inv = Manager()
    #inv.load()
    print("Pet Shop Inventory Program Running.....\n")
    while True:
        choice = input("Add? Remove? Display? Save? Exit?: ")
        if choice == "Exit":
            break
        if choice == "Display":
            inv.details()
        if choice == "Save":
            inv.save()
        if choice == "Add":
            key = input("Input Category to Add to: ")
            qty = int(input("Input Quantity to Add: "))
            inv.add(key, qty)
        if choice == "Remove":
            key = input("Input Category to Remove from: ")
            qty = int(input("Input Quantity to Remove: "))
            inv.remove(key, qty)

    inv.save()
    print("-"*20)
    print("Thanks for using our system")
    print("-"*20)

if __name__ == "__main__":
    main()