import pygame
import random
import heapq
import math

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
            t = self.astar(start, goal)
        return t

    def astar(self, start, goal):
        def heuristic(a, b):
            return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

        open_set = []
        closed_set = set()
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {spot: float("inf") for spot in self.graphe}
        g_score[start] = 0
        f_score = {spot: float("inf") for spot in self.graphe}
        f_score[start] = heuristic(start, goal)

        while open_set:
            current = heapq.heappop(open_set)[1]
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
            closed_set.add(current)
            for neighbor in self.graphe[current]:
                neighbor_node = neighbor[0]
                if neighbor_node in closed_set:
                    continue
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor_node]:
                    came_from[neighbor_node] = current
                    g_score[neighbor_node] = tentative_g_score
                    f_score[neighbor_node] = tentative_g_score + heuristic(neighbor_node, goal)
                    heapq.heappush(open_set, (f_score[neighbor_node], neighbor_node))

# Initialize Pygame
pygame.init()

# Set up the screen
cell_size = 20
l = 10
c = 10
width, height = l * cell_size, c * cell_size
screen = pygame.display.set_mode((width, height))

# Create a graph object
g = Graphe(l, c)

# Generate a path from (0, 0) to (9, 9) using A*
path = g.path_generator((0, 0), (9, 9))
print(path)
g.AfficherGraphe()

# Define start and end points
start_point = (0, 0)
end_point = (9, 9)
end_x, end_y = end_point
start_x, start_y = start_point

# Draw the player
player = pygame.draw.rect(screen, red, (start_x, start_y, cell_size, cell_size))
player_health = 3
current_point = start_point

running = True
while running:
    screen.fill(black)

    # Draw grid
    for x in range(0, l * cell_size, cell_size):
        pygame.draw.line(screen, blue, (x, 0), (x, c * cell_size))
    for y in range(0, c * cell_size, cell_size):
        pygame.draw.line(screen, blue, (0, y), (l * cell_size, y))

    # Draw end point
    pygame.draw.rect(screen, green, (end_x * cell_size, end_y * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, blue, (0, 0, l * cell_size, c * cell_size), 2)
    pygame.draw.rect(screen, green, (start_x * cell_size, start_y * cell_size, cell_size, cell_size))

    # Draw the path
    for point in path:
        pygame.draw.rect(screen, white, (point[0] * cell_size, point[1] * cell_size, cell_size, cell_size))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
