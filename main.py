from turtle import Screen, Turtle  

# turtle 은 모듈, Turtle 은 클래스

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


segment_1 = Turtle(shape="square")
segment_1.color("white")
#거북이 만들 때 모양 명시할 수 있음

segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(-20, 0)
#두번째, 세번째 거북이의 좌표는 -20 씩 옆으로 이동해야함.

segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(-40, 0)














screen.exitonclick()