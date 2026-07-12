from maze import make_maze
import pygame
import random




def visual():
    size_screen = (1600, 900)
    tile_size, maze, (x1, y1), start, end = make_maze(size_screen)
    pacgums = [[random.random() < 0.5 for _ in row] for row in maze]
    pacgums[start[1]][start[0]] = False
    pacgums[end[1]][end[0]] = False
    pygame.init()
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption("Pacman | yel-bakk")
    score = 0
    power = 0
    font1 = pygame.font.Font("font/PAC-FONT.TTF", 150)
    font2 = pygame.font.Font("font/Gokart Bubble.otf", 20)
    font3 = pygame.font.Font("font/SoundWaveRacing-Regular.ttf", 70)
    text1 = font1.render("PACMAN", True, (255, 255, 0))
    button_start = pygame.Rect(560, 390, 484, 55)
    button_view = pygame.Rect(455, 500, 697, 55)
    button_instr = pygame.Rect(530, 610, 558, 55)
    button_exit = pygame.Rect(725, 720, 179, 55)
    pacman_1 = pygame.image.load("image/right_pacman.png")
    pacman_1 = pygame.transform.scale(pacman_1, (tile_size - 4, tile_size - 4))
    pacman_2 = pygame.image.load("image/down_pacman.png")
    pacman_2 = pygame.transform.scale(pacman_2, (tile_size - 4, tile_size - 4))
    pacman_3 = pygame.image.load("image/north_pacman.png")
    pacman_3 = pygame.transform.scale(pacman_3, (tile_size - 4, tile_size - 4))
    pacman_4 = pygame.image.load("image/above_pacman.png")
    pacman_4 = pygame.transform.scale(pacman_4, (tile_size - 4, tile_size - 4))
    ora_ghost = pygame.image.load("image/orange_ghost.png")
    ora_ghost = pygame.transform.scale(ora_ghost, (tile_size - 4, tile_size - 4))
    pink_ghost = pygame.image.load("image/pink_ghost.png")
    pink_ghost = pygame.transform.scale(pink_ghost, (tile_size - 4, tile_size - 4))
    red_ghost = pygame.image.load("image/red_ghost.png")
    red_ghost = pygame.transform.scale(red_ghost, (tile_size - 4, tile_size - 4))
    blue_ghost = pygame.image.load("image/blue_ghost.png")
    blue_ghost = pygame.transform.scale(blue_ghost, (tile_size - 4, tile_size - 4))
    
    p = [True, False, False, False]
    pacman_col, pacman_row = end
    pacman_col = pacman_col // 2
    pacman_row = pacman_row // 2
    run = True
    show_maze = False
    ft_small = [
        [1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
    ]
    
    posy = (len(maze) - len(ft_small)) // 2
    posx = (len(maze[0]) - len(ft_small[0])) // 2

    def is_42(row, col):
        if not (posy <= row < posy + len(ft_small)):
            return False
        if not (posx <= col < posx + len(ft_small[0])):
            return False
        return ft_small[row - posy][col - posx] == 1
    power_pellets = [(0, 0), (len(maze[0]) - 1, 0),
                     (0, len(maze) - 1),
                     (len(maze[0]) - 1, len(maze) - 1)]

    # ghosts = [(1, 1),
    #           (len(maze[0]) - 2, 1),
    #           (1, len(maze) - 2),
    #           (len(maze[0] - 2, len(maze) - 1))]
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
            if event.type == pygame.KEYDOWN and show_maze:
                cell = maze[pacman_row][pacman_col]
                if event.key == pygame.K_UP and not (cell & 1):
                    pacman_row -= 1
                    p = [False, False, False, True]
                    print("UP")
                elif event.key == pygame.K_RIGHT and not (cell & 2):
                    pacman_col += 1
                    p = [True, False, False, False]
                    print("RIGHT")
                elif event.key == pygame.K_DOWN and not (cell & 4):
                    pacman_row += 1
                    p = [False, True, False, False]
                    print("DOWN")
                elif event.key == pygame.K_LEFT and not (cell & 8):
                    pacman_col -= 1
                    p = [False, False, True, False]
                    print("LEFT")
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
                    if is_42(row, col):
                        pygame.draw.rect(screen, (0, 180, 0), (x, y, tile_size, tile_size))
                    if cell & 1:
                        pygame.draw.line(screen, "blue", (x, y), (x + tile_size, y), 2)
                    if cell & 2:
                        pygame.draw.line(screen, "blue", (x + tile_size, y), (x + tile_size, y + tile_size), 2)
                    if cell & 4:
                        pygame.draw.line(screen, "blue", (x, y + tile_size), (x + tile_size, y + tile_size), 2)
                    if cell & 8:
                        pygame.draw.line(screen, "blue", (x, y), (x, y + tile_size), 2)
                for col, row in power_pellets:
                    pygame.draw.circle(screen, (255, 255, 255),
                                        (col * tile_size + tile_size // 2,
                                        row * tile_size + tile_size // 2), 8)




            for row in range(len(maze)):
                for col in range(len(maze[row])):
                    if pacgums[row][col] and not is_42(row, col):
                        pygame.draw.circle(
                            screen, (255, 255, 255),
                            (col * tile_size + tile_size // 2, row * tile_size + tile_size // 2), 3)

            if p[0]:
                screen.blit(pacman_1, (pacman_col * tile_size + 2, pacman_row * tile_size + 2))
            if p[1]:
                screen.blit(pacman_2, (pacman_col * tile_size + 2, pacman_row * tile_size + 2))
            if p[2]:
                screen.blit(pacman_3, (pacman_col * tile_size + 2, pacman_row * tile_size + 2))
            if p[3]:
                screen.blit(pacman_4, (pacman_col * tile_size + 2, pacman_row * tile_size + 2))
            screen.blit(blue_ghost, (1 * tile_size, 1 * tile_size))
            screen.blit(ora_ghost, ((len(maze[0]) - 2) * tile_size, 1 * tile_size))
            screen.blit(pink_ghost, (1 * tile_size, (len(maze) - 2) * tile_size))
            screen.blit(red_ghost, ((len(maze[0]) - 2) * tile_size, (len(maze) - 2) * tile_size))
            if pacgums[pacman_row][pacman_col]:
                pacgums[pacman_row][pacman_col] = False
                score += 1
            text_score = font2.render(f"Score: {score}", True, (0, 255, 255))
            screen.blit(text_score, (1450, 50))
            if (pacman_col, pacman_row) in power_pellets:
                power_pellets.remove((pacman_col, pacman_row))
                power += 1
            text_power = font2.render(f"Power: {power}", True, (0, 255, 255))
            screen.blit(text_power, (1450, 70))
                
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