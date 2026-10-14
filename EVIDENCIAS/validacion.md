# Evidencias de validación con Antigravity

**Laboratorio Nº 8 – Creación de contexto para IA**
**Repositorio:** https://github.com/ronaldtg223-ops/inventario-laboratorio
**Nota:** el laboratorio se desarrolló de forma individual, por lo que el historial de commits muestra un solo autor.

---

## Etapa 7 – ¿Por qué es importante que los archivos de contexto también se almacenen en GitHub?

Porque así las reglas del proyecto quedan en un solo lugar compartido y versionado. Cualquier persona (y la IA que use) trabaja con la misma versión de `README.md` y `AGENTS.md`. Si un archivo cambia, el historial muestra qué se modificó y cuándo, y se puede volver a una versión anterior si hace falta. Además, los archivos de contexto no se pierden si se cambia de computadora.

---

## Etapa 8 – Primera prueba del contexto (sin generar código)

Prompt usado:

```
Analiza el proyecto actual.
Revisa README.md y AGENTS.md.
No generes código.
Indica:
1. Cuál es el objetivo del proyecto.
2. Cuáles son las funcionalidades principales.
3. Qué estructura debe respetarse.
4. Qué convenciones de programación debes utilizar.
5. Qué restricciones existen.
6. Qué acciones no debes realizar.
```

| Elemento | Interpretación de la IA | ¿Correcto? |
|---|---|---|
| Objetivo | Registrar, consultar y mantener actualizada la información de los equipos del laboratorio en un registro único, para saber qué equipos existen, dónde están y en qué estado se encuentran. | Sí |
| Lenguaje | Exclusivamente Python 3. Nombres, comentarios y mensajes en español. | Sí |
| Convenciones | `snake_case` en variables y funciones, constantes en MAYUSCULAS, archivos en minúsculas sin espacios ni tildes, funciones cortas con una sola responsabilidad y procedimiento previo de 4 pasos. | Sí |
| Organización | `app.py` para el menú, `src/inventario.py` para la lógica y `data/equipos.json` para los datos. Cada equipo es un diccionario con `codigo`, `nombre`, `tipo`, `estado` y `ubicacion`. | Sí |
| Almacenamiento | Archivo JSON local. No se permiten bases de datos relacionales ni NoSQL. | Sí |
| Restricciones | Solo biblioteca estándar (`json`, `os`), `codigo` único, estados válidos (`operativo`, `en reparacion`, `de baja`) y validación de entradas con mensajes claros. | Sí |

La IA interpretó correctamente los seis elementos sin generar código y además identificó las acciones prohibidas (no usar librerías externas ni bases de datos, no crear archivos nuevos, no duplicar ni renombrar funciones, no "mejorar" código que ya funciona).

Captura: `evidencias/etapa8.png`

---

## Etapa 9 – Corrección del contexto

| Problema encontrado | Archivo modificado | Cambio realizado |
|---|---|---|
| La IA interpretó "Eliminar equipo" como "dar de baja/remover", lo que se confunde con el estado `de baja` (ambigüedad). | README.md | Se aclaró que eliminar borra el equipo del registro de forma definitiva: "Eliminar un equipo del registro de forma definitiva". |

Commit realizado: `Aclarar funcionalidad de eliminar equipo`.

---

## Etapa 10 – Generación de `registrar_equipo()`

Prompt usado:

```
Analiza primero el contexto del proyecto.
Implementa únicamente la funcionalidad registrar_equipo().
Antes de escribir código:
1. Indica qué archivo modificarás.
2. Indica qué reglas de AGENTS.md aplicarás.
3. No modifiques ninguna otra funcionalidad.
```

Antes de escribir código, la IA indicó que modificaría `src/inventario.py` (función `registrar_equipo`, más las auxiliares `cargar_equipos` y `guardar_equipos`) y citó las reglas 1 a 8 de AGENTS.md.

