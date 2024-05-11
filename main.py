from turtle import Screen, Turtle  
# turtle 은 모듈, Turtle 은 클래스
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #프로그램을 실행에도 아무동작도 하지 않음 (update 메소드를 호출하지 않는 한 화면을 갱신하지 않기 때문에)

snake = Snake() #Snake 클래스의 변수를 만들어줌. (초기화됨)

game_is_on = True #게임이 동작하는 지 결정

while game_is_on:
    screen.update()    #모든 세그먼트가 이동한 후 화면이 갱신됨
    time.sleep(0.1)    #모든 세그먼트가 이동한 후 시간 지연(좀더 빨라짐 -> 더빠르게 는 0.1로)
    snake.move()
    







screen.exitonclick()