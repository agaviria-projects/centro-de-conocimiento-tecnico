# Guía general para generar un `.exe` de cualquier proyecto Python

## 1. Objetivo

Convertir un proyecto Python en una versión distribuible para Windows, de forma que el usuario final pueda ejecutar la aplicación **sin recibir directamente los archivos `.py`**.

Esta guía aplica como base para proyectos como:

- Informe ANS ATC CHEC
- Órdenes Internas AIE
- SERVITRAVEL
- Consolidador de Actas
- Validación Mano de Obra vs Materiales
- Aplicaciones Tkinter similares

La estructura, nombres de archivos, carpetas externas y dependencias pueden cambiar en cada proyecto, pero el procedimiento general es el mismo.

---

# 2. Trabajar primero sobre una copia

Antes de convertir un proyecto a `.exe`:

1. Hacer una copia completa del proyecto.
2. Trabajar y probar sobre esa copia.
3. Mantener intacto el proyecto original hasta que el `.exe` quede validado.

Ejemplo:

```text
Proyecto original:
Ordenes_internas_AIE

Copia para pruebas:
Ordenes_internas_AIE_EXE
```

Esto permite corregir rutas, imports o dependencias sin poner en riesgo la versión original.

---

# 3. Identificar qué debe quedar dentro y fuera del `.exe`

Antes de compilar, separar conceptualmente dos tipos de elementos.

## Código que no se desea entregar directamente

Ejemplo:

```text
main.py
src/
*.py
```

Estos archivos serán empaquetados por PyInstaller.

## Archivos que deben permanecer externos

Ejemplos:

```text
config/
entrada/
salida/
assets/
dashboard/
plantillas/
logs/
```

Estos archivos normalmente deben permanecer fuera del `.exe` porque el usuario puede necesitarlos, modificarlos o porque la aplicación debe escribir en ellos.

Cada proyecto tendrá su propia estructura.

---

# 4. Preparar una ruta raíz compatible con Python y `.exe`

Una aplicación funciona diferente cuando se ejecuta desde:

```bash
py main.py
```

que cuando se ejecuta como:

```text
MiAplicacion.exe
```

Por eso conviene centralizar la ruta raíz.

Ejemplo recomendado en `config.py`:

```python
from pathlib import Path
import sys

if getattr(sys, "frozen", False):
    # Ejecutando como .exe
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    # Ejecutando desde Python
    BASE_DIR = Path(__file__).resolve().parent.parent
```

Después todas las carpetas deben construirse desde `BASE_DIR`.

Ejemplo:

```python
ENTRADA_DIR = BASE_DIR / "entrada"
SALIDA_DIR = BASE_DIR / "salida"
CONFIG_DIR = BASE_DIR / "config"
ASSETS_DIR = BASE_DIR / "assets"
```

## Regla importante

Evitar que diferentes módulos calculen la raíz por su cuenta.

Preferir:

```python
from src.config import BASE_DIR
```

en lugar de repetir:

```python
Path(__file__).resolve().parents[1]
```

---

# 5. Usar imports claros entre módulos

Para PyInstaller es recomendable utilizar imports absolutos dentro del proyecto.

Ejemplo:

```python
from src.procesador import procesar_datos
from src.lector import leer_archivo
from src.config import BASE_DIR
```

Evitar cuando sea posible:

```python
from procesador import procesar_datos
```

y evitar modificar manualmente `sys.path` dentro de los módulos.

Esto reduce errores como:

```text
ModuleNotFoundError
```

cuando la aplicación se ejecuta fuera del equipo de desarrollo.

---

# 6. Probar el proyecto normalmente antes de compilar

Antes de crear el `.exe`:

```bash
py main.py
```

Probar todas las funciones importantes.

Ejemplo general:

```text
Abrir aplicación
↓
Procesar archivo
↓
Generar salida
↓
Abrir resultados
↓
Actualizar Excel o dashboard si aplica
↓
Cerrar correctamente
```

No se debe generar el `.exe` hasta que la versión Python funcione correctamente.

---

# 7. Instalar PyInstaller

Dentro del entorno virtual del proyecto:

```bash
pip install pyinstaller
```

Verificar:

```bash
pyinstaller --version
```

---

# 8. Limpiar compilaciones anteriores

Si ya se había generado un `.exe`, antes de recompilar eliminar:

```text
build/
dist/
MiAplicacion.spec
```

Esto evita mezclar archivos de distintas compilaciones.

---

# 9. Generar una primera versión del `.exe`

Desde la carpeta raíz donde está `main.py`:

```bash
pyinstaller --clean --noconfirm --windowed --name MiAplicacion main.py
```

Cambiar:

```text
MiAplicacion
```

por el nombre real del proyecto.

Ejemplo:

```bash
pyinstaller --clean --noconfirm --windowed --name Ordenes_Internas_AIE main.py
```

## Qué significa

```text
--clean
Limpia archivos temporales de compilaciones anteriores.

--noconfirm
No solicita confirmación al sobrescribir.

--windowed
Evita mostrar consola negra en aplicaciones gráficas.

--name
Define el nombre del ejecutable.
```

