from datetime import datetime
class Insumo:

    def __init__(self, id_insumo, nombre, categoria, unidad_medida, cantidad, stock_minimo, sede, responsable):
        self.id_insumo = id_insumo
        self.nombre = nombre
        self.categoria = categoria
        self.unidad_medida = unidad_medida
        self.cantidad = cantidad
        self.stock_minimo = stock_minimo
        self.sede = sede
        self.responsable = responsable
        self.fecha_actualizacion = datetime.now()
    def mostrar_insumo(self):
        print ("\nInsumo")

        print (f"ID de insumo: {self.id_insumo}")
        print (f"Nombre: {self.nombre}")
        print (f"Categoría: {self.categoria}")
        print (f"Unidad de medida: {self.unidad_medida} ")
        print (f"Cantidad: {self.cantidad}")
        print (f"Stock mínimo: {self.stock_minimo}")
        print (f"Sede: {self.sede}")
        print (f"Responsable: {self.responsable}")
        print (f"Ultima actualización: {self.fecha_actualizacion}")

        if self.cantidad < self.stock_minimo:
            faltantes = self.stock_minimo - self.cantidad

            print(f"ALERTA DE STOCK: faltan {faltantes} unidades")
        else:
            print ("Stock suficiente")


class Produccion:
    def __init__(self, id_orden, cliente, prenda, cantidad, fecha_entrega, prioridad, sede, responsable):
        self.id_orden = id_orden
        self.cliente = cliente
        self.prenda = prenda
        self.cantidad = cantidad
        self.fecha_creacion = datetime.now()
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad
        self.estado = "Pendiente"
        self.sede = sede
        self.responsable = responsable

    def mostrar_orden(self):
        print ("\n Orden")

        print(f"ID de orden: {self.id_orden}")
        print(f"Cliente: {self.cliente}")
        print(f"Prenda: {self.prenda}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Fecha de creación: {self.fecha_creacion}")
        print(f"Fecha de entrega: {self.fecha_entrega}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Estado: {self.estado}")
        print(f"Sede: {self.sede}")
        print(f"Responsable: {self.responsable}")

inventario = []
ordenes = []

contador_insumos = 1
contador_ordenes = 1

while True:
    print ("Bienvenido al inventario de Maintegral")
    print ("1) Registrar insumo")
    print ("2) Ver inventario")
    print("3) Registrar orden")
    print("4) Ver ordenes")
    print("5) Salir")
    opcion = input("Seleccione una opcion: ")
    #   =================
    #   Registrar insumo
    #   =================
    if opcion == "1":
        nombre = input("Nombre del insumo")
        categoria = input("Categoria: ")
        unidad_medida = input("Unidad de medida: ")
        cantidad = int(input("Cantidad actual: "))
        stock_minimo = int(input("Stock minimo: "))
        sede = input("Sede: ")
        responsable = input("Responsable: ")
        encontrado = False

        # Validar si existe
        for insumo in inventario:
            if insumo.nombre == nombre:
                print("\n El insumo ya se encuentra registrado en el sistema")
        
        nuevo_Insumo = Insumo(contador_insumos, nombre, categoria, unidad_medida, cantidad, stock_minimo, sede, responsable)
        inventario.append(nuevo_Insumo)

        contador_insumos += 1

        print("\n Insumo registrado correctamente")
    
    #Ver inventario
    elif opcion == "2":

        if len(inventario) == 0:
            print("\n Inventario vacio")
        
        else:
            print("Inventario \n")

            for insumo in inventario:
                insumo.mostrar_insumo()
    
    #Registrar orden
    elif opcion == "3":
        cliente = input("Cliente o marca: ")
        prenda = input("Prenda a confeccionar: ")
        cantidad = int(input("Cantidad a producir: "))
        fecha_entrega = input("Fecha estimada de entrega: ")
        prioridad = input("Prioridad (Normal/Urgente): ")
        sede = input("Sede asignada: ")
        responsable = input("Responsable: ")

        nueva_orden = Produccion(contador_ordenes, cliente, prenda, cantidad, fecha_entrega, prioridad, sede, responsable)
        ordenes.append(nueva_orden)

        contador_ordenes +=1
        
        print("\n Orden registrada correctamente")

    #Ver ordenes
    elif opcion == "4":
        if len(ordenes) == 0:
            print("\n No hay ordenes")
        else:
            print("Ordenes")
            for orden in ordenes:
                orden.mostrar_orden()
    
    #Salir
    elif opcion == "5":
        print("\n Saliendo del sistema...")
        break

    #Opcion invalida
    else:
        print("\n Opcion inválida")