# Sistema de Inventario de Laboratorio

## 1. Descripción
LabControl es una aplicación de consola en Python que permite llevar el control de los equipos tecnológicos de un laboratorio. Reemplaza los cuadernos y hojas sueltas por un registro único y ordenado.

## 2. Objetivo
Registrar, consultar y mantener actualizada la información de los equipos del laboratorio, para saber qué equipos existen, dónde están y en qué estado se encuentran.

## 3. Usuarios
Técnico o docente responsable de los equipos del laboratorio.

## 4. Funcionalidades
- Registrar equipo
- Listar equipos
- Buscar equipo por código
- Modificar estado
-Eliminar un equipo del registro de forma definitiva
- Salir

## 5. Información de los equipos
Cada equipo contiene:
- codigo (identificador único)
- nombre
- tipo
- estado (operativo, en reparacion o de baja)
- ubicacion

## 6. Tecnologías
Lenguaje: Python 3 (solo biblioteca estándar)
Almacenamiento: archivo JSON (`data/equipos.json`)

## 7. Estructura del proyecto
```
inventario-laboratorio/
├── README.md
├── AGENTS.md
├── app.py
├── src/
│   └── inventario.py
└── data/
    └── equipos.json
```

## 8. Ejecución
```
python app.py
```