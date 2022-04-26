import random
import pygame


class Snake:

    def __init__(self, start_len: int, field_size: tuple) -> None:
        self.snake_len = start_len
        self.field_size = field_size
        self.snake = list()
        self.food = None
        self.food_exists = False
        self._init_snake()
        field = list()
        self.free_field = set()
        for x in range(field_size[0]):
            for y in range(field_size[1]):
                self.free_field.add((x, y))

    def _init_snale(self):
        for index in range(self.snake_len):
            self.snake.append((0, index))
            self.free_field.remove((0, index))
        self.snake = self.snake

    def move(self, direction_key: tuple) -> None:
        '''
        0, 1 - down
        0, -1 - up
        1, 0 - right
        -1, 0 - up
        '''
        head = self.snake[-1]
        new_head = (head[0] + direction_key[0], head[1] + direction_key[1])
        self.snake.append(new_head)
        self.free_field.remove(new_head)
        self.snake_len += 1
        if (not self._on_food):
            self.free_field.add(self.snake[0])
            self.snake = self.snake[1:]
            self.snake_len -= 1

    def generate_food(self) -> None:
        if self.food_exists:
            return
        self.food = random.choice(self.free_field)

    def _on_food(self) -> bool:
        if self.snake[-1] in self.food:
            self.food_exists = False
            return True
        else:
            return False

    def lose(self) -> bool:
        head = self.snake[-1]
        if head in self.snake[:-1]:
            return True
        if head[0] < 0 or head[1] < 0:
            return True
        if head[0] > self.field_size[0] or head[1] > self.field_size[1]:
            return True
        return False

    def draw(self):
        return self.snake, self.food


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
size = 50
snake = Snake()

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
