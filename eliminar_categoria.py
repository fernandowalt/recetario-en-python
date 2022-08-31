
import shutil

def eliminar_categoria(categoria):
   print(categoria)
   shutil.rmtree(categoria['path'])
   
   print(f"la categoria {categoria['name']} fue eliminada")
   input("presione enter para volver al menú principal: ")
  
   


   
   
   