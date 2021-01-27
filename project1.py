'''
Advance Rock paper sciecer game 
Game featurs:
1- Being able to choose to play against computer or multiple player
2- Bieng able to monitor resutls in both 1 player or 2 player mode
3- Writing data into excell in 2 player mode

Rule of the game is just like the traditional rock paper sciecer game 
Rock vs sciecer: Rock wins
Rock vs Paper : Paper wins
Paper vs Sciecer : Sciecer wins 

TODO: Coming soon: Game resutls will be stored in a database.
'''

import xlsxwriter #import module to write excell file
import random
import getpass #in 2 player mode players shouldn't be able to see eachother's input
def main():
    computer_score = 0
    user_score = 0
    second_player_score = 0
    print('Please choose if you want to play againt computer or another friend?\n Enter 1 for computer \ an Enter 2 to play with a friend ')
    cof = int(input())  #this game has 2 modes 1- to play with computer or 2- to play with another human (real player)
    
    if cof == 1:
        while True:
            user_name = input   ('please enter your name')
            #TODO: create a function to play against computer
            print('Please enter the number assosiated with your choice \n 1- ROCK \n 2-PAPER \n 3- SCISSOR')
            user_choices = getpass.getpass(f'{user_name}\'s turn: ') # this method will keep the player 1 input hidden so the player 2 will not be able to cheat
            computer_choice, computer_choice_name, user_choices_name = game(user_choices) # game function is in charge of the game against computer it will return the choices computer made
            computer_score,user_score = results(user_choices,computer_choice,user_choices_name,computer_choice_name,computer_score,user_score,user_name) # this function takes all the data in play against computer mode to desplay results
            #this function does not write data into excell
            print('Do you want to play again?')
            play_again = input('please answer using y or n')
            if play_again == 'n' or play_again == 'N':
                break
    elif cof == 2:
        while True:
            user_name = input   ('please enter your name')
            print('Please enter the number assosiated with your choice \n 1- ROCK \n 2-PAPER \n 3- SCISSOR')
            user_choices = getpass.getpass(f'{user_name}\'s turn: ') #keeps the user input hidden
            # TODO: creat a function to play against another player 
            second_player_name,second_player_choices,user_choices_name,second_player_choices_name = two_player_game(user_choices,user_name) # works just like game function but for 2 player mode
            two_player_results(second_player_name,second_player_choices,second_player_choices_name,user_name,user_choices_name,user_choices,second_player_score,user_score) # just like result function but for two player mode and also writes data into excell
            play_again = input('please answer using y or n')
            if play_again == 'n' or play_again == 'N':
                break
    else:
        print("Invalid Input, please enter 1 or 2")
        return main()
               
      


def game(user_choices):
    #setup and identify user input 
    user_choices_name = ''
    if int(user_choices) == 1 : # conver the user input into int
        user_choices_name = 'rock'  
        print('Your choice is rock')
    elif int(user_choices) == 2:
        user_choices_name = 'paper'
        print('Your choice is paper')
    elif int(user_choices) == 3:
        user_choices_name = 'sciecer'
        print('Your choice is sicssor')  
    else:
        print('your input is not valid')
        return
          

    computer_choice = random.randint(1,3) # computer must select a random number between 1 to 3
    computer_choice_name = ''
    if computer_choice == 1 :
        computer_choice_name = 'rock'
        print('Computer choice is rock')
    elif computer_choice == 2:
        computer_choice_name = 'paper'
        print('Computer choice is paper')
    elif computer_choice == 3:
        computer_choice_name = 'sicssor'
        print('Computer choice is sicssor')  
    else:
        print('Computer input is not valid')
    return computer_choice,computer_choice_name,user_choices_name

def results(user_choices, computer_choice, user_choices_name,computer_choice_name,computer_score,user_score,user_name):
    #TODO: possible ways to win in this game
    if(int(user_choices) == computer_choice):
        print(f'Your choice was {user_choices_name} and the computer choice was {computer_choice_name}, the choices are equal so no one gets a point ')
    elif int(user_choices) == 1 and computer_choice == 2:
        print(f'Your choice was {user_choices_name} and the computer choice was {computer_choice_name}, Computer wins! ')
        computer_score+=1
    elif int(user_choices) == 2 and computer_choice == 1:
         print(f'Your choice was {user_choices_name} and the computer choice was {computer_choice_name}, You win! ')
         user_score+=1
    elif int(user_choices) == 3 and computer_choice == 1 :
        print(f'Your choice was {user_choices_name} and the computer choice was {computer_choice_name}, Computer wins! ')
        computer_score+=1
    elif int(user_choices) == 3 and computer_choice == 2 :
        print(f'Your choice was {user_choices_name} and the computer choice was {computer_choice_name}, You win! ') 
        user_score+=1   
    elif computer_choice == 3 and int(user_choices) == 1 :
        print(f'Your choice was {user_choices_name} and the computer choice was {computer_choice_name}, You win! ') 
        user_score+=1   
    elif computer_choice == 3 and int(user_choices) == 2 :
        print(f'Your choice was {user_choices_name} and the computer choice was {computer_choice_name}, Computer wins! ')  
        computer_score+=1    
    print(f' Your score is: {str(user_score)} \n Computer score is: {str(computer_score)}')

    return computer_score,user_score
