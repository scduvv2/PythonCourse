import random
computer_choice = random.choice(['rock','paper','scissors'])
user_choice=input('do you want -  rock, paper, scissors?\n')

if computer_choice == user_choice:
  print('TIE -->' + computer_choice)
elif user_choice =='rock' and computer_choice =='scissors':
  print('WIN -->' + computer_choice)
elif user_choice =='paper' and computer_choice =='rock':
  print('WIN -->' + computer_choice)
elif user_choice =='scissors' and computer_choice =='paper':
  print('WIN -->' + computer_choice)
else:
  print('You loose :( Computer wins:D -->' + computer_choice)    
