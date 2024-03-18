import time
import sys

class story:

    def __init__(self):
        self.article()

    def article(self):
        self.text = input("WRITE AN ARTICLE OF YOUR CHOICE\n>>> ").strip().capitalize()
        print("PROCESSING...")
        time.sleep(2)
        print()
        self.num_replacement = int(input("ENTER THE NUMBER OF WORDS YOU WANT TO REPLACE\n>>> "))
        print()
        self.replacement = {}
        print()
        for i in range(self.num_replacement):
            self.target_words = input(f"ENTER WORD {i + 1}  YOU WANT TO REPLACE\n>>> ").strip()
            time.sleep(1)
            print()
            self.new_words = input(f"ENTER THE WORD YOU WANT TO REPLACE {self.target_words.upper()} WITH\n>>> ").strip()
            time.sleep(1)
            print()
            if self.target_words not in self.text:
                print("PROCESSING...")
                time.sleep(2)
                print()
                print("WORD NOT FOUND!!!")
            else:
                self.text = self.text.replace(self.target_words, self.new_words)
        print("PROCESSING...")
        time.sleep(2)
        print()
        print(self.text)
story()


# article = input("Write your own article").strip()
# replacement = input("Enter the word you want to replace: ").strip().lower()
# new_word = input("enter the word you want to replace with: ")
# if replacement not in article:
#     print('word not found')
# else:
#     new_article = article.replace(replacement, new_word)
#     print(new_article)



# # TO REPLACE MANY WORDS IN AN ARTICLE ALL AT ONCE

# article = input("Write your article: ").strip()
# num_replacement = int(input("Enter the number of words you want to replace: "))
# replacement = {}
# for i in range(num_replacement):
#     target_words = input(f"Enter word {i + 1} you want to replace: ")
#     new_words = input(f"Enter the word you want to replace {target_words} with: ")
#     if target_words not in article:
#         print('word not found')
#     else:
#         article = article.replace(target_words,new_words)
#         # print(article)
# print(article)