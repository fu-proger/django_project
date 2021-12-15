import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг x')
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    running = True
    x_pos = 0
    v = 3200  # пикселей в секунду
    clock = pygame.time.Clock()
    fps = 60  # количество кадров в секунду
    running = True
    color = (255, 0, 0)
    r = 1.0
    screen.fill((255, 0, 0))
    while running:
        #screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, color, event.pos, int(r))
                r += 0.1
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                color = (0, 255, 0)
            if event.type == pygame.MOUSEBUTTONUP:
                color = (255, 0, 0)
        pygame.display.flip()
        clock.tick(fps)