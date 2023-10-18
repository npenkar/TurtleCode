from pickle import FALSE, TRUE
import turtle
import time

window = turtle.Screen()
window.bgcolor("black")
window.title("Seracle Logo")
st = turtle.Turtle()

time.sleep(3)

st.setpos(-325,100)
st.color("white")
st.speed(6)
st.width(5)
st.hideturtle()

#1st sqr
st.forward(615)
st.color("white")
st.left(135)
st.forward(400)
st.left(90)
st.forward(400)
st.left(90)
st.forward(400)
st.left(90)
st.forward(400)

#2nd sqr
st.left(135)
st.forward(50)
st.right(45)
st.forward(400)
st.left(90)
st.forward(400)
st.left(90)
st.forward(400)
st.left(90)
st.forward(400)

st.speed(5)

#3rd sqr
st.left(135)
st.forward(52)
st.right(45)
st.forward(200)
st.left(90)
st.forward(200)
st.left(90)
st.forward(200)
st.left(90)
st.forward(200)

# extra
# st.forward(-55)
# st.right(90)
# st.color("blue")
# st.forward(-55)


#4th sqr
st.backward(45)
st.left(90)
st.forward(1)
st.color("blue")
st.forward(44)
st.color("white")
st.forward(200)
st.color("blue")
st.forward(119)
st.forward(-119)
st.color("white")
st.left(90)
st.forward(200)
st.left(90)
st.forward(200) #extra
st.color("red")
st.forward(115)
st.forward(-115)
st.color("white")
st.left(90)
st.forward(200)
st.color("red")
st.forward(44)
st.forward(-44)
st.color("white")


# # #5th sqr
st.left(135)
st.forward(62.5)
st.right(45)
st.forward(200)
st.left(90)
st.forward(200)
st.color("blue")
st.forward(38.5)
st.color("white")
st.right(90)
st.forward(38.5)
st.right(90)
st.forward(38.5)
st.right(90)
st.color("red")
st.forward(40)
st.color("white")
st.forward(200)
st.left(90)
st.forward(201)

st.speed(4)

# #6th lines
st.left(135)
st.forward(339.1)
st.right(135)
st.forward(200)
st.right(90)
st.forward(1)
st.color("blue")
st.forward(199)
st.right(90)
st.color("red")
st.forward(1)
st.forward(199)

# # 7th line
st.color("white")
st.left(90)
st.forward(165)
st.left(90)
st.forward(365)
st.left(90)
st.forward(200)
st.left(90)
st.forward(1)
st.color("red")
st.forward(199)
st.left(90)
st.color("blue")
st.forward(200)

st.speed(3)

# # 8th green line 
st.color("white")
st.right(90)
st.forward(200)
st.right(90)
st.forward(400)
st.right(135)
st.color("green")
# st.forward(-1)
st.forward(615)
st.color("white")
st.forward(3)


st.speed(0)
# # logo text
st.color("black")
st.forward(10)
st.right(90)
st.forward(400)
st.right(90)
st.forward(310)
st.color("#5a80fb")

st.speed(1)

st.write("Seracle", move= TRUE, align='center', font=("Montserrat", 100,  "italic"))

turtle.exitonclick()
turtle.done()