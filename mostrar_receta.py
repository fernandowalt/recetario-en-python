from pathlib import Path

def mostrar_receta(receta):
   ruta= Path(receta)
   print(ruta.read_text())
   return input("presione enter para volver al menu principal")


   
 


 
      
   
   
   
   
   
   
   
   
   

