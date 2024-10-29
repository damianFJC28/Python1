class Tarea:

    def __init__(self,titulo,descripcion,estado="pendiente"):
        self.titulo=titulo
        self.descripcion=descripcion
        self.estado=estado
def mostrar_menu():
    print("Sistema Gestion de  tareas")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por titulo")
    print("4. Actualizar estado de la tarea a 'completada' ")
    print("5. Eliminar tarea por titulo")
    print("6. Salir")

lista_tareas=[]

while True:
    mostrar_menu()
    opcion=input("Elige una opcion: ")

    if opcion=="6":
        print("Saliendo del programa: ")
        break

    if opcion=="1":
        titulo=input("Ingrese el titulo de la tarea: ")
        try:
            descripcion=str(input("ingrese la descripcion de la tarea: "))
            estado = str(input("ingrese el estado de la tarea: "))
            tarea= Tarea(titulo,descripcion,estado)
            lista_tareas.append(tarea)

            print("tarea agregada con exito: ")
        except ValueError:
            print("Error: Entrada no valida")

    elif opcion=="2":
        for t in lista_tareas:
            print(f"Titulo:{t.titulo},Descripcion:{t.descripcion},Estado:{t.estado}")
    elif opcion=="3":
         titulo=input("ingrese el titulo de la tarea a buscar: ")
         encontrado=False
         for t in lista_tareas:
             if t.titulo==titulo:
                 print(f"Titulo:{t.titulo},Descripcion:{t.descripcion},Estado:{t.estado}")
                 encontrado=True
                 break
             if not encontrado:
                 print("tarea no encontrada")

    elif opcion=="4":
        try:
            estado=str(input("ingrese el titulo de la tarea que desea marcar como completada: "))
            for t in lista_tareas:
                if t.titulo==titulo:
                    t.completado=estado
                    print("el estado de la tarea se cambio a completada")
                    break
        except ValueError:
            print("Error: Entrada no valida")

    elif opcion == "5":
        titulo = input("ingrese el titulo de la tarea q desea  eliminar:")
        for t in lista_tareas:
            if t.titulo == titulo:
                lista_tareas.remove(t)
                print("el titulo de la tarea fue eliminado con exito.")
                break

    else:
        print("titulo de la tarea no encontrado.")


