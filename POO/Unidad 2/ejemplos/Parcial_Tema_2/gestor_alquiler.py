import csv
from clase_alquiler import alquiler

class gestor_al:
    __lista:list
    def __init__(self):
        self.__lista=[]
        self.recuperar()
    def agregar(self,al):
        self.__lista.append(al)
    def recuperar(self):
        with open('Alquiler.csv','r',newline='') as archivo:
            reader= csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                self.agregar(alquiler(*fila))
    def listar_reservas(self,GC):
        self.__lista=sorted(self.__lista,reverse=True)
        print("Hora   Id de Cancha     Duracion Alquiler Importe por hora Importe alquiler")
        i=0
        while i < len(self.__lista):
            texto='{}  {}\t\t{}\t\t\t{}\t\t{}'
            hora=f"{self.__lista[i].get_hora()}:{self.__lista[i].get_min()}"
            ide=self.__lista[i].get_id()
            duracion=self.__lista[i].get_dura()
            imp_h=GC.importe_hora(ide)
            importe_alquiler=(duracion/60)* imp_h
            print(texto.format(hora,ide,str(duracion)+'m',imp_h,importe_alquiler))
            i+=1
    def alquiler_total(self):
        ide=input("Ingrese Identifiador de una cancha:\n")
        acum=0
        for alquiler in self.__lista:
            if alquiler.get_id() == ide:
                acum+= alquiler.get_dura()
        print(f"El total de minutos que estuvo ocupada la cancha {ide} fue de {acum}m")