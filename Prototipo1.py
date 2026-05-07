"""Sistema de Gestión - Maintegral"""

from datetime import datetime


sedes = [
    {"id_sede": 1, "nombre": "Sede Laureles", "direccion": "Calle 33 #76-40, Medellín",   "responsable": "Carlos Gómez"},
    {"id_sede": 2, "nombre": "Sede Envigado", "direccion": "Carrera 48 #32-10, Envigado", "responsable": "María Ríos"},
    {"id_sede": 3, "nombre": "Sede Itagüí",   "direccion": "Calle 77 Sur #50-12, Itagüí", "responsable": "Luis Herrera"},
]

usuarios = [
    {"id_usuario": 1,  "nombre": "Juan Maintegral", "rol": "Dueño",                   "id_sede": 1, "usuario_acceso": "dueno",  "contrasena": "1234"},
    {"id_usuario": 2,  "nombre": "Carlos Gómez",    "rol": "Administrador",           "id_sede": 1, "usuario_acceso": "admin1", "contrasena": "1234"},
    {"id_usuario": 3,  "nombre": "María Ríos",      "rol": "Administrador",           "id_sede": 2, "usuario_acceso": "admin2", "contrasena": "1234"},
    {"id_usuario": 4,  "nombre": "Luis Herrera",    "rol": "Administrador",           "id_sede": 3, "usuario_acceso": "admin3", "contrasena": "1234"},
    {"id_usuario": 5,  "nombre": "Daniela Ospina",  "rol": "Jefe de Producción",      "id_sede": 1, "usuario_acceso": "jprod1", "contrasena": "5678"},
    {"id_usuario": 6,  "nombre": "Ricardo Salazar", "rol": "Jefe de Producción",      "id_sede": 2, "usuario_acceso": "jprod2", "contrasena": "5678"},
    {"id_usuario": 7,  "nombre": "Valentina Muñoz", "rol": "Jefe de Producción",      "id_sede": 3, "usuario_acceso": "jprod3", "contrasena": "5678"},
    {"id_usuario": 8,  "nombre": "Andrés Patiño",   "rol": "Encargado de Inventario", "id_sede": 1, "usuario_acceso": "inv1",   "contrasena": "5678"},
    {"id_usuario": 9,  "nombre": "Paola Vélez",     "rol": "Encargado de Inventario", "id_sede": 2, "usuario_acceso": "inv2",   "contrasena": "5678"},
    {"id_usuario": 10, "nombre": "Camila Torres",   "rol": "Encargado de Inventario", "id_sede": 3, "usuario_acceso": "inv3",   "contrasena": "5678"},
]

