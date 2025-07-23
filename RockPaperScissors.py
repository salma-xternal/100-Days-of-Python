import random

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


x = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
p = (rock, paper, scissors)
i = random.randint(0, 2)
r = p[i]


# Game

if 0 <= x <= 2:
    print("You chose:")
    print(p[x])           # this prints the correct art for your choice
    print("Computer plays:")
    print(r)
else:
    print("Error! Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")


# Score

if x == 0 and i == 2:
    print("You Win!")
elif x == 2 and i == 1:
    print("You Win!")
elif x == 1 and i == 0:
    print("You Win")
elif x == i:
    print("Draw")
else:
    print("You Lose!")
