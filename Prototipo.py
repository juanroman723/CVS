from datetime import datetime


# =================
# Clases del sistema
# =================

class Sede:
    def __init__(self, id_sede, nombre, direccion, responsable):
        self.id_sede = id_sede
        self.nombre = nombre
        self.direccion = direccion
        self.responsable = responsable
        self.fecha_registro = datetime.now()

    def mostrar_sede(self):
        print("\n--- Sede ---")
        print(f"ID de sede:      {self.id_sede}")
        print(f"Nombre:          {self.nombre}")
        print(f"Dirección:       {self.direccion}")
        print(f"Responsable:     {self.responsable}")
        print(f"Fecha registro:  {self.fecha_registro.strftime('%Y-%m-%d %H:%M')}")


class Usuario:
    def __init__(self, id_usuario, nombre, rol, id_sede, usuario_acceso, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.rol = rol
        self.id_sede = id_sede
        self.usuario_acceso = usuario_acceso
        self.contrasena = contrasena
        self.fecha_registro = datetime.now()

    def mostrar_usuario(self):
        sede = buscar_sede_por_id(self.id_sede)
        nombre_sede = sede.nombre if sede else f"Sede {self.id_sede}"
        print("\n--- Usuario ---")
        print(f"ID de usuario:   {self.id_usuario}")
        print(f"Nombre:          {self.nombre}")
        print(f"Rol:             {self.rol}")
        print(f"Sede:            {nombre_sede}")
        print(f"Usuario acceso:  {self.usuario_acceso}")
        print(f"Fecha registro:  {self.fecha_registro.strftime('%Y-%m-%d %H:%M')}")


class Insumo:
    def __init__(self, id_insumo, nombre, categoria, unidad_medida, cantidad, stock_minimo, id_sede, id_usuario_responsable):
        self.id_insumo = id_insumo
        self.nombre = nombre
        self.categoria = categoria
        self.unidad_medida = unidad_medida
        self.cantidad = cantidad
        self.stock_minimo = stock_minimo
        self.id_sede = id_sede
        self.id_usuario_responsable = id_usuario_responsable
        self.fecha_actualizacion = datetime.now()
        self.alertas_stock = 0

    def mostrar_insumo(self):
        sede = buscar_sede_por_id(self.id_sede)
        nombre_sede = sede.nombre if sede else f"Sede {self.id_sede}"
        print("\n--- Insumo ---")
        print(f"ID de insumo:    {self.id_insumo}")
        print(f"Nombre:          {self.nombre}")
        print(f"Categoría:       {self.categoria}")
        print(f"Unidad medida:   {self.unidad_medida}")
        print(f"Cantidad actual: {self.cantidad}")
        print(f"Stock mínimo:    {self.stock_minimo}")
        print(f"Sede:            {nombre_sede}")
        print(f"Última act.:     {self.fecha_actualizacion.strftime('%Y-%m-%d %H:%M')}")
        if self.cantidad < self.stock_minimo:
            faltantes = self.stock_minimo - self.cantidad
            print(f"⚠ ALERTA DE STOCK: faltan {faltantes} {self.unidad_medida}")
        else:
            print("✓ Stock suficiente")


class MovimientoInventario:
    def __init__(self, id_movimiento, tipo, id_insumo, cantidad, id_usuario, motivo, id_sede):
        self.id_movimiento = id_movimiento
        self.tipo = tipo
        self.id_insumo = id_insumo
        self.cantidad = cantidad
        self.fecha = datetime.now()
        self.id_usuario = id_usuario
        self.motivo = motivo
        self.id_sede = id_sede

    def mostrar_movimiento(self):
        insumo = buscar_insumo_por_id(self.id_insumo)
        nombre_insumo = insumo.nombre if insumo else f"Insumo {self.id_insumo}"
        sede = buscar_sede_por_id(self.id_sede)
        nombre_sede = sede.nombre if sede else f"Sede {self.id_sede}"
        usuario = buscar_usuario_por_id(self.id_usuario)
        nombre_usuario = usuario.nombre if usuario else f"Usuario {self.id_usuario}"
        print("\n--- Movimiento ---")
        print(f"ID movimiento:   {self.id_movimiento}")
        print(f"Tipo:            {self.tipo}")
        print(f"Insumo:          {nombre_insumo}")
        print(f"Cantidad:        {self.cantidad}")
        print(f"Fecha:           {self.fecha.strftime('%Y-%m-%d %H:%M')}")
        print(f"Usuario:         {nombre_usuario}")
        print(f"Motivo:          {self.motivo}")
        print(f"Sede:            {nombre_sede}")


class Produccion:
    def __init__(self, id_orden, cliente, prenda, cantidad, fecha_entrega, prioridad, id_sede, id_usuario_responsable):
        self.id_orden = id_orden
        self.cliente = cliente
        self.prenda = prenda
        self.cantidad = cantidad
        self.fecha_creacion = datetime.now()
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad
        self.estado = "Pendiente"
        self.id_sede = id_sede
        self.id_usuario_responsable = id_usuario_responsable
        self.fecha_finalizacion = None

    def mostrar_orden(self):
        sede = buscar_sede_por_id(self.id_sede)
        nombre_sede = sede.nombre if sede else f"Sede {self.id_sede}"
        print("\n--- Orden de Producción ---")
        print(f"ID de orden:     {self.id_orden}")
        print(f"Cliente:         {self.cliente}")
        print(f"Prenda:          {self.prenda}")
        print(f"Cantidad:        {self.cantidad}")
        print(f"Fecha creación:  {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}")
        print(f"Fecha entrega:   {self.fecha_entrega}")
        print(f"Prioridad:       {self.prioridad}")
        print(f"Estado:          {self.estado}")
        print(f"Sede:            {nombre_sede}")

    def mostrar_orden_jefe(self):
        print("\n--- Orden de Producción ---")
        print(f"ID de orden:     {self.id_orden}")
        print(f"Prenda:          {self.prenda}")
        print(f"Cantidad:        {self.cantidad}")
        print(f"Fecha creación:  {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}")
        print(f"Fecha entrega:   {self.fecha_entrega}")
        print(f"Prioridad:       {self.prioridad}")
        print(f"Estado:          {self.estado}")


class ConsumoInsumo:
    def __init__(self, id_consumo, id_orden, id_insumo, cantidad_consumida, id_usuario):
        self.id_consumo = id_consumo
        self.id_orden = id_orden
        self.id_insumo = id_insumo
        self.cantidad_consumida = cantidad_consumida
        self.id_usuario = id_usuario
        self.fecha_consumo = datetime.now()

    def mostrar_consumo(self):
        insumo = buscar_insumo_por_id(self.id_insumo)
        nombre_insumo = insumo.nombre if insumo else f"Insumo {self.id_insumo}"
        print("\n--- Consumo de Insumo ---")
        print(f"ID consumo:      {self.id_consumo}")
        print(f"ID orden:        {self.id_orden}")
        print(f"Insumo:          {nombre_insumo}")
        print(f"Cantidad:        {self.cantidad_consumida}")
        print(f"Fecha:           {self.fecha_consumo.strftime('%Y-%m-%d %H:%M')}")


# =================
# Datos globales
# =================
sedes = []
usuarios = []
inventario = []
movimientos = []
ordenes = []
consumos = []

contador_sedes = 1
contador_usuarios = 1
contador_insumos = 1
contador_movimientos = 1
contador_ordenes = 1
contador_consumos = 1

usuario_activo = None


# =================
# Funciones de búsqueda
# =================
def buscar_sede_por_id(id_sede):
    for sede in sedes:
        if sede.id_sede == id_sede:
            return sede
    return None

def buscar_usuario_por_id(id_usuario):
    for usuario in usuarios:
        if usuario.id_usuario == id_usuario:
            return usuario
    return None

def buscar_insumo_por_id(id_insumo):
    for insumo in inventario:
        if insumo.id_insumo == id_insumo:
            return insumo
    return None

def buscar_orden_por_id(id_orden):
    for orden in ordenes:
        if orden.id_orden == id_orden:
            return orden
    return None


# =================
# Funciones de acceso
# =================
def iniciar_sesion():
    global usuario_activo
    print("\n========== INICIO DE SESIÓN ==========")
    usuario_acceso = input("Usuario: ")
    contrasena = input("Contraseña: ")
    for usuario in usuarios:
        if usuario.usuario_acceso == usuario_acceso and usuario.contrasena == contrasena:
            usuario_activo = usuario
            print(f"\n Bienvenido, {usuario.nombre} ({usuario.rol})")
            return
    print("\n Credenciales incorrectas")

def cerrar_sesion():
    global usuario_activo
    if usuario_activo:
        print(f"\n Sesión cerrada. Hasta luego, {usuario_activo.nombre}")
        usuario_activo = None
    else:
        print("\n No hay sesión activa")

def tiene_permiso(roles_permitidos):
    if usuario_activo is None:
        print("\n Debe iniciar sesión primero")
        return False
    if usuario_activo.rol not in roles_permitidos:
        print(f"\n Acceso denegado. Su rol es: {usuario_activo.rol}")
        return False
    return True

def es_su_sede(id_sede):
    # El Dueño ve todas las sedes, los demás solo la suya
    if usuario_activo.rol == "Dueño":
        return True
    return usuario_activo.id_sede == id_sede


# =================
# Reportes y KPIs
# =================
def generar_reporte_kpis():
    if not tiene_permiso(["Dueño", "Administrador"]):
        return

    print("\n========== REPORTE DE KPIs ==========")

    # Filtrar por sede si es Administrador
    def aplica_sede(id_sede):
        if usuario_activo.rol == "Dueño":
            return True
        return id_sede == usuario_activo.id_sede

    # Rotación de inventario
    print("\n--- Rotación de inventario ---")
    for insumo in inventario:
        if not aplica_sede(insumo.id_sede):
            continue
        total_consumido = sum(c.cantidad_consumida for c in consumos if c.id_insumo == insumo.id_insumo)
        print(f"  {insumo.nombre}: consumido={total_consumido} {insumo.unidad_medida}, stock actual={insumo.cantidad}")

    # Órdenes retrasadas
    print("\n--- Órdenes retrasadas ---")
    hoy = datetime.now()
    retrasadas = 0
    for orden in ordenes:
        if not aplica_sede(orden.id_sede):
            continue
        if orden.estado not in ["Terminada"]:
            try:
                fecha = datetime.strptime(orden.fecha_entrega, "%Y-%m-%d")
                if fecha < hoy:
                    print(f"  RETRASADA - Orden {orden.id_orden}: {orden.prenda} para {orden.cliente} (entrega: {orden.fecha_entrega})")
                    retrasadas += 1
            except ValueError:
                pass
    if retrasadas == 0:
        print("  No hay órdenes retrasadas")

    # Consumo promedio por insumo
    print("\n--- Consumo promedio por insumo ---")
    for insumo in inventario:
        if not aplica_sede(insumo.id_sede):
            continue
        consumos_insumo = [c.cantidad_consumida for c in consumos if c.id_insumo == insumo.id_insumo]
        if len(consumos_insumo) > 0:
            promedio = sum(consumos_insumo) / len(consumos_insumo)
            print(f"  {insumo.nombre}: promedio={promedio:.2f} {insumo.unidad_medida} ({len(consumos_insumo)} registro(s))")
        else:
            print(f"  {insumo.nombre}: sin consumos registrados")

    # Tiempo promedio de producción
    print("\n--- Tiempo promedio de producción ---")
    tiempos = []
    for orden in ordenes:
        if not aplica_sede(orden.id_sede):
            continue
        if orden.estado == "Terminada" and orden.fecha_finalizacion is not None:
            diferencia = orden.fecha_finalizacion - orden.fecha_creacion
            tiempos.append(diferencia.total_seconds() / 3600)
    if len(tiempos) > 0:
        promedio_horas = sum(tiempos) / len(tiempos)
        print(f"  Promedio: {promedio_horas:.2f} horas ({len(tiempos)} orden(es) terminada(s))")
    else:
        print("  Sin órdenes terminadas aún")

    # Frecuencia de alertas de stock mínimo
    print("\n--- Alertas de stock mínimo registradas ---")
    for insumo in inventario:
        if not aplica_sede(insumo.id_sede):
            continue
        print(f"  {insumo.nombre}: {insumo.alertas_stock} alerta(s)")

    print("\n=====================================")


# =================
# Datos de prueba iniciales
# =================
def cargar_datos_iniciales():
    global contador_sedes, contador_usuarios

    sede1 = Sede(contador_sedes, "Sede Laureles", "Calle 33 #76-40, Medellín", "Carlos Gómez")
    sedes.append(sede1)
    contador_sedes += 1

    sede2 = Sede(contador_sedes, "Sede Envigado", "Carrera 48 #32-10, Envigado", "María Ríos")
    sedes.append(sede2)
    contador_sedes += 1

    dueno = Usuario(contador_usuarios, "Juan Maintegral", "Dueño", 1, "dueno", "1234")
    usuarios.append(dueno)
    contador_usuarios += 1

    admin1 = Usuario(contador_usuarios, "Carlos Gómez", "Administrador", 1, "admin1", "1234")
    usuarios.append(admin1)
    contador_usuarios += 1

    admin2 = Usuario(contador_usuarios, "María Ríos", "Administrador", 2, "admin2", "1234")
    usuarios.append(admin2)
    contador_usuarios += 1

    print("\n Datos iniciales cargados:")
    print("  Sedes: Laureles (ID 1), Envigado (ID 2)")
    print("  Usuarios de prueba:")
    print("    dueno / 1234  → Dueño (ambas sedes)")
    print("    admin1 / 1234 → Administrador Sede Laureles")
    print("    admin2 / 1234 → Administrador Sede Envigado")


# =================
# Menú principal
# =================
print("===========================================")
print("   Sistema de Gestión - Maintegral")
print("===========================================")
cargar_datos_iniciales()

while True:
    print("\n===========================================")
    if usuario_activo:
        sede_activa = buscar_sede_por_id(usuario_activo.id_sede)
        nombre_sede = sede_activa.nombre if sede_activa else "-"
        sede_texto = "Todas las sedes" if usuario_activo.rol == "Dueño" else nombre_sede
        print(f" Sesión: {usuario_activo.nombre} | {usuario_activo.rol} | {sede_texto}")
    else:
        print(" Sin sesión activa")
    print("===========================================")
    print("1)  Iniciar sesión")
    print("2)  Cerrar sesión")
    print("--- SEDES ---")
    print("3)  Registrar sede")
    print("4)  Ver sedes")
    print("--- USUARIOS ---")
    print("5)  Registrar usuario")
    print("6)  Ver usuarios")
    print("--- INVENTARIO ---")
    print("7)  Registrar insumo")
    print("8)  Ver inventario")
    print("9)  Registrar movimiento de inventario")
    print("10) Ver movimientos")
    print("11) Reportar faltante de insumo")
    print("--- PRODUCCIÓN ---")
    print("12) Registrar orden de producción")
    print("13) Ver órdenes de producción")
    print("14) Actualizar estado de orden")
    print("15) Registrar consumo de insumo en orden")
    print("--- REPORTES ---")
    print("16) Ver reporte de KPIs")
    print("---")
    print("17) Salir")
    opcion = input("\nSeleccione una opción: ")

    # =================
    # 1. Iniciar sesión
    # =================
    if opcion == "1":
        iniciar_sesion()

    # =================
    # 2. Cerrar sesión
    # =================
    elif opcion == "2":
        cerrar_sesion()

    # =================
    # 3. Registrar sede
    # =================
    elif opcion == "3":
        if not tiene_permiso(["Dueño"]):
            continue

        nombre = input("Nombre de la sede: ")
        direccion = input("Dirección: ")
        responsable = input("Responsable: ")

        encontrado = False
        for sede in sedes:
            if sede.nombre == nombre:
                print("\n La sede ya se encuentra registrada")
                encontrado = True

        if not encontrado:
            nueva_sede = Sede(contador_sedes, nombre, direccion, responsable)
            sedes.append(nueva_sede)
            contador_sedes += 1
            print("\n Sede registrada correctamente")

    # =================
    # 4. Ver sedes
    # =================
    elif opcion == "4":
        if not tiene_permiso(["Dueño", "Administrador"]):
            continue

        sedes_visibles = sedes if usuario_activo.rol == "Dueño" else [s for s in sedes if s.id_sede == usuario_activo.id_sede]

        if len(sedes_visibles) == 0:
            print("\n No hay sedes registradas")
        else:
            for sede in sedes_visibles:
                sede.mostrar_sede()

    # =================
    # 5. Registrar usuario
    # =================
    elif opcion == "5":
        if not tiene_permiso(["Dueño", "Administrador"]):
            continue

        nombre = input("Nombre completo: ")

        if usuario_activo.rol == "Dueño":
            print("Roles disponibles: Dueño / Administrador / Jefe de Producción / Encargado de Inventario")
        else:
            print("Roles disponibles: Jefe de Producción / Encargado de Inventario")

        rol = input("Rol: ")

        roles_validos = ["Dueño", "Administrador", "Jefe de Producción", "Encargado de Inventario"]
        roles_admin = ["Jefe de Producción", "Encargado de Inventario"]

        if rol not in roles_validos:
            print("\n Rol inválido")
            continue

        if usuario_activo.rol == "Administrador" and rol not in roles_admin:
            print("\n El Administrador solo puede crear Jefes de Producción o Encargados de Inventario")
            continue

        if usuario_activo.rol == "Dueño":
            print("\nSedes disponibles:")
            for sede in sedes:
                print(f"  {sede.id_sede}) {sede.nombre}")
            id_sede = int(input("ID de sede asociada: "))
        else:
            id_sede = usuario_activo.id_sede

        usuario_acceso = input("Nombre de usuario para acceso: ")
        contrasena = input("Contraseña: ")

        encontrado = False
        for u in usuarios:
            if u.usuario_acceso == usuario_acceso:
                print("\n El nombre de usuario ya está en uso")
                encontrado = True

        if not encontrado:
            nuevo_usuario = Usuario(contador_usuarios, nombre, rol, id_sede, usuario_acceso, contrasena)
            usuarios.append(nuevo_usuario)
            contador_usuarios += 1
            print("\n Usuario registrado correctamente")

    # =================
    # 6. Ver usuarios
    # =================
    elif opcion == "6":
        if not tiene_permiso(["Dueño", "Administrador"]):
            continue

        usuarios_visibles = usuarios if usuario_activo.rol == "Dueño" else [u for u in usuarios if u.id_sede == usuario_activo.id_sede]

        if len(usuarios_visibles) == 0:
            print("\n No hay usuarios registrados")
        else:
            for usuario in usuarios_visibles:
                usuario.mostrar_usuario()

    # =================
    # 7. Registrar insumo
    # =================
    elif opcion == "7":
        if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
            continue

        nombre = input("Nombre del insumo: ")
        categoria = input("Categoría (tela/hilo/botón/cierre/otro): ")
        unidad_medida = input("Unidad de medida (metros/unidades/kilos): ")
        cantidad = int(input("Cantidad actual en stock: "))
        stock_minimo = int(input("Stock mínimo permitido: "))

        if usuario_activo.rol == "Dueño":
            print("\nSedes disponibles:")
            for sede in sedes:
                print(f"  {sede.id_sede}) {sede.nombre}")
            id_sede = int(input("ID de sede: "))
        else:
            id_sede = usuario_activo.id_sede

        encontrado = False
        for insumo in inventario:
            if insumo.nombre == nombre and insumo.id_sede == id_sede:
                print("\n El insumo ya se encuentra registrado en esta sede")
                encontrado = True

        if not encontrado:
            nuevo_insumo = Insumo(contador_insumos, nombre, categoria, unidad_medida, cantidad, stock_minimo, id_sede, usuario_activo.id_usuario)
            if cantidad < stock_minimo:
                nuevo_insumo.alertas_stock += 1
            inventario.append(nuevo_insumo)

            # Registrar movimiento de entrada inicial
            motivo = "Registro inicial de insumo"
            mov = MovimientoInventario(contador_movimientos, "Entrada", contador_insumos, cantidad, usuario_activo.id_usuario, motivo, id_sede)
            movimientos.append(mov)
            contador_movimientos += 1
            contador_insumos += 1
            print("\n Insumo registrado correctamente")

    # =================
    # 8. Ver inventario
    # =================
    elif opcion == "8":
        if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
            continue

        inventario_visible = [i for i in inventario if es_su_sede(i.id_sede)]

        if len(inventario_visible) == 0:
            print("\n Inventario vacío")
        else:
            for insumo in inventario_visible:
                insumo.mostrar_insumo()

    # =================
    # 9. Registrar movimiento de inventario
    # =================
    elif opcion == "9":
        if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
            continue

        inventario_visible = [i for i in inventario if es_su_sede(i.id_sede)]
        if len(inventario_visible) == 0:
            print("\n No hay insumos registrados en su sede")
            continue

        print("\nInsumos disponibles:")
        for i in inventario_visible:
            print(f"  {i.id_insumo}) {i.nombre} - Stock: {i.cantidad} {i.unidad_medida}")

        id_insumo = int(input("ID del insumo: "))
        insumo = buscar_insumo_por_id(id_insumo)

        if insumo is None or not es_su_sede(insumo.id_sede):
            print("\n Insumo no encontrado en su sede")
            continue

        print("Tipo de movimiento: Entrada / Salida")
        tipo = input("Tipo: ")
        if tipo not in ["Entrada", "Salida"]:
            print("\n Tipo inválido")
            continue

        cantidad = int(input("Cantidad: "))
        print("Motivos: Compra / Uso en orden / Ajuste / Pérdida / Otro")
        motivo = input("Motivo: ")

        if tipo == "Salida" and cantidad > insumo.cantidad:
            print(f"\n Stock insuficiente. Disponible: {insumo.cantidad} {insumo.unidad_medida}")
            continue

        if tipo == "Entrada":
            insumo.cantidad += cantidad
        else:
            insumo.cantidad -= cantidad

        insumo.id_usuario_responsable = usuario_activo.id_usuario
        insumo.fecha_actualizacion = datetime.now()

        if insumo.cantidad < insumo.stock_minimo:
            insumo.alertas_stock += 1
            faltantes = insumo.stock_minimo - insumo.cantidad
            print(f"\n ⚠ ALERTA: {insumo.nombre} por debajo del mínimo. Faltan {faltantes} {insumo.unidad_medida}")

        mov = MovimientoInventario(contador_movimientos, tipo, id_insumo, cantidad, usuario_activo.id_usuario, motivo, insumo.id_sede)
        movimientos.append(mov)
        contador_movimientos += 1
        print("\n Movimiento registrado correctamente")

    # =================
    # 10. Ver movimientos
    # =================
    elif opcion == "10":
        if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
            continue

        movimientos_visibles = [m for m in movimientos if es_su_sede(m.id_sede)]

        if len(movimientos_visibles) == 0:
            print("\n No hay movimientos registrados")
        else:
            for mov in movimientos_visibles:
                mov.mostrar_movimiento()

    # =================
    # 11. Reportar faltante de insumo
    # =================
    elif opcion == "11":
        if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
            continue

        inventario_visible = [i for i in inventario if es_su_sede(i.id_sede)]
        faltantes_encontrados = False

        print("\n========== REPORTE DE FALTANTES ==========")
        for insumo in inventario_visible:
            if insumo.cantidad < insumo.stock_minimo:
                faltantes = insumo.stock_minimo - insumo.cantidad
                sede = buscar_sede_por_id(insumo.id_sede)
                nombre_sede = sede.nombre if sede else f"Sede {insumo.id_sede}"
                print(f"\n ⚠ FALTANTE - {insumo.nombre}")
                print(f"   Sede: {nombre_sede}")
                print(f"   Stock actual: {insumo.cantidad} {insumo.unidad_medida}")
                print(f"   Stock mínimo: {insumo.stock_minimo} {insumo.unidad_medida}")
                print(f"   Faltan: {faltantes} {insumo.unidad_medida}")
                insumo.alertas_stock += 1
                faltantes_encontrados = True

        if not faltantes_encontrados:
            print("\n Todos los insumos están sobre el stock mínimo")
        print("==========================================")

    # =================
    # 12. Registrar orden de producción
    # =================
    elif opcion == "12":
        if not tiene_permiso(["Dueño", "Administrador", "Jefe de Producción"]):
            continue

        cliente = input("Cliente o marca: ")
        prenda = input("Prenda a confeccionar: ")
        cantidad = int(input("Cantidad a producir: "))
        fecha_entrega = input("Fecha estimada de entrega (YYYY-MM-DD): ")
        print("Prioridad: Normal / Urgente")
        prioridad = input("Prioridad: ")

        if usuario_activo.rol == "Dueño":
            print("\nSedes disponibles:")
            for sede in sedes:
                print(f"  {sede.id_sede}) {sede.nombre}")
            id_sede = int(input("ID de sede asignada: "))
        else:
            id_sede = usuario_activo.id_sede

        nueva_orden = Produccion(contador_ordenes, cliente, prenda, cantidad, fecha_entrega, prioridad, id_sede, usuario_activo.id_usuario)
        ordenes.append(nueva_orden)
        contador_ordenes += 1
        print("\n Orden registrada correctamente")

    # =================
    # 13. Ver órdenes de producción
    # =================
    elif opcion == "13":
        if not tiene_permiso(["Dueño", "Administrador", "Jefe de Producción"]):
            continue

        ordenes_visibles = [o for o in ordenes if es_su_sede(o.id_sede)]

        if len(ordenes_visibles) == 0:
            print("\n No hay órdenes registradas")
        else:
            for orden in ordenes_visibles:
                if usuario_activo.rol == "Jefe de Producción":
                    orden.mostrar_orden_jefe()
                else:
                    orden.mostrar_orden()

    # =================
    # 14. Actualizar estado de orden
    # =================
    elif opcion == "14":
        if not tiene_permiso(["Dueño", "Administrador", "Jefe de Producción"]):
            continue

        id_orden = int(input("ID de la orden: "))
        orden = buscar_orden_por_id(id_orden)

        if orden is None or not es_su_sede(orden.id_sede):
            print("\n Orden no encontrada en su sede")
            continue

        print("Estados disponibles: Pendiente / En proceso / Pausada / Terminada")
        nuevo_estado = input("Nuevo estado: ")

        if nuevo_estado not in ["Pendiente", "En proceso", "Pausada", "Terminada"]:
            print("\n Estado inválido")
            continue

        orden.estado = nuevo_estado
        if nuevo_estado == "Terminada":
            orden.fecha_finalizacion = datetime.now()

        print(f"\n Estado de la orden {orden.id_orden} actualizado a: {nuevo_estado}")

    # =================
    # 15. Registrar consumo de insumo en orden
    # =================
    elif opcion == "15":
        if not tiene_permiso(["Dueño", "Administrador", "Jefe de Producción", "Encargado de Inventario"]):
            continue

        id_orden = int(input("ID de la orden: "))
        orden = buscar_orden_por_id(id_orden)

        if orden is None or not es_su_sede(orden.id_sede):
            print("\n Orden no encontrada en su sede")
            continue

        print("\nInsumos disponibles en su sede:")
        inventario_visible = [i for i in inventario if es_su_sede(i.id_sede)]
        for i in inventario_visible:
            print(f"  {i.id_insumo}) {i.nombre} - Stock: {i.cantidad} {i.unidad_medida}")

        id_insumo = int(input("ID del insumo utilizado: "))
        insumo = buscar_insumo_por_id(id_insumo)

        if insumo is None or not es_su_sede(insumo.id_sede):
            print("\n Insumo no encontrado en su sede")
            continue

        cantidad_consumida = int(input("Cantidad consumida: "))

        if cantidad_consumida > insumo.cantidad:
            print(f"\n Stock insuficiente. Disponible: {insumo.cantidad} {insumo.unidad_medida}")
            continue

        insumo.cantidad -= cantidad_consumida
        insumo.fecha_actualizacion = datetime.now()

        if insumo.cantidad < insumo.stock_minimo:
            insumo.alertas_stock += 1
            faltantes = insumo.stock_minimo - insumo.cantidad
            print(f"\n ⚠ ALERTA: {insumo.nombre} por debajo del mínimo. Faltan {faltantes} {insumo.unidad_medida}")

        nuevo_consumo = ConsumoInsumo(contador_consumos, id_orden, id_insumo, cantidad_consumida, usuario_activo.id_usuario)
        consumos.append(nuevo_consumo)

        mov = MovimientoInventario(contador_movimientos, "Salida", id_insumo, cantidad_consumida, usuario_activo.id_usuario, "Uso en orden", insumo.id_sede)
        movimientos.append(mov)
        contador_movimientos += 1
        contador_consumos += 1
        print("\n Consumo registrado correctamente")

    # =================
    # 16. Reporte de KPIs
    # =================
    elif opcion == "16":
        generar_reporte_kpis()

    # =================
    # 17. Salir
    # =================
    elif opcion == "17":
        print("\n Saliendo del sistema. Hasta luego.")
        break

    else:
        print("\n Opción inválida")