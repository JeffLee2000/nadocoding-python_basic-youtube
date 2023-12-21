import pygame
from random import *
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
                                 
# 화면 타이틀 설정
pygame.display.set_caption("게임 이름") # 게임 이름

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
class Character():
    def __init__(self, character, screen_width, screen_height):
        self.character = character
        self.speed = 0.6
        self.rect = self.character.get_rect()
        self.size = self.character.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = (screen_width / 2) - (self.width / 2)
        self.y_pos = screen_height - self.height
    def update_rect(self):
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos
class Ddong():
    def __init__(self, ddong, screen_width, screen_height):
        self.ddong = ddong
        self.speed = 0.3
        self.rect = self.ddong.get_rect()
        self.size = self.ddong.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = randint(self.width, 480) - self.width
        self.y_pos = 0
    def update_rect(self):
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos
        
bakcground = pygame.image.load("C:\\Users\\lnb20\\OneDrive\\바탕 화면\\이태호\\Programming\\vscode-wrokspace\\pygame_basic\\background.png")
character = Character(pygame.image.load("C:\\Users\\lnb20\\OneDrive\\바탕 화면\\이태호\\Programming\\vscode-wrokspace\\pygame_basic\\character.png"), screen_width, screen_height)
ddong = Ddong(pygame.image.load("C:\\Users\\lnb20\\OneDrive\\바탕 화면\\이태호\\Programming\\vscode-wrokspace\\pygame_basic\\enemy.png"), screen_width, screen_height)

# 캐릭터가 이동할 좌표
ch_to_x = 0
# 똥이 이동할 좌표
dd_to_y = ddong.speed
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # fps 설정
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
            
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                ch_to_x -= character.speed
            elif event.key == pygame.K_RIGHT:
                ch_to_x += character.speed
            
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ch_to_x = 0
                
    # 3. 게임 캐릭터, 똥 위치 정의
    character.x_pos += ch_to_x * dt
    ddong.y_pos += dd_to_y * dt
    
    # 캐릭터 가로 경계값 처리
    if character.x_pos < 0:
        character.x_pos = 0
    elif character.x_pos > screen_width - character.width:
        character.x_pos = screen_width - character.width
        
    # 똥 세로 경계값 처리
    if ddong.y_pos > screen_height:
        ddong.y_pos = -200
        ddong.x_pos = randint(ddong.width, 480) - ddong.width
    
    # 4. 충돌 처리
    character.update_rect()
    ddong.update_rect()
    if character.rect.colliderect(ddong.rect):
        running = False
        print("충돌했어요")
        pygame.time.delay(1000)
        continue
    
    # 5. 화면에 그리기

    screen.blit(bakcground, (0, 0))
    
    screen.blit(character.character, (character.x_pos, character.y_pos))
    
    screen.blit(ddong.ddong, (ddong.x_pos, ddong.y_pos))
    
    pygame.display.update() # 게임 화면을 다시 그리기

# pygame 종료
pygame.quit()