score = 0
        
questions = ["Where is SQI located in Ibadan?\n", "Where is oyo located in the geo-political zone\n",
                "Which of these is a colour?\n"]
options = ["a). Oke - ado b). Mokola c). Dugbe\n",
            "a). South-West b). South-East c). South-South\n",
            "a). Red b). Water c). Eba\n"]
answers = ["c", "a", "a"]

for i in range(len(questions)):
    print(questions[i])
    print(options[i])
    student_answer = input("enter your answer: ")
    if student_answer == answers[i]:
        print("good!")
        score += 10
    else:
        print("bad")
        score -= 5
print(score)