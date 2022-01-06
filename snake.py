import random
import pygame

class Snake:
    def __init__(self, id: int, field, ln: int) -> None:
        self.id = id
        self.body = list()
        self.field = field  # чтобы удалять яблоко и свободные клетки
        self.init_snale(ln)
        self.direction = (0, 1)
        self.last_direction = (0, 1)

    def init_snale(self, snake_len):
        for index in range(snake_len):
            self.body.append((self.id * 2, index))  # было self.id * 2 + 1 и index + 1, хз зачем это
        self.head = (self.id * 2, snake_len - 1)

    def change_direction(self, direction: tuple):  # тут я меняю направление змеи
        if self.last_direction[0] + direction[0] or self.last_direction[1] + direction[1]:  # проверка что змея не двигается назад
            self.direction = direction  # собственно направление

    def move(self) -> None:  # я сделал так, что направление меняется в функции change_direction, а тут змея только двигается
        '''
        0, 1 - down
        0, -1 - up
        1, 0 - right
        -1, 0 - up
        '''
        new_head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])
        self.body.append(new_head)
        self.head = new_head
        tail = self.body[0]  # хвост
        self.field.free_cells.add(tail)  # + свободная клетка в хвосте
        self.field.free_cells.discard(new_head)  # - свободная клетка в голове
        # del self.body[0]  # удаляем хвост
        self.last_direction = self.direction  # куда двигалась змея в последний раз

class Field:
    def __init__(self, field_size: tuple, start_len: int):
        self.size = field_size
        self.start_len = start_len
        self.free_cells = set()
        self.food = (-1, -1)
        self.food_exists = False
        for x in range(field_size[0]):
            for y in range(field_size[1]):
                self.free_cells.add((x, y))
        self.players = list()

    def move(self):
        for s in self.players:
            s.move()
            if s.head == self.food:
                self.generate_food()
            else:
                del s.body[0]

    def add_player(self, ln) -> None:  # добавил длину змеи
        self.players.append(Snake(len(self.players), self, ln))
        for pixel in self.players[-1].body:
            self.free_cells.remove(pixel)

    def generate_food(self) -> None:
        if self.food_exists:
            return
        self.food = random.choice(list(self.free_cells))  # кажись нельзя брать choice из set


'''while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYUP and event.key == pygame.K_p:
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_l:
            pass
    pygame.display.flip()'''

pygame.init()
sc = pygame.display.set_mode([1000, 1000])
flag = True
sc.fill((0, 0, 0))
size = 20
field = Field((size, size), 3)
field.add_player(3)
# field.add_player()
# clock = pygame.time.Clock()
Snigger = field.players[0]
fps = 20
field.generate_food()
while flag:
    # print("debug cycle")
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            flag = False
            pygame.quit()
            break
        if ev.type == pygame.KEYDOWN:
            # print("debug key")
            if ev.key == pygame.K_LEFT:
                Snigger.change_direction((-1, 0))
            elif ev.key == pygame.K_RIGHT:
                Snigger.change_direction((1, 0))
            elif ev.key == pygame.K_UP:
                Snigger.change_direction((0, -1))
            elif ev.key == pygame.K_DOWN:
                Snigger.change_direction((0, 1))
    field.move()
    # print("debug Snigger moved")
    for i in range(50):
        for j in range(50):
            # print("debug double cycle")
            if (i, j) in Snigger.body:
                if (i, j) == Snigger.head:
                    sc.blit(pygame.image.load("wtf.png"), (i * size, j * size, i * size + size, j * size + size))
                else:
                    pygame.draw.rect(sc, pygame.Color("white"), (i * size, j * size, i * size + size, j * size + size))
            elif (i, j) == field.food:
                sc.blit(pygame.image.load("a.png"), (i * size, j * size, i * size + size, j * size + size))
            else:
                pygame.draw.rect(sc, pygame.Color("black"), (i * size, j * size, i * size + size, j * size + size))
    pygame.display.flip()
    # clock.tick(fps)
