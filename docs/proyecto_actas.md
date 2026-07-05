# 📄 Proyecto Actas
# Automatización de Consolidación de Actas

---

# Objetivo

El objetivo de este proyecto fue automatizar completamente la consolidación de las actas operativas provenientes de las diferentes zonas de operación.

Antes del desarrollo, el proceso se realizaba manualmente:

- Abrir cada archivo Excel.
- Copiar la información.
- Pegarla en un histórico.
- Revisar pedidos.
- Corregir inconsistencias.
- Generar indicadores.

A medida que el histórico fue creciendo (más de 100.000 registros), este proceso comenzó a consumir demasiado tiempo y aumentó el riesgo de errores.

Por esta razón se desarrolló un proceso ETL en Python que realiza toda la consolidación de forma automática.

---

# Estructura del proyecto

```text
Proyecto_Actas

│

├── ACTAS_RAW
│      ACTA 1
│      ACTA 2
│      ACTA 3
│      ...
│
├── CONFIG
│      correcciones_pedidos.xlsx
│
├── UNIFICADAS
│      ACTAS_UNIFICADAS.xlsx
│
└── consolidar_actas.py
```

Cada carpeta cumple una función específica.

- **ACTAS_RAW** contiene todas las actas originales.
- **CONFIG** almacena archivos auxiliares.
- **UNIFICADAS** contiene el histórico consolidado.
- **consolidar_actas.py** ejecuta todo el proceso.

---

# Flujo General

Todo el proceso sigue siempre el mismo flujo.

```text
ACTAS_RAW

↓

Buscar archivos Excel

↓

Leer información

↓

Limpiar datos

↓

Normalizar pedidos

↓

Aplicar correcciones

↓

Agregar columnas nuevas

↓

Agrupar actividades

↓

Construir DataFrame final

↓

Modo RECONSTRUIR
o
Modo ANEXAR

↓

Generar ACTAS_UNIFICADAS.xlsx
```

Todo el proceso se ejecuta automáticamente.

---

# Modos de Ejecución

El sistema trabaja con dos modos.

---

## RECONSTRUIR

Este modo vuelve a construir completamente el histórico.

¿Cuándo se utiliza?

- Cuando cambia una regla de negocio.
- Cuando se desea regenerar completamente el consolidado.
- Cuando se requiere validar nuevamente toda la información.

El proceso realiza:

- Lee todas las actas.
- Consolida toda la información.
- Genera nuevamente el archivo ACTAS_UNIFICADAS.xlsx.

---

## ANEXAR

Este es el modo utilizado diariamente.

El objetivo es evitar volver a procesar información que ya existe.

El proceso realiza:

- Lee el histórico existente.
- Identifica las combinaciones ACTA + ZONA ya procesadas.
- Omite automáticamente las existentes.
- Procesa únicamente las nuevas.
- Agrega únicamente los nuevos registros.

Con esto se reduce considerablemente el tiempo de procesamiento.

---
# Inicio de la Ejecución del Consolidador

Una vez ejecutamos el script:

```bash
py consolidar_actas.py
```

el sistema inicia mostrando una pantalla de bienvenida.

```text
============================================================
             PROYECTO ACTAS
      Sistema de Consolidación de Actas
                 Versión 1.0
============================================================
```

Esta pantalla simplemente identifica la aplicación que se está ejecutando y permite saber que el proceso inició correctamente.

---

# Selección del Modo de Trabajo

Antes de comenzar el procesamiento, el sistema solicita al usuario el modo de ejecución.

```text
[1] RECONSTRUIR

[2] ANEXAR

[0] Cancelar
```

La idea es que el mismo programa pueda utilizarse para dos escenarios completamente diferentes sin necesidad de modificar el código.

---

## Modo RECONSTRUIR

Este modo vuelve a construir completamente el histórico.

Se utiliza cuando:

- Se modificó una regla de negocio.
- Se requiere reconstruir todas las actas.
- Se desea validar nuevamente toda la información.

En este modo el sistema:

- Busca todas las actas.
- Procesa todos los archivos Excel.
- Genera nuevamente el histórico completo.

Es decir, comienza desde cero.

---

## Modo ANEXAR

Este es el modo utilizado normalmente durante la operación diaria.

Su objetivo es evitar volver a procesar información que ya existe.

En lugar de reconstruir todo el histórico, el sistema:

- Abre el histórico actual.
- Revisa qué Actas y Zonas ya fueron procesadas.
- Omite automáticamente esas combinaciones.
- Procesa únicamente las nuevas.

Con esto se reduce considerablemente el tiempo de ejecución.

---

# Confirmación del Modo Seleccionado

Una vez seleccionada la opción, el sistema informa claramente qué proceso realizará.

Por ejemplo:

```text
Modo seleccionado : ANEXAR
```

También explica qué ocurrirá.

```text
Se conservará el histórico existente.

Solo se agregarán ACTAS + ZONAS nuevas.
```

Esta confirmación evita ejecutar el proceso incorrecto por error.

---

# Información General del Proceso

Antes de comenzar el procesamiento, el sistema muestra información importante sobre la ejecución.

```text
Carpeta origen

Carpeta salida

Archivo destino

Modo seleccionado
```

