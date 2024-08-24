from tkinter import messagebox
from claseJugador import jugador

class gestorJugador:
    __jugadores: list

    def __init__(self):
        self.__jugadores=[]

    def agregarJugador(self, juga):
        self.__jugadores.append(juga)

    def agregar(self, nom, pun, fech):
        juga=jugador(nom, pun, fech)
        self.__jugadores.append(juga)

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            jugadores=[jugador.toJSON() for jugador in self.__jugadores]
            )
        return d

    def ordenarPuntaje(self):
        self.__jugadores.sort(reverse=True)

    def mostrarPuntaje(self):
        self.ordenarPuntaje()
        puntajes="\n".join([f"{j.getNombre()} - {j.getPuntaje()} - {j.getFecha()}" for j in self.__jugadores])
        messagebox.showinfo("Puntajes", puntajes)