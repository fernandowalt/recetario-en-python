from os import system
from pathlib import Path


def crear_categoria(ruta):
   
   nombre=input("ingresa el nombre de la nueva categoria: ")
   direccion=Path(f"{ruta}/{nombre}")
   direccion.mkdir()
   
   print(f"nueva categoria creada en la ruta {direccion} ")
   input("precione enter para volver al menú principal")
   system("clear")
   
  
   
   
   
   
   

   
   
   
   