def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            jugadores=[jugador.toJSON() for jugador in self.__jugadores]        #Modificar con la clase correcta
            )
        return d