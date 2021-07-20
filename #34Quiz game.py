
def new_game():
    guesses = []                    # collect the user guess answer
    correct_guesses = 0             # collect the correct answer from user
    question_num = 1                # question number 
    
    for key in question1:
        print("--------------------------------------")
        print(key)                                      # print the question 
        for i in options[question_num-1]:               # print the option from each rows of array 這樣的寫法是針對每一列值去做顯示
            print(i)


        user_answer = input("Enter (A,B,C,D): ")        # user input the answer
        user_answer = user_answer.upper()               # change to uppercase
        guesses.append(user_answer)                     # collect the user answer to the guesses list

        # check the answer
        correct_guesses += check_answer(question1.get(key) , user_answer)


        question_num += 1
    


    #final execution 

    # show the final score
    displayer_score(correct_guesses, guesses)

    # Ask to play again
    play_again()


def check_answer(correct_answer,guess):
    if(correct_answer == guess):
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0

    

def displayer_score(correct_guesses, guesses):
    print("---------------------------------------")
    print("Results")
    print("---------------------------------------")
    
    print("Answer: ",end = '') 
    for i in question1:
        print(question1.get(i) ,end=' ')        # The correct answer from the dictionary 
    print()

    print("Guesses: ",end = '')                 # User answer from the guess list
    for i in guesses:
        print(i ,end=' ')
    print()


    score = int((correct_guesses / len(question1))*100)
    print("Your score is: "+str(score)+"%")



def play_again():
    again = input("Want to play agaian? (yes / no): ").lower()

    if (again == 'yes'):
        print('\n\n\n')
        new_game()
    else:
        print('\n\n\n')
        print("---------------------------------------")
        print("Good Bye~~~ See You")
        print("---------------------------------------")


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


new_game()



