# 🚗 SERVITRAVEL
# Automatización ETL con Python + Excel

> **Estado del proyecto:** En desarrollo  
> **Autor:** Héctor Alejandro Gaviria  
> **Lenguaje:** Python 3  
> **Tecnologías:** Pandas · xlwings · OpenPyXL · Excel (.xlsx / .xlsb)

---

# 1. Introducción

## Objetivo

SERVITRAVEL es un proyecto de automatización ETL cuyo propósito es consolidar información proveniente de múltiples archivos Excel operativos en un único archivo maestro de liquidación.

El proceso elimina tareas manuales repetitivas, reduce errores de digitación y garantiza que toda la información quede centralizada con un formato uniforme.

---

## Problema que resuelve

Antes de esta automatización, la consolidación se realizaba manualmente:

- Abrir múltiples archivos Excel.
- Copiar información hoja por hoja.
- Pegar datos en el consolidado.
- Validar formatos.
- Revisar zonas.
- Calcular meses y cortes.
- Evitar duplicidades.

Este procedimiento consumía una gran cantidad de tiempo y era propenso a errores humanos.

SERVITRAVEL automatiza completamente este flujo.

---

## Alcance

Actualmente el proyecto consolida cuatro procesos independientes:

- Año 2026
- Viáticos
- Parqueaderos
- Peajes

Todos los procesos escriben directamente sobre un archivo consolidado en formato **.xlsb**, conservando el formato original del archivo.

---

# 2. Arquitectura del Proyecto

## Estructura

```text
SERVITRAVEL
│
├── backup
├── entrada
├── logs
├── procesados
├── salida
│
├── src
│   ├── config.py
│   ├── excel_utils.py
│   ├── consolidador.py
│   └── main.py
│
├── docs
│   └── 14_servitravel_etl.md
│
├── README.md
└── requirements.txt
```

---
# 0. Guía de Ejecución

Esta sección describe el procedimiento operativo para ejecutar correctamente el proceso de consolidación.

---

## Paso 1. Preparar los archivos origen

Copiar los archivos Excel enviados por cada zona dentro de la carpeta:

```
SERVITRAVEL/
└── entrada/
```

Ejemplo:

```
entrada/
│
├── METROPOLITANO.xlsx
├── OCCIDENTE.xlsx
├── ORIENTE.xlsx
├── NORDESTE.xlsx
└── SUROESTE.xlsx
```

---

## Paso 2. Verificar el archivo consolidado

Comprobar que existe el archivo:

```
salida/
└── INFORME_LIQUIDACION.xlsb
```

Este será el archivo donde se escribirá toda la información consolidada.

---

## Paso 3. Ejecutar el proyecto

Abrir Visual Studio Code.

Abrir una terminal.

Ingresar a la carpeta del proyecto.

Activar el entorno virtual.

Windows

```bash
venv\Scripts\activate
```

Luego ejecutar:

```bash
python src/main.py
```

---

## Paso 4. Creación automática del Backup

Antes de realizar cualquier modificación, el sistema crea automáticamente una copia de seguridad en:

```
backup/
```

Ejemplo:

```
INFORME_LIQUIDACION_20260704_093512.xlsb
```

---

## Paso 5. Apertura del consolidado

El sistema abre automáticamente:

```
salida/
INFORME_LIQUIDACION.xlsb
```

utilizando **xlwings**.

---

## Paso 6. Consolidación de información

Durante la ejecución se procesan, en este orden:

1. Año 2026
2. Viáticos
3. Parqueaderos
4. Peajes

Cada módulo:

- Lee el archivo origen.
- Detecta automáticamente los encabezados.
- Construye el DataFrame destino.
- Agrega la información al consolidado.
- Conserva el formato de Excel.

---

## Paso 7. Guardado

Finalizada la consolidación:

- Se guarda el archivo.
- Se cierran todas las instancias de Excel.
- Se libera la memoria utilizada.

---

## Paso 8. Verificación

Revisar el archivo:

```
salida/
INFORME_LIQUIDACION.xlsb
```

Verificar que existan datos en:

- Año 2026
- Viáticos
- Parqueaderos
- Peajes

---

## Paso 9. Validar consola

Al finalizar debe visualizarse un mensaje similar a:

```
==================================================
PROCESO FINALIZADO CORRECTAMENTE
==================================================
```

Sin errores.

---

## Flujo resumido

```
Copiar archivos

↓

Abrir VS Code

↓

Activar entorno virtual

↓

python src/main.py

↓

Backup automático

↓

Abrir consolidado

↓

Procesar Año 2026

↓

Procesar Viáticos

↓

Procesar Parqueaderos

↓

Procesar Peajes

↓

Guardar

↓

Cerrar Excel

↓

Proceso finalizado
```

---

## Propósito de cada carpeta

### entrada

Contiene los archivos Excel enviados por cada zona.

