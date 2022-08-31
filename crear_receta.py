from os import system
from pathlib import Path

def crear_receta(ruta):
   nombre=input("escribe el nombre de la receta: ")
   contenido=input("escribe el contenido: ")
   system("clear")
   
   home=ruta['path']+f'/{nombre}.txt'
   Path(home).touch()
   Path(home).write_text(contenido)
   
   print(f"nueva receta creada en la ruta {ruta['path']}")
   
   input("preciona enter para volver al menú principal")
   system("clear")





   
  
   

   

   
   
   
   
   
   
   
   
   
   
   
   

     
      
      
      
      
   


      
      
   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   

   