| Criterio | Cumple | No cumple | Evidencia |
|---|---|---|---|
| Utiliza snake_case | ✅ | | `registrar_equipo`, `cargar_equipos`, `guardar_equipos`, `nuevo_equipo` |
| Respeta el idioma acordado | ✅ | | Nombres, comentarios y mensajes en español |
| No utiliza librerías no autorizadas | ✅ | | Solo `import json` e `import os` |
| Respeta la estructura | ⚠️ Parcial | | La lógica quedó en `src/inventario.py`, pero incluye `input()` y `print()`, que según la estructura corresponden a `app.py` |
| Modifica solo lo necesario | ✅ | | Solo se modificó `src/inventario.py`. Las funciones auxiliares eran necesarias para leer y guardar el JSON. No se tocó `app.py`. |
| Respeta el almacenamiento definido | ✅ | | Usa `data/equipos.json` mediante la constante `RUTA_DATOS` |

Observación: la IA ya había agregado docstrings de una sola línea sin que existiera una regla de documentación.

Capturas: `evidencias/etapa10_plan.png`, `evidencias/etapa10_codigo.png`

---

## Etapa 11 – Nueva regla de documentación

Se agregó a AGENTS.md la sección "9. Documentación" (docstring en español, multilínea, con secciones "Parámetros:" y "Retorna:", y comentarios que expliquen el porqué). Commit: `Agregar regla de documentación`.

Prompt usado (sin mencionar la regla):

```
Implementa la función buscar_equipo() respetando el contexto actual del proyecto.
```

- **Nombre de la función generada:** `buscar_equipo`
- **¿Incluyó docstring?** Sí, multilínea, con descripción, sección `Parámetros:` y sección `Retorna:`, todo en español.
- **¿Fue necesario volver a explicar la regla dentro del prompt?** No. La IA citó por su cuenta la Regla 9 en su plan y la aplicó.

Capturas: `evidencias/etapa11_plan.png`, `evidencias/etapa11_codigo.png`

---

## Etapa 12 – Efecto del Context Engineering

```
ANTES:  Prompt → IA → Código (sin reglas del equipo)

AHORA:  README.md + AGENTS.md + Prompt
                   ↓
                  IA
                   ↓
        Código consistente con las reglas
```

**¿Qué cambió al agregar la regla del docstring?**
Al agregar la regla de documentación en AGENTS.md, la IA generó `buscar_equipo()` con un docstring de varias líneas (descripción, "Parámetros:" y "Retorna:") y con comentarios que explican el porqué de cada acción. Esto ocurrió sin repetir la regla en el prompt: el prompt solo pidió implementar la función. Antes de la regla, `registrar_equipo()` solo tenía docstrings de una línea. Esto demuestra que el comportamiento de la IA se controla desde los archivos de contexto y no repitiendo instrucciones en cada prompt.

---

## Etapa 13 – Contradicciones

Se agregó temporalmente en AGENTS.md la sección "10. Almacenamiento alternativo" indicando que los datos se guardan en SQLite (`data/inventario.db`), lo que contradice al README y a otras reglas. Al terminar la prueba, la sección se eliminó.

Prompt usado:

```
Analiza los archivos de contexto del proyecto.
Identifica contradicciones, ambigüedades o reglas incompatibles.
No generes código.
```

| Problema detectado | Archivo | Corrección propuesta |
|---|---|---|
| Contradicción de almacenamiento: la Regla 10 dice SQLite, pero las Reglas 3, 5 y 6 y el README dicen solo JSON y sin bases de datos | AGENTS.md / README.md | Eliminar la Regla 10 y dejar JSON como único almacenamiento en ambos archivos |
| Librerías: usar SQLite exige `sqlite3`, que no está en la lista permitida (`json`, `os`) | AGENTS.md | Se resuelve al eliminar la Regla 10 |
| Archivos nuevos: `data/inventario.db` no existe y crearlo violaría la Regla 3 | AGENTS.md | Se resuelve al eliminar la Regla 10 |
| Tensión entre Regla 9 (docstrings multilínea) y Regla 7 (no modificar código funcional): los docstrings antiguos son de una línea | AGENTS.md | Permitir actualizar solo el docstring cuando se pida documentar una función existente |
| Ambigüedad entre `app.py` y `inventario.py`: no se aclara quién usa `input()` y `print()` | AGENTS.md | Indicar que `src/inventario.py` no usa `input()` ni `print()`, y que `app.py` pide los datos y muestra los mensajes |
| Ambigüedad de tildes: no se define si "en reparación" se normaliza o se rechaza | README.md / AGENTS.md | Definir una regla clara de normalización de estados |

