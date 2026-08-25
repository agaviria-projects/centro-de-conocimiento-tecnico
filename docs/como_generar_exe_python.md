# Guía estándar para generar un `.exe` de proyectos Python con PyInstaller

## 1. Objetivo

Convertir un proyecto Python de escritorio en una versión distribuible para Windows, de forma que el usuario final pueda ejecutar la aplicación **sin instalar Python, sin crear un `venv` y sin recibir directamente los archivos `.py`**.

Esta guía sirve como procedimiento base reutilizable para proyectos como:

- Informe ANS ATC CHEC
- Órdenes Internas AIE
- SERVITRAVEL
- Consolidador de Actas
- Validación Mano de Obra vs Materiales
- Aplicaciones Tkinter similares

> **Importante:** el procedimiento general es el mismo, pero cada proyecto puede tener carpetas externas, archivos de configuración, dependencias o `hidden-import` particulares.

> **Nota de seguridad:** PyInstaller empaqueta el código Python, pero no debe considerarse un mecanismo de protección u ofuscación fuerte del código fuente. El usuario no recibe los `.py` directamente, pero un ejecutable puede ser analizado por terceros con conocimientos técnicos.

---

# 2. Estándar adoptado: usar `--onedir`

Para estos proyectos se recomienda usar PyInstaller en modo **`--onedir`**.

Esto genera una carpeta distribuible similar a:

```text
dist/
└── MiAplicacion/
    ├── _internal/
    └── MiAplicacion.exe
```

La aplicación se entrega como **una carpeta completa**, no como un `.exe` aislado.

## ¿Por qué usar `--onedir`?

- Es más fácil de diagnosticar.
- Facilita actualizaciones.
- Suele iniciar más rápido que `--onefile`.
- Permite mantener archivos operativos externos.
- Reduce problemas al trabajar con plantillas, Excel, imágenes y configuraciones externas.

> Esta guía queda estandarizada sobre `--onedir`. Si algún día se desea usar `--onefile`, el procedimiento cambia en algunos puntos y no debe asumirse que existirá `_internal/`.

---

# 3. Trabajar primero sobre una copia

Antes de generar el `.exe`:

1. Hacer una copia completa del proyecto.
2. Trabajar y probar sobre esa copia.
3. Mantener intacta la versión fuente estable.

Ejemplo:

```text
Proyecto original:
Ordenes_internas_AIE

Copia para distribución:
Ordenes_internas_AIE_EXE
```
### NOTA:
# Entorno virtual cuando se trabaja sobre una copia del proyecto

Cuando se crea una copia del proyecto para preparar o generar el `.exe`, es recomendable que esa copia tenga su propio entorno virtual `venv`.

Ejemplo:

```text
Proyecto original:

Ordenes_internas_AIE/
└── venv/

Copia para empaquetado:

Ordenes_internas_AIE_C/
└── venv/
```

## ¿Por qué?
Aunque la consola esté ubicada dentro de la carpeta de la copia:

```text
C:\Users\...\Ordenes_internas_AIE_C>
```

puede ocurrir que el venv activo siga perteneciendo al proyecto original.

Ejemplo incorrecto:

Proyecto actual:

```text
C:\Users\...\Ordenes_internas_AIE_C

Python utilizado:

C:\Users\...\Ordenes_internas_AIE\venv\Scripts\python.exe
```

Esto significa que la copia está utilizando las librerías instaladas en el entorno virtual del proyecto original.

Para evitar dependencias accidentales, conviene crear y utilizar un venv propio dentro de la copia.

## Procedimiento recomendado

Ubicarse primero en la copia:

```text
cd C:\Users\...\Ordenes_internas_AIE_C
```

Si existe otro entorno virtual activo:

```text
deactivate
```

Crear el entorno virtual de la copia:

```text
python -m venv venv
```

Activarlo

```text
venv\Scripts\activate
```

Instalar las dependencias:

```text
python -m pip install -r requirements.txt
```

Verificar qué Python está utilizando la consola:

```text
python -c "import sys; print(sys.executable)"
```

El resultado debe apuntar al venv de la copia:

```text
C:\Users\...\Ordenes_internas_AIE_C\venv\Scripts\python.exe
```

Después probar normalmente:

```text
python main.py
```

y posteriormente instalar o utilizar PyInstaller dentro de ese mismo entorno.

## Regla práctica

Proyecto original
→ utiliza su propio venv

Copia para pruebas o empaquetado
→ utiliza su propio venv

El nombre de la copia, por ejemplo _C, solamente sirve para identificarla visualmente. Python y PyInstaller no le dan ningún significado especial.

Tener un venv independiente en la copia evita que la compilación dependa accidentalmente de librerías instaladas únicamente en el proyecto original.

