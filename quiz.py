

def start_game():
    question_num = 0
    answer = []
    responce = []
    correct_num = 0

    for keys,values in question1.items():
        print(keys)
        answer.append(values)
        for select in options[question_num]:
            print(select)

        # change the next question 
        question_num += 1

        # user input 
        user_input= input('Please input your answer A,B,C or D: ').upper()
        print()

        # collect the answer
        responce.append(user_input)

    # check the correct number of question
    correctNum = check_answer(answer,responce)
    
    
    # check the grade
    Endgrade = show_grade(correctNum)
    print("Your grade is: "+ str(Endgrade)+  " %")


    #play again?
    again = input("Play again? (yes / no)").lower()
    if (again == 'yes'):
        play_again()
        print()
        print()

    elif(again == 'no' ):
        print("======================================================")
        print("------------------------------------------------------")
        print("Thanks for playing!")
        print("------------------------------------------------------")
        print("======================================================")

    



    

def check_answer(answer,response):
    correctNum = 0
    for i in range(len(answer)):
      if(answer[i] == response[i]):
        correctNum +=1
      else:
        correctNum +=0
    return correctNum


def show_grade(correctNumber):
    grade = (correctNumber/len(question1))*100
    return grade

def play_again():
    start_game()



# question (dictionary)
question1 = {
    'Who created Python?: ': 'A',
    'What year was the Python created?: ': 'B',
    'Pythonn is tributed to which comedy group?: ':'C',
    'Is the Earth round?: ':'A'
}

#options 2D array
options = [
    ['A. Gudio van Rossum', 'B. Elon Musk','C. Bill Gastes', 'D. Mark Zuckerburg'],
    ['A. 1989','B. 1991','C. 2000','D. 2016'],
    ['A. Lonely Island','B. Smosh','C. Monty Python','D. SNL'],
    ['A. True','B. False','C. sometimes','D. What\'s earth?']
]


start_game()