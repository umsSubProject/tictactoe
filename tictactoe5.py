from multiprocessing.dummy import current_process
from collections import Counter

import pygame # 1. pygame 선언

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

pygame.display.set_caption("tic-tac-toe")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ttt_size = int(input("게임 판 사이즈 입력(3~9) : "))
gap = 100
viewer_size = ttt_size * gap
size = [viewer_size, viewer_size]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

row_index = None
col_index = None
position = ["",""]
turn = 0
x = None
y = None
stack_position = []
stack_a = []
stack_b = []
a = []
b = []
c = []
d = []

def draw_line():
    #가로줄, 세로줄
    for i in range(ttt_size + 1):
        next_pos = i * gap
        pygame.draw.line(screen, BLACK, (0, next_pos), (ttt_size * gap, next_pos),2)
        pygame.draw.line(screen, BLACK, (next_pos, 0), (next_pos, ttt_size * gap),2)
        
# def win(stack):
#     for i in range(len(stack)):
#         a.append(stack[i][0])
#         b.append(stack[i][1])
#         print(a)
#         print(b)
        
        
# 4. pygame 무한루프
def runGame():
    global done, row_index, col_index, position, turn, x, y, stack_position, stack_a, stack_b , a, b ,c, d
    screen.fill(WHITE)
    print("시작 : ○\na행 좌표 : a~i\n열 좌표: 0~9")
    while not done:
        clock.tick(10)
        draw_line()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #윈도우 x 버튼을 눌렀을 때
                done=True
            
            elif event.type == pygame.KEYUP: #키보드 키가 올라갔을 때
                print(chr(event.key)) # 현재 누를 키값 터미널에 출력
                if 96 < event.key < 106: # a~i
                    row_index = chr(event.key) # a~i 값 중 눌린 값 저장
                    position[0] = row_index
                    print(f"{position}\n위치가 맞으면 Enter!")
                elif 47 < event.key < 58: # 0~9
                    col_index = chr(event.key) # 0~9 값 중 눌린 값 저장
                    position[1] = col_index
                    print(f"{position}\n위치가 맞으면 Enter!")
                if event.key == 13:
                    if position[0:2] in stack_position:
                        print("중복위치")
                    else:
                        stack_position.append(position[0:2])
                        print(f"position : {position}")
                        print(f"stack_position : {stack_position}")
                        print(len(stack_position))
                        # a = set([tuple(set(i)) for i in stack_position])
                        # print(a)
                        
                        if position[0] == "a":
                            y = 50
                            if position[1] == "0":
                                x = 50
                            elif position[1] == "1":
                                x = 150
                            elif position[1] == "2":
                                x = 250
                        elif position[0] == "b":
                            y = 150
                            if position[1] == "0":
                                x = 50
                            elif position[1] == "1":
                                x = 150
                            elif position[1] == "2":
                                x = 250
                        elif position[0] == "c":
                            y = 250
                            if position[1] == "0":
                                x = 50
                            elif position[1] == "1":
                                x = 150
                            elif position[1] == "2":
                                x = 250
                        if turn == 0:
                            pygame.draw.circle(screen, BLACK, (x,y),30,3)
                            stack_a.append(position[0:2])
                            print(f"stack_a : {stack_a}")
                            for i in range(len(stack_a)):
                                a.append(stack_a[i][0])
                                b.append(stack_a[i][1])
                            print(a)
                            print(b)
                            # win(stack_a,a,b)
                            # for i in range(len(stack_a)):
                            #     print(a.append(stack_a[i][0]))
                            #     print(stack_a[i][1])
                            turn += 1
                            turn = turn % 2
                            print("현재턴 : ●")
                        else:
                            pygame.draw.circle(screen,BLACK, (x,y),30)
                            stack_b.append(position[0:2])
                            print(f"stack_b : {stack_b}")
                            for i in range(len(stack_b)):
                                c.append(stack_b[i][0])
                                d.append(stack_b[i][1])
                            print(c)
                            print(d)
                            # win(stack_b,c,d)
                            turn += 1
                            turn = turn % 2
                            print("현재턴 : ○")
                
        # if row_index =="a":
        #     pygame.draw.circle(screen,BLACK, (50,50),30,3)
        # elif row_index == "b":
        #     pygame.draw.circle(screen,BLACK, (150,150),30)
            
        ############################
        # 여기에 도형을 그리세요
        ############################        
        
        
        pygame.display.update()

runGame()
pygame.quit()