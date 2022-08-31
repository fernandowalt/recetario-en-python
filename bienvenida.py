
from os import system
from pathlib import Path

def bienvenido():
   ruta=Path(Path.home(),"Recetas")
   contador=0
   
   for archivo in ruta.glob("**/*.txt"):
      contador+=1
   print(f"""
         Bienvenido.
         tus recetas se encuentran en: {ruta}
         tienes un total de {contador} recetas.
         """)
   input("presione enter para continuar")
   system("clear")
   
   return ruta
      
   
   
   

     
   
 



   





