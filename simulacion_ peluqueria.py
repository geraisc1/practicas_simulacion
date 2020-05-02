
import pygame
from pygame.locals import *

import random
import math
import time 

#FUNCIONES PARA EL PROGRAMA

def tiempoEnQueSeDesocupaLaEstacion(estacion):
    return estacion[1]

t_llegada1 = int(input("Iingresa el tiempo entre llegadas:    "))
t_min = int(input("timer minimo de tiempo:    "))
t_max = int(input("Tiempo maximo de corte:    "))
total_clientes = int(input("No de clientes:     "))
peluquero = int(input("No de barberos:   "))

tiempo_total = 0
salida_anterior = 0
espera_total1 = 0
t_corte1 = 0

tiempo_llegada = []
tiempo_corte1 = []
clte = []
salir = []
espr = []
t_llegada_entero = []
salir_entero = []

estaciones = []
peluquero1 = []
peluquero2= []
for e in range(0, peluquero):
    estaciones.append([e+1, 0])

for i in range(total_clientes):
	R = random.random()
	t_llegada = abs((((-1)*(t_llegada1))*((math.log(R)))))
	tiempo_total = t_llegada + tiempo_total 
	tiempo_llegada.append(tiempo_total) 
	t_llegada_entero.append(int(tiempo_total))
	t_corte = ((t_min + ((t_max - t_min) * (R)))) 
	tiempo_corte1.append(t_corte)
	clte.append(i) 
	t_salida = tiempo_total + t_corte 
	salir.append(t_salida)
	salir_entero.append(int(t_salida))
	espera_total = (salida_anterior - tiempo_total)
	estaciones.sort(key=tiempoEnQueSeDesocupaLaEstacion)
	espera_total = estaciones[0][1] - tiempo_total
	espr.append(espera_total)

	
	if espera_total < 0:
		espera_total = 0
	t_salida += espera_total
	estaciones[0][1] = salida_anterior

	peluquero1.append([i+1, tiempo_total, t_salida, estaciones[0][0], espera_total])

	
	salida_anterior = t_salida
	
	espera_total1 = espera_total + espera_total1
	t_corte1 = (t_corte) + (t_corte1)
	
sep = '|{}|{}|{}|{}|{}|'.format('-'*10, '-'*16, '-'*16, '-'*16, '-'*16)
print('{0}\n| CLIENTE  |    LLEGADA     |   SALIDA       |     BARBERO    |     ESPERA     |\n{0}'.format(sep))
for b in peluquero1:
	n_cliente = b[0]
	t_llegada = b[1]
	tiempo = b[2]
	pelu = b[3]
	espera = b[4]
	print('| {:>8.2f} | {:>14.2f} | {:>14.2f} | {:>14.2f} | {:>14.2f} |'.format(n_cliente, t_llegada,tiempo,pelu, espera,sep))
	peluquero2.append(pelu)


estaciones.sort(key=tiempoEnQueSeDesocupaLaEstacion)
t_salida_ultimo = estaciones[-1][1]
n_estaciones_ocupadas = 0
n_clientes_en_espera = 0

long_de_fila = (espera_total1) / (salida_anterior) 
t_espera_promedio = (espera_total1) / (total_clientes)
uso_instalacion = (t_corte1) / (salida_anterior) 

print ("LONGITUD PROMEDIO DE FILA   %.2f" %(long_de_fila))
print ("TIEMPO DE ESPERA PROMEDIO     %.2f" %(t_espera_promedio))
print ("USO PROMEDIO DE LA INSTALACION      %.2f" %(uso_instalacion))
raw_input("TIEMPO DE SIMULACION (%ssegundos) " %(int(salida_anterior)))



pygame.init()

FPS = 10 
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((710,599))
pygame.display.set_caption('drawing')

imagen = pygame.image.load('escenario.jpeg')
peluqueros1 = pygame.image.load('muneco.jpeg')
peluqueros2 = pygame.image.load('muneco.jpeg')
cliente = pygame.image.load('cliente.png')

clientes_en_pantalla = []

t=1
fps_contador = 0
posy = 100

while True:
	if t == int(salida_anterior):
		pygame.quit()
        	exit()

	screen.fill((0,0,0))
    	screen.blit(imagen, (0, 0))
	screen.blit(peluqueros1, (0, 0))
	screen.blit(peluqueros2, (300, 0))

	
	for c in clientes_en_pantalla:
		if c[5] == True:
			screen.blit(cliente, (c[1], c[2]))

			if c[3] == 1:
				limite = 170

			else:
				limite = 530

			if c[1] < limite and c[4] <= 0:
				c[1]+= 10
				c[4]-= 1


	fps_contador += 1
	if fps_contador == 10:
		print "%s/%s" %(t, salida_anterior)
		for b in peluquero1:
			if int (b[1]) == t:
			    clientes_en_pantalla.append([b[0], 0, posy, b[3], b[4], True])
			    posy += 15
			    if n_estaciones_ocupadas < peluquero:
				n_estaciones_ocupadas += 1

			    if b[4] > 0:
				n_clientes_en_espera += 1

			elif int(b[2]) == t:
			    for c in clientes_en_pantalla:
				if c[0] == b[0]:
					c[5] = False

			    if n_estaciones_ocupadas > 0 and n_clientes_en_espera == 0:
				n_estaciones_ocupadas -= 1

			    if n_clientes_en_espera > 0:
				n_clientes_en_espera -= 1

		t += 1
		fps_contador = 0

	

	for event in pygame.event.get():
    		if event.type == QUIT:
        		pygame.quit()
        		sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)



for t in range(0, int(salida_anterior+1)):
    mensaje = ("%s: (%s/%s) LUGARES EN SERVICIO, %s CLIENTES EN ESPERA" %(t, n_estaciones_ocupadas, peluquero, n_clientes_en_espera))