```text
Crear copia
↓
Crear/activar venv propio de la copia
↓
Instalar requirements
↓
Verificar sys.executable
↓
Probar python main.py
↓
PyInstaller
```
---

# 4. Identificar código y recursos externos

## Código Python que será empaquetado

Ejemplo:

```text
main.py
src/
config/configuracion.py
otros módulos .py
```

## Recursos que pueden permanecer externos

Ejemplos:

```text
entrada/
salida/
logs/
assets/
config/
plantillas/
dashboard/
mapas/
archivos .xlsx de configuración
```

> **Muy importante:** si una carpeta como `config/` contiene tanto `.py` como archivos externos, **no es necesario copiar los `.py` al usuario**. Por ejemplo:

```text
config/
└── BASE_DIRECCIONES_MUNICIPIOS.xlsx
```

El archivo `configuracion.py` ya queda empaquetado por PyInstaller.

Una carpeta del proyecto puede contener simultáneamente código Python y archivos funcionales externos. Al construir la versión distribuible, los .py importados quedan empaquetados por PyInstaller, mientras que solo deben copiarse externamente los archivos que el usuario o la aplicación necesiten consultar o modificar después de la compilación.

Por ejemplo:

```text
PROYECTO FUENTE

config/
├── configuracion.py
└── BASE_DIRECCIONES_MUNICIPIOS.xlsx
```

se transforma conceptualmente en:

```text
DISTRIBUCIÓN

Ordenes_Internas_AIE.exe
    └── contiene configuracion.py empaquetado

config/
└── BASE_DIRECCIONES_MUNICIPIOS.xlsx
```
Así que sí: puedes entregar la carpeta config solamente con el Excel. Esa es la estructura correcta para este proyecto, osea:

Tu proyecto de desarrollo debe conservar:

```text
Ordenes_internas_AIE/
└── config/
    ├── configuracion.py
    └── BASE_DIRECCIONES_MUNICIPIOS.xlsx
```

Después de generar el .exe, en:

```text
dist/Ordenes_Internas_AIE/
```
creas o dejas la carpeta:

```text
config/
└── BASE_DIRECCIONES_MUNICIPIOS.xlsx
```
y no copias configuracion.py ahí.
PROYECTO FUENTE
→ conserva configuracion.py

DISTRIBUCIÓN PARA EL USUARIO
→ solo conserva el Excel externo


---

# 5. Preparar una ruta raíz compatible con Python y `.exe`

Si el archivo central de configuración está en:

```text
config/configuracion.py
```
Todo proyecto debe tener un módulo central de configuración, preferiblemente config/configuracion.py, encargado de definir BASE_DIR y todas las rutas del proyecto

Para tus proyectos, esa convención me parece muy buena porque te simplifica mucho la vida.

La base sería esta:


```python
from pathlib import Path
import sys


# ============================================================
# RUTA RAIZ DEL PROYECTO
# ============================================================

if getattr(sys, "frozen", False):

    # Ejecutando como .exe generado con PyInstaller
    BASE_DIR = Path(
        sys.executable
    ).resolve().parent

else:

    # Ejecutando normalmente con Python
    BASE_DIR = (
        Path(__file__)
        .resolve()
        .parent
        .parent
    )
```

Después construir las rutas externas desde `BASE_DIR`:

```python
# ============================================================
# CARPETAS DEL PROYECTO
# ============================================================

ENTRADA_DIR = BASE_DIR / "entrada"
SALIDA_DIR = BASE_DIR / "salida"
LOGS_DIR = BASE_DIR / "logs"
ASSETS_DIR = BASE_DIR / "assets"
CONFIG_DIR = BASE_DIR / "config"
```

## Regla importante

No permitir que diferentes módulos calculen independientemente la raíz del proyecto.

Preferir importar las rutas centralizadas:

```python
from config.configuracion import (
    BASE_DIR,
    ENTRADA_DIR,
    SALIDA_DIR,
    ASSETS_DIR,
)
```

> Si en otro proyecto el archivo de configuración está ubicado directamente en la raíz y no dentro de `config/`, la línea de desarrollo cambia. La regla universal es **calcular correctamente la raíz una sola vez y centralizarla**.

---

# 6. Usar imports claros

Preferir imports absolutos:

```python
from src.procesador import procesar_datos
from src.lector import leer_archivo
from config.configuracion import BASE_DIR
```

Evitar, cuando sea posible:

```python
from procesador import procesar_datos
```

También conviene evitar modificaciones manuales de `sys.path` salvo que exista una necesidad real.

---

# 7. Activar el entorno virtual

Desde la raíz del proyecto:

```bat
venv\Scripts\activate
```

La consola debe mostrar algo parecido a:

```text
(venv) C:\...\MiProyecto>
```

---

# 8. Probar Python antes de compilar

