rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
you_choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
art=[rock, paper, scissors]
print(art[you_choose])
computer_choose=random.randint(0,2)
print(f"Computer chose:\n {art[computer_choose]}\n\n")
if (you_choose==computer_choose==0) or (you_choose==computer_choose==1) or (you_choose==computer_choose==2) :
    print("It\'s Draw!\n\n")
elif (you_choose==0 and computer_choose==1) or (you_choose==2 and computer_choose==1) or (you_choose==0 and computer_choose==2) :
    print(">>>>>----- You Won!-----<<<<<\n\n")
elif  (you_choose==1 and computer_choose==0) or (you_choose==1 and computer_choose==2) or (you_choose==2 and computer_choose==0) :
    print("-----You lose. Computer Won!-----\n\n")
else :
    print("Enter correct option.")