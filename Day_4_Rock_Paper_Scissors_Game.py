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

stop = '''
   __
 /    \
| STOP |
 \ __ /
   ||
   ||
 ~~~~~~
'''
#Write your code below this line 👇


my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

hand_options = [rock, paper, scissors]
num_hand_options = len(hand_options)

# find user selection and print on screen
print("Your chose: ")
for i in range (num_hand_options):
  if my_choice == i:
    print(hand_options[i])


# create pc selection and print out on screen 

if my_choice<0 or my_choice>=3:
  print(f"You typed invalid number,you lose!\n{stop}")
else:
    pc_choice = random.randint(0,2)
    print("Computer chose: ")
    if pc_choice == 0:
        print(hand_options[pc_choice])
    
    elif pc_choice == 1:
        print(hand_options[pc_choice])
    
    else: 
        print(hand_options[pc_choice])
    # control of the conditions of the game rules👇
    # game rules👇
    # Rock  - 0wins against scissors.
    # Scissors -2 win against paper.
    # Paper wins-1 against rock.

    if my_choice == pc_choice:
        print("You are same")
    elif my_choice == 0 and pc_choice == 1:
        print("you lose")
    elif my_choice == 0 and pc_choice == 2:
        print("you win")
    elif my_choice == 1 and pc_choice == 0:
        print("you win")
    elif my_choice == 1 and pc_choice == 2:
        print("you lose")
    elif my_choice == 2 and pc_choice == 0:
        print("you lose")
    elif my_choice == 2 and pc_choice == 1:
        print("you win")




  