Con el `venv` activo usar preferiblemente:

```bat
python main.py
```

Validar todas las funciones principales:

```text
Abrir aplicación
↓
Detectar archivos
↓
Procesar información
↓
Generar salida
↓
Abrir resultados
↓
Cerrar correctamente
```

No continuar con PyInstaller hasta que esta prueba sea satisfactoria.

---

# 9. Instalar PyInstaller

Con el `venv` activo:

```bat
python -m pip install pyinstaller
```

Verificar:

```bat
python -m PyInstaller --version
```

> PyInstaller es una herramienta de construcción. No es obligatorio incluirlo en el `requirements.txt` destinado al usuario final.

---

# 10. Limpiar compilaciones anteriores

Si ya existe una compilación anterior, eliminar de la copia de distribución:

```text
build/
dist/NOMBRE_APLICACION/
NOMBRE_APLICACION.spec
```

También puede eliminarse toda `dist/` si en esa copia no contiene información que deba conservarse.

---

# 11. Comando estándar para generar el `.exe`

## Sin icono

```bat
python -m PyInstaller --clean --noconfirm --onedir --windowed --name NOMBRE_APLICACION main.py
```

## Con icono

```bat
python -m PyInstaller --clean --noconfirm --onedir --windowed --icon=assets\LOGO_PRO.ico --name NOMBRE_APLICACION main.py
```

## Significado

```text
--clean      Limpia caché y archivos temporales.
--noconfirm  Permite reemplazar resultados anteriores.
--onedir     Genera una carpeta con el .exe y _internal.
--windowed   No muestra consola negra en aplicaciones gráficas.
--icon       Asigna el icono de Windows al ejecutable.
--name       Define el nombre del ejecutable.
```

---

# 12. Dependencias ocultas

No existe un `hidden-import` universal.

Solo se agrega cuando el proyecto realmente lo necesita.

Ejemplo:

```bat
python -m PyInstaller --clean --noconfirm --onedir --windowed --hidden-import=win32timezone --name MiAplicacion main.py
```

Caso conocido:

```text
Informe ANS ATC CHEC
→ puede requerir win32timezone
```

Esto no significa que otros proyectos también lo necesiten.

---

# 13. Resultado esperado

Después de compilar aparecerán:

```text
build/
dist/
NOMBRE_APLICACION.spec
```

En modo `--onedir`:

```text
dist/
└── NOMBRE_APLICACION/
    ├── _internal/
    └── NOMBRE_APLICACION.exe
```

## Regla

No copiar únicamente el `.exe`.

El `.exe` y `_internal/` deben considerarse **un mismo conjunto de compilación**.

---

# 14. Copiar archivos externos necesarios

Dentro de:

```text
dist/NOMBRE_APLICACION/
```

copiar únicamente los elementos externos que el programa necesita durante su ejecución.

Ejemplo:

```text
Ordenes_Internas_AIE/
├── _internal/
├── assets/
├── config/
│   └── BASE_DIRECCIONES_MUNICIPIOS.xlsx
├── entrada/
├── salida/
├── logs/
└── Ordenes_Internas_AIE.exe
```

---

# 15. Prueba obligatoria desde `dist`

Ejecutar:

```text
dist/NOMBRE_APLICACION/NOMBRE_APLICACION.exe
```

Validar:

```text
La interfaz abre
El icono aparece
Los archivos de entrada se detectan
Los archivos de configuración se leen
La información se procesa
Los archivos de salida se generan
Los botones funcionan
La aplicación cierra sin error
```

Si la ventana abre pero no puede procesar o generar la salida, **todavía no está listo**.

---

# 16. Prueba en otro computador

1. Copiar toda la carpeta de distribución.
2. Llevarla mediante USB, red o carpeta compartida.
3. Copiarla al disco del computador destino.
4. No ejecutarla directamente desde la USB si se puede evitar.
5. Abrir el `.exe`.
6. Ejecutar el flujo completo.

> El usuario final no necesita instalar Python ni crear un `venv`.

---

# 17. Posibles avisos de Windows

Un `.exe` generado internamente y no firmado digitalmente puede producir advertencias de Windows Defender o SmartScreen.

En entornos empresariales pueden existir además políticas de seguridad que bloqueen ejecutables desconocidos. Si ocurre, debe revisarse con TI.

---

# 18. Errores frecuentes

## `ModuleNotFoundError`

Revisar:

```text
imports
módulo faltante
hidden-import
dependencias instaladas en el venv usado para compilar
```

## Busca archivos dentro de `_internal`

Revisar `BASE_DIR` y cualquier uso directo de `__file__` para rutas externas.

## No encuentra configuración o plantilla

Verificar que el archivo externo exista junto al ejecutable en la ubicación esperada.

