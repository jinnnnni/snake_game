from turtle import Screen, Turtle  

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
    for seg in segments:
        seg.forward(20)  #거북이 배열이 하나씩 앞으로(오른쪽으로) 20씩 움직임 
        seg.update()
        seg.sleep(1)    #세그먼트가 이동하고 나서 1초 지연이 걸림
            










screen.exitonclick()