from os import system
from bienvenida import bienvenido
from crear_categoria import crear_categoria
from crear_receta import crear_receta
from eliminar_categoria import eliminar_categoria
from eliminar_receta import eliminar_receta
from menu_principal import menu_principal
from menu_categorias import menu_categorias
from mostrar_receta import mostrar_receta
from recetas import recetas

ruta_principal =bienvenido()

def recetario():
   ruta=ruta_principal
   resultado=menu_principal()
   
   match resultado:
      
      case 1:
       
        categoria= menu_categorias(ruta)
        system("clear")
    
        receta_elegida=recetas(categoria)
        if receta_elegida==[]:
           system("clear")
           recetario()
           
        system("clear")
        mostrar_receta(receta_elegida['path'])
        system("clear")
        recetario()
           
      case 2:
         categoria=menu_categorias(ruta)
         system("clear")
         crear_receta(categoria)
         recetario()
      case 3:
         crear_categoria(ruta)
         recetario()
      case 4:
         categoria=menu_categorias(ruta)
         system("clear")
         receta_elegida=recetas(categoria)
         system("clear")
         eliminar_receta(receta_elegida)
         recetario()
      case 5:
        respuesta=menu_categorias(ruta)
        system("clear")
        eliminar_categoria(respuesta)
        system("clear")
        recetario()
 
      case 6:
         return         
recetario()   
         
   
   
   
   
   





   
         
         
        
       
       

         
       
  
        
   
        
      
        


   
   
               
         
         
        
 

   
   
   
   
   
   
   
   
   
   
   