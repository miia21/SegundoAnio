from clasereserva import reserva
import csv

class gestorreservas:
    __listareservas=list

    def __init__(self):
        self.__listareservas=[]

    def agregareserva(self,unareserva):
        self.__listareservas.append(unareserva)
    
    def testreservas(self):
        archivo=open('Reservas.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregareserva(reserva(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6]))
        archivo.close()

    def listadofechas(self,gc):
        fecha=input('Ingrese Fecha:')
        i=0
        print('Reservas para la fecha: ')
        print('N° de Cabaña                Importe Diario               Cantidad de dias                Seña                    Importe a cobrar')
        while i<len(self.__listareservas):
            if(self.__listareservas[i].getfechainicio()==fecha):
                importediar=float(gc.importediario(self.__listareservas[i].getnrocabaña()))
                importeacobrar=int(self.__listareservas[i].getcantidaddias())*importediar-float(self.__listareservas[i].getimporteseña())
                print('    ',self.__listareservas[i].getnrocabaña(),'                     ',importediar,'$                          ',self.__listareservas[i].getcantidaddias(),'                     ',self.__listareservas[i].getimporteseña(),'$                    ',importeacobrar,'$')
            i=i+1

    def notreserva(self,num):
        i=0
        band=False
        while i<len(self.__listareservas) and band is False:
            if(self.__listareservas[i].getnrocabaña()==num):
                band=True
            i=i+1
        return band
