import sys
import pygame
import random
import math



class Rectangulo:

	def __init__(self):
		v = random.randrange(50,100)
		self.x = 0
		self.y = 0
		self.x_pro = 0
		self.y_pro = 0
		self.pos_x = 0
		self.pos_y = 0
		self.width = random.randrange(3,10)
		self.heigth = self.width
		self.move_x = random.randrange(-3,5)
		self.move_y = random.randrange(-3,5)
		self.color= (r1, r2, r3)
		self.t_vida = v
		self.angulo = math.radians(random.randrange(1,360))
		self.v0 = 20
		self.t = 0

		self.vo_pro = 0
		self.angu_pro = 0


	def mover(self):
		self.vo_pro = 100

		self.x_pro=10 + ((self.vo_pro * math.cos(self.angu_pro)) * self.t)
		self.y_pro= 690 - ((self.vo_pro * math.sin(self.angu_pro) * self.t)-((9.81*(self.t**2)/2.0)))

		self.x = self.pos_x + (((self.vo_pro * math.cos(self.angu_pro))+(self.v0 * math.cos(self.angulo))) * self.t)
		self.y = self.pos_y - ((self.v0 * math.sin(self.angulo) * self.t)-((9.81*(self.t**2)/2.0)))

	def draw(self, pantalla):
		pygame.draw.rect(pantalla, self.color, [self.x, self.y, self.width, self.heigth])

		pygame.draw.rect(pantalla, self.color, [self.x_pro,self.y_pro,10, 10])





FONDO = (0,0,0)
cantidad_de_particulas = 50
def pygamepac(x,y):
	print (x,y)
	y=700-y
	return x,y

def pacpygame(x,y):
	pass
def calcularangulo(x1,y1,x2,y2):
	x1 = float(x1)
	y1 = float(y1)
	x2 = float(x2)
	y2 = float(y2)
	pygamepac(x1,y1)
	pen=((y2-y1)/(x2-x1))
	a= math.atan(pen)

	print (math.degrees(a))
	return a

def crearParticulas(x,y,adisparo):
	particulasLista = []

	for i in range (cantidad_de_particulas):
		particula= Rectangulo()
		particula.x=x
		particula.y=y
		particula.pos_x = x
		particula.pos_y = y
		particula.angu_pro = adisparo


		particulasLista.append(particula)
	return particulasLista

pygame.init()
pantalla = pygame.display.set_mode([700,700])
pygame.display.set_caption("Simulacion de Particulas")
FPS=60
reloj = pygame.time.Clock()

sub_lista = []

while True:
	r1 = random.randrange(0,255)
	r2 = random.randrange(0,255)
	r3 =random.randrange(0,255)
	for evento in pygame.event.get():
		if evento.type== pygame.QUIT:
			pygame.quit()
			sys.exit()

		elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:


			x,y = evento.pos
			c1,c2 = pygamepac(x,y)
			adisparo = calcularangulo (c1,c2,0,0) 

			lista = crearParticulas(x,y,adisparo)
			sub_lista.append(lista)




	pantalla.fill(FONDO)
	for lista in sub_lista:
		i = 0
		for particula in lista:
			particula.draw(pantalla)

			particula.mover()

			particula.t_vida -= (1.0/FPS)
			particula.t += (1.0/FPS)

			if particula.t_vida <= 0:
				lista.pop(i)

			i += 1


	pygame.display.flip()
	reloj.tick(FPS)