## Funciona con Python pero no como `.exe`

Revisar:

```text
BASE_DIR
imports
hidden-import
archivos externos
dependencias
permisos
```

---

# 19. Crear acceso directo

El `.exe` debe permanecer dentro de su carpeta de instalación.

Crear un acceso directo:

```text
Clic derecho sobre NOMBRE_APLICACION.exe
→ Mostrar más opciones
→ Enviar a
→ Escritorio (crear acceso directo)
```

---

# 20. Qué se entrega al usuario

Ejemplo:

```text
Ordenes_Internas_AIE/
├── _internal/
├── assets/
├── config/
│   └── BASE_DIRECCIONES_MUNICIPIOS.xlsx
├── entrada/
├── salida/
├── logs/
└── Ordenes_Internas_AIE.exe
```

Normalmente **no es necesario entregar**:

```text
src/
venv/
main.py
*.py
build/
*.spec
requirements.txt
```

---

# 21. Actualización cuando cambia el código Python

Si cambia código Python, se debe volver a compilar.

Flujo:

```text
Modificar código
↓
Probar con python main.py
↓
Compilar nueva versión
↓
Probar nueva versión en dist
↓
Respaldar instalación actual
↓
Actualizar runtime
↓
Probar nuevamente
```

## Regla importante para `--onedir`

El nuevo `.exe` y la nueva carpeta `_internal/` deben provenir de **la misma compilación**.

No mezclar un `.exe` nuevo con un `_internal` antiguo.

Es preferible reemplazar completamente `_internal/`.

---

# 22. Qué carpetas conservar durante una actualización

Normalmente conservar:

```text
entrada/
entrada_redes/
salida/
salida_redes/
logs/
```

Actualizar solamente si corresponde:

```text
assets/
config/
dashboard/
mapas/
plantillas/
```

Antes de reemplazar `config/`, verificar si el usuario realizó cambios propios.

---

# 23. Si cambia solamente un archivo externo

Si cambia únicamente un archivo externo como:

```text
BASE_DIRECCIONES_MUNICIPIOS.xlsx
configuracion.xlsx
plantilla.xlsx
archivo maestro
logo externo
```

normalmente **no es necesario recompilar**.

Solo se reemplaza el archivo externo correspondiente y se vuelve a probar.

---

# 24. Plantilla universal de trabajo

```text
1. Crear copia de distribución.
2. Identificar main.py.
3. Identificar código Python.
4. Identificar recursos externos.
5. Centralizar BASE_DIR.
6. Revisar imports.
7. Activar venv.
8. Probar con python main.py.
9. Instalar/verificar PyInstaller.
10. Limpiar compilación anterior.
11. Compilar con --onedir --windowed.
12. Agregar --icon si corresponde.
13. Agregar hidden-import solo si es necesario.
14. Copiar recursos externos requeridos.
15. Probar flujo completo desde dist.
16. Copiar carpeta completa a otro PC.
17. Probar flujo completo en otro PC.
18. Crear acceso directo.
19. Entregar sin src, venv ni archivos .py.
```

---

# 25. Ejemplo — Informe ANS ATC CHEC

```bat
python -m PyInstaller --clean --noconfirm --onedir --windowed --hidden-import=win32timezone --name Informe_ANS_ATC_CHEC main.py
```

---

# 26. Ejemplo — Órdenes Internas AIE

Comando inicial recomendado:

```bat
python -m PyInstaller --clean --noconfirm --onedir --windowed --icon=assets\LOGO_PRO.ico --name Ordenes_Internas_AIE main.py
```

Distribución esperada:

```text
Ordenes_Internas_AIE/
├── _internal/
├── assets/
├── config/
│   └── BASE_DIRECCIONES_MUNICIPIOS.xlsx
├── entrada/
├── salida/
├── logs/
└── Ordenes_Internas_AIE.exe
```

Antes de considerarlo terminado:

```text
1. Probar Ordenes_Internas_AIE.exe desde dist.
2. Generar un consolidado completo.
3. Abrir el consolidado desde la interfaz.
4. Verificar BASE_DIRECCIONES_MUNICIPIOS.xlsx.
5. Verificar logo/icono.
6. Probar la carpeta completa en otro computador.
7. Crear acceso directo.
```

---

# 27. Regla final

> El procedimiento base de PyInstaller puede reutilizarse en todos los proyectos, pero cada nuevo desarrollo debe pasar por una revisión corta de:
>
> - ruta raíz;
> - recursos externos;
> - dependencias;
> - icono;
> - `hidden-import`;
> - prueba desde `dist`;
> - prueba en otro computador.

El `.exe` se considera terminado únicamente cuando **el flujo funcional completo** opera correctamente desde `dist` y posteriormente en un computador diferente al equipo de desarrollo.
