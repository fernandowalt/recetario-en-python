
from validador import validador

def menu_categorias(ruta):
   directorios_hijos=[]
   contador=0

   print(f"==========Categorias===========\n")   
   for direct in ruta.iterdir():
      directorios_hijos.append({"name":direct.name,"path":str(direct)})
      contador+=1
      print(f" {contador}. {direct.name}")
      
   respuesta=validador(len(directorios_hijos))
   return directorios_hijos[respuesta-1]


   



   

   
   

      






   

   
   
      

      
      

   
   