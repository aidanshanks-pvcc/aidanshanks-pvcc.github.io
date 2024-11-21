#Name: Aidan Shanks
#Purpose: This program finds the cost of tuition at PVCC
import random

answers=("Yes", "Possibly", "Perchance","Why not", "Indubitably",
         "Think Harder", "Rest","Be more confident"
           "Open your mind to the possibilities","Unlikely"
           "Sources suggest not","Certainly","I believe not"
           "Astrology predicts it to be so","Try again later",
           "Better to not know", "Guess", "Without a doubt")
print("I am the magic 8-ball and can answer any YES or NO question")
another=True
while another:
    solution = random.choice(answers)
    print("\n Shaking the ball now")
    print("...and now...")
    input("\n What is your question?")
    print("The Magic 8 ball says: " + solution)
    again=input("would you like to ask another (Y or N)?")
    if again=="N":
        another=False
print("Come back if you have other important question")
print("*The 8-ball vanishes into nothingness*")