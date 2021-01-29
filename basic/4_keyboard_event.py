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

# 이동 할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
runnung = True  # 게임이 진행중인지 확인하는 변수

while runnung:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnung = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:  # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 케릭터 배치

    pygame.display.update()  # 화면 다시 그리기

# pygame 종료
pygame.quit()
