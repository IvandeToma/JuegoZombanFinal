import pygame
from pygame.locals import *
from todo_lo_utilizado._funcion_mostrar_text import *
from todo_lo_utilizado.colores import *

def w_ejecu():
    pygame.init()
    
    #Inicializacion sobre la pantalla
    ANCHO_VENTANA = 1200
    ALTO_VENTANA = 800
    pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
    pygame.display.set_caption("ZOMBAN")
    fondo = pygame.transform.scale(pygame.image.load("imagenes\_background_inicial.py\_background.jpg"),(1200,800))
    icono = pygame.image.load("imagenes\walk_zom_3_izq\image_2.png")
    pygame.display.set_icon(icono)
    
    #sonido ambiente
    ambiente = pygame.mixer.Sound("sonidos\sonido_ambiente_principal.mp3")
    ambiente.set_volume(0.5)
    ambiente.play()

    running_flag = True
    while running_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_flag = False
                retorno = "salio"
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running_flag = False
                    retorno = "salio"
                if event.key == pygame.K_RETURN:
                    running_flag = False
                    retorno = "continuo"
                if event.key == pygame.K_r:
                    running_flag = False
                    retorno = "ranking"

        pantalla.blit(fondo, (0,0))
        muestra_texto(pantalla,"fonts\Odachi.ttf", "VENCISTE A TODOS LOS ZOMBIES",ROJO, 100, ANCHO_VENTANA//2,ALTO_VENTANA//2)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "IMPRESIONANTE!!!",ROJO, 50, ANCHO_VENTANA//2,ALTO_VENTANA//2 + 150)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "presiona R para ver el ranking",ROJO_CUATRO, 40, ANCHO_VENTANA//2,ALTO_VENTANA//2 + 250)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "ESC",ROJO, 30, 50,30)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "para salir",ROJO, 15, 100,30)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "enter",ROJO, 30, 1050,30)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "para continuar",ROJO, 15, 1130,30)
        pygame.display.flip()
    pygame.quit()
    return retorno