Captura: `evidencias/etapa13.png`

---

## Preguntas finales

1. **¿Cuál es la diferencia entre un prompt y un archivo de contexto?**
   El prompt es una instrucción puntual que solo vale para esa conversación. El archivo de contexto es permanente, vive en el proyecto y la IA lo lee cada vez que trabaja.

2. **¿Qué información debe contener README.md?**
   Qué hace el proyecto: descripción, objetivo, usuarios, funcionalidades, datos de los equipos, tecnologías, estructura y cómo ejecutarlo.

3. **¿Qué información debe contener AGENTS.md?**
   Cómo debe trabajar la IA: lenguaje, convenciones de nombres, organización del código, restricciones, qué no debe modificar y el procedimiento antes de cambiar código.

4. **¿Por qué es importante redactar reglas claras?**
   Porque la IA interpreta lo que lee de forma literal. Una regla ambigua puede entenderse de varias formas, como pasó con "eliminar" y "dar de baja" o con la interacción por consola en `inventario.py`.

5. **¿Qué ocurre si existen contradicciones entre los archivos de contexto?**
   La IA no sabe qué regla seguir: puede elegir una al azar o mezclar ambas, generando código inconsistente (por ejemplo, mezclar JSON y SQLite).

6. **¿Por qué usar GitHub para los archivos de contexto?**
   Mantiene una versión única y compartida, guarda el historial de cambios y permite volver atrás si una modificación causa problemas.

7. **¿Por qué es importante que todos usen el mismo contexto?**
   Para que el código tenga el mismo estilo, nombres y estructura, sin importar quién lo escriba o qué asistente use.

8. **¿Qué pasaría si AGENTS.md no se actualiza?**
   La IA seguiría reglas viejas y generaría código que no coincide con lo que se decidió después, como ocurrió antes de agregar la regla de docstrings.

9. **¿Qué es más efectivo: repetir las reglas en cada prompt o guardarlas en archivos de contexto?**
   Guardarlas en archivos. Se escriben una sola vez, se aplican siempre y no dependen de que uno se acuerde de repetirlas.

10. **Si la IA genera algo incorrecto, ¿qué archivo modificarías primero?**
    AGENTS.md (o README.md si el problema es funcional). Primero revisaría si la regla falta, es ambigua o se contradice, la corregiría y repetiría la prueba, en lugar de corregir solo el prompt.

---

## Observaciones y conclusiones

- Validar que la IA entendió el contexto antes de pedirle código evita errores de nombres, estructura y librerías. En este laboratorio la IA interpretó correctamente los seis elementos del proyecto.
- La IA siguió el procedimiento de 4 pasos definido en AGENTS.md: leyó el contexto, indicó el archivo y la función, citó las reglas y recién después escribió código.
- Cuando algo no queda claro, la corrección se hace en los archivos de contexto y no en el prompt, como en la ambigüedad de "eliminar" que se corrigió en el README.
- Al agregar la regla de docstrings, la IA la aplicó sin que se repitiera en el prompt, lo que demuestra que el contexto controla el comportamiento de la IA.
- Aun con un buen contexto, la IA mezcló interacción por consola y lógica en `inventario.py`. Esto muestra que las reglas deben ser explícitas, y que conviene pedirle a la IA que revise el contexto en busca de ambigüedades.
- Las contradicciones entre archivos confunden a la IA. En la prueba de la Etapa 13 detectó la contradicción JSON/SQLite y además otras tensiones reales entre reglas, por lo que revisar periódicamente los archivos de contexto es una buena práctica.
- Guardar el contexto en GitHub deja una versión única, con historial y respaldo del trabajo.
