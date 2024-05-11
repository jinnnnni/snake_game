from turtle import Screen, Turtle  
import time
# turtle 은 모듈, Turtle 은 클래스

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #프로그램을 실행에도 아무동작도 하지 않음 (update 메소드를 호출하지 않는 한 화면을 갱신하지 않기 때문에)
starting_position = [(0, 0), (-20, 0), (-40, 0)]
#튜플
segments=[]

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup() #펜을 들지 않으면 밑으로 밑줄이 그어짐    
    new_segment.goto(position)
    segments.append(new_segment) #배열에 담아줌    


game_is_on = True #게임이 동작하는 지 결정

while game_is_on:
    screen.update()    #모든 세그먼트가 이동한 후 화면이 갱신됨
    time.sleep(0.1)    #모든 세그먼트가 이동한 후 시간 지연(좀더 빨라짐 -> 더빠르게 는 0.1로)
    for seg in segments:
        seg.forward(20)  #거북이 배열이 하나씩 앞으로(오른쪽으로) 20씩 움직임 
           
    segments[0].left(20) #거북이의 첫번째 세그먼트를 왼쪽으로 20만큼 돌림










screen.exitonclick()