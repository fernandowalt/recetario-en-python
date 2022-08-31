from pathlib import Path

from validador import validador


def recetas(ruta):

   guia=Path(ruta["path"])
   directorio_archivos=[]
   contador=0
   print(f"*******************************{ruta['name']}*********************************\n")
   print (guia)

   for direct in guia.iterdir():
       directorio_archivos.append({"name":direct.name,"path":str(direct)})
       contador+=1
       print(f"{contador}.  {direct.name}")
       
   if len(directorio_archivos)<1:
      print("=============no hay recetas aún en esta categoria============\n")
      input("presione enter para volver al al menu principal")
      return []
   
   respuesta= validador (len(directorio_archivos))
   
   return directorio_archivos[respuesta-1]
       
       
      
      
      
       
       
   
    

      


   
   

   
   


   

   

      
   

   
      
      
      
      
   
       
   
    
      
      
   
   


   
   
   

      
   
  