class Contacto: #definimos la calse y el nombre de la clase
    def __init__(self,nombre, telefono):#inicializamos clase con sus atributos
       self.nombre=nombre
       self.telefono=telefono

def mostrar_menu():
    print("Gestion de contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

contactos=[]

while True:
      mostrar_menu()
      opcion=input("Elige una opcion:")

      if opcion=="5":
        print("Saliendo del programa.")
        break

      if opcion=="1":
         nombre=input("Ingresa el nombre:")
         telefono=input("Ingresa el telefono:")
         contacto=Contacto(nombre, telefono)
         contactos.append(contacto)
         print("contacto agregado.")

      elif opcion=="2":
         for c in contactos:
             print(f"Nombre: {c.nombre}, telefono: {c.telefono}")

      elif opcion=="3":
         nombre=input("Ingrese el nombre a buscar:")
         encontrado =False
         for c in contactos:
             if c.nombre==nombre:
                 print(f"Nombre: {c.nombre}, telefono: {c.telefono}")
                 encontrado=True
                 break

         if not encontrado:
             print("contacto no encontrado.")

      elif opcion=="4":
         nombre=input("ingrese el nombre a eliminar:")
         for c in contactos:
             if c.nombre==nombre:
                 contactos.remove(c)
                 print("contacto eliminado.")
                 break

      else:
        print("opcion no valida. Intentelo denuevo.")

