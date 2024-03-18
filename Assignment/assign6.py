import time
import sys

class cbt_exam:
    
    def __init__(self):
        print("WELCOME TO NEECORP ONLINE UNIVERSITY FINAL EXAM")
        print("<---------------------------------------------->")
        print() 
        time.sleep(1)      
        self.usernames = ['jen', 'Jackie chan', 'Jumong']
        self.password = ['jn44', 'jc34', 'j255']
        self.main_menu()
        
    def main_menu(self):
        self.option = input("ENTER 1  TO LOG IN\n\nENTER ANY OTHER KEY TO EXIT\n\n>>> ")
        if self.option == "1":
            self.login()
        else:
            print(f"GOODBYE, {self.user}")
                     
    def login(self):
        self.xz = list(zip(self.usernames, self.password))
        self.user = input("PLEASE ENTER YOUR USERNAME CORRECTLY\n>>> ").strip().lower()
        time.sleep(1)
        self.pwd = input("PLEASE ENTER YOUR PASSWORD CORRECTLY\n>>> ").strip().lower()
        if (self.user, self.pwd) in self.xz:
            print()
            print("PROCESSING...")
            time.sleep(2)
            print(f"DEAR {self.user}, YOU HAVE LOGGED IN SUCCESSFULLY!!! ")
            self.Exam()
        else:
            print("INVALID LOGIN DETAILS")
            self.login()
            
    def Exam(self):
        self.scores = 0
        self.questions = ["1) Who is the President of USA", "2) Who is the CEO of Facebook", "3) Which of these is a colour"
                          "4) Who won the worldcup in 2022"]
        
        self.options = ['a) Vladmir Putin\n  b) Joe Biden\n  c) Bola Tinubu',
                        'a) Elon Musk\n  b) Mark Zuckerberg\n  c) Jack Dorsey',
                        'a) Red\n  b) Umbrella\n  c) jar',
                        'a) France\n  b) Argentina\n  c) Japan']
        
        self.answers = ['b', 'b', 'a', 'b']
        
        
        
        
                

cbt_exam()



















































































































# usernames = ['jen', 'Jackie chan', 'Jumong']
# password = ['jn44', 'jc34', 'j255']
# username_input = input("Enter your username: ").strip()
# print("Processing...")
# time.sleep(1)
# user_password = input("Enter your password: ").strip().lower()
# x = list(zip(usernames, password))
# if (username_input, user_password) in x:
#     print("Processing...")
#     time.sleep(1)
#     print("LOGIN SUCCESSFUL!!")

#     score, nt = 0,0

#     questions = ["Where is SQI located in Ibadan?\n", "Where is oyo located in the geo-political zone\n",
#                  "Which of these is a colour?\n", "Which of these is a country in Europe"]
#     options = ["a). Oke - ado b). Mokola c). Dugbe\n",
#                "a). South-West b). South-East c). South-South\n",
#                "a). Red b). Water c). Eba\n",
#                "a). China b). Dubai c). France\n"]
#     answers = ["c", "a", "a", "c"]

#     for index, question in enumerate(questions, start=1):
#         print(index, question)
#         time.sleep(1)
#         print()
#         print(options[nt])
#         student_answer = input("Enter your answer (a/b/c): ")
#         if student_answer == answers[nt]:
#             time.sleep(1)
#             print("correct!")
#             score +=1
#         else:
#             time.sleep(1)
#             print("Failed!")
#             score -= 1
#         nt += 1
#         print()
        
# else:
#     print("INVALID LOGIN!!!😥")

# result = score / len(questions)
# print(f"you scored {score} / {len(questions)}, That is {result * 100}")
