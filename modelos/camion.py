from vehiculo import Vehiculo

class Camion(Vehiculo):
   """Clase que representa un camión de carga"""

   def __init__(self, marca: str, modelo: str, año: int,
                capacidad_carga: float, numero_ejes: int):

       super().__init__(marca, modelo, año)
       self._capacidad_carga = capacidad_carga
       self._numero_ejes = numero_ejes
       self._carga_actual = 0.0   

   def cargar(self, peso: float) -> bool:
       """
       Intenta cargar [peso] toneladas.
       Retorna True si pudo cargar, False si supera la capacidad.
       """
       if self._carga_actual + peso <= self._capacidad_carga:
           self._carga_actual += peso
           print(f"✅ Cargado {peso} ton. "
                 f"Total: {self._carga_actual}/{self._capacidad_carga} ton")
           return True
       else:
           print(f"❌ No se puede cargar. Supera la capacidad máxima "
                 f"de {self._capacidad_carga} toneladas")
           return False

   def descargar(self) -> None:
       """Descarga completamente el camión"""
       print(f"Descargando {self._carga_actual} toneladas...")
       self._carga_actual = 0.0
       print("Camión descargado completamente ✅")

   def obtener_informacion(self) -> str:
       """Implementación del método abstracto"""
       return (f"{self._marca} {self._modelo} ({self._año}) | "
               f"Carga: {self._carga_actual}/{self._capacidad_carga} ton | "
               f"Ejes: {self._numero_ejes} | "
               f"Vel: {self._velocidad_actual} km/h")