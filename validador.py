def validador(limite):

   respuesta=(input("Selecciona un numero asociado a la categoria: "))
   while not respuesta.isnumeric() or int(respuesta) not in range(1,limite+1):
        
        respuesta=input(f"por favor elige una opción valida (1-{limite}): ")
     
     
   return int(respuesta) 
   

   
        
   
      
      
   
   