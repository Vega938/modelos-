from abc import ABC, abstractmethod

class Vehiculo(ABC):
   """
   Clase abstracta que define las características comunes
   de todos los vehículos. No se puede instanciar directamente.
   """

   def __init__(self, marca: str, modelo: str, año: int):
       """Constructor de la clase Vehiculo"""
       self._marca = marca
       self._modelo = modelo
       self._año = año
       self._velocidad_actual = 0.0

   def acelerar(self) -> None:
       """Incrementa la velocidad del vehículo en 10 km/h"""
       self._velocidad_actual += 10
       print(f"Acelerando... Velocidad actual: {self._velocidad_actual} km/h")

   def frenar(self) -> None:
       """Reduce la velocidad del vehículo en 10 km/h"""
       if self._velocidad_actual >= 10:
           self._velocidad_actual -= 10
       else:
           self._velocidad_actual = 0
       print(f"Frenando... Velocidad actual: {self._velocidad_actual} km/h")

   @abstractmethod
   def obtener_informacion(self) -> str:
       
       pass