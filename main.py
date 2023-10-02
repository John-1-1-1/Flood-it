from random import randint

import pygame as pg
import pygame.time
from pygame import *
import sys

COLORS = [
    (255, 0, 0),   # RED
    (0, 255, 0),   # GREEN
    (0,0,255),     # BLUE
    (255, 255, 0), # YELLOW
    (0,255,255),   # TURQUOISE
    (255, 0, 255)  # PING
]

SIZE_FIELD = 14
SIZE_CELL = 25
SIZE_LINE = 3
SIZE_EDGE = 40

class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

map = []
for i in range(SIZE_FIELD):
    map.append([])
    for j in range(SIZE_FIELD):
        map[i].append(Cell(i, j, COLORS[randint(0,5)]))

xy = SIZE_EDGE*2 + (SIZE_CELL+ SIZE_LINE) * SIZE_FIELD
sc = pg.display.set_mode((xy,xy))

clock = pygame.time.Clock()


def check_cells(pos):
    x = (pos[0] - SIZE_EDGE) // (SIZE_LINE + SIZE_CELL)
    y = (pos[1] - SIZE_EDGE) // (SIZE_LINE + SIZE_CELL)
    new_color = map[x][y].color
    old_color = map[0][0].color
    if new_color == old_color:
         return
    ch_cells = [map[0][0]]
    while len(ch_cells) != 0:
        cell = ch_cells.pop(0)
        cell.color = new_color
        check_neighbour(cell, ch_cells, new_color, old_color)



def check_neighbour(cell, ch_cells, new_color, old_color):
    positions = [(cell.x - 1, cell.y),
                 (cell.x + 1, cell.y),
                 (cell.x, cell.y - 1),
                 (cell.x, cell.y + 1)]
    for pos in positions:
        if 0 <= pos[0] < SIZE_FIELD and 0 <= pos[1] < SIZE_FIELD:
            if map[pos[0]][pos[1]].color == old_color:
                ch_cells.append(map[pos[0]][pos[1]])
                map[pos[0]][pos[1]].color = new_color

while 1:
    for i in pg.event.get():
        if i.type == QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            check_cells(i.pos)

    for i in map:
        for item in i:
            pygame.draw.rect(sc, item.color,
                         (SIZE_EDGE + item.x * SIZE_CELL + SIZE_LINE * item.x,
                          SIZE_EDGE + item.y*SIZE_CELL + SIZE_LINE * item.y,
                          SIZE_CELL, SIZE_CELL))

    pygame.display.update()
    clock.tick(60)