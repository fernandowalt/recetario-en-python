from pathlib import Path

def eliminar_receta(receta):
   Path(receta['path']).unlink()
   
   print(f"la receta que se encontraba en {receta['path']} fue eliminada.")
   input("presione enter para volver al menú principal")
   

   
 
   
   