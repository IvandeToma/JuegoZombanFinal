import pygame
from todo_lo_utilizado.colores import *
from todo_lo_utilizado.personaje import *
from todo_lo_utilizado.zombie import *
from todo_lo_utilizado.imagenes import *
from todo_lo_utilizado._funcion_mostrar_text import *
from todo_lo_utilizado.ranking import *
from todo_lo_utilizado.meteoros import *

def lvl_tres(nombre_jugador):
    pygame.init()

    #Inicializacion sobre la pantalla
    ANCHO_VENTANA = 1200
    ALTO_VENTANA = 800
    pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
    pygame.display.set_caption("ZOMBAN")
    fondo = pygame.transform.scale(pygame.image.load("imagenes\_1_game_background\_3_game_background.png"),(1200,800))
    x_para_fondo = 0
    FPS = 25
    RELOJ = pygame.time.Clock()
    icono = pygame.image.load("imagenes\walk_zom_3_izq\image_2.png")
    pygame.display.set_icon(icono)
    
    #sonido ambiente
    ambiente = pygame.mixer.Sound("sonidos\sonido_ambiente_zombie.mp3")
    ambiente.set_volume(0.5)
    ambiente.play()
    
    #requerido para utilizar al personaje,zombie,corazon y disparo
    lista_disparos = pygame.sprite.Group()
    lista_zombies = pygame.sprite.Group()
    lista_personaje = pygame.sprite.Group()
    lista_corazones = pygame.sprite.Group()
    lista_meteoros = pygame.sprite.Group() 
    personaje = Personaje(lista_disparos)
    zombie = ZombieTres()
    corazones = Corazon()
    lista_zombies.add(zombie)
    lista_corazones.add(corazones)
    lista_personaje.add(personaje)
    
    #posicion de la sangre
    sangre_posicion_personaje = (-100,-100)
    sangre_posicion_zombie = (-100,-100)

    for i in range(10):
        meteoro = MeteoroTres()
        meteoro.rect.x = random.randrange(60,1140,80)
        meteoro.rect.y = random.randrange(-700,0,70)
        lista_meteoros.add(meteoro)

    retorno = None
    running_flag = True

    while running_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_flag = False
                retorno = "salio"
        #fondo
        x_relativa_para_fondo = x_para_fondo % fondo.get_rect().width
        pantalla.blit(fondo, (x_relativa_para_fondo - fondo.get_rect().width, 0))
        if x_relativa_para_fondo < ANCHO_VENTANA:
            pantalla.blit(fondo,(x_relativa_para_fondo,0)) 
        x_para_fondo -= 1
        muestra_texto(pantalla,"fonts\HoMicIDE EFfeCt.ttf","Kills",ROJO, 55, 100,90)

        #updates necesarios para ver las diferentes cosas
        lista_corazones.update()
        lista_disparos.update()
        lista_zombies.update()
        lista_meteoros.update()

        #funciones de movimiento
        personaje.detecto_precionado()
        personaje.movimiento(pantalla)
        corazones.update()

        #dibujo en pantalla corazones y diparos
        lista_meteoros.draw(pantalla)
        lista_corazones.draw(pantalla)
        lista_disparos.draw(pantalla) 
        
        #coliciones entre personaje y zombie
        if personaje.rect.colliderect(zombie.rect):
            zombie.sonido_mordida.play()
            personaje.hp -= 60
            zombie.kill()
            zombie = ZombieTres()
            lista_zombies.add(zombie)
            sangre_posicion_personaje = (personaje.px+20,personaje.py+200)

        colicion_perso_meteoro = pygame.sprite.groupcollide(lista_personaje,lista_meteoros,False,True)
        if colicion_perso_meteoro:
            personaje.hp -= 30

        #si se que sin vida
        if personaje.hp <= 0:
            running_flag = False
            retorno =  "perdio"
            
        #zombie movimiento
        zombie.zombie_mov(pantalla)

        #zombie colicion con disparos
        colicion_disparo_zom = pygame.sprite.groupcollide(lista_zombies,lista_disparos,False,True)
        if colicion_disparo_zom:
            personaje.kills(8)

        #muestro la sangre
        pantalla.blit(sangre, (sangre_posicion_personaje))
        pantalla.blit(sangre, (sangre_posicion_zombie))

        #puntuacion
        muestra_texto(pantalla,"fonts\HoMicIDE EFfeCt.ttf",str(personaje.puntuacion),ROJO, 50, 220,75)

        #vida del personaje
        personaje.barra_hp(pantalla,500,15,personaje.hp)
        muestra_texto(pantalla,"fonts\HoMicIDE EFfeCt.ttf",str(personaje.hp),ROJO, 20, 520,25)
        colicion_perso_corazon = pygame.sprite.groupcollide(lista_personaje,lista_corazones,False,True)
        if colicion_perso_corazon:
            personaje.hp += 40
            corazones.sonido_corazon.play()
        
        #personaje mato al zombie
        if personaje.contador_kills ==  1:
            sangre_posicion_zombie = (zombie.zx+50,zombie.zy+480)
            zombie.kill()
            zombie = ZombieTres()
            lista_zombies.add(zombie)
            personaje.contador_kills = 0
            
        #timer
        RELOJ.tick(FPS)

        pygame.display.flip()

        #paso de nivel
        if personaje.puntuacion == 4:
            running_flag = False
            retorno = "gano"
            actualizar_ranking(personaje.puntuacion + 10,nombre_jugador)

    pygame.quit()
    return retorno