---

# 10. Dependencias ocultas

Algunos proyectos utilizan librerías que PyInstaller no detecta automáticamente.

En ese caso aparece un error parecido a:

```text
ModuleNotFoundError
```

después de compilar.

La solución puede requerir:

```bash
--hidden-import=NOMBRE_MODULO
```

Ejemplo real con automatización de Excel mediante `pywin32`:

```bash
pyinstaller --clean --noconfirm --windowed --hidden-import=win32timezone --name MiAplicacion main.py
```

## Importante

No todos los proyectos necesitan `win32timezone`.

Solo se agrega cuando la dependencia realmente existe.

Cada proyecto puede requerir sus propios `hidden-import`.

---

# 11. Resultado de PyInstaller

Normalmente se crean:

```text
build/
dist/
MiAplicacion.spec
```

La versión distribuible queda dentro de:

```text
dist/
└── MiAplicacion/
    ├── _internal/
    └── MiAplicacion.exe
```

## Regla importante

No copiar solamente:

```text
MiAplicacion.exe
```

También se necesita:

```text
_internal/
```

porque contiene dependencias necesarias para ejecutar la aplicación.

---

# 12. Copiar las carpetas externas necesarias

Después de compilar, dentro de:

```text
dist/MiAplicacion/
```

se deben copiar las carpetas externas que realmente utiliza ese proyecto.

Ejemplo genérico:

```text
MiAplicacion/
├── _internal/
├── assets/
├── config/
├── entrada/
├── salida/
├── logs/
└── MiAplicacion.exe
```

En otro proyecto podría ser:

```text
Ordenes_Internas_AIE/
├── _internal/
├── CONFIG/
├── entrada/
├── salida/
├── plantillas/
└── Ordenes_Internas_AIE.exe
```

La estructura depende del desarrollo.

---

# 13. Probar primero el `.exe` en el equipo de desarrollo

Antes de llevarlo a otro computador:

```text
dist/
└── MiAplicacion/
    └── MiAplicacion.exe
```

Ejecutarlo desde esa carpeta.

Validar:

```text
La interfaz abre
Los archivos de entrada se encuentran
Los archivos de configuración se leen
Las salidas se generan
Los botones funcionan
Los archivos externos se abren correctamente
```

---

# 14. Probar en otro computador

Esta prueba es obligatoria para considerar la distribución terminada.

Procedimiento:

1. Copiar toda la carpeta `MiAplicacion`.
2. Llevarla mediante USB, red o carpeta compartida.
3. Copiarla al disco del otro computador.
4. Ejecutar el `.exe`.
5. Probar todas las funciones principales.

No ejecutar directamente desde la USB si se puede evitar.

## Objetivo de esta prueba

Detectar:

- rutas absolutas;
- módulos faltantes;
- dependencias no empaquetadas;
- permisos;
- archivos externos faltantes;
- diferencias entre computadores.

---

# 15. Errores frecuentes

## Error: `ModuleNotFoundError`

Revisar:

- imports absolutos;
- módulos que no fueron incluidos;
- necesidad de `--hidden-import`.

---

## Error: busca archivos dentro de `_internal`

Normalmente significa que algún módulo todavía utiliza una ruta como:

```python
Path(__file__).resolve().parents[1]
```

en lugar de utilizar el `BASE_DIR` central preparado para PyInstaller.

---

## Error: no encuentra archivo de configuración

Confirmar que la carpeta externa fue copiada junto al `.exe`.

Ejemplo:

```text
config/
└── configuracion.xlsx
```

---

## Error: aplicación funciona con Python pero no como `.exe`

Revisar:

```text
imports
rutas
hidden-import
archivos externos
dependencias
```

---

# 16. Crear un acceso directo para el usuario

El `.exe` debe permanecer dentro de su carpeta.

No moverlo solo al Escritorio.

Crear un acceso directo:

```text
Clic derecho sobre MiAplicacion.exe
→ Mostrar más opciones
→ Enviar a
→ Escritorio (crear acceso directo)
```

El usuario ejecutará la aplicación desde ese acceso directo.

---

# 17. Qué se entrega al usuario

Ejemplo:

```text
MiAplicacion/
├── _internal/
├── assets/
├── config/
├── entrada/
├── salida/
└── MiAplicacion.exe
```

No es necesario entregar:

```text
src/
venv/
main.py
*.py
build/
*.spec
```

Esto permite que el usuario utilice la aplicación sin recibir directamente el código fuente Python.

---

# 18. Si posteriormente cambia el código

Si se modifica:

```text
main.py
config.py
interfaz.py
procesadores
lectores
reglas Python
```

se debe generar nuevamente el `.exe`.

Flujo:

```text
Modificar código
↓
Probar con py main.py
↓
Eliminar build / dist / .spec
↓
Compilar nuevamente
↓
Copiar carpetas externas
↓
Probar el .exe
↓
Probar en otro PC si el cambio es importante
```

