from claseGestorJugador import gestorJugador
from claseObjectEncoder import objectEncoder
import tkinter as tk
from tkinter import simpledialog, Tk, messagebox
import datetime
import random
import os

class simon:
    __ventana: object
    __secuencia: list
    __pulsados: list
    __puntaje: int
    __nombre: str
    __colores: list
    __botones: dict
    __gestorJugadores: object
    __json: object

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Simon Dice")
        self.__ventana.geometry("208x350")
        ancho=self.__ventana.winfo_screenwidth()
        alto=self.__ventana.winfo_screenheight()
        pos1=(ancho//2)-(208//2)
        pos2=(alto//2)-(350//2)
        self.__ventana.geometry(f"208x350+{pos1}+{pos2}")
        self.__ventana.resizable(False, False)
        self.__secuencia=[]
        self.__pulsados=[]
        self.__puntaje=0
        self.__nombre=""
        self.__colores=["red", "green2", "blue", "yellow"]
        self.__botones={}
        self.__gestorJugadores=gestorJugador()
        self.__json=objectEncoder()
        self.dirjson=os.path.join(os.path.dirname(__file__), "pysimonpuntajes.json")

        self.carga()
        self.crearWidgets()
        self.crearMenu()
        self.nombreJugador()
        self.juego()
        self.__ventana.mainloop()
    
    def carga(self):
        if not os.path.exists(self.dirjson):
            with open(self.dirjson, "w") as f:
                f.write("{}")
        else:
            dict=self.__json.leerJSONArchivo(self.dirjson)
            if dict:
                self.__gestorJugadores=self.__json.decodificarDiccionario(dict)

    def crearMenu(self):
        barraMenu=tk.Menu(self.__ventana)
        self.__ventana.config(menu=barraMenu)
        menuOpciones=tk.Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label="Opciones", menu=menuOpciones)
        menuOpciones.add_command(label="Ver puntajes", command=self.verPuntajes)
        menuOpciones.add_command(label="Cambiar jugador", command=self.cambiarJugador)
        menuOpciones.add_separator()
        menuOpciones.add_command(label="Salir", command=self.__ventana.quit)

    def verPuntajes(self):
        self.__gestorJugadores.mostrarPuntaje()

    def cambiarJugador(self):
        self.nombreJugador()
        self.juego()

    def crearWidgets(self):
        for i, color in enumerate(self.__colores):
            fila=i//2  
            col=i%2 
            boton=tk.Canvas(self.__ventana, bg=color, width=100, height=150, relief='flat')
            boton.grid(row=fila, column=col)
            boton.bind("<Button-1>", lambda event, col=color: self.agregarPulsados(col))
            self.__botones[color]=boton
        self.labelPuntaje=tk.Label(self.__ventana, text="Puntaje: 0")
        self.labelPuntaje.grid(row=2, columnspan=2)
        self.labelJugador=tk.Label(self.__ventana, text="")
        self.labelJugador.grid(row=3, columnspan=2)

    def agregarPulsados(self, color):
        self.__pulsados.append(color)
        self.animarColor(color)
        if not self.comparar():
            self.gameOver()
        elif len(self.__pulsados)==len(self.__secuencia):
            self.__puntaje+=1
            self.actualizarPuntaje()
            self.__ventana.after(1000, self.nuevoColor)

    def comparar(self):
        for i in range(len(self.__pulsados)):
            if self.__pulsados[i]!=self.__secuencia[i]:
                return False
        return True
    
    def gameOver(self):
        fecha_hora=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__gestorJugadores.agregar(self.__nombre, self.__puntaje, fecha_hora)
        self.__json.guardarJSONArchivo(self.__gestorJugadores.toJSON(), self.dirjson)
        self.verPuntajes()
        respuesta=messagebox.askquestion("Game Over", f"Perdiste!\nPuntaje: {self.__puntaje}\n¿Quieres reintentar?")
        if respuesta=='yes':
            self.juego()
        else:
            self.__ventana.quit()

    def nombreJugador(self):
        self.__ventana.withdraw()
        self.__nombre=simpledialog.askstring("Nombre del jugador", "Ingrese su nombre:")
        self.__ventana.deiconify()
        if not self.__nombre:
            self.__nombre="Jugador"
        self.actualizarNombre()

    def actualizarNombre(self):
        self.labelJugador.config(text=f"Jugador: {self.__nombre}")

    def mostrarColores(self):
        delay=0
        for i, color in enumerate(self.__secuencia):
            self.__ventana.after(i * 1000, lambda col=color: self.animarColor(col))
            delay+=1000

    def animarColor(self, color):
        boton=self.__botones[color]
        colorOriginal=boton["bg"]
        colorOscuro=self.colorOscuro(colorOriginal)
        boton["bg"]=colorOscuro
        self.__ventana.after(500, lambda: self.resetearColor(boton, colorOriginal))

    def colorOscuro(self, color):
        coloresOscuros={
            "red": "red4",
            "green2": "dark green",
            "blue": "blue4",
            "yellow": "gold4"
        }
        return coloresOscuros[color]

    def resetearColor(self, boton, color):
        boton["bg"]=color

    def juego(self):
        self.__secuencia=[]
        self.__pulsados=[]
        self.__puntaje=0
        self.actualizarPuntaje()
        self.nuevoColor()

    def actualizarPuntaje(self):
        self.labelPuntaje.config(text=f"Puntaje: {self.__puntaje}")

    def nuevoColor(self):
        self.__pulsados=[]
        sig=random.choice(self.__colores)
        self.__secuencia.append(sig)
        self.mostrarColores()