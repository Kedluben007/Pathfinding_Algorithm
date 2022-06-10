#-----------------------------import-----------------------------
import pygame
from queue import PriorityQueue


#----------------------------variables----------------------------
WIDTH = 800
ROWS = 50
GAP = WIDTH // ROWS
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


#------------------------------class------------------------------
class Point:
	def __init__(self, row, col, width, rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.width = width
		self.rows = rows
		self.color = WHITE
		self.neighbors = []


	def make_start(self):
		self.color = ORANGE

	def make_end(self):
		self.color = TURQUOISE

	def make_barrier(self):
		self.color = BLACK

	def reset(self):
		self.color = WHITE


	def draw(self):
		pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))


#----------------------------functions----------------------------
def make_grid():
	grid = []
	for i in range(ROWS):
		grid.append([])							#vytvoření rastru
		for j in range(ROWS):
			point = Point(i, j, GAP, ROWS)
			grid[i].append(point)
	return grid

def draw(grid):
	for row in grid:
		for point in row:			#nakreslení jednotlivých bodů
			point.draw()
	draw_grid()
	pygame.display.update()

def draw_grid():
	for i in range(ROWS):
		pygame.draw.line(WIN, GREY, (0, i * GAP), (WIDTH, i * GAP))
		for j in range(ROWS):											#nakreslení dělících čar
			pygame.draw.line(WIN, GREY, (j * GAP, 0), (j * GAP, WIDTH))

def get_clicked_pos(pos):
	y, x = pos
	row = y // GAP
	col = x // GAP

	return row, col


#--------------------------main function--------------------------
def main():
	grid = make_grid()

	start = None
	end = None

	run = True
	Alg_started = False

	while run:
		draw(grid)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:			#LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos)
				point = grid[row][col]
				if not start and point != end:
					start = point
					start.make_start()

				elif not end and point != start:
					end = point
					end.make_end()

				elif point != start and point != end:
					point.make_barrier()

			elif pygame.mouse.get_pressed()[2]:			#RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos)
				point = grid[row][col]
				point.reset()
				if point == start:
					start = None
				elif point == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid()

				if event.key == pygame.K_SPACE and start and end:
					

main()