def two_player_game(user_choices,user_name): # this function produce second player choice
    # and must identify 1st player choices too
    second_player_name = input('What is the second player\'s name?')
    print('Please enter the number assosiated with your choice \n 1- ROCK \n 2-PAPER \n 3- SCISSOR')
    second_player_choices = int(input(f'{second_player_name} turn: '))
    if int(user_choices) == 1 :
        user_choices_name = 'rock'
        print('Your choice is rock')
    elif int(user_choices) == 2:
        user_choices_name = 'paper'
        print('Your choice is paper')
    elif int(user_choices) == 3:
        user_choices_name = 'sciecer'
        print('Your choice is sicssor')  
    else:
        print('your input is not valid')
        
    if second_player_choices == 1 :
        second_player_choices_name = 'rock'
        print(f'{second_player_name} choice is rock')
    elif second_player_choices == 2:
        second_player_choices_name = 'paper'
        print(f'{second_player_name} choice is paper')
    elif second_player_choices == 3:
        second_player_choices_name = 'sciecer'
        print(f'{second_player_name} choice is sicssor')  
    else:
        print('your input is not valid')
    return second_player_name,second_player_choices,user_choices_name,second_player_choices_name

def two_player_results(second_player_name,second_player_choices,second_player_choices_name,user_name,user_choices_name,user_choices,second_player_score,user_score):
    workbook = xlsxwriter.Workbook('results.xlsx') # create the file and use results as file name
    worksheet = workbook.add_worksheet('Two player Results') # add a new sheet to the excell file
    #in order to tell the program ro start writing in excell from the first row and colum
    row = 0
    col = 0
    if(int(user_choices) == second_player_choices):
        print(f'second_player_name is: {second_player_name} ,  second_player_choices_name is: {second_player_choices_name}')
        print(f'{user_name}\'s choice was {user_choices_name} and the {second_player_name}\'s choice was {second_player_choices_name}, the choices are equal so no one gets a point ')
    elif int(user_choices) == 1 and second_player_choices == 2:
        print(f'second_player_name is: {second_player_name} ,  second_player_choices_name is: {second_player_choices_name}')
        print(f'{user_name}\'s choice was {user_choices_name} and the {second_player_name}\'s choice was {second_player_choices_name}, {second_player_name} Wins! ')
        second_player_score+=1
    elif int(user_choices) == 2 and second_player_choices == 1:
        print(f'second_player_name is: {second_player_name} ,  second_player_choices_name is: {second_player_choices_name}')
        print(f'{user_name}\'s choice was {user_choices_name} and the {second_player_name}\'s choice was {second_player_choices_name}, {user_name} Wins! ')
        user_score+=1
    elif int(user_choices) == 3 and second_player_choices == 1 :
        print(f'{user_name}\'s choice was {user_choices_name} and the {second_player_name}\'s choice was {second_player_choices_name}, {second_player_name} Wins! ')
        second_player_score+=1
    elif int(user_choices) == 3 and second_player_choices == 2 :
        print(f'{user_name}\'s choice was {user_choices_name} and the {second_player_name}\'s choice was {second_player_choices_name}, {user_name} Wins! ') 
        user_score+=1   
    elif second_player_choices == 3 and int(user_choices) == 1 :
        print(f'{user_name}\'s choice was {user_choices_name} and the {second_player_name}\'s choice was {second_player_choices_name}, {user_name} Wins! ') 
        user_score+=1   
    elif second_player_choices == 3 and int(user_choices) == 2 :
        print(f'{user_name}\'s choice was {user_choices_name} and the {second_player_name}\'s choice was {second_player_choices_name}, {second_player_name} Wins! ')  
        second_player_score+=1  
    worksheet.write('A1', 'Player Name') # setting up the header of the excell
    worksheet.write('B1', 'Scores')  
    worksheet.write(row,col, user_name)   # write the first player name
    worksheet.write(row+1,col, second_player_name) # write the sound player name
    worksheet.write(row,col +1, user_score)  # write the current score for player 1
    worksheet.write(row+1,col +1, second_player_score) # # write the current score for player 1

    workbook.close() # must close the file to save
    
    
    #TODO: FINAL: display the results
    print(f'{user_name} score is: {str(user_score)} \n {second_player_name} score is: {str(second_player_score)}')


        

if __name__ == "__main__":
    main()
    