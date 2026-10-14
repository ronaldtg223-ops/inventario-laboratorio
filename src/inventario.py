# Lógica del inventario de equipos del laboratorio
import json
import os

# Constantes
RUTA_DATOS = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "data", "equipos.json")
)
ESTADOS_VALIDOS = ("operativo", "en reparacion", "de baja")


def cargar_equipos():
    """Carga la lista de equipos desde el archivo JSON."""
    if not os.path.exists(RUTA_DATOS):
        return []
    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        return []


def guardar_equipos(equipos):
    """Guarda la lista de equipos en el archivo JSON."""
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(equipos, archivo, indent=4, ensure_ascii=False)


def registrar_equipo(codigo=None, nombre=None, tipo=None, estado=None, ubicacion=None):
    """Registra un nuevo equipo en el inventario."""
    # Solicitar datos al usuario si no fueron proporcionados por parámetros
    if codigo is None:
        codigo = input("Ingrese el código del equipo: ").strip()
    else:
        codigo = str(codigo).strip()

    if nombre is None:
        nombre = input("Ingrese el nombre del equipo: ").strip()
    else:
        nombre = str(nombre).strip()

    if tipo is None:
        tipo = input("Ingrese el tipo de equipo: ").strip()
    else:
        tipo = str(tipo).strip()

    if estado is None:
        estado = input(
            "Ingrese el estado (operativo, en reparacion, de baja): "
        ).strip().lower()
    else:
        estado = str(estado).strip().lower()

    if ubicacion is None:
        ubicacion = input("Ingrese la ubicación del equipo: ").strip()
    else:
        ubicacion = str(ubicacion).strip()

    # Validación: campos obligatorios
    if not codigo or not nombre or not tipo or not estado or not ubicacion:
        print("Error: Todos los campos son obligatorios.")
        return None

    # Normalizar si se ingresa con tilde
    if estado == "en reparación":
        estado = "en reparacion"

    # Validación: estado válido
    if estado not in ESTADOS_VALIDOS:
        print(
            f"Error: Estado no válido. Los estados permitidos son: {', '.join(ESTADOS_VALIDOS)}."
        )
        return None

    # Cargar equipos existentes y validar código único
    equipos = cargar_equipos()
    for equipo in equipos:
        if equipo.get("codigo") == codigo:
            print(f"Error: Ya existe un equipo con el código '{codigo}'.")
            return None

    # Registrar el nuevo equipo
    nuevo_equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        "ubicacion": ubicacion,
    }
    equipos.append(nuevo_equipo)
    guardar_equipos(equipos)

    print(f"Equipo '{nombre}' registrado exitosamente.")
    return nuevo_equipo