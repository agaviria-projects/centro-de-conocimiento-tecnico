## 🎯 Objetivo


La herramienta de Validación Mano de Obra Vs Materiales fue desarrollada para verificar automáticamente que los materiales reportados en Fénix correspondan correctamente a la mano de obra ejecutada en cada pedido.

Cada mano de obra debe tener asociados uno o varios materiales obligatorios definidos en una base maestra.

El sistema compara lo reportado en Fénix contra esa base maestra y determina si la información está correcta o si existen materiales faltantes, sobrantes, duplicados o cantidades que requieren revisión.

Más adelante, la base maestra permite explicar qué materiales debe llevar cada mano de obra y qué reglas especiales aplican para cada caso.

El objetivo principal es detectar inconsistencias operativas antes del cierre del proceso, reduciendo errores manuales y mejorando la calidad de la información reportada.

---

## 🧩 Problema que resuelve

Antes del desarrollo, la validación entre manos de obra y materiales se realizaba manualmente, revisando grandes volúmenes de información en Excel.

Este proceso podía generar:

- Errores humanos.
- Omisión de materiales obligatorios.
- Registro de materiales no permitidos.
- Duplicidad de actividades.
- Inconsistencias en cantidades.
- Demoras en la auditoría operativa.

La herramienta automatiza completamente estas validaciones.

---

## 📂 Archivos requeridos

El proceso requiere dos fuentes principales de información.

### 📄 Exportación Fénix

- Se exportan los archivos desde Fenix.
- Se realiza por rangos de fechas.
- Se exporta por Zonas.

La herramienta permite procesar uno o varios archivos exportados desde Fénix al mismo tiempo.

Cuando se exporta un archivo por cada zona operativa, el sistema consolida automáticamente toda la información en un único informe, facilitando el análisis global de la operación y permitiendo posteriormente filtrar por zona cuando sea necesario.

### 📘 Base Maestra

La base maestra es el archivo donde se define qué materiales debe llevar cada código de mano de obra.

`RELACION_MO_MATERIALES.xlsx`

Cada fila representa una mano de obra y sus materiales asociados.

La base permite identificar:

- Materiales obligatorios.
- Materiales permitidos.
- Reglas especiales como “uno de los dos” o “uno de los cinco”.
- Excepciones operativas.

---

## ⚙️ Funcionamiento general

El sistema realiza automáticamente las siguientes tareas:

1. Lee todos los archivos TXT ubicados en la carpeta de entrada.
2. Identifica las manos de obra registradas.
3. Identifica los materiales asociados a cada pedido.
4. Normaliza los códigos.
5. Consolida la información.
6. Cruza la información contra la base maestra.
7. Aplica reglas especiales de negocio.
8. Genera alertas automáticas.
9. Exporta un informe final en Excel.

---

## 🔍 Validaciones realizadas

### ✅ Materiales correctos

Todos los materiales requeridos fueron encontrados.

**Estado:** `OK`

---

### ❌ Faltan materiales

La actividad requiere materiales que no fueron reportados.

**Estado:** `FALTAN`

---

### ⚠️ Materiales sobrantes

Se reportaron materiales que no corresponden a la actividad ejecutada.

**Estado:** `SOBRAN`

---

### 🚨 Faltan y sobran materiales

Existen simultáneamente materiales faltantes y materiales sobrantes.

**Estado:** `AMBOS`

---

### ❌ Mano de obra no existente

Cuando el código de mano de obra no existe en la base maestra.

**Estado:** `NO EXISTEN EN BD`

---
## 📋 Base Maestra de Reglas de Negocio

El sistema utiliza una base maestra donde se definen las reglas que relacionan cada código de mano de obra con los materiales permitidos u obligatorios.

Esta tabla constituye la principal regla de negocio del desarrollo.

Cada fila representa una actividad y los materiales válidos asociados.

---

## 🔄 Tipos de validaciones definidas

La base maestra permite definir diferentes comportamientos de validación.

### ✅ UNO DE LOS MATERIALES

Para algunas actividades basta con que exista al menos uno de los materiales definidos.

Ejemplo:

| Código MO | Materiales permitidos | Regla |
|------------|----------------------|--------|
| A05 | 200492, 200410, 200411, 200493, 323739 | UNO DE LOS CINCO = OK |

