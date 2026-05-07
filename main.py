"""
Sistema de Gestión - Maintegral
API REST con FastAPI · datos en memoria (listas)
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(title="Maintegral API", version="1.0.0")

# Permitir llamadas desde Bubble (CORS abierto)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# DATOS EN MEMORIA
# ============================================================

sedes = [
    {"id_sede": 1, "nombre": "Sede Laureles", "direccion": "Calle 33 #76-40, Medellín",   "responsable": "Carlos Gómez"},
    {"id_sede": 2, "nombre": "Sede Envigado", "direccion": "Carrera 48 #32-10, Envigado", "responsable": "María Ríos"},
    {"id_sede": 3, "nombre": "Sede Itagüí",   "direccion": "Calle 77 Sur #50-12, Itagüí", "responsable": "Luis Herrera"},
]

usuarios = [
    {"id_usuario": 1,  "nombre": "Juan Maintegral", "rol": "Dueño",                   "id_sede": 1, "usuario_acceso": "dueno",  "contrasena": "1234"},
    {"id_usuario": 2,  "nombre": "Carlos Gómez",    "rol": "Administrador",            "id_sede": 1, "usuario_acceso": "admin1", "contrasena": "1234"},
    {"id_usuario": 3,  "nombre": "María Ríos",      "rol": "Administrador",            "id_sede": 2, "usuario_acceso": "admin2", "contrasena": "1234"},
    {"id_usuario": 4,  "nombre": "Luis Herrera",    "rol": "Administrador",            "id_sede": 3, "usuario_acceso": "admin3", "contrasena": "1234"},
    {"id_usuario": 5,  "nombre": "Daniela Ospina",  "rol": "Jefe de Producción",       "id_sede": 1, "usuario_acceso": "jprod1", "contrasena": "5678"},
    {"id_usuario": 6,  "nombre": "Ricardo Salazar", "rol": "Jefe de Producción",       "id_sede": 2, "usuario_acceso": "jprod2", "contrasena": "5678"},
    {"id_usuario": 7,  "nombre": "Valentina Muñoz", "rol": "Jefe de Producción",       "id_sede": 3, "usuario_acceso": "jprod3", "contrasena": "5678"},
    {"id_usuario": 8,  "nombre": "Andrés Patiño",   "rol": "Encargado de Inventario",  "id_sede": 1, "usuario_acceso": "inv1",   "contrasena": "5678"},
    {"id_usuario": 9,  "nombre": "Paola Vélez",     "rol": "Encargado de Inventario",  "id_sede": 2, "usuario_acceso": "inv2",   "contrasena": "5678"},
    {"id_usuario": 10, "nombre": "Camila Torres",   "rol": "Encargado de Inventario",  "id_sede": 3, "usuario_acceso": "inv3",   "contrasena": "5678"},
]

insumos = [
    {"id_insumo":  1, "nombre": "Tela algodón blanca",    "categoria": "tela",   "unidad_medida": "metros",   "cantidad": 320, "stock_minimo": 100, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  2, "nombre": "Tela denim azul",        "categoria": "tela",   "unidad_medida": "metros",   "cantidad":  85, "stock_minimo": 100, "alertas_stock": 2, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  3, "nombre": "Hilo poliéster blanco",  "categoria": "hilo",   "unidad_medida": "kilos",    "cantidad":  40, "stock_minimo":  15, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  4, "nombre": "Hilo negro",             "categoria": "hilo",   "unidad_medida": "kilos",    "cantidad":  12, "stock_minimo":  15, "alertas_stock": 1, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  5, "nombre": "Botón 4 huecos blanco",  "categoria": "botón",  "unidad_medida": "unidades", "cantidad":1800, "stock_minimo": 500, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  6, "nombre": "Cierre metálico 20cm",   "categoria": "cierre", "unidad_medida": "unidades", "cantidad": 290, "stock_minimo": 100, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  7, "nombre": "Entretela fusionable",   "categoria": "otro",   "unidad_medida": "metros",   "cantidad":  60, "stock_minimo":  30, "alertas_stock": 0, "id_sede": 1, "id_usuario_responsable": 8},
    {"id_insumo":  8, "nombre": "Tela lino beige",        "categoria": "tela",   "unidad_medida": "metros",   "cantidad": 210, "stock_minimo":  80, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo":  9, "nombre": "Tela seda champán",      "categoria": "tela",   "unidad_medida": "metros",   "cantidad":  55, "stock_minimo":  60, "alertas_stock": 1, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 10, "nombre": "Hilo seda crema",        "categoria": "hilo",   "unidad_medida": "kilos",    "cantidad":  18, "stock_minimo":  10, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 11, "nombre": "Botón nácar redondo",    "categoria": "botón",  "unidad_medida": "unidades", "cantidad": 750, "stock_minimo": 300, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 12, "nombre": "Cierre invisible 25cm",  "categoria": "cierre", "unidad_medida": "unidades", "cantidad": 160, "stock_minimo":  80, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 13, "nombre": "Elástico 2cm",           "categoria": "otro",   "unidad_medida": "metros",   "cantidad": 130, "stock_minimo":  50, "alertas_stock": 0, "id_sede": 2, "id_usuario_responsable": 9},
    {"id_insumo": 14, "nombre": "Tela polar gris",        "categoria": "tela",   "unidad_medida": "metros",   "cantidad": 400, "stock_minimo": 120, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 15, "nombre": "Tela franela a cuadros", "categoria": "tela",   "unidad_medida": "metros",   "cantidad": 175, "stock_minimo":  80, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 16, "nombre": "Hilo gris oscuro",       "categoria": "hilo",   "unidad_medida": "kilos",    "cantidad":  30, "stock_minimo":  20, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 17, "nombre": "Botón metálico dorado",  "categoria": "botón",  "unidad_medida": "unidades", "cantidad": 620, "stock_minimo": 200, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 18, "nombre": "Cierre plástico 15cm",   "categoria": "cierre", "unidad_medida": "unidades", "cantidad": 410, "stock_minimo": 150, "alertas_stock": 0, "id_sede": 3, "id_usuario_responsable": 10},
    {"id_insumo": 19, "nombre": "Cinta reflectiva",       "categoria": "otro",   "unidad_medida": "metros",   "cantidad":  25, "stock_minimo":  30, "alertas_stock": 1, "id_sede": 3, "id_usuario_responsable": 10},
]

movimientos = [
    {"id_movimiento":  1, "tipo": "Entrada", "id_insumo":  1, "cantidad":  400, "id_usuario":  8, "motivo": "Registro inicial",                "id_sede": 1, "fecha": "2025-01-10 08:30:00"},
    {"id_movimiento":  2, "tipo": "Entrada", "id_insumo":  2, "cantidad":  200, "id_usuario":  8, "motivo": "Registro inicial",                "id_sede": 1, "fecha": "2025-01-10 08:35:00"},
    {"id_movimiento":  3, "tipo": "Entrada", "id_insumo":  3, "cantidad":   50, "id_usuario":  8, "motivo": "Registro inicial",                "id_sede": 1, "fecha": "2025-01-10 08:40:00"},
    {"id_movimiento":  4, "tipo": "Entrada", "id_insumo":  4, "cantidad":   25, "id_usuario":  8, "motivo": "Registro inicial",                "id_sede": 1, "fecha": "2025-01-10 08:45:00"},
    {"id_movimiento":  5, "tipo": "Entrada", "id_insumo":  5, "cantidad": 2000, "id_usuario":  8, "motivo": "Registro inicial",                "id_sede": 1, "fecha": "2025-01-10 09:00:00"},
    {"id_movimiento":  6, "tipo": "Entrada", "id_insumo":  6, "cantidad":  350, "id_usuario":  8, "motivo": "Registro inicial",                "id_sede": 1, "fecha": "2025-01-10 09:05:00"},
    {"id_movimiento":  7, "tipo": "Entrada", "id_insumo":  7, "cantidad":   80, "id_usuario":  8, "motivo": "Registro inicial",                "id_sede": 1, "fecha": "2025-01-10 09:10:00"},
    {"id_movimiento":  8, "tipo": "Salida",  "id_insumo":  1, "cantidad":   50, "id_usuario":  8, "motivo": "Uso en orden",                    "id_sede": 1, "fecha": "2025-02-15 14:00:00"},
    {"id_movimiento":  9, "tipo": "Salida",  "id_insumo":  2, "cantidad":   40, "id_usuario":  8, "motivo": "Uso en orden",                    "id_sede": 1, "fecha": "2025-02-20 10:00:00"},
    {"id_movimiento": 10, "tipo": "Salida",  "id_insumo":  3, "cantidad":    5, "id_usuario":  8, "motivo": "Uso en orden",                    "id_sede": 1, "fecha": "2025-03-01 11:00:00"},
    {"id_movimiento": 11, "tipo": "Salida",  "id_insumo":  4, "cantidad":    8, "id_usuario":  8, "motivo": "Uso en orden",                    "id_sede": 1, "fecha": "2025-03-05 09:00:00"},
    {"id_movimiento": 12, "tipo": "Salida",  "id_insumo":  5, "cantidad":  100, "id_usuario":  8, "motivo": "Uso en orden",                    "id_sede": 1, "fecha": "2025-03-10 15:00:00"},
    {"id_movimiento": 13, "tipo": "Salida",  "id_insumo":  2, "cantidad":   75, "id_usuario":  8, "motivo": "Uso en orden",                    "id_sede": 1, "fecha": "2025-04-10 10:00:00"},
    {"id_movimiento": 14, "tipo": "Salida",  "id_insumo":  4, "cantidad":    5, "id_usuario":  8, "motivo": "Uso en orden",                    "id_sede": 1, "fecha": "2025-04-15 08:30:00"},
    {"id_movimiento": 15, "tipo": "Entrada", "id_insumo":  1, "cantidad":   50, "id_usuario":  2, "motivo": "Compra proveedor TextilAndes",     "id_sede": 1, "fecha": "2025-04-01 08:00:00"},
    {"id_movimiento": 16, "tipo": "Salida",  "id_insumo":  7, "cantidad":   20, "id_usuario":  8, "motivo": "Pérdida por daño en bodega",      "id_sede": 1, "fecha": "2025-04-18 12:00:00"},
    {"id_movimiento": 17, "tipo": "Entrada", "id_insumo":  8, "cantidad":  250, "id_usuario":  9, "motivo": "Registro inicial",                "id_sede": 2, "fecha": "2025-01-12 09:00:00"},
    {"id_movimiento": 18, "tipo": "Entrada", "id_insumo":  9, "cantidad":  100, "id_usuario":  9, "motivo": "Registro inicial",                "id_sede": 2, "fecha": "2025-01-12 09:05:00"},
    {"id_movimiento": 19, "tipo": "Entrada", "id_insumo": 10, "cantidad":   25, "id_usuario":  9, "motivo": "Registro inicial",                "id_sede": 2, "fecha": "2025-01-12 09:10:00"},
    {"id_movimiento": 20, "tipo": "Entrada", "id_insumo": 11, "cantidad": 1000, "id_usuario":  9, "motivo": "Registro inicial",                "id_sede": 2, "fecha": "2025-01-12 09:15:00"},
    {"id_movimiento": 21, "tipo": "Entrada", "id_insumo": 12, "cantidad":  200, "id_usuario":  9, "motivo": "Registro inicial",                "id_sede": 2, "fecha": "2025-01-12 09:20:00"},
    {"id_movimiento": 22, "tipo": "Entrada", "id_insumo": 13, "cantidad":  150, "id_usuario":  9, "motivo": "Registro inicial",                "id_sede": 2, "fecha": "2025-01-12 09:25:00"},
    {"id_movimiento": 23, "tipo": "Salida",  "id_insumo":  8, "cantidad":   40, "id_usuario":  9, "motivo": "Uso en orden",                    "id_sede": 2, "fecha": "2025-02-18 10:00:00"},
    {"id_movimiento": 24, "tipo": "Salida",  "id_insumo":  9, "cantidad":   45, "id_usuario":  9, "motivo": "Uso en orden",                    "id_sede": 2, "fecha": "2025-03-08 11:00:00"},
    {"id_movimiento": 25, "tipo": "Salida",  "id_insumo": 11, "cantidad":  250, "id_usuario":  9, "motivo": "Uso en orden",                    "id_sede": 2, "fecha": "2025-03-20 14:00:00"},
    {"id_movimiento": 26, "tipo": "Entrada", "id_insumo":  8, "cantidad":   30, "id_usuario":  3, "motivo": "Compra proveedor Sedas del Valle", "id_sede": 2, "fecha": "2025-04-05 08:00:00"},
    {"id_movimiento": 27, "tipo": "Salida",  "id_insumo": 13, "cantidad":   20, "id_usuario":  9, "motivo": "Uso en orden",                    "id_sede": 2, "fecha": "2025-04-22 09:00:00"},
    {"id_movimiento": 28, "tipo": "Entrada", "id_insumo": 14, "cantidad":  500, "id_usuario": 10, "motivo": "Registro inicial",                "id_sede": 3, "fecha": "2025-01-20 08:30:00"},
    {"id_movimiento": 29, "tipo": "Entrada", "id_insumo": 15, "cantidad":  200, "id_usuario": 10, "motivo": "Registro inicial",                "id_sede": 3, "fecha": "2025-01-20 08:35:00"},
    {"id_movimiento": 30, "tipo": "Entrada", "id_insumo": 16, "cantidad":   40, "id_usuario": 10, "motivo": "Registro inicial",                "id_sede": 3, "fecha": "2025-01-20 08:40:00"},
    {"id_movimiento": 31, "tipo": "Entrada", "id_insumo": 17, "cantidad":  700, "id_usuario": 10, "motivo": "Registro inicial",                "id_sede": 3, "fecha": "2025-01-20 08:45:00"},
    {"id_movimiento": 32, "tipo": "Entrada", "id_insumo": 18, "cantidad":  500, "id_usuario": 10, "motivo": "Registro inicial",                "id_sede": 3, "fecha": "2025-01-20 08:50:00"},
    {"id_movimiento": 33, "tipo": "Entrada", "id_insumo": 19, "cantidad":   40, "id_usuario": 10, "motivo": "Registro inicial",                "id_sede": 3, "fecha": "2025-01-20 08:55:00"},
    {"id_movimiento": 34, "tipo": "Salida",  "id_insumo": 14, "cantidad":   60, "id_usuario": 10, "motivo": "Uso en orden",                    "id_sede": 3, "fecha": "2025-02-25 10:00:00"},
    {"id_movimiento": 35, "tipo": "Salida",  "id_insumo": 16, "cantidad":    5, "id_usuario": 10, "motivo": "Uso en orden",                    "id_sede": 3, "fecha": "2025-03-15 11:00:00"},
    {"id_movimiento": 36, "tipo": "Salida",  "id_insumo": 17, "cantidad":   80, "id_usuario": 10, "motivo": "Uso en orden",                    "id_sede": 3, "fecha": "2025-03-22 14:00:00"},
    {"id_movimiento": 37, "tipo": "Salida",  "id_insumo": 18, "cantidad":   90, "id_usuario": 10, "motivo": "Uso en orden",                    "id_sede": 3, "fecha": "2025-04-12 09:00:00"},
    {"id_movimiento": 38, "tipo": "Salida",  "id_insumo": 15, "cantidad":   25, "id_usuario": 10, "motivo": "Uso en orden",                    "id_sede": 3, "fecha": "2025-04-20 10:00:00"},
    {"id_movimiento": 39, "tipo": "Salida",  "id_insumo": 19, "cantidad":   15, "id_usuario": 10, "motivo": "Uso en orden",                    "id_sede": 3, "fecha": "2025-04-25 08:00:00"},
    {"id_movimiento": 40, "tipo": "Entrada", "id_insumo": 14, "cantidad":   60, "id_usuario":  4, "motivo": "Compra proveedor PolyTex",         "id_sede": 3, "fecha": "2025-04-08 09:00:00"},
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


# ============================================================
# HELPERS
# ============================================================

def buscar_usuario(id_usuario: int):
    return next((u for u in usuarios if u["id_usuario"] == id_usuario), None)

def buscar_insumo(id_insumo: int):
    return next((i for i in insumos if i["id_insumo"] == id_insumo), None)

def buscar_orden(id_orden: int):
    return next((o for o in ordenes if o["id_orden"] == id_orden), None)

def nombre_sede(id_sede: int) -> str:
    s = next((s for s in sedes if s["id_sede"] == id_sede), None)
    return s["nombre"] if s else f"Sede {id_sede}"

def es_su_sede(usuario: dict, id_sede: int) -> bool:
    if usuario["rol"] == "Dueño":
        return True
    return usuario["id_sede"] == id_sede

def verificar_permiso(usuario: dict, roles_permitidos: list):
    if usuario["rol"] not in roles_permitidos:
        raise HTTPException(status_code=403, detail=f"Acceso denegado. Su rol es: {usuario['rol']}")

def enriquecer_insumo(i: dict) -> dict:
    """Agrega nombre de sede y estado de stock al dict del insumo."""
    return {
        **i,
        "sede_nombre":  nombre_sede(i["id_sede"]),
        "estado_stock": "ALERTA" if i["cantidad"] < i["stock_minimo"] else "OK",
        "faltantes":    max(0, i["stock_minimo"] - i["cantidad"]),
    }

def enriquecer_orden(o: dict) -> dict:
    """Agrega nombre de sede y días de retraso."""
    hoy = datetime.now().date()
    fecha_e = datetime.strptime(o["fecha_entrega"], "%Y-%m-%d").date()
    retraso = max(0, (hoy - fecha_e).days) if o["estado"] != "Terminada" and hoy > fecha_e else 0
    return {
        **o,
        "sede_nombre": nombre_sede(o["id_sede"]),
        "dias_retraso": retraso,
    }

def enriquecer_movimiento(m: dict) -> dict:
    insumo  = buscar_insumo(m["id_insumo"])
    usuario = buscar_usuario(m["id_usuario"])
    return {
        **m,
        "insumo_nombre":  insumo["nombre"]  if insumo  else "—",
        "usuario_nombre": usuario["nombre"] if usuario else "—",
        "sede_nombre":    nombre_sede(m["id_sede"]),
    }


# ============================================================
# MODELOS (Pydantic)
# ============================================================

class LoginRequest(BaseModel):
    usuario_acceso: str
    contrasena: str

class InsumoCreate(BaseModel):
    nombre: str
    categoria: str
    unidad_medida: str
    cantidad: int
    stock_minimo: int
    id_sede: Optional[int] = None   # obligatorio solo si el usuario es Dueño
    id_usuario: int                 # quien hace la petición

class MovimientoCreate(BaseModel):
    id_insumo: int
    tipo: str           # "Entrada" | "Salida"
    cantidad: int
    motivo: str
    id_usuario: int

class OrdenCreate(BaseModel):
    cliente: str
    prenda: str
    cantidad: int
    fecha_entrega: str  # YYYY-MM-DD
    prioridad: str      # "Normal" | "Urgente"
    id_sede: Optional[int] = None
    id_usuario: int

class OrdenEstadoUpdate(BaseModel):
    nuevo_estado: str   # "Pendiente" | "En proceso" | "Pausada" | "Terminada"
    id_usuario: int


# ============================================================
# ENDPOINTS
# ============================================================

@app.get("/")
def root():
    return {"mensaje": "Maintegral API activa ✔"}


# ---------- AUTH ----------

@app.post("/login")
def login(body: LoginRequest):
    u = next(
        (u for u in usuarios
         if u["usuario_acceso"] == body.usuario_acceso and u["contrasena"] == body.contrasena),
        None
    )
    if not u:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {
        "id_usuario":     u["id_usuario"],
        "nombre":         u["nombre"],
        "rol":            u["rol"],
        "id_sede":        u["id_sede"],
        "sede_nombre":    nombre_sede(u["id_sede"]),
        "usuario_acceso": u["usuario_acceso"],
    }


# ---------- SEDES ----------

@app.get("/sedes")
def listar_sedes():
    return sedes


# ---------- INVENTARIO ----------

@app.get("/inventario")
def ver_inventario(id_usuario: int, id_sede: Optional[int] = None):
    usuario = buscar_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    verificar_permiso(usuario, ["Dueño", "Administrador", "Encargado de Inventario"])

    if id_sede:
        if not es_su_sede(usuario, id_sede):
            raise HTTPException(status_code=403, detail="No tiene acceso a esa sede")
        resultado = [i for i in insumos if i["id_sede"] == id_sede]
    elif usuario["rol"] == "Dueño":
        resultado = insumos
    else:
        resultado = [i for i in insumos if i["id_sede"] == usuario["id_sede"]]

    return [enriquecer_insumo(i) for i in resultado]


@app.get("/inventario/faltantes")
def ver_faltantes(id_usuario: int):
    usuario = buscar_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    verificar_permiso(usuario, ["Dueño", "Administrador", "Encargado de Inventario"])

    if usuario["rol"] == "Dueño":
        resultado = [i for i in insumos if i["cantidad"] < i["stock_minimo"]]
    else:
        resultado = [i for i in insumos if i["id_sede"] == usuario["id_sede"] and i["cantidad"] < i["stock_minimo"]]

    # Incrementar alerta
    for i in resultado:
        i["alertas_stock"] += 1

    return [enriquecer_insumo(i) for i in resultado]


@app.post("/inventario/insumo")
def registrar_insumo(body: InsumoCreate):
    usuario = buscar_usuario(body.id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    verificar_permiso(usuario, ["Dueño", "Administrador", "Encargado de Inventario"])

    if body.categoria not in ("tela","hilo","botón","cierre","otro"):
        raise HTTPException(status_code=400, detail="Categoría inválida")
    if body.unidad_medida not in ("metros","unidades","kilos"):
        raise HTTPException(status_code=400, detail="Unidad de medida inválida")

    id_sede = body.id_sede if usuario["rol"] == "Dueño" else usuario["id_sede"]
    if id_sede is None:
        raise HTTPException(status_code=400, detail="Debe especificar id_sede")
    if not es_su_sede(usuario, id_sede):
        raise HTTPException(status_code=403, detail="No tiene acceso a esa sede")

    if any(i["nombre"] == body.nombre and i["id_sede"] == id_sede for i in insumos):
        raise HTTPException(status_code=409, detail="El insumo ya existe en esa sede")

    alertas = 1 if body.cantidad < body.stock_minimo else 0
    nuevo = {
        "id_insumo":              _next_id["insumo"],
        "nombre":                 body.nombre,
        "categoria":              body.categoria,
        "unidad_medida":          body.unidad_medida,
        "cantidad":               body.cantidad,
        "stock_minimo":           body.stock_minimo,
        "alertas_stock":          alertas,
        "id_sede":                id_sede,
        "id_usuario_responsable": body.id_usuario,
    }
    insumos.append(nuevo)
    movimientos.append({
        "id_movimiento": _next_id["movimiento"],
        "tipo":     "Entrada",
        "id_insumo": _next_id["insumo"],
        "cantidad":  body.cantidad,
        "id_usuario": body.id_usuario,
        "motivo":   "Registro inicial de insumo",
        "id_sede":  id_sede,
        "fecha":    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
    _next_id["insumo"]     += 1
    _next_id["movimiento"] += 1

    alerta_msg = None
    if alertas:
        alerta_msg = f"Stock inicial por debajo del mínimo. Faltan {body.stock_minimo - body.cantidad} {body.unidad_medida}"

    return {"mensaje": "Insumo registrado correctamente", "id_insumo": nuevo["id_insumo"], "alerta": alerta_msg}


# ---------- MOVIMIENTOS ----------

@app.get("/movimientos")
def ver_movimientos(id_usuario: int, id_insumo: Optional[int] = None):
    usuario = buscar_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    verificar_permiso(usuario, ["Dueño", "Administrador", "Encargado de Inventario"])

    if usuario["rol"] == "Dueño":
        resultado = movimientos
    else:
        resultado = [m for m in movimientos if m["id_sede"] == usuario["id_sede"]]

    if id_insumo:
        resultado = [m for m in resultado if m["id_insumo"] == id_insumo]

    return [enriquecer_movimiento(m) for m in sorted(resultado, key=lambda x: x["fecha"], reverse=True)]


@app.post("/movimientos")
def registrar_movimiento(body: MovimientoCreate):
    usuario = buscar_usuario(body.id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    verificar_permiso(usuario, ["Dueño", "Administrador", "Encargado de Inventario"])

    if body.tipo not in ("Entrada","Salida"):
        raise HTTPException(status_code=400, detail="Tipo debe ser Entrada o Salida")

    insumo = buscar_insumo(body.id_insumo)
    if not insumo or not es_su_sede(usuario, insumo["id_sede"]):
        raise HTTPException(status_code=404, detail="Insumo no encontrado en su sede")

    if body.tipo == "Salida" and body.cantidad > insumo["cantidad"]:
        raise HTTPException(status_code=400, detail=f"Stock insuficiente. Disponible: {insumo['cantidad']} {insumo['unidad_medida']}")

    insumo["cantidad"] += body.cantidad if body.tipo == "Entrada" else -body.cantidad
    insumo["id_usuario_responsable"] = body.id_usuario

    alerta_msg = None
    if insumo["cantidad"] < insumo["stock_minimo"]:
        insumo["alertas_stock"] += 1
        faltantes = insumo["stock_minimo"] - insumo["cantidad"]
        alerta_msg = f"{insumo['nombre']} por debajo del mínimo. Faltan {faltantes} {insumo['unidad_medida']}"

    movimientos.append({
        "id_movimiento": _next_id["movimiento"],
        "tipo":      body.tipo,
        "id_insumo": body.id_insumo,
        "cantidad":  body.cantidad,
        "id_usuario": body.id_usuario,
        "motivo":    body.motivo,
        "id_sede":   insumo["id_sede"],
        "fecha":     datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
    _next_id["movimiento"] += 1

    return {"mensaje": "Movimiento registrado correctamente", "stock_actual": insumo["cantidad"], "alerta": alerta_msg}


# ---------- ÓRDENES DE PRODUCCIÓN ----------

@app.get("/ordenes")
def ver_ordenes(id_usuario: int, estado: Optional[str] = None):
    usuario = buscar_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    verificar_permiso(usuario, ["Dueño", "Administrador", "Jefe de Producción"])

    if usuario["rol"] == "Dueño":
        resultado = ordenes
    else:
        resultado = [o for o in ordenes if o["id_sede"] == usuario["id_sede"]]

    if estado:
        resultado = [o for o in resultado if o["estado"] == estado]

    enriquecidas = [enriquecer_orden(o) for o in resultado]

    # Jefe de Producción no ve datos del cliente
    if usuario["rol"] == "Jefe de Producción":
        for o in enriquecidas:
            o.pop("cliente", None)

    return sorted(enriquecidas, key=lambda x: x["fecha_entrega"])


@app.post("/ordenes")
def registrar_orden(body: OrdenCreate):
    usuario = buscar_usuario(body.id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    verificar_permiso(usuario, ["Dueño", "Administrador", "Jefe de Producción"])

    try:
        datetime.strptime(body.fecha_entrega, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha inválido (use YYYY-MM-DD)")

    if body.prioridad not in ("Normal","Urgente"):
        raise HTTPException(status_code=400, detail="Prioridad debe ser Normal o Urgente")

    id_sede = body.id_sede if usuario["rol"] == "Dueño" else usuario["id_sede"]
    if id_sede is None:
        raise HTTPException(status_code=400, detail="Debe especificar id_sede")
    if not es_su_sede(usuario, id_sede):
        raise HTTPException(status_code=403, detail="No tiene acceso a esa sede")

    nueva = {
        "id_orden":               _next_id["orden"],
        "cliente":                body.cliente,
        "prenda":                 body.prenda,
        "cantidad":               body.cantidad,
        "fecha_entrega":          body.fecha_entrega,
        "prioridad":              body.prioridad,
        "estado":                 "Pendiente",
        "id_sede":                id_sede,
        "id_usuario_responsable": body.id_usuario,
    }
    ordenes.append(nueva)
    _next_id["orden"] += 1
    return {"mensaje": "Orden registrada correctamente", "id_orden": nueva["id_orden"]}


@app.patch("/ordenes/{id_orden}/estado")
def actualizar_estado_orden(id_orden: int, body: OrdenEstadoUpdate):
    usuario = buscar_usuario(body.id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    verificar_permiso(usuario, ["Dueño", "Administrador", "Jefe de Producción"])

    if body.nuevo_estado not in ("Pendiente","En proceso","Pausada","Terminada"):
        raise HTTPException(status_code=400, detail="Estado inválido")

    orden = buscar_orden(id_orden)
    if not orden or not es_su_sede(usuario, orden["id_sede"]):
        raise HTTPException(status_code=404, detail="Orden no encontrada en su sede")

    orden["estado"] = body.nuevo_estado
    return {"mensaje": f"Orden {id_orden} actualizada a: {body.nuevo_estado}"}