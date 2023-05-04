from art import logo
from art import vs
from data import data
import random

print(logo)
print(" ")
print("Guess who has more followers on instagram \n")
DATA_LENGTH=len(data)

still_playing=True

points=0

while still_playing==True:

    random_picker1=random.randint(0,DATA_LENGTH-1)
    nomulti=False

    while nomulti==False:
        random_picker2=random.randint(0,DATA_LENGTH-1)

        if random_picker2 != random_picker1:
            nomulti=True

    print(f"{data[random_picker1]['name']} from {data[random_picker1]['country']} is {data[random_picker1]['description']}")
    print(vs)
    print(f"{data[random_picker2]['name']} from {data[random_picker2]['country']} is {data[random_picker2]['description']}. \n")
    print("Type A for first one or B for the 2nd one")

    Guess=input()

    A=int(data[random_picker1]['follower_count'])
    B=int(data[random_picker2]['follower_count'])

    if (Guess =="A" and A>B) or (Guess == "B" and B>A):
        points+=1
    else:
        print("You lose")
        still_playing=False

    print(f"Points: {points} \n")
    print(f"{data[random_picker1]['name']}:{data[random_picker1]['follower_count']}")
    print(f"{data[random_picker2]['name']}:{data[random_picker2]['follower_count']} \n")