En este caso, si el pedido contiene cualquiera de estos materiales, la actividad se considera correctamente reportada.

---

### ✅ UNO DE LOS DOS

Ejemplo:

| Código MO | Materiales permitidos | Regla |
|------------|----------------------|--------|
| A12 | 200092, 200093 | UNO DE LOS DOS = OK |

Si existe cualquiera de los dos materiales, la validación es correcta.

---

### ✅ OBLIGATORIO LOS DOS

Existen actividades donde todos los materiales definidos deben encontrarse obligatoriamente.

Ejemplo:

| Código MO | Materiales obligatorios | Regla |
|------------|------------------------|--------|
| A18 | 211357 y 213333 | OBLIGATORIO LOS DOS |

Si alguno de los materiales no aparece, el sistema genera una alerta de faltantes.

---

### 🚨 Validaciones especiales

Existen actividades con reglas especiales de auditoría.

Por ejemplo:

| Código MO | Materiales | Regla |
|------------|------------|--------|
| A31 | 211618, 336759 | UNO DE LOS DOS = OK |

El sistema también puede validar excepciones operativas y generar alertas específicas cuando se incumplen las reglas establecidas.

El núcleo del desarrollo es una base maestra donde se encuentran definidas todas las reglas de negocio entre actividades y materiales. Python cruza automáticamente la información reportada en Fénix contra esta base y determina si la actividad cumple o no las condiciones establecidas.

---

## 🎯 Beneficio de la Base Maestra

La utilización de una base maestra permite:

- Modificar reglas sin cambiar el código Python.
- Agregar nuevas actividades fácilmente.
- Adaptar el desarrollo a cambios operativos.
- Estandarizar el proceso de auditoría.
- Mantener la lógica del negocio centralizada.

## 🔄 Reglas especiales implementadas

Existen actividades donde basta con reportar uno de varios materiales posibles.

Por ejemplo, para la actividad:

`A05`

El sistema valida que exista al menos uno de los siguientes materiales:

- 200492
- 200410
- 200411
- 200493
- 323739

Si encuentra cualquiera de ellos, la actividad se considera correctamente reportada.

---

## 🚨 Alertas automáticas

### 📌 Mano de obra duplicada

Detecta cuando un mismo pedido posee la misma mano de obra registrada más de una vez.

Ejemplo:

`Pedido 23144539 - C01 x2`

Estas novedades se exportan en la hoja:

`MO_DUPLICADAS`

---

### 📌 Cantidades mayores a uno

El sistema identifica:

- Manos de obra con cantidad superior a uno.
- Materiales con cantidad superior a uno.

Estas novedades requieren validación operativa.

Las alertas son exportadas en la hoja:

`ALERTA_CANTIDADES`

---

### 📌 Validación especial A31

Para la actividad:

`A31`

El sistema verifica que no se reporten simultáneamente los materiales:

- 211618
- 336759

Si ambos materiales aparecen registrados, el sistema genera una alerta especial para revisión.

---

## 📊 Hojas generadas

### 📄 ¿Qué contiene la hoja VALIDACION?

Contiene el resultado completo de la auditoría.

Incluye:

- Pedido.
- Subzona.
- Mano de obra.
- Estado.
- Materiales faltantes.
- Materiales sobrantes.
- Alertas especiales.

---

### 🚨 ¿Qué contiene la hoja MO_DUPLICADAS?

Contiene todas las actividades registradas más de una vez dentro del mismo pedido.

---

### ⚠️ ¿Qué contiene la hoja ALERTA_CANTIDADES?

Contiene materiales cuya cantidad reportada es superior a uno y requiere validación operativa.

---

## 🎨 Formato profesional del informe

El archivo generado incluye:

- Encabezados coloreados.
- Filtros automáticos.
- Congelación de paneles.
- Ajuste automático de columnas.
- Resaltado de alertas críticas.
- Barras visuales para cantidades.
- Colores por tipo de novedad.

---

## ⚡ Tecnologías utilizadas

- Python.
- Pandas.
- OpenPyXL.
- Expresiones Regulares.
- Excel.

---

## 🚀 Beneficios del desarrollo

La herramienta aporta:

- Reducción del trabajo manual.
- Estandarización de auditorías.
- Detección temprana de errores.
- Mayor calidad de la información.
- Disminución de tiempos de revisión.
- Mejor control operativo.

---

