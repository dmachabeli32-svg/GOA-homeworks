from turtle import *
#we want to paint a house 


#step 1: draw a square

width(7)
color("purple")
forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90) 

forward(300)
left(90) 
#end of square

#drawing a door
forward(100)
color("yellow")
begin_fill()
left(90)
forward(150)
right(90)
forward(100)
right(90)
forward(150)
end_fill()

penup()
goto(300,300,)
pendown()


color("red")
begin_fill()
right(150)
forward(300)
left(120)
forward(300)
end_fill()


#drawing windows 
penup()
goto(20,280)
pendown()
left(30)

forward(60)
left(90)

forward(60)
left(90)

forward(60)
left(90)

forward(60)
left(90)
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)

penup()
goto(220,280)
pendown()
forward(60)
right(90)

forward(60)
right(90)

forward(60)
right(90)

forward(60)
right(90)
right(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)



exitonclick()