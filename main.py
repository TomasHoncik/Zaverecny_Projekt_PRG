import pygame
import pygame_gui

img = pygame.image.load("assets/character.png")


pygame.init()
pygame.display.set_caption("CUBIQ")
pygame.display.set_icon(img)

SCREEN_WIDTH = 700  # 14
SCREEN_HEIGHT = 350  # 10
SQUARE_SIZE = 50

img = pygame.image.load("assets/character.png")
character = pygame.transform.scale(img, (50, 50))
character_rect = character.get_rect()
character_rect.x = 50
character_rect.y = 350

global game_state
game_state = "menu"
global level_counter
level_counter = 0
global game_score
game_score = 0
last_edge_touched = None
font = pygame.font.SysFont("Arial",30)

info_list = []
world_data = [
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
]

level_2 = [
    [3,0,0,0,0,0,0,3,0,0,0,0,0,0],
    [0,0,0,3,0,0,0,0,0,3,0,2,0,0],
    [0,0,0,0,0,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,2,0,0,0,0,0,3,0,2,0],
    [0,2,0,0,0,0,3,0,2,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,3,0,0],
]

level_3 = [
    [0,0,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,3,0,0,0,0,0,0,0,0,1,0,3,0],
    [1,1,1,1,1,1,1,1,1,0,1,0,0,0],
    [1,1,0,1,0,1,0,1,1,0,1,2,0,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,0,3,3,2,3,2,3,2,3,0,3,0,0],

]

level_4 = [
    [0,1,0,0,0,0,0,0,0,2,0,1,3,0],
    [0,0,0,0,0,2,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,2,0,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,0,0,2,0,0,0,1,0,0],
    [0,1,0,0,2,0,0,0,0,2,0,3,0,0],
    [0,1,0,0,0,0,3,0,0,0,0,0,2,2],
]

points = [[650,100,50,50],[150,50,50,50],[0,0,50,50],[300,200,50,50],[500,150,50,50],[350,0,50,50], [450,50,50,50],[500,150,50,50],
          [100,300,50,50],[0,300,50,50],[150,300,50,50], [250,300,50,50],[450,300,50,50],[550,300,50,50],[50,50,50,50],[600,50,50,50],
          [300,300,50,50],[450,150,50,50],[600,0,50,50]
          ]




clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

UI_MANAGER = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
LOST_MANAGER = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

menu_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((200, 120), (275, 80)),
    text='Hrát',
    manager=UI_MANAGER
)

menu_text = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((200, 80), (278, 50)),
    text="Klikni a zahraj!",
    manager=UI_MANAGER
)

lost_text = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((200, 80), (278, 50)),
    text="Bohužel jsi prohrál",
    manager= UI_MANAGER
)

lost_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((200, 120), (275, 80)),
    text='Hrát znovu',
    manager= UI_MANAGER
)

won_text = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((200, 80), (278, 50)),
    text="Vyhrál jsi gratuluji!",
    manager= UI_MANAGER
)

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))





def draw_grid():
    for line in range(0, 14):
        pygame.draw.line(screen, (255, 255, 255), (0, line * SQUARE_SIZE), (SCREEN_WIDTH, line * SQUARE_SIZE))
        pygame.draw.line(screen, (255, 255, 255), (line * SQUARE_SIZE, 0), (line * SQUARE_SIZE, SCREEN_HEIGHT))

def square_position(position):
    global info_list
    info_list = [] 
    row_count = 0
    for row in position:
        col_count = 0
        for square in row:
            if square == 1:
                border = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
                border.x = col_count * SQUARE_SIZE
                border.y = row_count * SQUARE_SIZE
                color = (0, 0, 0)
                info = (border, color)
                info_list.append(info)
            elif square == 2:
                border = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
                border.x = col_count * SQUARE_SIZE
                border.y = row_count * SQUARE_SIZE
                color = (1, 50, 32)
                info = (border, color)
                info_list.append(info)
            elif square == 3:
                border = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
                border.x = col_count * SQUARE_SIZE
                border.y = row_count * SQUARE_SIZE
                color = (144, 238, 144)
                info = (border, color)
                info_list.append(info)
            col_count += 1
        row_count += 1
    return info_list


def draw_square(level_number):
    if level_number == 0:
        for info in square_position(world_data):
            square_info, square_color = info
            pygame.draw.rect(screen, square_color, square_info)
    elif level_number == 1:
        for info in square_position(level_2):
            square_info, square_color = info
            pygame.draw.rect(screen, square_color, square_info)
    elif level_number == 2:
        for info in square_position(level_3):
            square_info, square_color = info
            pygame.draw.rect(screen, square_color, square_info)
    elif level_number == 3:
        for info in square_position(level_4):
            square_info, square_color = info
            pygame.draw.rect(screen, square_color, square_info)

