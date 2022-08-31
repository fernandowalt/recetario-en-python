from os import system

from validador import validador

def menu_principal():
   print(
      """
          ==========Menú Principal==========
        
      1. Leer recetas.
      2. Crear recetas.
      3. Crear Categoria.
      4. Eliminar Recetas.
      5. Eliminar categoria.
      6. Salir.""")
   
   respuesta= validador(6)
   system("clear")   
   return respuesta   
  
   
   

   


   
      
   
   
   
      
      
      
 
      
   
      

      


   
   

   
