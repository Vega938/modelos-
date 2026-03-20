from vehiculo import Vehiculo

class Automovil(Vehiculo):
   """Clase que representa un automóvil de pasajeros"""

   def __init__(self, marca: str, modelo: str, año: int,
                numero_puertas: int, tipo_transmision: str):

       
       super().__init__(marca, modelo, año)

       
       self._numero_puertas = numero_puertas
       self._tipo_transmision = tipo_transmision

   def abrir_maletero(self) -> None:
       """Abre el maletero del automóvil"""
       print(f"Abriendo maletero del {self._marca} {self._modelo}")

   def activar_aire_acondicionado(self) -> None:
       """Activa el sistema de aire acondicionado"""
       print("Aire acondicionado activado 🌡️")

   def encender_luces(self) -> None:
       """Enciende las luces del automóvil"""
       print(f"Luces del {self._marca} {self._modelo} encendidas 💡")

   def obtener_informacion(self) -> str:
       """Implementación del método abstracto"""
       info_base = super().obtener_informacion()  
       return (f"{self._marca} {self._modelo} ({self._año}) | "
               f"Puertas: {self._numero_puertas} | "
               f"Transmisión: {self._tipo_transmision} | "
               f"Vel: {self._velocidad_actual} km/h")