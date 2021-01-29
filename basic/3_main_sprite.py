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

# 스프라이트(케릭터) 불러오기
character = pygame.image.load(
    "/Users/sanghoyun/Documents/PYTHON/py_game/pang_project/basic/character.png"
)

character_size = character.get_rect().size  # 이미지 크기를 구해온다.
character_width = character_size[0]  # 케릭터의 가로 크기
character_height = character_size[1]  # 케릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_size[0] / 2)  # 화면 가로 크기의 절반 (중앙)
character_y_pos = screen_height - character_height  # 화면 높이 가장 밑에 위치하도록

# 이벤트 루프
runnung = True  # 게임이 진행중인지 확인하는 변수

while runnung:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnung = False

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 케릭터 배치

    pygame.display.update()  # 화면 다시 그리기

# pygame 종료
pygame.quit()
