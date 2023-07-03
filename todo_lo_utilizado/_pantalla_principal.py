import pygame
from pygame.locals import *
from todo_lo_utilizado._funcion_mostrar_text import *
from todo_lo_utilizado.colores import *

def ejecucion_princi():
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
    maximo_caract = False
    minimo_caract = False
    nombre_jugador = ""
    retorno = ''
    running_flag = True
    while running_flag:
        pantalla.blit(fondo, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_flag = False
                retorno = "salio"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    retorno = "salio"
                    running_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN and len(nombre_jugador) > 3:
                    running_flag = False
                    retorno = "paso"
                
                if event.key == K_RETURN and len(nombre_jugador) < 4:
                    minimo_caract = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # Borrar un carácter cuando se presiona la tecla Retroceso
                    nombre_jugador = nombre_jugador[:-1]
                    maximo_caract = False
                else:
                    if event.key != pygame.K_RETURN and event.key != pygame.K_SPACE:
                    # Agregar el carácter ingresado al nombre del usuario
                        if len(nombre_jugador) < 10:
                            nombre_jugador += event.unicode
                            maximo_caract = False
                        else:
                            maximo_caract = True

        if len(nombre_jugador) > 3:
            minimo_caract = False
        muestra_texto(pantalla,"fonts\Odachi.ttf", "ENTER PARA EMPEZAR",ROJO, 100, ANCHO_VENTANA//2,ALTO_VENTANA//2)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "Ingrese el usuario",ROJO_CUATRO, 50, ANCHO_VENTANA//2,ALTO_VENTANA//2 + 180)
        muestra_texto(pantalla,"fonts\Odachi.ttf", f"{nombre_jugador}",ROJO_CUATRO, 40, ANCHO_VENTANA//2,ALTO_VENTANA//2 + 250)
        if maximo_caract:
            muestra_texto(pantalla,"fonts\Odachi.ttf", "maximo 9 caracteres",ROJO_CUATRO, 30, ANCHO_VENTANA//2,ALTO_VENTANA//2 + 290)
        if minimo_caract:
            muestra_texto(pantalla,"fonts\Odachi.ttf", "Minimo 4 caracteres",ROJO_CUATRO, 30, ANCHO_VENTANA//2,ALTO_VENTANA//2 + 290)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "ESC",ROJO, 30, 50,30)
        muestra_texto(pantalla,"fonts\Odachi.ttf", "para salir",ROJO, 15, 100,30)
        pygame.draw.line(pantalla, ROJO_CUATRO, [500,670], [700,670], 2)
        pygame.display.flip()
    pygame.quit()
    return retorno,nombre_jugador