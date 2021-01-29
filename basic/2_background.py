import pygame

pygame.init()  # 초기화 - 반드시 필요

# 화면 크기 설정
screen_width = 640
screen_height = 860

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("4LEAF Game")

# 배경 이미지 설정

background = pygame.image.load(
    "/Users/sanghoyun/Documents/PYTHON/py_game/pang_project/basic/background.png"
)

# 이벤트 루프
runnung = True  # 게임이 진행중인지 확인하는 변수

while runnung:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnung = False

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))  # 배경 그리기
    pygame.display.update()  # 화면 다시 그리기

# pygame 종료
pygame.quit()
