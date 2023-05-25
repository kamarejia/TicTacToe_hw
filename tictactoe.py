import pygame
import sys
import math
import random
#grid
"""
(0,0)(0.1)(0,2)
(1,0)(1,1)(1,2)
(2,0)(2,1)(2,2)
"""
pygame.init()
#size
WIDTH, HEIGHT = 640,640 
LINE_WIDTH=5
CIRCLE_WIDTH=5
#color
BLACK=(0,0,0)
WHITE=(255,255,255)

#プレイヤークラス（O）
class Player:
    def __init__(self):
        self.myturn=0
    
    def play(self,events):
        if self.myturn==game.turn:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    grid_width = WIDTH // 3
                    grid_height = HEIGHT // 3
                    mouse_x,mouse_y = pygame.mouse.get_pos()
                    for i in range(3):
                        for j in range(3):
                            if mouse_x>i*grid_width and mouse_x < (i + 1) * grid_width and mouse_y>j*grid_height and mouse_y < (j + 1) * grid_height:
                                game.board[j][i]=1
                                game.turn=1
                    
#NPCクラス（X）
class NPC:
    def __init__(self):
        self.myturn=1
    
    def play(self):
        if self.myturn==game.turn:
            if any(0 in i for i in game.board):
                available_list=[(i,j)for i in range(0,3) for j in range(0,3)if game.board[i][j]==0]
                move=random.choice(available_list)
                game.board[move[0]][move[1]]=-1
                game.turn=0

#ゲームシステムクラス
class GameSystem:
    def __init__(self):
        self.board=[[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        self.turn=0
        self.winlose=0
        
    def draw_gameboard(self):
        for i in range(1,3):
            pygame.draw.line(window, WHITE, (i*WIDTH/3,0), (i*WIDTH/3,HEIGHT), LINE_WIDTH)
            pygame.draw.line(window, WHITE, (0,i*HEIGHT/3), (WIDTH,i*HEIGHT/3), LINE_WIDTH)

    def draw_OX(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j]==1:
                    self.draw_circle((i,j))
                elif self.board[i][j]==-1:
                    self.draw_cross((i,j))

    def draw_circle(self,position):
        pos_x,pos_y=position
        center_x=(2*(pos_y+1)-1)/6*WIDTH
        center_y=(2*(pos_x+1)-1)/6*HEIGHT
        pygame.draw.circle(window,WHITE,(center_x,center_y),17,CIRCLE_WIDTH)

    def draw_cross(self,position):
        length=17
        angle=[45,135,225,315]
        pos_x,pos_y=position
        center_x=(2*(pos_y+1)-1)/6*WIDTH
        center_y=(2*(pos_x+1)-1)/6*HEIGHT
        for angle in angle:
            end_x=center_x + length * math.cos(math.radians(angle))
            end_y=center_y + length*math.sin(math.radians(angle))
            pygame.draw.line(window,WHITE,(center_x,center_y),(end_x,end_y),LINE_WIDTH)

    def judgment(self):
        global flag
        for i in range(0,3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]:
                if self.board[i][0]==1:
                    print("Oの勝ち!")
                    self.winlose=1
                    flag="GAMEEND"
                elif self.board[i][0]==-1:
                    print("Xの勝ち!")
                    self.winlose=-1
                    flag="GAMEEND"
            
            if self.board[0][i]==self.board[1][i]==self.board[2][i]:
                if self.board[0][i]==1:
                    print("Oの勝ち!")
                    self.winlose=1
                    flag="GAMEEND"
                elif self.board[0][i]==-1:
                    print("Xの勝ち!")
                    self.winlose=-1
                    flag="GAMEEND"
        if self.board[0][0]==self.board[1][1]==self.board[2][2]:
                if self.board[0][0]==1:
                    print("Oの勝ち!")
                    self.winlose=1
                    flag="GAMEEND"
                elif self.board[0][0]==-1:
                    print("Xの勝ち!")
                    self.winlose=-1
                    flag="GAMEEND"
        if self.board[0][2]==self.board[1][1]==self.board[2][0]:
                if self.board[0][2]==1:
                    print("Oの勝ち!")
                    self.winlose=1
                    flag="GAMEEND"
                elif self.board[0][2]==-1:
                    print("Xの勝ち!")
                    self.winlose=-1
                    flag="GAMEEND"
        elif not any(0 in i for i in self.board):
            self.winlose=2
            flag="GAMEEND"

    def draw_gameend(self):
        window.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        if game.winlose==1:
            text = font.render("You Win!", True, WHITE)
        elif game.winlose==-1:
            text = font.render("You Lose", True, WHITE)
        elif game.winlose==2:
            text = font.render("Draw", True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = window.get_rect().centerx
        text_rect.centery = window.get_rect().centery
        window.blit(text, text_rect)

#インスタンス
window = pygame.display.set_mode((WIDTH, HEIGHT))
game=GameSystem()
player=Player()
npc=NPC()

#ゲーム
flag="GAME"
while True:
    # イベント処理
    events=pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()  
            sys.exit()  
    
    if flag=="GAME":
        window.fill(BLACK) 
        game.draw_gameboard()
        player.play(events)
        npc.play()
        game.draw_OX()
        game.judgment()
    elif flag=="GAMEEND":
        game.draw_gameend()

    pygame.display.flip()
