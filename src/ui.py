from maze import make_maze
import pygame

def visual():
    size_screen = (1600, 900)
    tile_size, maze, (x1, y1), start, end = make_maze(size_screen)

    pygame.init()
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption("Pacman | yel-bakk")
    
    font1 = pygame.font.Font("../font/PAC-FONT.TTF", 150)
    font2 = pygame.font.Font("../font/Gokart Bubble.otf", 50)
    font3 = pygame.font.Font("../font/SoundWaveRacing-Regular.ttf", 70)
    text1 = font1.render("PACMAN", True, (255, 255, 0))
    button_start = pygame.Rect(560, 390, 484, 55)
    button_view = pygame.Rect(455, 500, 697, 55)
    button_instr = pygame.Rect(530, 610, 558, 55)
    button_exit = pygame.Rect(725, 720, 179, 55)
    run = True
    show_maze = False
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos):
                    print("Start Game")
                    show_maze = True
                if button_view.collidepoint(event.pos):
                    print("View Highscores")
                if button_instr.collidepoint(event.pos):
                    print("Instructions")
                if button_exit.collidepoint(event.pos):
                    print("Exit")
                    run = False
        mouse_pos = pygame.mouse.get_pos()
        text2 = font3.render("Start Game", True, (0, 255, 0))
        if button_start.collidepoint(mouse_pos):
            text2 = font3.render("Start Game", True, (0, 255, 255))
        text3 = font3.render("View Highscores", True, (0, 255, 0))
        if button_view.collidepoint(mouse_pos):
            text3 = font3.render("View Highscores", True, (0, 255, 255))
        text4 = font3.render("Instructions", True, (0, 255, 0))
        if button_instr.collidepoint(mouse_pos):
            text4 = font3.render("Instructions", True, (0, 255, 255))
        text5 = font3.render("Exit", True, (0, 255, 0))
        if button_exit.collidepoint(mouse_pos):
            text5 = font3.render("Exit", True, (0, 255, 255))
            
        screen.fill("black")
        if show_maze:
            for row in range(len(maze)):
                for col in range(len(maze[row])):
                    cell = maze[row][col]
                    x = col * tile_size
                    y = row * tile_size
                    if cell & 1:
                        pygame.draw.line(screen, "blue", (x, y), (x + tile_size, y), 2)
                    if cell & 2:
                        pygame.draw.line(screen, "blue", (x + tile_size, y), (x + tile_size, y + tile_size), 2)
                    if cell & 4:
                        pygame.draw.line(screen, "blue", (x, y + tile_size), (x + tile_size, y + tile_size), 2)
                    if cell & 8:
                        pygame.draw.line(screen, "blue", (x, y), (x, y + tile_size), 2)
        else:
            screen.fill((0, 0, 0))
            screen.blit(text1, (385, 120))
            screen.blit(text2, (560, 370))
            screen.blit(text3, (455, 480))
            screen.blit(text4, (530, 590))
            screen.blit(text5, (725, 700))
        pygame.display.flip()
    pygame.quit()

if "__main__" == __name__:
    visual()