---

# 19. Si solamente cambia un archivo externo

Si cambia únicamente:

```text
configuracion.xlsx
plantilla.xlsx
archivo maestro
parámetro externo
```

y ese archivo está fuera del `.exe`, normalmente **no es necesario recompilar**.

Solo se reemplaza el archivo externo correspondiente.

---

# 20. Plantilla general reutilizable

Para un nuevo proyecto, revisar esta lista:

```text
1. Crear copia del proyecto.
2. Identificar main.py.
3. Identificar carpetas externas.
4. Preparar BASE_DIR.
5. Revisar imports.
6. Probar con py main.py.
7. Instalar/verificar PyInstaller.
8. Eliminar build, dist y .spec anteriores.
9. Compilar.
10. Corregir hidden-import si aparece alguno.
11. Copiar carpetas externas dentro de dist.
12. Probar el .exe localmente.
13. Copiar la carpeta completa a otro PC.
14. Probar todas las funciones.
15. Crear acceso directo.
16. Entregar sin src, venv ni archivos .py.
```

---

# 21. Comando base reutilizable

Para la mayoría de aplicaciones gráficas:

```bash
pyinstaller --clean --noconfirm --windowed --name NOMBRE_APLICACION main.py
```

Si requiere módulos ocultos:

```bash
pyinstaller --clean --noconfirm --windowed --hidden-import=NOMBRE_MODULO --name NOMBRE_APLICACION main.py
```

---

# Ejemplo 1 - Informe ANS ATC CHEC

```bash
pyinstaller --clean --noconfirm --windowed --hidden-import=win32timezone --name Informe_ANS_ATC_CHEC main.py
```

Estructura externa utilizada:

```text
_internal/
assets/
config/
dashboard/
entrada/
entrada_redes/
logs/
mapas/
salida/
salida_redes/
MiAplicacion.exe
```

---

# Ejemplo 2 - Órdenes Internas AIE

El mismo procedimiento aplica.

Solo se deben revisar:

```text
Nombre del archivo principal
Nombre del ejecutable
Carpetas de entrada y salida
Archivos de configuración
Plantillas
Imports
Dependencias particulares del proyecto
```

Ejemplo conceptual:

```bash
pyinstaller --clean --noconfirm --windowed --name Ordenes_Internas_AIE main.py
```

Si durante las pruebas aparece una dependencia no detectada, se agrega el `--hidden-import` correspondiente.

---

# Regla final

> PyInstaller no reemplaza las pruebas. El `.exe` se considera listo únicamente cuando funciona correctamente desde la carpeta `dist` y después en un computador diferente al equipo donde fue desarrollado.

---

# ⚠️ ACTUALIZACIÓN DE UNA APLICACIÓN YA ENTREGADA

> ⚠️ **IMPORTANTE: NO REEMPLAZAR A CIEGAS LAS CARPETAS OPERATIVAS**
>
> Cuando una aplicación ya fue entregada al usuario y posteriormente se modifica algún archivo `.py`, se debe generar una nueva versión del `.exe`.
>
> **No se debe reemplazar toda la carpeta de la aplicación sin revisar primero qué información ya existe en el computador del usuario.**

### ✅ Normalmente se pueden reemplazar

```text
_internal/
MiAplicacion.exe
assets/        → si cambió
dashboard/     → si cambió
config/        → si cambió
mapas/         → si cambió
```

### ❌ Se deben conservar especialmente

```text
entrada/
entrada_redes/
salida/
salida_redes/
logs/
```

> Estas carpetas pueden contener archivos operativos, informes generados o información propia del usuario.


## Regla práctica

```text
¿Cambió código Python?
→ Probar con py main.py
→ Volver a compilar con PyInstaller
→ Generar nuevo .exe y nuevo _internal

¿Cambió solamente un archivo externo?
→ No es necesario recompilar
→ Reemplazar únicamente ese archivo
```

## Antes de actualizar en otro computador

1. Hacer una copia de seguridad de la carpeta actualmente instalada.
2. Cerrar la aplicación.
3. Reemplazar el nuevo archivo `.exe` de la aplicación.
4. Reemplazar `_internal/`.
5. Reemplazar `assets/`, `config/`, `dashboard/` o `mapas/` únicamente si realmente cambiaron.
6. Conservar `entrada/`, `entrada_redes/`, `salida/`, `salida_redes/` y `logs/`.
7. Ejecutar nuevamente la aplicación.
8. Validar las funciones principales.

> **Regla de seguridad:** antes de reemplazar `config/` o `dashboard/`, verificar si el usuario realizó cambios propios. Si existen cambios locales, respaldarlos primero.

## Flujo resumido de actualización

```text
Modificar .py
↓
Probar con py main.py
↓
Compilar nueva versión
↓
Respaldar versión instalada
↓
Reemplazar .exe + _internal
↓
Actualizar solo carpetas técnicas que cambiaron
↓
Conservar entrada / salida / logs
↓
Probar nuevamente
```