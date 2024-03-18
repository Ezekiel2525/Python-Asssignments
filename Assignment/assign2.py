import sys
import time

class calculator:
    def __init__(self):
        self.calculate()

    def calculate(self):
        self.value_1 = float(input("ENTER THE FIRST VALUE\n>>> "))
        time.sleep(1)
        print()
        self.operation = input("""
                                ENTER 1 TO PERFORM ADDITION
                                ENTER 2 TO PERFORM SUBTRACTION
                                ENTER 3 TO PERFORM MULTIPLICATION
                                ENTER 4 TO PERFORM DIVISION\n>>> """)
        time.sleep(1)
        print()
        self.value_2 = float(input("ENTER THE SECOND VALUE\n>>>  "))
        print()
        if self.operation == "1":
            print("PROCESSING...")
            print()
            time.sleep(1)
            print(self.value_1 + self.value_2)
            print()
            self.choose()
        elif self.operation == "2":
            print("PROCESSING...")
            print()
            time.sleep(1)
            print(self.value_1 - self.value_2)
            print()
            self.choose()
        elif self.operation == "3":
            print("PROCESSING...")
            print()
            time.sleep(1)
            print(self.value_1 * self.value_2)
            print()
            self.choose()
        elif self.operation == "4":
            print("PROCESSING...")
            print()
            time.sleep(1)
            print(self.value_1 / self.value_2)
            print()
            self.choose()
        else:
            print("INVALID OPERATION")
            self.calculate()
            print()

    def choose(self):
       self.decide = input("DO YOU WANT TO PERFORM ANOTHER OPERATION?\nENTER 1 TO PERFORM ANOTHER OPERATION\nENTER ANY OTHER KEY TO EXIT\n>>> ")
       if self.decide == "1":
        print()
        self.calculate()
       else:
            sys.exit()
    
calculator()

