from turtle import *

edge = 20
angle = 15
i = 0

#head

fillcolor('brown')
begin_fill()

while i < 360/angle:
    forward(edge)
    left(angle)
    i  = i + 1

end_fill()

#eyes

forward(10)
left(90)
penup()
forward(120)
left(90)
forward(40)
pendown()
fillcolor('white')
begin_fill()
circle(10)
end_fill()
left(90)
penup()
forward(8)
fillcolor('black')
begin_fill()
circle(4)
end_fill()
right(180)
forward(8)
right(90)
forward(80)
left(180)
pendown()
fillcolor('white')
begin_fill()
circle(10)
end_fill()
left(90)
penup()
forward(8)
fillcolor('black')
begin_fill()
circle(4)
end_fill()
penup()
right(90)
forward(40)
left(90)
forward(112)



# #body
pendown()
forward(20)
left(90)
forward(60)
right(180)
forward(120)
right(180)
forward(60)
right(90)
forward(50)
left(45)
forward(85)
right(180)
forward(85)
left(90)
forward(85)

done()
