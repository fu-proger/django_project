from pygame import *
import random


def lose():
    print("YOU LOSE!!!(LOSER)")
    exit(0)


def random_apple(sn):
    sp = []
    for i in range(50):
        for j in range(50):
            if [i, j] not in sn:
                sp.append([i, j])
    return random.choice(sp)


coord_of_apple = [-1, -1]


class snake:  # 1 - право, 2 - вниз, 3 - вверх, 4 - влево
    def __init__(self, l):
        self.l = l
        self.sp = []
        self.d = 1
        for i in range(l):
            self.sp.append([i, 9])

    def change_direction(self, direction):
        if self.d != direction:
            if self.d + direction != 5:
                self.d = direction

    def move(self):
        global coord_of_apple
        coord = [self.sp[-1][0], self.sp[-1][1]]
        if self.d == 1:
            coord[0] += 1
        elif self.d == 2:
            coord[1] += 1
        elif self.d == 3:
            coord[1] -= 1
        else:
            coord[0] -= 1
        for el in self.sp:
            if el == coord:
                lose()
        if not 0 <= coord[0] <= 49 or not 0 <= coord[1] <= 49:
            lose()
        if coord == coord_of_apple:
            self.sp.append(coord)
            coord_of_apple = random_apple(self.sp)
        else:
            del self.sp[0]
            self.sp.append(coord)


init()
sc = display.set_mode([1000, 1000])
flag = True
sc.fill((0, 0, 0))
Snigger = snake(3)
size = 20
clock = time.Clock()
coord_of_apple = random_apple(Snigger.sp)
while flag:
    for ev in event.get():
        if ev.type == QUIT:
            flag = False
            break
        if ev.type == KEYDOWN:
            s = Snigger.d
            if ev.key == K_LEFT:
                Snigger.change_direction(4)
                if s != Snigger.d:
                    break
            elif ev.key == K_RIGHT:
                Snigger.change_direction(1)
                if s != Snigger.d:
                    break
            elif ev.key == K_UP:
                Snigger.change_direction(3)
                if s != Snigger.d:
                    break
            elif ev.key == K_DOWN:
                Snigger.change_direction(2)
                if s != Snigger.d:
                    break
    # print(Snigger.sp)
    Snigger.move()
    fps = 25
    for i in range(50):
        for j in range(50):
            if [i, j] in Snigger.sp:
                if [i, j] == Snigger.sp[-1]:
                    sc.blit(image.load("wtf.png"), (i * size, j * size, i * size + size, j * size + size))
                else:
                    draw.rect(sc, Color("white"), (i * size, j * size, i * size + size, j * size + size))
            elif [i, j] == coord_of_apple:
                sc.blit(image.load("a.png"), (i * size, j * size, i * size + size, j * size + size))
            else:
                draw.rect(sc, Color("black"), (i * size, j * size, i * size + size, j * size + size))
    display.flip()
    clock.tick(fps)