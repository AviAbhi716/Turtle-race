import turtle
import random
def no_turtle():
    while True:
        n=int(input("How many turtles you want to race(2-10)"))
        if 2<=n<=10:
            return n
        else:
            print("Input out of range")
turtles=no_turtle()
Width,Height=400,400
s1=turtle.Screen()
s1.setup(400,400)
x_s=Width/(turtles+1)
x=-Width//2
y=-Height//2+10
turtle_list=[]
turtle.colormode(255)
speeds=[1,3,6,10]
for i in range(1,turtles+1):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new=turtle.Turtle()
    new.shape("turtle")
    new.lt(90)
    new.color((r,g,b),(r,g,b))
    new.penup()
    new.goto(x+(i*x_s),y)
    turtle_list.append(new)
def race():
    races = True
    while races:
        for t in turtle_list:
            t.speed(random.choice(speeds))
            t.forward(random.randint(1, 20))
            if t.ycor() >= Height // 2-20:
                print(f"The winner is {t.color()} turtle")
                races = False
                break
race()
s1.exitonclick()
