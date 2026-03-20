from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
   """Clase que representa una motocicleta"""

   def __init__(self, marca: str, modelo: str, año: int,
                cilindrada: int, tiene_caballete: bool = True):

       super().__init__(marca, modelo, año)
       self._cilindrada = cilindrada
       self._tiene_caballete = tiene_caballete

   def levantar_caballete(self) -> None:
       """Levanta el caballete de la motocicleta"""
       if self._tiene_caballete:
           print("Levantando caballete, lista para arrancar 🏍️")
       else:
           print("Esta motocicleta no tiene caballete")

   def hacer_caballito(self) -> None:
       """Realiza un caballito (wheelie)"""
       if self._velocidad_actual > 0:
           print("¡Haciendo caballito! 🤘")
       else:
           print("Necesitas acelerar primero para hacer un caballito")

   def obtener_informacion(self) -> str:
       """Implementación del método abstracto"""
       return (f"{self._marca} {self._modelo} ({self._año}) | "
               f"Cilindrada: {self._cilindrada}cc | "
               f"Vel: {self._velocidad_actual} km/h")