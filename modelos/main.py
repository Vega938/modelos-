from automovil   import Automovil
from motocicleta import Motocicleta
from camion      import Camion

def acelerar_todos(vehiculos: list, veces: int = 3) -> None:
   """Acelera todos los vehículos de la lista 'veces' veces"""
   for v in vehiculos:
       for _ in range(veces):
           v.acelerar()

def frenar_todos(vehiculos: list) -> None:
   """Frena todos los vehículos hasta detenerlos"""
   for v in vehiculos:
       while v._velocidad_actual > 0:
           v.frenar()

def main():
   print("=" * 55)
   print("     SISTEMA DE GESTIÓN DE VEHÍCULOS")
   print("=" * 55)

  
   print("\n--- AUTOMÓVIL ---")
   auto = Automovil("Toyota", "Corolla", 2023,4, "Automática")
   print(auto.obtener_informacion())
   auto.acelerar()
   auto.acelerar()
   auto.activar_aire_acondicionado()
   auto.abrir_maletero()
   auto.encender_luces()
   auto.frenar()
   print(auto.obtener_informacion())

   
   print("\n--- MOTOCICLETA ---")
   moto = Motocicleta("Yamaha", "YZF-R6", 2022, 600)
   print(moto.obtener_informacion())
   moto.levantar_caballete()
   moto.acelerar()
   moto.acelerar()
   moto.hacer_caballito()
   print(moto.obtener_informacion())

   
   print("\n--- CAMIÓN ---")
   camion = Camion("Volvo", "FH16", 2021, 25.0, 3)
   print(camion.obtener_informacion())
   camion.cargar(10.5)
   camion.cargar(8.0)
   camion.cargar(10.0)   
   print(camion.obtener_informacion())

   
   print("\n--- POLIMORFISMO ---")
   print("Acelerando todos los vehículos 3 veces:\n")
   flota = [auto, moto, camion]
   acelerar_todos(flota, veces=3)

   print("\nInformación actualizada de la flota:")
   for i, v in enumerate(flota, 1):
       print(f"  {i}. {v.obtener_informacion()}")

   print("\nFrenando toda la flota...")
   frenar_todos(flota)

if __name__ == "__main__":
   main()