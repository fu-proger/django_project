import random
import pygame

class Snake:
    def __init__(self, id: int) -> None:
        self.id = id
        self.body = list()


    def init_snale(self, snake_len):
        for index in range(snake_len):
            self.body.append((self.id * 2 + 1, index + 1))

    def move(self, direction_key: tuple) -> None:
        '''
        0, 1 - down
        0, -1 - up
        1, 0 - right
        -1, 0 - up
        '''
        head = self.body[-1]
        new_head = (head[0] + direction_key[0], head[1] + direction_key[1])
        self.body.append(new_head)

class Field:

    def __init__(self, field_size: tuple, start_len: int):
        self.size = field_size
        self.start_len = start_len
        self.free_cells = set()
        self.food = None
        self.food_exists = False
        for x in range(field_size[0]):
            for y in range(field_size[1]):
                self.free_cells.add((x, y))
        self.players = list()

    def add_player(self) -> None:
        self.players.append(Snake(len(self.players)))
        for pixel in self.players[-1].body:
            self.free_cells.remove(pixel)


    def generate_food(self) -> None:
        if self.food_exists:
            return
        self.food = random.choice(self.free_field)






pygame.init()
screen = pygame.display.set_mode((1000, 1000))
size = 50
field = Field((size,size), 3)
field.add_player()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYUP and event.key == pygame.K_p:
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_l:
            pass

        
    pygame.display.flip()
pygame.quit()