Con esta información es posible verificar rápidamente que el sistema está trabajando sobre las rutas correctas.

---

# Inicio del Procesamiento

Cuando se presiona ENTER comienza realmente el proceso.

El sistema muestra:

```text
Iniciando proceso...
```

A partir de este momento empieza la búsqueda de todas las actas disponibles.

---

# Validación de Actas Existentes

Cuando se selecciona el modo **ANEXAR**, el sistema primero abre el histórico existente:

```text
ACTAS_UNIFICADAS.xlsx
```

De este archivo únicamente obtiene las combinaciones **Acta + Zona** que ya fueron consolidadas.

Posteriormente comienza a recorrer todos los archivos encontrados dentro de la carpeta **ACTAS_RAW**.

Para cada archivo identifica automáticamente:

- Número de acta.
- Zona.
- Nombre del archivo.

Con esta información compara si esa combinación ya existe dentro del histórico.

Cuando la combinación ya fue procesada anteriormente, el sistema no vuelve a consolidar ese archivo y muestra un mensaje como:

```text
⏭️ ACTA 2 - METROPOLITANO ya existe. Se omite.
```

Luego continúa automáticamente con el siguiente archivo disponible.

Este proceso se repite hasta revisar todas las actas encontradas.

---

# Cuando no existen actas nuevas

Si después de revisar todos los archivos el sistema determina que todas las Actas + Zonas ya existen dentro del histórico, finaliza mostrando:

```text
✅ No se encontraron actas nuevas para anexar.
```

Este mensaje indica que el histórico ya se encuentra actualizado y que no fue necesario agregar nuevos registros.


---

# Beneficio de esta validación

Gracias a esta lógica el sistema evita procesar información repetida.

Esto permite que durante la operación diaria únicamente se lean las actas nuevas, reduciendo considerablemente el tiempo de ejecución y evitando duplicar información dentro del histórico.

# Búsqueda Automática de Archivos

No es necesario indicar manualmente qué archivos deben procesarse.

El sistema busca automáticamente todos los archivos Excel ubicados dentro de:

```text
ACTAS_RAW
```

También ignora automáticamente archivos temporales de Excel.

---

# Lectura de la Información

Por cada archivo encontrado el sistema realiza:

- Lectura de la hoja correcta.
- Normalización de nombres de columnas.
- Conversión de algunos campos a texto.
- Eliminación de columnas técnicas.
- Eliminación de filas vacías.

El objetivo es garantizar que todos los archivos tengan exactamente la misma estructura antes de consolidarlos.

---

# Normalización de Pedidos

Uno de los pasos más importantes del proyecto consiste en normalizar el campo Pedido.

Durante este proceso el sistema:

- elimina espacios
- elimina saltos de línea
- elimina ".0"
- elimina valores nulos
- convierte todos los pedidos al mismo formato

Posteriormente muestra información de validación como:

- cantidad de pedidos
- pedidos únicos
- pedidos repetidos
- longitud de los pedidos

Esta validación permite detectar problemas antes de consolidar la información.

---

# Corrección Automática de Pedidos

No todas las correcciones deben realizarse desde el código.

Por esta razón el proyecto utiliza un archivo independiente.

```text
CONFIG

↓

correcciones_pedidos.xlsx
```

Cuando un pedido requiere modificar:

- contrato
- zona

simplemente se actualiza esta tabla.

Durante la ejecución el sistema consulta automáticamente este archivo y aplica las correcciones correspondientes.

De esta manera no es necesario modificar el código Python.

---

# Columnas de Trazabilidad

Durante la consolidación se agregan columnas que permiten identificar fácilmente el origen de cada registro.

Entre ellas:

- Acta
- Zona

Estas columnas permiten posteriormente realizar filtros, indicadores y auditorías.

---

# Agrupación de Actividades

Las actividades llegan con muchos códigos diferentes.

Para facilitar el análisis se agrupan automáticamente en categorías de negocio como:

- Legalización
- AGPE
- HV
- Prepago
- Movimiento de Redes
- Puntos de Conexión
- Movilidad Eléctrica
- Órdenes Internas

Esto permite construir indicadores mucho más fáciles de interpretar.

---

# Construcción del Histórico

Una vez procesados todos los archivos se crea un único DataFrame consolidado.

Dependiendo del modo seleccionado:

## RECONSTRUIR

Se genera completamente desde cero.

## ANEXAR

Se conserva el histórico y únicamente se agregan los nuevos registros.

---

# Indicadores Generados

Además del histórico principal se generan automáticamente tres hojas adicionales.

---

## ACTAS_UNIFICADAS

Es el histórico completo.

Contiene todos los registros consolidados.

Es la hoja principal del proyecto.

---

## PEDIDOS_POR_ACTA

Permite conocer los eventos operativos únicos para cada acta.

---

## PEDIDOS_UNICOS

Contiene todos los pedidos empresariales únicos.

Esta hoja facilita posteriores consultas y validaciones.

---

## PEDIDOS_REPETIDOS

Identifica automáticamente los pedidos presentes en más de una acta.

Esta hoja sirve como herramienta de control para revisar posibles inconsistencias.

---
