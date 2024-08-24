from zope.interface import Interface

class IDirector(Interface):
   
   def modificarBasico(dni, nuevoSueldo):
      pass
   
   def modificarImporteExtra(dni, nuevoImporte):
      pass
   
   def modificarPorcentajePorCategoria(dni, nuevoPorcentaje):
      pass
   
   def modificarPorcentajePorCargo(dni, nuevoPorcentaje):
      pass