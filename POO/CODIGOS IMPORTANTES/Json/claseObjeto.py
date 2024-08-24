#Clase Madre
def toJSON(self):
    d=dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(       #Modificar con los atributos del objeto
            nombre=self.__nombre,
            puntaje=self.__puntaje,
            fecha=self.__fecha,
            )
        )
    return d

#Clase Hija
def toJSON(self):   
    d = dict(
        __clase__ = self.__class__.__name__,  
        __atributos__ = dict(       #Modificar con los atributos del objeto
            cuil = super().getCuil(),
            nombre = super().getNombre(),
            apellido = super().getApellido(),
            sueldoBasico = super().getSueldoBasico(), #Probar modificando super por self
            antiguedad = super().getAntiguedad(),
            carrera = self.__carrera,
            cargo = self.__cargo,
            catedra = self.__catedra,
            porcentaje = self.__porcentaje
            )
        )
    return d