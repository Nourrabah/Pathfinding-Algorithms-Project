import pygame
import random

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
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
            t = self.DFS(start, goal)
        return t

    def DFS(self, start, goal):
        stack = [start]
        visited = [start]
        accessible = {}
        while stack:
            x = stack.pop()
            if x == goal:
                break
            for voisin in self.successeur(x):
                if voisin not in visited:
                    accessible[voisin] = x
                    stack.append(voisin)
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


pygame.init()

#hedhi lel ecron
cell_size = 20
l = 10
c = 10
width, height = l * cell_size, c * cell_size
screen = pygame.display.set_mode((width, height))

g = Graphe(l, c)

#path gebeneretou b dfs
path = g.path_generator((0, 0), (9, 9))
print(path)
g.AfficherGraphe()

# coordonner
start_point = (0, 0)
end_point = (9, 9)
end_x, end_y = end_point
start_x, start_y = start_point

#l partie  hedhi torsom l path
joue = pygame.draw.rect(screen, red, (start_x, start_y, cell_size, cell_size))
joueur = 3
current_point = start_point

running = True
while running:
    screen.fill(black)

    # Draw grid
    for x in range(0, l * cell_size, cell_size):
        pygame.draw.line(screen, blue, (x, 0), (x, c * cell_size))
    for y in range(0, c * cell_size, cell_size):
        pygame.draw.line(screen, blue, (0, y), (l * cell_size, y))

    # Draw walls
    for sommet, neighbors in g.graphe.items():
        i, j = sommet
        for neighbor in neighbors:
            x, y = neighbor[0]
            if neighbor[1]:
                pygame.draw.line(screen, black, (i * cell_size, j * cell_size), (x * cell_size, y * cell_size))

    
    pygame.draw.rect(screen, green, (end_x * cell_size, end_y * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, blue, (0, 0, l * cell_size, c * cell_size), 2)
    pygame.draw.rect(screen, green, (start_x * cell_size, start_y * cell_size, cell_size, cell_size))

    #cette partie dessine  le chemin du joueur
    for key, value in path.items():
        pygame.draw.rect(screen, white, (key[0] * cell_size, key[1] * cell_size, cell_size, cell_size))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.update()


pygame.quit()
