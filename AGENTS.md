# Reglas para agentes de IA

## 1. Lenguaje
- El proyecto se programa únicamente en Python 3.
- Los nombres, mensajes al usuario y comentarios se escriben en español.

## 2. Convenciones de nombres
- Variables y funciones en snake_case (ejemplo: buscar_equipo).
- Constantes en MAYUSCULAS (ejemplo: RUTA_DATOS).
- Archivos y carpetas en minúsculas, sin espacios ni tildes.

## 3. Organización del código
- app.py solo contiene el menú y llama a las funciones de src/inventario.py.
- Toda la lógica del inventario va en src/inventario.py.
- Los datos se guardan solo en data/equipos.json.
- No crear archivos ni carpetas nuevas sin que se pida.

## 4. Funciones
- Cada función hace una sola tarea.
- Las funciones deben ser cortas y con nombres claros.
- No duplicar funciones que ya existen.

## 5. Datos
- Cada equipo es un diccionario con las claves: codigo, nombre, tipo, estado, ubicacion.
- El codigo es único: no puede haber dos equipos con el mismo.
- Estados válidos: "operativo", "en reparacion", "de baja".
- El almacenamiento es un archivo JSON.

## 6. Restricciones
- Usar solo la biblioteca estándar de Python (json, os).
- No instalar ni importar librerías externas.
- No usar bases de datos.
- Validar las entradas del usuario y mostrar mensajes de error claros.

## 7. Modificación del código
- Modificar solo el archivo y la función que se pidan.
- No cambiar ni "mejorar" código que ya funciona si no se solicitó.
- No renombrar funciones existentes.

## 8. Procedimiento antes de realizar cambios
1. Leer README.md y AGENTS.md.
2. Indicar qué archivo y qué función se va a modificar.
3. Indicar qué reglas de este archivo se van a aplicar.
4. Recién después escribir el código.