import random

choices = ['rock','paper','scissors']
computer = random.choice(choices)

player = None


while(1):                      # if user input not in the list
    resonse = input("Q: quit the game, C: play again")
    if resonse=='Q' or resonse =='q':
        break
    elif resonse=='C' or resonse =='c':
        player = input('rock, paper, or scissors?: ').lower()
        if player == 'rock':
            if(computer == 'paper'):
                print("You lose....")
                print("Com: "+computer)
                print("User: "+player)
            elif(computer == 'scissors'):
                print('You win!')
                print("Com: "+computer)
                print("User: "+player)
            else:
                print('Same no winner and loser')
                print("Com: "+computer)
                print("User: "+player)


        elif player == 'scissors':
            if(computer == 'rock'):
                print("You lose....")
                print("Com: "+computer)
                print("User: "+player)
            elif(computer == 'paper'):
                print('You win!')
                print("Com: "+computer)
                print("User: "+player)
            else:
                print('Same no winner and loser')
                print("Com: "+computer)
                print("User: "+player)


        elif player == 'paper':
            if(computer == 'scissors'):
                print("You lose....")
                print("Com: "+computer)
                print("User: "+player)
            elif(computer == 'rock'):
                print('You win!')
                print("Com: "+computer)
                print("User: "+player)
            else:
                print('Same no winner and loser')
                print("Com: "+computer)
                print("User: "+player)
    else:
        print("Enter the Q and C")

    
    