insumos = [
    {"id_insumo":  1, "nombre": "Tela algodón blanca",   "categoria": "tela",   "unidad_medida": "metros",   "cantidad": 320, "stock_minimo": 100, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  2, "nombre": "Tela denim azul",       "categoria": "tela",   "unidad_medida": "metros",   "cantidad":  85, "stock_minimo": 100, "alertas_stock": 2, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  3, "nombre": "Hilo poliéster blanco", "categoria": "hilo",   "unidad_medida": "kilos",    "cantidad":  40, "stock_minimo":  15, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  4, "nombre": "Hilo negro",            "categoria": "hilo",   "unidad_medida": "kilos",    "cantidad":  12, "stock_minimo":  15, "alertas_stock": 1, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  5, "nombre": "Botón 4 huecos blanco", "categoria": "botón",  "unidad_medida": "unidades", "cantidad":1800, "stock_minimo": 500, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  6, "nombre": "Cierre metálico 20cm",  "categoria": "cierre", "unidad_medida": "unidades", "cantidad": 290, "stock_minimo": 100, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  7, "nombre": "Entretela fusionable",  "categoria": "otro",   "unidad_medida": "metros",   "cantidad":  60, "stock_minimo":  30, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  8, "nombre": "Tela lino beige",       "categoria": "tela",   "unidad_medida": "metros",   "cantidad": 210, "stock_minimo":  80, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo":  9, "nombre": "Tela seda champán",     "categoria": "tela",   "unidad_medida": "metros",   "cantidad":  55, "stock_minimo":  60, "alertas_stock": 1, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 10, "nombre": "Hilo seda crema",       "categoria": "hilo",   "unidad_medida": "kilos",    "cantidad":  18, "stock_minimo":  10, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 11, "nombre": "Botón nácar redondo",   "categoria": "botón",  "unidad_medida": "unidades", "cantidad": 750, "stock_minimo": 300, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 12, "nombre": "Cierre invisible 25cm", "categoria": "cierre", "unidad_medida": "unidades", "cantidad": 160, "stock_minimo":  80, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 13, "nombre": "Elástico 2cm",          "categoria": "otro",   "unidad_medida": "metros",   "cantidad": 130, "stock_minimo":  50, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 14, "nombre": "Tela polar gris",        "categoria": "tela",   "unidad_medida": "metros",   "cantidad": 400, "stock_minimo": 120, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 15, "nombre": "Tela franela a cuadros", "categoria": "tela",   "unidad_medida": "metros",   "cantidad": 175, "stock_minimo":  80, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 16, "nombre": "Hilo gris oscuro",       "categoria": "hilo",   "unidad_medida": "kilos",    "cantidad":  30, "stock_minimo":  20, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 17, "nombre": "Botón metálico dorado",  "categoria": "botón",  "unidad_medida": "unidades", "cantidad": 620, "stock_minimo": 200, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 18, "nombre": "Cierre plástico 15cm",   "categoria": "cierre", "unidad_medida": "unidades", "cantidad": 410, "stock_minimo": 150, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 19, "nombre": "Cinta reflectiva",       "categoria": "otro",   "unidad_medida": "metros",   "cantidad":  25, "stock_minimo":  30, "alertas_stock": 1, "id_sede": 3, "id_usuario_responsable": 10},
]

movimientos = [
    {"id_movimiento":  1, "tipo": "Entrada", "id_insumo":  1, "cantidad":  400, "id_usuario":  8, "motivo": "Registro inicial",               "id_sede": 1},
    {"id_movimiento":  2, "tipo": "Entrada", "id_insumo":  2, "cantidad":  200, "id_usuario":  8, "motivo": "Registro inicial",               "id_sede": 1},
    {"id_movimiento":  3, "tipo": "Entrada", "id_insumo":  3, "cantidad":   50, "id_usuario":  8, "motivo": "Registro inicial",               "id_sede": 1},
    {"id_movimiento":  4, "tipo": "Entrada", "id_insumo":  4, "cantidad":   25, "id_usuario":  8, "motivo": "Registro inicial",               "id_sede": 1},
    {"id_movimiento":  5, "tipo": "Entrada", "id_insumo":  5, "cantidad": 2000, "id_usuario":  8, "motivo": "Registro inicial",               "id_sede": 1},
    {"id_movimiento":  6, "tipo": "Entrada", "id_insumo":  6, "cantidad":  350, "id_usuario":  8, "motivo": "Registro inicial",               "id_sede": 1},
    {"id_movimiento":  7, "tipo": "Entrada", "id_insumo":  7, "cantidad":   80, "id_usuario":  8, "motivo": "Registro inicial",               "id_sede": 1},
    {"id_movimiento":  8, "tipo": "Salida",  "id_insumo":  1, "cantidad":   50, "id_usuario":  8, "motivo": "Uso en orden",                   "id_sede": 1},
    {"id_movimiento":  9, "tipo": "Salida",  "id_insumo":  2, "cantidad":   40, "id_usuario":  8, "motivo": "Uso en orden",                   "id_sede": 1},
    {"id_movimiento": 10, "tipo": "Salida",  "id_insumo":  3, "cantidad":    5, "id_usuario":  8, "motivo": "Uso en orden",                   "id_sede": 1},
    {"id_movimiento": 11, "tipo": "Salida",  "id_insumo":  4, "cantidad":    8, "id_usuario":  8, "motivo": "Uso en orden",                   "id_sede": 1},
    {"id_movimiento": 12, "tipo": "Salida",  "id_insumo":  5, "cantidad":  100, "id_usuario":  8, "motivo": "Uso en orden",                   "id_sede": 1},
    {"id_movimiento": 13, "tipo": "Salida",  "id_insumo":  2, "cantidad":   75, "id_usuario":  8, "motivo": "Uso en orden",                   "id_sede": 1},
    {"id_movimiento": 14, "tipo": "Salida",  "id_insumo":  4, "cantidad":    5, "id_usuario":  8, "motivo": "Uso en orden",                   "id_sede": 1},
    {"id_movimiento": 15, "tipo": "Entrada", "id_insumo":  1, "cantidad":   50, "id_usuario":  2, "motivo": "Compra proveedor TextilAndes",    "id_sede": 1},
    {"id_movimiento": 16, "tipo": "Salida",  "id_insumo":  7, "cantidad":   20, "id_usuario":  8, "motivo": "Pérdida por daño en bodega",     "id_sede": 1},
    {"id_movimiento": 17, "tipo": "Entrada", "id_insumo":  8, "cantidad":  250, "id_usuario":  9, "motivo": "Registro inicial",               "id_sede": 2},
    {"id_movimiento": 18, "tipo": "Entrada", "id_insumo":  9, "cantidad":  100, "id_usuario":  9, "motivo": "Registro inicial",               "id_sede": 2},
    {"id_movimiento": 19, "tipo": "Entrada", "id_insumo": 10, "cantidad":   25, "id_usuario":  9, "motivo": "Registro inicial",               "id_sede": 2},
    {"id_movimiento": 20, "tipo": "Entrada", "id_insumo": 11, "cantidad": 1000, "id_usuario":  9, "motivo": "Registro inicial",               "id_sede": 2},
    {"id_movimiento": 21, "tipo": "Entrada", "id_insumo": 12, "cantidad":  200, "id_usuario":  9, "motivo": "Registro inicial",               "id_sede": 2},
    {"id_movimiento": 22, "tipo": "Entrada", "id_insumo": 13, "cantidad":  150, "id_usuario":  9, "motivo": "Registro inicial",               "id_sede": 2},
    {"id_movimiento": 23, "tipo": "Salida",  "id_insumo":  8, "cantidad":   40, "id_usuario":  9, "motivo": "Uso en orden",                   "id_sede": 2},
    {"id_movimiento": 24, "tipo": "Salida",  "id_insumo":  9, "cantidad":   45, "id_usuario":  9, "motivo": "Uso en orden",                   "id_sede": 2},
    {"id_movimiento": 25, "tipo": "Salida",  "id_insumo": 11, "cantidad":  250, "id_usuario":  9, "motivo": "Uso en orden",                   "id_sede": 2},
    {"id_movimiento": 26, "tipo": "Entrada", "id_insumo":  8, "cantidad":   30, "id_usuario":  3, "motivo": "Compra proveedor Sedas del Valle","id_sede": 2},
    {"id_movimiento": 27, "tipo": "Salida",  "id_insumo": 13, "cantidad":   20, "id_usuario":  9, "motivo": "Uso en orden",                   "id_sede": 2},
    {"id_movimiento": 28, "tipo": "Entrada", "id_insumo": 14, "cantidad":  500, "id_usuario": 10, "motivo": "Registro inicial",               "id_sede": 3},
    {"id_movimiento": 29, "tipo": "Entrada", "id_insumo": 15, "cantidad":  200, "id_usuario": 10, "motivo": "Registro inicial",               "id_sede": 3},
    {"id_movimiento": 30, "tipo": "Entrada", "id_insumo": 16, "cantidad":   40, "id_usuario": 10, "motivo": "Registro inicial",               "id_sede": 3},
    {"id_movimiento": 31, "tipo": "Entrada", "id_insumo": 17, "cantidad":  700, "id_usuario": 10, "motivo": "Registro inicial",               "id_sede": 3},
    {"id_movimiento": 32, "tipo": "Entrada", "id_insumo": 18, "cantidad":  500, "id_usuario": 10, "motivo": "Registro inicial",               "id_sede": 3},
    {"id_movimiento": 33, "tipo": "Entrada", "id_insumo": 19, "cantidad":   40, "id_usuario": 10, "motivo": "Registro inicial",               "id_sede": 3},
    {"id_movimiento": 34, "tipo": "Salida",  "id_insumo": 14, "cantidad":   60, "id_usuario": 10, "motivo": "Uso en orden",                   "id_sede": 3},
    {"id_movimiento": 35, "tipo": "Salida",  "id_insumo": 16, "cantidad":    5, "id_usuario": 10, "motivo": "Uso en orden",                   "id_sede": 3},
    {"id_movimiento": 36, "tipo": "Salida",  "id_insumo": 17, "cantidad":   80, "id_usuario": 10, "motivo": "Uso en orden",                   "id_sede": 3},
    {"id_movimiento": 37, "tipo": "Salida",  "id_insumo": 18, "cantidad":   90, "id_usuario": 10, "motivo": "Uso en orden",                   "id_sede": 3},
    {"id_movimiento": 38, "tipo": "Salida",  "id_insumo": 15, "cantidad":   25, "id_usuario": 10, "motivo": "Uso en orden",                   "id_sede": 3},
    {"id_movimiento": 39, "tipo": "Salida",  "id_insumo": 19, "cantidad":   15, "id_usuario": 10, "motivo": "Uso en orden",                   "id_sede": 3},
    {"id_movimiento": 40, "tipo": "Entrada", "id_insumo": 14, "cantidad":   60, "id_usuario":  4, "motivo": "Compra proveedor PolyTex",        "id_sede": 3},
]

ordenes = [
    {"id_orden":  1, "cliente": "Marca Urbana S.A.",      "prenda": "Camiseta algodón básica",      "cantidad": 200, "fecha_entrega": "2025-02-28", "prioridad": "Normal",  "estado": "Terminada",  "id_sede": 1, "id_usuario_responsable": 5},
    {"id_orden":  2, "cliente": "Comercial Ropa Jeans",   "prenda": "Jean clásico slim fit",        "cantidad":  80, "fecha_entrega": "2025-03-20", "prioridad": "Normal",  "estado": "Terminada",  "id_sede": 1, "id_usuario_responsable": 5},
    {"id_orden":  3, "cliente": "Tienda Moda Centro",     "prenda": "Blusa manga larga denim",      "cantidad": 120, "fecha_entrega": "2025-04-05", "prioridad": "Urgente", "estado": "Terminada",  "id_sede": 1, "id_usuario_responsable": 5},
    {"id_orden":  4, "cliente": "Exportaciones Textiles", "prenda": "Camiseta polo colores",        "cantidad": 300, "fecha_entrega": "2025-04-30", "prioridad": "Normal",  "estado": "En proceso", "id_sede": 1, "id_usuario_responsable": 5},
    {"id_orden":  5, "cliente": "Boutique Élite",         "prenda": "Vestido cóctel algodón",       "cantidad":  40, "fecha_entrega": "2025-05-10", "prioridad": "Urgente", "estado": "Pendiente",  "id_sede": 1, "id_usuario_responsable": 5},
    {"id_orden":  6, "cliente": "Casa de Modas Lucía",    "prenda": "Blusa seda manga corta",       "cantidad":  60, "fecha_entrega": "2025-03-10", "prioridad": "Normal",  "estado": "Terminada",  "id_sede": 2, "id_usuario_responsable": 6},
    {"id_orden":  7, "cliente": "Diseños Valentina",      "prenda": "Vestido lino playa",           "cantidad":  35, "fecha_entrega": "2025-03-30", "prioridad": "Normal",  "estado": "Terminada",  "id_sede": 2, "id_usuario_responsable": 6},
    {"id_orden":  8, "cliente": "Novias del Valle",       "prenda": "Traje de noche seda",          "cantidad":  15, "fecha_entrega": "2025-04-25", "prioridad": "Urgente", "estado": "En proceso", "id_sede": 2, "id_usuario_responsable": 6},
    {"id_orden":  9, "cliente": "Corporativo Textil SA",  "prenda": "Camisa ejecutiva lino",        "cantidad": 100, "fecha_entrega": "2025-05-05", "prioridad": "Normal",  "estado": "Pendiente",  "id_sede": 2, "id_usuario_responsable": 6},
    {"id_orden": 10, "cliente": "Tienda Primavera",       "prenda": "Vestido casual lino",          "cantidad":  50, "fecha_entrega": "2025-05-15", "prioridad": "Normal",  "estado": "Pendiente",  "id_sede": 2, "id_usuario_responsable": 6},
    {"id_orden": 11, "cliente": "Deportivos Norte Ltda.", "prenda": "Chaqueta polar deportiva",     "cantidad": 150, "fecha_entrega": "2025-03-05", "prioridad": "Normal",  "estado": "Terminada",  "id_sede": 3, "id_usuario_responsable": 7},
    {"id_orden": 12, "cliente": "Uniformes Colombia",     "prenda": "Camisa franela institucional", "cantidad": 200, "fecha_entrega": "2025-04-10", "prioridad": "Urgente", "estado": "Terminada",  "id_sede": 3, "id_usuario_responsable": 7},
    {"id_orden": 13, "cliente": "WorkWear SAS",           "prenda": "Overol franela seguridad",     "cantidad":  75, "fecha_entrega": "2025-04-30", "prioridad": "Normal",  "estado": "En proceso", "id_sede": 3, "id_usuario_responsable": 7},
    {"id_orden": 14, "cliente": "Escuelas Medellín",      "prenda": "Chaqueta escolar polar",       "cantidad": 350, "fecha_entrega": "2025-05-20", "prioridad": "Urgente", "estado": "En proceso", "id_sede": 3, "id_usuario_responsable": 7},
    {"id_orden": 15, "cliente": "Camping Total Ltda.",    "prenda": "Chaleco reflectivo polar",     "cantidad":  90, "fecha_entrega": "2025-05-30", "prioridad": "Normal",  "estado": "Pendiente",  "id_sede": 3, "id_usuario_responsable": 7},
]

_next_id = {"insumo": 20, "movimiento": 41, "orden": 16}

usuario_activo = None


def buscar_sede(id_sede):
    """Retorna el dict de la sede con ese id, o None si no existe."""
    return next((s for s in sedes if s["id_sede"] == id_sede), None)

def buscar_insumo(id_insumo):
    """Retorna el dict del insumo con ese id, o None si no existe."""
    return next((i for i in insumos if i["id_insumo"] == id_insumo), None)

def buscar_orden(id_orden):
    """Retorna el dict de la orden con ese id, o None si no existe."""
    return next((o for o in ordenes if o["id_orden"] == id_orden), None)

def nombre_sede(id_sede):
    """Retorna el nombre legible de una sede dado su id."""
    s = buscar_sede(id_sede)
    return s["nombre"] if s else f"Sede {id_sede}"


def iniciar_sesion():
    """Autentica al usuario comparando usuario_acceso y contrasena."""
    global usuario_activo
    print("\n========== INICIO DE SESIÓN ==========")
    acceso = input("Usuario: ").strip()
    clave  = input("Contraseña: ").strip()
    u = next((u for u in usuarios if u["usuario_acceso"] == acceso and u["contrasena"] == clave), None)
    if u:
        usuario_activo = u
        print(f"\n Bienvenido, {u['nombre']} ({u['rol']})")
    else:
        print("\n Credenciales incorrectas")

def cerrar_sesion():
    """Cierra la sesión del usuario activo."""
    global usuario_activo
    if usuario_activo:
        print(f"\n Sesión cerrada. Hasta luego, {usuario_activo['nombre']}")
        usuario_activo = None
    else:
        print("\n No hay sesión activa")

def tiene_permiso(roles_permitidos):
    """Verifica que haya sesión activa y que el rol del usuario esté en la lista permitida."""
    if not usuario_activo:
        print("\n Debe iniciar sesión primero")
        return False
    if usuario_activo["rol"] not in roles_permitidos:
        print(f"\n Acceso denegado. Su rol es: {usuario_activo['rol']}")
        return False
    return True

def es_su_sede(id_sede):
    """Retorna True si el usuario puede operar en esa sede. El Dueño accede a todas."""
    if usuario_activo["rol"] == "Dueño":
        return True
    return usuario_activo["id_sede"] == id_sede


def registrar_insumo():
    """Agrega un nuevo insumo al inventario y registra su entrada inicial como movimiento."""
    if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
        return

    nombre        = input("Nombre del insumo: ").strip()
    categoria     = input("Categoría (tela/hilo/botón/cierre/otro): ").strip()
    unidad_medida = input("Unidad de medida (metros/unidades/kilos): ").strip()
    try:
        cantidad     = int(input("Cantidad actual en stock: "))
        stock_minimo = int(input("Stock mínimo permitido: "))
    except ValueError:
        print("\n Valor numérico inválido")
        return

    if usuario_activo["rol"] == "Dueño":
        print("\nSedes disponibles:")
        for s in sedes:
            print(f"  {s['id_sede']}) {s['nombre']}")
        try:
            id_sede = int(input("ID de sede: "))
        except ValueError:
            print("\n ID inválido")
            return
    else:
        id_sede = usuario_activo["id_sede"]

    if any(i["nombre"] == nombre and i["id_sede"] == id_sede for i in insumos):
        print("\n El insumo ya se encuentra registrado en esta sede")
        return

    alertas = 1 if cantidad < stock_minimo else 0
    insumos.append({
        "id_insumo":              _next_id["insumo"],
        "nombre":                 nombre,
        "categoria":              categoria,
        "unidad_medida":          unidad_medida,
        "cantidad":               cantidad,
        "stock_minimo":           stock_minimo,
        "alertas_stock":          alertas,
        "id_sede":                id_sede,
        "id_usuario_responsable": usuario_activo["id_usuario"],
    })
    movimientos.append({
        "id_movimiento": _next_id["movimiento"],
        "tipo": "Entrada", "id_insumo": _next_id["insumo"],
        "cantidad": cantidad, "id_usuario": usuario_activo["id_usuario"],
        "motivo": "Registro inicial de insumo", "id_sede": id_sede,
    })
    _next_id["insumo"]     += 1
    _next_id["movimiento"] += 1
    print("\n Insumo registrado correctamente")
    if alertas:
        print(f" ⚠ ALERTA: stock inicial por debajo del mínimo, faltan {stock_minimo - cantidad} {unidad_medida}")


def ver_inventario():
    """Muestra todos los insumos de la sede del usuario con su estado de stock."""
    if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
        return

    visibles = [i for i in insumos if es_su_sede(i["id_sede"])]
    if not visibles:
        print("\n Inventario vacío")
        return

    for i in visibles:
        estado = "⚠ ALERTA" if i["cantidad"] < i["stock_minimo"] else "✓ OK"
        print(f"\n--- Insumo ---")
        print(f"  ID:           {i['id_insumo']}")
        print(f"  Nombre:       {i['nombre']}")
        print(f"  Categoría:    {i['categoria']}")
        print(f"  Unidad:       {i['unidad_medida']}")
        print(f"  Stock actual: {i['cantidad']}  {estado}")
        print(f"  Stock mínimo: {i['stock_minimo']}")
        print(f"  Sede:         {nombre_sede(i['id_sede'])}")


def registrar_movimiento():
    """Registra una entrada o salida de un insumo y actualiza su cantidad en inventario."""
    if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
        return

    visibles = [i for i in insumos if es_su_sede(i["id_sede"])]
    if not visibles:
        print("\n No hay insumos en su sede")
        return

    print("\nInsumos disponibles:")
    for i in visibles:
        print(f"  {i['id_insumo']}) {i['nombre']} - Stock: {i['cantidad']} {i['unidad_medida']}")

    try:
        id_insumo = int(input("ID del insumo: "))
    except ValueError:
        print("\n ID inválido")
        return

    insumo = buscar_insumo(id_insumo)
    if not insumo or not es_su_sede(insumo["id_sede"]):
        print("\n Insumo no encontrado en su sede")
        return

    tipo = input("Tipo (Entrada / Salida): ").strip()
    if tipo not in ["Entrada", "Salida"]:
        print("\n Tipo inválido")
        return

    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("\n Cantidad inválida")
        return

    if tipo == "Salida" and cantidad > insumo["cantidad"]:
        print(f"\n Stock insuficiente. Disponible: {insumo['cantidad']} {insumo['unidad_medida']}")
        return

    print("Motivos: Compra / Uso en orden / Ajuste / Pérdida / Otro")
    motivo = input("Motivo: ").strip()

    insumo["cantidad"] += cantidad if tipo == "Entrada" else -cantidad
    insumo["id_usuario_responsable"] = usuario_activo["id_usuario"]

    if insumo["cantidad"] < insumo["stock_minimo"]:
        insumo["alertas_stock"] += 1
        faltantes = insumo["stock_minimo"] - insumo["cantidad"]
        print(f"\n ⚠ ALERTA: {insumo['nombre']} por debajo del mínimo. Faltan {faltantes} {insumo['unidad_medida']}")

    movimientos.append({
        "id_movimiento": _next_id["movimiento"],
        "tipo": tipo, "id_insumo": id_insumo, "cantidad": cantidad,
        "id_usuario": usuario_activo["id_usuario"], "motivo": motivo,
        "id_sede": insumo["id_sede"],
    })
    _next_id["movimiento"] += 1
    print("\n Movimiento registrado correctamente")


def reportar_faltantes():
    """Lista todos los insumos de la sede cuya cantidad está por debajo del stock mínimo."""
    if not tiene_permiso(["Dueño", "Administrador", "Encargado de Inventario"]):
        return

    faltantes = [i for i in insumos if es_su_sede(i["id_sede"]) and i["cantidad"] < i["stock_minimo"]]

    print("\n========== REPORTE DE FALTANTES ==========")
    if not faltantes:
        print("\n Todos los insumos están sobre el stock mínimo")
    else:
        for i in faltantes:
            i["alertas_stock"] += 1
            diff = i["stock_minimo"] - i["cantidad"]
            print(f"\n ⚠ FALTANTE - {i['nombre']}")
            print(f"   Sede:          {nombre_sede(i['id_sede'])}")
            print(f"   Stock actual:  {i['cantidad']} {i['unidad_medida']}")
            print(f"   Stock mínimo:  {i['stock_minimo']} {i['unidad_medida']}")
            print(f"   Faltan:        {diff} {i['unidad_medida']}")
    print("==========================================")


def registrar_orden():
    """Crea una nueva orden de producción con estado inicial Pendiente."""
    if not tiene_permiso(["Dueño", "Administrador", "Jefe de Producción"]):
        return

    cliente       = input("Cliente o marca: ").strip()
    prenda        = input("Prenda a confeccionar: ").strip()
    try:
        cantidad  = int(input("Cantidad a producir: "))
    except ValueError:
        print("\n Cantidad inválida")
        return

    fecha_entrega = input("Fecha estimada de entrega (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(fecha_entrega, "%Y-%m-%d")
    except ValueError:
        print("\n Formato de fecha inválido (use YYYY-MM-DD)")
        return

    prioridad = input("Prioridad (Normal / Urgente): ").strip()
    if prioridad not in ["Normal", "Urgente"]:
        print("\n Prioridad inválida")
        return

    if usuario_activo["rol"] == "Dueño":
        print("\nSedes disponibles:")
        for s in sedes:
            print(f"  {s['id_sede']}) {s['nombre']}")
        try:
            id_sede = int(input("ID de sede asignada: "))
        except ValueError:
            print("\n ID inválido")
            return
    else:
        id_sede = usuario_activo["id_sede"]

    ordenes.append({
        "id_orden":               _next_id["orden"],
        "cliente":                cliente,
        "prenda":                 prenda,
        "cantidad":               cantidad,
        "fecha_entrega":          fecha_entrega,
        "prioridad":              prioridad,
        "estado":                 "Pendiente",
        "id_sede":                id_sede,
        "id_usuario_responsable": usuario_activo["id_usuario"],
    })
    _next_id["orden"] += 1
    print("\n Orden registrada correctamente")


def ver_ordenes():
    """Muestra las órdenes de producción de la sede. El Jefe de Producción no ve el cliente ni la sede."""
    if not tiene_permiso(["Dueño", "Administrador", "Jefe de Producción"]):
        return

    es_jefe  = usuario_activo["rol"] == "Jefe de Producción"
    visibles = [o for o in ordenes if es_su_sede(o["id_sede"])]

    if not visibles:
        print("\n No hay órdenes registradas")
        return

    for o in visibles:
        print(f"\n--- Orden de Producción ---")
        print(f"  ID:             {o['id_orden']}")
        if not es_jefe:
            print(f"  Cliente:        {o['cliente']}")
        print(f"  Prenda:         {o['prenda']}")
        print(f"  Cantidad:       {o['cantidad']}")
        print(f"  Fecha entrega:  {o['fecha_entrega']}")
        print(f"  Prioridad:      {o['prioridad']}")
        print(f"  Estado:         {o['estado']}")
        if not es_jefe:
            print(f"  Sede:           {nombre_sede(o['id_sede'])}")


def gestionar_produccion():
    """Actualiza el estado de una orden de producción existente."""
    if not tiene_permiso(["Dueño", "Administrador", "Jefe de Producción"]):
        return

    try:
        id_orden = int(input("ID de la orden a actualizar: "))
    except ValueError:
        print("\n ID inválido")
        return

    orden = buscar_orden(id_orden)
    if not orden or not es_su_sede(orden["id_sede"]):
        print("\n Orden no encontrada en su sede")
        return

    print(f"\n Estado actual: {orden['estado']}")
    print("Estados disponibles: Pendiente / En proceso / Pausada / Terminada")
    nuevo_estado = input("Nuevo estado: ").strip()

    if nuevo_estado not in ["Pendiente", "En proceso", "Pausada", "Terminada"]:
        print("\n Estado inválido")
        return

    orden["estado"] = nuevo_estado
    print(f"\n Estado de la orden {id_orden} actualizado a: {nuevo_estado}")


def mostrar_menu():
    """Imprime el menú principal con el estado de la sesión activa."""
    print("\n===========================================")
    if usuario_activo:
        sede_txt = "Todas las sedes" if usuario_activo["rol"] == "Dueño" else nombre_sede(usuario_activo["id_sede"])
        print(f" Sesión: {usuario_activo['nombre']} | {usuario_activo['rol']} | {sede_txt}")
    else:
        print(" Sin sesión activa")
    print("===========================================")
    print("1)  Iniciar sesión")
    print("2)  Cerrar sesión")
    print("--- INVENTARIO ---")
    print("3)  Registrar insumo")
    print("4)  Ver inventario")
    print("5)  Registrar movimiento (entrada/salida)")
    print("6)  Reportar faltante de insumo")
    print("--- PRODUCCIÓN ---")
    print("7)  Registrar orden de producción")
    print("8)  Ver órdenes de producción")
    print("9)  Actualizar estado de orden")
    print("---")
    print("10) Salir")


def main():
    """Punto de entrada del sistema. Carga el menú principal en un bucle hasta que el usuario salga."""
    print("===========================================")
    print("   Sistema de Gestión - Maintegral")
    print("===========================================")
    print("\n Usuarios disponibles:")
    print("  dueno  / 1234  → Dueño       (todas las sedes)")
    print("  admin1 / 1234  → Admin        Sede Laureles")
    print("  admin2 / 1234  → Admin        Sede Envigado")
    print("  admin3 / 1234  → Admin        Sede Itagüí")
    print("  jprod1 / 5678  → Jefe Prod.   Sede Laureles")
    print("  jprod2 / 5678  → Jefe Prod.   Sede Envigado")
    print("  jprod3 / 5678  → Jefe Prod.   Sede Itagüí")
    print("  inv1   / 5678  → Inventario   Sede Laureles")
    print("  inv2   / 5678  → Inventario   Sede Envigado")
    print("  inv3   / 5678  → Inventario   Sede Itagüí")

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if   opcion == "1":  iniciar_sesion()
        elif opcion == "2":  cerrar_sesion()
        elif opcion == "3":  registrar_insumo()
        elif opcion == "4":  ver_inventario()
        elif opcion == "5":  registrar_movimiento()
        elif opcion == "6":  reportar_faltantes()
        elif opcion == "7":  registrar_orden()
        elif opcion == "8":  ver_ordenes()
        elif opcion == "9":  gestionar_produccion()
        elif opcion == "10":
            print("\n Saliendo del sistema. Hasta luego.")
            break
        else:
            print("\n Opción inválida")


if __name__ == "__main__":
    main()