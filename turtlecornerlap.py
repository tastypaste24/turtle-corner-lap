import turtle
import random
t=turtle.Pen()
t.pencolor("black")
turtle.title("The Turtle Lap")
turtle.bgcolor("green")
#player one setup
player_one=turtle.Turtle()
player_one.color("black")
player_one.shape("turtle")
player_one.pencolor("black")
player_one.pensize(5)
#Track setup
player_one.penup()
player_one.goto(-200,-200)
player_one.pendown()
player_one.fd(400)
player_one.lt(90)
player_one.stamp()
player_one.fd(400)
player_one.stamp()
player_one.lt(90)
player_one.fd(400)
player_one.lt(90)
player_one.fd(400)
player_one.color("red")
player_one.penup()
#player two setup
player_two=player_one.clone()
player_two.color("blue")
player_two.shape("turtle")
player_two.pencolor("black")
player_two.penup()
player_two.goto(180,-200)
player_two.rt(90)
player_one.goto(180,-200)
player_one.rt(90)
die=[1,2,3,4,5,6]
#direction instructions
for i in range(20):
    if player_one.pos()>=(200,-200):
        player_one.goto(200,-200)
        player_one.lt(90)
        player_one.fd(10)
    elif player_one.pos()>=(200,200):
        player_one.goto(200,200)
        player_one.lt(90)
        player_one.fd(10)
    elif player_one.pos()<=(-200,200):
        player_one.goto(-200,200)
        player_one.lt(90)
        player_one.fd(10)
    #player one finish line
    elif player_one.pos()>=(185,200):
        print("Raphael wins!")
        print("FLAWLESS VICTORY!")
        break
    elif player_two.pos()>=(200,-200):
        player_two.goto(200,-200)
        player_two.lt(90)
        player_two.fd(10)
    elif player_two.pos()>=(200,200):
        player_two.goto(200,200)
        player_two.lt(90)
        player_two.fd(10)
    elif player_two.pos()<=(-200,200):
        player_two.goto(-200,200)
        player_two.lt(90)
        player_two.fd(10)
    #player two finish line
    elif player_two.pos()>=(185,200):
        print("Leonardo wins!")
        print("FLAWLESS VICTORY!")
        break
    #main game loop
    else:
        player_one_turn=input("Press 'Enter' to roll the die")
        die_outcome=random.choice(die)
        print("The result of the die roll is:")
        print(die_outcome)
        print("The number of steps will be:")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        player_two_turn=input("Press 'Enter' to roll the die")
        die_outcome=random.choice(die)
        print("The result of thr die roll is:")
        print(die_outcome)
        print("The number of steps will be:")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)
