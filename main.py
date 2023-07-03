from todo_lo_utilizado._pantalla_principal import *
import pygame
from todo_lo_utilizado.personaje import *
from  todo_lo_utilizado.nivel_uno import *
from todo_lo_utilizado.nivel_dos import *
from todo_lo_utilizado.nivel_tres import *
from todo_lo_utilizado.game_over import *
from todo_lo_utilizado.win_final import *
from todo_lo_utilizado.ranking import *

def ejecucion_perdio(en_juego:False,nombre_jugador):
    retorno = juego_game_over()
    if retorno == "continuo":
        en_juego = True
    if retorno == "ranking":
        retorno = pantalla_ranking(nombre_jugador)
        if retorno == "continuo":
            en_juego = True
    return en_juego

pygame.init()
en_juego = True 
while en_juego:
    en_juego = False
    lvl_uno = False
    retorno,nombre_jugador = ejecucion_princi()
    if retorno == "paso":
        lvl_uno = True
    while lvl_uno:  
        lvl_dos = False
        lvl_uno = False
        retorno = lvl_1(nombre_jugador)
        if retorno == "gano":
            lvl_dos = True
        elif retorno == "perdio":
            retorno = ejecucion_perdio(en_juego,nombre_jugador)
            lvl_uno = retorno
        while lvl_dos:
            lvl_dos = False
            lvl_3_while = False
            retorno = lvl_dos_ejecu(nombre_jugador)
            if retorno == "gano":
                lvl_3_while = True
            elif retorno == "perdio":
                retorno = ejecucion_perdio(en_juego,nombre_jugador)
                lvl_uno = retorno
            while lvl_3_while:
                lvl_3_while = False
                retorno = lvl_tres(nombre_jugador)
                if retorno == "perdio":
                    retorno = ejecucion_perdio(en_juego,nombre_jugador)
                    lvl_uno = retorno
                if retorno == "gano":
                    retorno = w_ejecu()
                    if retorno == "continuo":
                        lvl_uno = True
                    if retorno == "ranking":
                        retorno = pantalla_ranking(nombre_jugador)
                        if retorno == "continuo":
                            lvl_uno = True                  
pygame.quit()