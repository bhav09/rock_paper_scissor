# game of rock paper scissor

import random

choice=['rock','scissor','paper']


def game():
    game_is_still_going=True
    while game_is_still_going==True:
        
        player_input=input('Your turn:')
        pc=random.choice(choice)
        if pc==player_input:
            print('Tie')
            game()
            
        elif pc=='rock' and player_input=='scissor' or pc=='paper' and player_input=='rock' or pc=='scissor' and player_input=='paper':
            print('Random_Output was:',pc)
            print('PC won')
            
            play_again=input('Want to play again?(y/n)')
            if play_again=='y' or play_again=='Y':
                game()
            else :
                game_is_still_going=False
                
        elif  player_input=='rock' and pc=='scissor' or player_input=='paper' and pc=='rock' or player_input=='scissor' and pc=='paper':
            print('Random_Output was:',pc)
            print('Player won')
            play_again=input('Want to play again?(y/n)')
            if play_again=='y' or play_again=='Y':
                game()
            else :
                print('Game over')
                game_is_still_going=False
game()