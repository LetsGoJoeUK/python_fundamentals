import random
computer_choice = random.choice(['rock','paper','scissors'])
user_choice = input('rock, paper or scissors\n')

print('Computer choice',computer_choice)
if computer_choice==user_choice:
    print('TIE')
elif user_choice=='rock' and computer_choice=='scissors':
    print('YOU WIN! Computer had : ' + str({computer_choice}))
elif user_choice=='paper' and computer_choice=='rock':
    print('YOU WIN!')
elif user_choice=='scissors' and computer_choice=='paper':
    print('YOU WIN!')
else:
    print('You LOSE, computer wins :)')
