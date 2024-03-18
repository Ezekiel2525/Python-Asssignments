import time
import sys


class fast_food:

    def __init__(self):
        print("WELCOME TO NEECORP FAST FOOD RESTAURANT")
        print("<-------------------------------------->")
        print()
        print("PROCEED TO MAKE YOUR ORDER")
        print()
        self.food = ['Rice', 'Beans', 'Yam', 'Semovita', 'Eba', 'Amala', 'Spaghetti', 'Macaroni', 'Fried-Plantain']
        self.protein = ['Egg', 'Fish', 'Meat', 'Bokoto', 'kponmo']
        self.soup = ['Egusi', 'Stew', 'Vegetable-soup', 'Ogbono', 'Okro']
        time.sleep(2)
        self.restaurant()

    def restaurant(self):
        print("<-----------FOOD CHOICE---------->")
        for index, foods in enumerate(self.food, start=1):
            print()
            print(index, foods)
            print()
        self.foodchc = input(f"ENTER YOUR FOOD CHOICE\n\n>>> ").strip().capitalize()
        time.sleep(1)
        print()
        print("<-----------SOUP CHOICE---------->")
        for index, soups in enumerate(self.soup, start=1):
            print()
            print(index, soups)  
            print()
        self.soupchc = input(f"ENTER YOUR SOUP CHOICE\n\n>>>  ").strip().capitalize()
        time.sleep(1)
        print()
        if self.foodchc in self.food and self.soupchc in self.soup:
            print("<-----------PROTEIN CHOICE---------->")
            for index, pro in enumerate(self.protein, start=1):
                print()
                print(index, pro)
                print()
            self.prochc = input(f"ENTER YOUR PROTEIN CHOICE\n\n>>> ").strip().capitalize()
            print()
            print("PROCESSING...")
            time.sleep(2) 
            print(f"YOU ORDERED FOR\n\n{self.foodchc.upper()}\n\n{self.soupchc.upper()}\n\n{self.prochc.upper()}")
            print()
            self.decide()
        else:
            print(f"YOUR ORDER {self.foodchc.upper()}, {self.soupchc.upper()}, AND {self.prochc.upper()} IS NOT AVAILABLE😣...PLEASE ENTER THE AVAILABLE OPTIONS")
            self.restaurant()
   
    def decide(self):
        self.choose = input("ENTER 1 TO ORDER AGAIN\nENTER 2 TO EXIT\n>>> ")
        if self.choose == "1":
            self.restaurant()
        else:
            print("THANKS FOR YOUR PATRONAGE...DO HAVE A NICE DAY!👌")
            sys.exit()

fast_food()
        
      

    

# food = input("Which food would you like?: ").strip().lower()
# protein = input("What protein would you like?: ").strip().lower()
# if food == "rice" and protein == "egg":
#     print("I will buy rice and egg")
# else:
#     print("I will not buy anything")


# food = ['Rice', 'Beans', 'Yam', 'Semovita']
# for index, i in enumerate(food, start=1):
#     print(index, i)


# food = ['Rice', 'Beans', 'Yam', 'Semovita', 'Eba', 'Amala', 'Spaghetti', 'Macaroni', 'Fried-Plantain']
# for index, i in enumerate(food, start=1):
#     print(index, i)