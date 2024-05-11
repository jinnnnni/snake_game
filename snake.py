from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)] #상수는 대문자로
MOVE_DISTANCE = 20
class Snake: 

    def __init__(self):
        #class 호출될 때 초기화하면서 할 작동
        self.segments=[] #클래스 안에서 쓸때는 self 를 써줘야 함
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup() #펜을 들지 않으면 밑으로 밑줄이 그어짐    
            new_segment.goto(position)
            self.segments.append(new_segment) #배열에 담아줌    

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): #range() 함수는 순수함수가 아니기 때문에 키워드 인자를 넣으면 에러가 남
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # 세번째 세그먼트를 두번째 위치로 보낼거기 떄문에 두번째 세그먼트의 위치좌표를 구해줌
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
        self.segments[0].left(90)