Cada archivo representa la información origen que será consolidada.

---

### salida

Contiene el archivo maestro:

```
INFORME_LIQUIDACION.xlsb
```

Este archivo recibe toda la información consolidada.

---

### backup

Antes de iniciar cualquier proceso se genera automáticamente una copia de seguridad del consolidado.

Esto permite recuperar la información ante cualquier error inesperado.

---

### procesados

En versiones futuras almacenará los archivos ya procesados para evitar reprocesamientos.

---

### logs

Reservada para registrar:

- errores
- advertencias
- tiempos de ejecución
- estadísticas del proceso

---

### docs

Contiene toda la documentación técnica del proyecto.

La documentación es evolutiva y se actualiza durante el desarrollo.

---

# 3. Arquitectura del Código

El proyecto está dividido en cuatro módulos principales.

## config.py

Centraliza toda la configuración del sistema.

Responsabilidades:

- Definir rutas.
- Definir nombres de hojas.
- Definir nombres de archivos.
- Evitar rutas escritas directamente en el código.

---

## excel_utils.py

Contiene todas las funciones reutilizables relacionadas con Excel.

Ejemplos:

- crear_backup()
- abrir_excel()
- cerrar_excel()
- leer_tabla()
- buscar_encabezados()
- escribir_dataframe()
- obtener_mes()
- obtener_corte()
- obtener_zona()

Este módulo concentra toda la lógica técnica relacionada con la lectura y escritura de archivos Excel.

---

## consolidador.py

Contiene la lógica de negocio.

Actualmente implementa los procesos:

- consolidar_anio()
- consolidar_viaticos()
- consolidar_parqueaderos()
- consolidar_peajes()

Cada función transforma los datos antes de escribirlos en el consolidado.

---

## main.py

Es el punto de entrada del sistema.

Orquesta completamente el flujo ETL.

No contiene lógica de transformación.

Su única responsabilidad es coordinar el proceso.

---

# 4. Flujo ETL

El proceso completo sigue la siguiente secuencia:

```text
Inicio

↓

Crear Backup

↓

Abrir INFORME_LIQUIDACION.xlsb

↓

Consolidar Año 2026

↓

Consolidar Viáticos

↓

Consolidar Parqueaderos

↓

Consolidar Peajes

↓

Guardar archivo

↓

Cerrar Excel

↓

Proceso Finalizado
```

Este flujo garantiza que todas las hojas sean procesadas en una única ejecución.

---

# 5. Principios de Diseño

Durante el desarrollo se adoptaron varios principios de arquitectura para facilitar el mantenimiento y la escalabilidad del proyecto.

## Separación de responsabilidades

Cada módulo tiene una responsabilidad claramente definida.

Esto evita código duplicado y facilita futuras modificaciones.

---

## Configuración centralizada

Las rutas y constantes se almacenan únicamente en `config.py`.

De esta manera, un cambio de ubicación o nombre de archivo solo requiere una modificación en un único lugar.

---

## Reutilización de funciones

Las tareas repetitivas se encapsulan en funciones reutilizables.

Ejemplos:

- abrir_excel()
- leer_tabla()
- escribir_dataframe()
- obtener_zona()

Este enfoque reduce la duplicidad de código y simplifica el mantenimiento.

---

## Automatización del proceso

El usuario únicamente ejecuta el archivo principal.

El sistema se encarga automáticamente de:

- crear el respaldo,
- abrir el consolidado,
- procesar todas las hojas,
- guardar los cambios,
- cerrar Excel.

---

# 6. Estado Actual del Proyecto

## Funcionalidades implementadas

- Configuración centralizada.
- Creación automática de backup.
- Apertura y cierre seguro de Excel.
- Lectura dinámica de tablas.
- Detección automática de encabezados.
- Normalización de encabezados.
- Consolidación Año 2026.
- Consolidación Viáticos.
- Consolidación Parqueaderos.
- Consolidación Peajes.
- Cálculo automático de mes.
- Cálculo automático de corte.
- Obtención automática de zona.
- Copia de formatos del consolidado.
- Resumen por zonas.
- Manejo básico de errores.

---

# 7. Próximas Versiones

## Versión 2.0

Objetivos propuestos:

- Abrir cada archivo Excel una única vez.
- Procesar todas las hojas durante una sola lectura.
- Mover automáticamente los archivos procesados.
- Implementar sistema de logs.
- Reducir significativamente el tiempo de ejecución.
- Incorporar métricas de rendimiento.

---

# 8. Filosofía del Proyecto

SERVITRAVEL no busca únicamente automatizar archivos Excel.

El objetivo es construir un proceso ETL mantenible, escalable y documentado, siguiendo principios de ingeniería de software.

La documentación evoluciona junto con el código, permitiendo que cualquier desarrollador pueda comprender el funcionamiento del sistema y continuar su evolución sin depender del conocimiento del autor original.