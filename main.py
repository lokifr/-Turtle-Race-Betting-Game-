import turtle
from turtle import Turtle, Screen
import random
#Tom = Turtle()
from turtle import Turtle, Screen
import random

colors = ['red', 'green', 'blue', 'purple', 'violet', 'indigo']
ypos = [-70, -40, -10, 10, 40, 70]  # Corrected y-positions
all_turtle = []

sc = Screen()
sc.setup(500, 400)
user_bet = sc.textinput(title='Bet on a turtle', prompt='Which turtle will win the race? Enter a color:')

print(user_bet)

# Create turtles before starting the race
for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=ypos[i])
    all_turtle.append(new_turtle)

race_on = False
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        dist = random.randint(0,10)
        turtle.forward(dist)
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Youve won with {winning_color} color turtle. ")

            else:
                print(f"Sorry, the {winning_color} turtle has won. Better luck next time!")





sc.exitonclick()