def update_player():
    global game_state, game_score, level_counter, last_edge_touched, square_touched
    jumped = False
    jump_height = 0
    x_difference = 0
    y_difference = 0

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and not jumped:
        jump_height = -12
        jumped = True
    if not key[pygame.K_SPACE]:
        jumped = False
    if key[pygame.K_a]:
        x_difference -= 5
    if key[pygame.K_d]:
        x_difference += 5

    jump_height += 2  
    if jump_height > 10:
        jump_height = 10
    y_difference += jump_height

    for square in info_list:
        if square[0].colliderect(character_rect.x + x_difference, character_rect.y, 50, 50):
            if square[1] == (1, 50, 32):  # Dark green
                game_state = "lost"
            elif square[1] == (144, 238, 144): # light green
                if list(square[0]) in points:
                    game_score += 1
                    points.remove(list(square[0]))




            x_difference = 0

        if square[0].colliderect(character_rect.x, character_rect.y + y_difference, 50, 50):
            if jump_height < 0:  # Jumping up
                if square[1] == (1, 50, 32):
                    game_state = "lost"
                elif square[1] == (144, 238, 144):
                    if list(square[0]) in points:
                        game_score += 1
                        points.remove(list(square[0]))

                y_difference = square[0].bottom - character_rect.top
                jump_height = 0
            elif jump_height >= 0:  # Falling down
                if square[1] == (1, 50, 32):
                    game_state = "lost"
                if square[1] == (144,238,144):
                    if list(square[0]) in points:
                        game_score += 1
                        points.remove(list(square[0]))
                y_difference = square[0].top - character_rect.bottom
                jump_height = 0

    character_rect.x += x_difference
    character_rect.y += y_difference

    if character_rect.right >= SCREEN_WIDTH:
        if level_counter == 3:  
            game_state = "end" 
        else:
            last_edge_touched = "right"
            level_counter += 1
            character_rect.x = 50
            character_rect.y = 350

    if character_rect.left <= 0:
        if level_counter > 0:  
            level_counter -= 1  
            character_rect.x = SCREEN_WIDTH - 50 
            character_rect.y = 350
            last_edge_touched = "left"

    if character_rect.bottom > SCREEN_HEIGHT:
        character_rect.bottom = SCREEN_HEIGHT
        y_difference = 0




def draw_player():
    screen.blit(character, character_rect)

jumped = False
jump_height = 0

run = True
while run:
    time_delta = clock.tick(60) / 1000
    screen.fill((160, 244, 219))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == menu_button:
                game_state = "game"
                lost_button.visible = False
                lost_text.visible = False
                won_text.visible = False
                level_counter = 0
            if event.ui_element == lost_button:
                game_state = "game"

        UI_MANAGER.process_events(event)

    if game_state == "game":
        draw_grid()
        draw_square(level_counter)
        update_player()
        draw_text(f"{game_score} X",font, (255,255,255),0,0)
        draw_player()

    if game_state == "lost":
        points = [[650,100,50,50],[150,50,50,50],[0,0,50,50],[300,200,50,50],[500,150,50,50],[350,0,50,50], [450,50,50,50],[500,150,50,50],[100,300,50,50],[0,300,50,50],[150,300,50,50], [250,300,50,50],[450,300,50,50],[550,300,50,50],[50,50,50,50],[600,50,50,50],[300,300,50,50],[450,150,50,50],[600,0,50,50]]
        level_counter = 0
        game_score = 0
        lost_button.visible = True
        lost_text.visible = True
        menu_button.visible = False
        menu_text.visible = False
        won_text.visible = False    
        UI_MANAGER.draw_ui(screen)
        character_rect.x = 50
        character_rect.y = 350

    if game_state == "menu":
        UI_MANAGER.draw_ui(screen)
        lost_button.visible = False
        lost_text.visible = False
        won_text.visible = False   
    if game_state == "end":
        if game_score >= 18:
            won_text.visible = True
            menu_button.visible = False
            menu_text.visible = False



            UI_MANAGER.draw_ui(screen)
        else:
            menu_text.visible = False
            menu_button.visible = False
            lost_text.visible = True
            lost_button.visible = False

            UI_MANAGER.draw_ui(screen)


    UI_MANAGER.update(time_delta)
    pygame.display.update()

pygame.quit()
