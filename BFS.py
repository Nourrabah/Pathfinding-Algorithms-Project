import pygame
from collections import deque
import random


white = (255, 255, 255)
black = (0, 0, 0)
Pink= (255, 192, 203)
Purple= (128, 0, 128)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0) 


class Graphe:
    def __init__(self, L, C):
        self.L = L
        self.C = C
        self.graphe = {(0, 0): []}

    def ajouterNoeud(self, i, j):
        if (i, j) not in self.graphe.keys():
            self.graphe[(i, j)] = []

    def ajouterArc(self, c1, c2, porte=False):
        if c2 in self.graphe.keys() and c1 in self.graphe.keys() and ((c2), True) not in self.graphe[c1] and ((c2), False) not in self.graphe[c1] and ((c1), True) not in self.graphe[c2] and ((c1), False) not in self.graphe[c2]:
            self.graphe[c1].append((c2, porte))
            self.graphe[c2].append((c1, porte))

    def listerNoeuds(self):
        return self.graphe.keys()

    def listerArcs(self, c):
        if c not in self.graphe.keys():
            return self.graphe.values()

    def adjacenceNoeud(self, c1, c2):
        l = self.graphe[c1]
        return (c2, True) in l or (c2, False) in l

    def AfficherGraphe(self):
        print("Graphe:")
        for sommet, voisins in self.graphe.items():
            print(sommet, ": ", voisins)

    def successeur(self, k):
        l = []
        for i in g.graphe[k]:
            if i[1]:
                l.append(i[0])
        return l

    def ajouterArcsVoisins(self):

        for i in range(self.L):
            for j in range(self.C):
                if i > 0:
                    self.ajouterArc((i, j), (i - 1, j), random.choice([True, False]))
                if i < self.L - 1:
                    self.ajouterArc((i, j), (i + 1, j), random.choice([True, False]))
                if j > 0:
                    self.ajouterArc((i, j), (i, j - 1), random.choice([True, False]))
                if j < self.C - 1:
                    self.ajouterArc((i, j), (i, j + 1), random.choice([True, False]))

    def path_generator(self, start, goal):
        t = None
        while t is None:
            self.graphe = {(0, 0): []}
            for i in range(l):
                for j in range(c):
                    self.ajouterNoeud(i, j)
            self.ajouterArcsVoisins()
            t = self.BFS(start, goal)
        return t

    def BFS(self, start, goal):
        pile = deque()
        pile.append(start)
        visited = [start]
        accessible = {}
        while(len(pile) > 0):
            x = pile.popleft()
            for voisin in self.successeur(x):
                if voisin not in visited:
                    accessible[voisin] = x
                    pile.append(voisin)
                    visited.append(voisin)

        fwdPath = {}
        cell = goal
        while cell != (0, 0):
            try:
                fwdPath[accessible[cell]] = cell
                cell = accessible[cell]
            except:
                print('nexiste pas!')
                return None
        return fwdPath


def can_move(key):
    global chances
    if chances > 0:
        x, y = current_point
        if key == pygame.K_LEFT:
            next_point = (x - 1, y)
        elif key == pygame.K_RIGHT:
            next_point = (x + 1, y)
        elif key == pygame.K_UP:
            next_point = (x, y - 1)
        elif key == pygame.K_DOWN:
            next_point = (x, y + 1)
        if next_point in path.values():
            print("player can move to location ", next_point)
            return True
        print("player can't move to location ", next_point)
        chances -= 1
        return False


def move(player, key):
    global current_point
    x, y = current_point
    if key == pygame.K_LEFT and can_move(key):
        player.x -= cell_size
        current_point = (x - 1, y)
        print(player.x, ", ", player.y)
    elif key == pygame.K_RIGHT and can_move(key):
        player.x += cell_size
        current_point = (x + 1, y)
        print(player.x, ", ", player.y)
    elif key == pygame.K_UP and can_move(key):
        player.y -= cell_size
        current_point = (x, y - 1)
        print(player.x, ", ", player.y)
    elif key == pygame.K_DOWN and can_move(key):
        player.y += cell_size
        current_point = (x, y + 1)
        print(player.x, ", ", player.y)
    return player.x, player.y, current_point


def draw_grid():
    for x in range(0, l * cell_size, cell_size):
        pygame.draw.line(screen, blue, (x, 0), (x, c * cell_size))
    for y in range(0, c * cell_size, cell_size):
        pygame.draw.line(screen, blue, (0, y), (l * cell_size, y))


def draw_path(graphe, path):
    for sommet, neighbors in graphe.items():
        i, j = sommet
        if sommet in path:
            pygame.draw.rect(screen, Purple, (i * cell_size, j * cell_size, cell_size, cell_size))


def draw_walls(graphe):
    for sommet, neighbors in graphe.items():
        i, j = sommet
        for neighbor in neighbors:
            x, y = neighbor[0]
            if neighbor[1]:
                pygame.draw.line(screen, Pink, (i * cell_size, j * cell_size), (x * cell_size, y * cell_size))


pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
Pink= (255, 192, 203)
green = (0, 255, 0)
blue = (0, 0, 255)
cell_size = 60
l = 20
c = 10
g = Graphe(l, c)

width, height = l * cell_size, c * cell_size
screen = pygame.display.set_mode((width, height))

path = g.path_generator((0, 0), (5, 9))
print(path)
g.AfficherGraphe()
start_point = (0, 0)
end_point = (5, 9)
end_x, end_y = end_point

start_x, start_y = start_point
player = pygame.draw.rect(screen, Purple, (start_x, start_y, cell_size, cell_size))
chances = 5
current_point = start_point
running = True
while running:
    screen.fill(Pink)
    draw_grid()
    draw_walls(g.graphe)
    pygame.draw.rect(screen, green, (end_x * cell_size, end_y * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, blue, (0, 0, l * cell_size, c * cell_size), 2)
    

    
    draw_path(g.graphe, path)

    font = pygame.font.Font(None, 20)
    text = font.render("Health: {}".format(chances), True, Purple)
    text_rect = text.get_rect()
    text_rect.center = (30, height + 12)
    screen.blit(text, text_rect)

    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key = event.key
            player.x, player.y, current_point = move(player, key)
    player = pygame.draw.rect(screen, red, (player.x, player.y, cell_size, cell_size))

    if current_point == end_point:
        screen.fill(Pink)
        font = pygame.font.Font(None, 36)
        win_text = font.render("You win!", True, Purple)
        text_rect = win_text.get_rect()
        text_rect.center = (width // 2, height // 2)
        screen.blit(win_text, text_rect)

    if chances == 0:
        screen.fill(Pink)
        font = pygame.font.Font(None, 36)
        lose_text = font.render("You lose", True, Purple)
        text_rect = lose_text.get_rect()
        text_rect.center = (width // 2, height // 2)
        screen.blit(lose_text, text_rect)
    pygame.display.update()
pygame.quit()



