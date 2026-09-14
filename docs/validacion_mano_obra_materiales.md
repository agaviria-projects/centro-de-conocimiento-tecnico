## 🎯 Entrada a la reunión

Buenos días a todos.

En esta primera parte les voy a presentar el objetivo del proceso de validación, el problema que busca resolver y cómo funciona de manera general.

También voy a explicar de dónde salen las reglas de negocio que se aplican al informe y qué tipo de novedades se identifican en cada una de las hojas del archivo final.

Estas reglas se han venido definiendo a partir de los requerimientos y criterios entregados por los analistas que realizan la revisión de la información. Por esta razón, pueden ajustarse posteriormente si durante la operación se identifica una nueva condición, excepción o necesidad de validación.

Para facilitar la explicación, voy a utilizar un archivo de simulación que contiene ejemplos de las diferentes alertas. Al finalizar, les mostraré el archivo final que encontrarán en la carpeta compartida y que será el utilizado para la revisión diaria.

---

## 🎯 Objetivo

El proceso de **Validación Mano de Obra Vs Materiales** fue desarrollado para verificar automáticamente que los materiales reportados en Fénix correspondan con la mano de obra ejecutada en cada pedido, de acuerdo con las reglas de negocio definidas para la operación.

El proceso permite trabajar con uno o múltiples archivos exportados desde Fénix para las diferentes zonas operativas y consolidar toda la información en un único informe de validación.

[Aquí explico brevemente cómo realizo los exportes desde Fénix y cuáles archivos utilizo como entrada para el proceso.]

Una vez obtenidos los archivos, se ejecuta el proceso de consolidación y se aplican automáticamente las diferentes reglas de validación definidas para Mano de Obra Vs Materiales.

Las reglas actualmente implementadas corresponden a los requerimientos definidos por los analistas y pueden ser ajustadas cuando se identifique alguna novedad operativa, una excepción o un cambio en la regla de negocio.

Al finalizar el proceso, el archivo generado se comparte a través de OneDrive, en la carpeta:

`Relación_MO_Vs_Materiales`

El informe correspondiente a la información del día anterior se almacena utilizando la siguiente nomenclatura:

`VALIDACION_MO_MATERIALES_ALMACEN_2026-09-10.xlsx`

Posteriormente, cada usuario responsable deberá filtrar la zona operativa que le corresponda para realizar la validación de su información.

Como recomendación, debido a que varios usuarios pueden acceder al mismo archivo, se sugiere descargar una copia en el equipo local antes de iniciar la validación. De esta manera se evitan conflictos por ediciones simultáneas y se garantiza una revisión más estable de la información.

Adicionalmente, sobre las **2:30 p. m.** se realiza un segundo corte correspondiente a la información digitada durante el día hasta ese momento.

Este segundo archivo se genera con la siguiente nomenclatura:

`INFORME_VALIDACION_MO_MATERIALES_ALMACEN_2026-09-11.xlsx`

---

## 📘 Base Maestra: de dónde salen los cruces

Cada código de mano de obra tiene asociados materiales definidos en una **Base Maestra de reglas de negocio**:

`RELACION_MO_MATERIALES.xlsx`

Esta base se ha venido construyendo de acuerdo con las reglas y requerimientos definidos por los analistas para la operación.

Por esta razón, los cruces que realiza el proceso se basan en reglas de negocio previamente establecidas. Estas reglas no se consideran estáticas: pueden ajustarse cuando en la revisión diaria se detecte una nueva condición, excepción o necesidad operativa.

### Ejemplos sencillos

- `A05`: basta con uno de `200492`, `200410`, `200411`, `200493` o `323739`.
- `A12`: basta con `200092` o `200093`.
- `A18`: los materiales definidos son obligatorios.

---

## 📄 Archivo de simulación y archivo final

Para explicar las diferentes validaciones se utilizará inicialmente un **archivo de simulación**, en el cual se encuentran ejemplos de las alertas que puede generar el proceso.

**Archivo de Simulación:**<br>
`C:\Users\hector.gaviria\Desktop\Launcher_Elite\Control_ANS_v5\`<br>
`Capacitacion_validacion_mo_materiales_20260913_110854.xlsx`

Este archivo permite visualizar de manera sencilla qué significa cada alerta y cómo debe interpretarse.

La finalidad del informe es facilitar la identificación de posibles novedades. La revisión final continúa dependiendo del criterio operativo del analista, especialmente cuando se presenten casos especiales o situaciones que requieran confirmar la regla de negocio.

---

# 📊 ¿Qué hace cada hoja del archivo final?

## 🟢 `VALIDACION`

Es la hoja principal.

```text
Mano de obra reportada
        +
Materiales reportados
        ↓
Base Maestra y reglas especiales
        ↓
Resultado
```

Estados principales:

- `OK`: cumple la regla.
- `FALTAN`: faltan materiales requeridos.
- `SOBRAN`: aparecen materiales no correspondientes.
- `AMBOS`: faltan y sobran materiales.
- `NO EXISTEN EN BD`: la mano de obra no está en la Base Maestra.

**Pregunta que responde:**

> ¿La mano de obra y los materiales del pedido cumplen con la regla definida?

---

## 🔴 `MO_DUPLICADAS`

Detecta una misma mano de obra registrada más de una vez para el mismo pedido y subzona.

Ejemplo: `C01 x2`.

**Pregunta que responde:**

> ¿Existe una mano de obra repetida que deba revisarse?

---

## 🟠 `ALERTA_CANTIDADES`

Esta hoja muestra todos los materiales reportados cuya cantidad es mayor a 1.

No valida una lista específica de materiales. Su función es identificar rápidamente cantidades superiores a 1 para que el analista revise si corresponden realmente a la operación.

La alerta sirve como punto de revisión; no significa automáticamente que exista un error.

**Pregunta que responde:**

> ¿Hay materiales con cantidades superiores a 1 que requieran revisión?

---

## 🟣 `ALERTA_RURAL_URBANO`

Valida que la clasificación Rural/Urbano del pedido coincida con la terminación de `item_cont`.

```text
R → el código debe terminar en R
U → el código debe terminar en U
```

Ejemplo:

`urbrur = R` y `item_cont = D01U` genera inconsistencia.

La regla no aplica a una lista específica de ítems; revisa los códigos cuya terminación corresponda a `R` o `U`.

**Pregunta que responde:**

> ¿El código corresponde correctamente a la clasificación Rural/Urbano?

---

## 🔵 `ALERTA_ACTIVIDADES`

Esta hoja aplica reglas específicas de acuerdo con la actividad reportada.

### AMRTR - MOVIMIENTO DE REDES

Códigos válidos:

`D02U`, `D02R`, `D03U`, `D03R`, `D04U`, `D04R`.

Debe existir al menos uno de estos códigos.

Si aparece otro código `Dxx` diferente a los permitidos, se genera una alerta de:

`ERROR EN DIGITACIÓN`

### ACREV - PUNTOS DE CONEXIÓN

Códigos válidos:

`D01U` o `D01R`.

Debe existir al menos uno.

Si aparece otro código `Dxx` diferente a los permitidos, se genera una alerta de:

`ERROR EN DIGITACIÓN`

### AEJDO - HV (HABILITACIÓN VIVIENDA)

Actualmente se está revisando la regla de negocio asociada a esta actividad.

La validación existente considera los códigos:

`CALE1F`, `A12U`, `A18U` y `A19U`.

Sin embargo, esta condición se encuentra en proceso de revisión con los analistas, por lo que las alertas relacionadas con AEJDO deben tomarse como informativas hasta confirmar la regla definitiva.

**Pregunta que responde:**

> ¿Los códigos registrados corresponden con la actividad ejecutada?

---

## 🟢 `ALERTA_LEGALIZACIONES`

Controla cantidades para los siguientes ítems:

`C01U/C01R`, `C02U/C02R`, `C03U/C03R`, `C04U/C04R`, `C05U/C05R`, `C07U/C07R`.

```text
cantidad <= 1 → sin alerta
cantidad > 1  → alerta
```

La regla se evalúa por registro; no suma filas distintas.

**Pregunta que responde:**

> ¿Alguna legalización controlada tiene cantidad mayor a 1?

---

## 🔷 `MASIVAS`

Para esta validación se utilizan los primeros 14 dígitos del campo `pagina`, con los cuales se genera el campo `pagina_base`.

Para una misma `pagina_base`, todos los `item_cont` encontrados deben ser iguales.

Si dentro de esos mismos primeros 14 dígitos aparecen dos o más `item_cont` diferentes, se genera la alerta:

`ITEM_CONT_INCONSISTENTE`

La validación se activa cuando dentro del grupo existe al menos uno de estos códigos:

`C02U`, `C02R`, `C03U`, `C03R`, `C04U`, `C04R`.

### ¿Qué representa el campo `pagina`?

En el exporte de Fénix, el campo `pagina` contiene un identificador proveniente del archivo origen.

Para esta regla se utilizan únicamente sus primeros 14 dígitos con el fin de agrupar registros relacionados y validar la consistencia del `item_cont`.

Ejemplo:

```text
pagina       = 190607100316666202
pagina_base  = 19060710031666
```

Ejemplo de validación:

```text
pagina_base      item_cont
19060710031666   C02U
19060710031666   C02U
19060710031666   C01U
```

En este caso se genera una alerta porque dentro de la misma `pagina_base` aparecen diferentes valores de `item_cont`.

**Pregunta que responde:**

> ¿Los registros que comparten los primeros 14 dígitos del campo `pagina` presentan diferentes códigos `item_cont`?

---

## 🧭 Resumen rápido

| Hoja | Qué revisa |
|---|---|
| `VALIDACION` | MO + materiales contra Base Maestra y reglas |
| `MO_DUPLICADAS` | MO repetida por pedido/subzona |
| `ALERTA_CANTIDADES` | Materiales con cantidad > 1 para revisión |
| `ALERTA_RURAL_URBANO` | R/U contra terminación del código |
| `ALERTA_ACTIVIDADES` | Reglas AMRTR, ACREV y AEJDO |
| `ALERTA_LEGALIZACIONES` | Cantidad > 1 en legalizaciones controladas |
| `MASIVAS` | Consistencia de `item_cont` por `pagina_base` |

---

## ✅ Cierre de la explicación

Hasta aquí se presenta el funcionamiento general del proceso, de dónde salen las reglas de negocio y qué tipo de novedades identifica cada hoja.

El informe automatiza los cruces y facilita la identificación de posibles inconsistencias, pero la validación final continúa teniendo un componente operativo.

Las reglas implementadas corresponden a los requerimientos definidos por los analistas y se mantienen abiertas a ajustes cuando, durante la revisión diaria, se identifique una nueva condición, excepción o necesidad de la operación.

A continuación, utilizando el archivo de simulación, se pueden revisar ejemplos de las diferentes alertas. Finalmente, se presenta el archivo definitivo que quedará disponible en la carpeta compartida para la validación diaria.

---

## NO TENER EN CUENTA PARA LA EXPLICACIÓN

# 🧑‍💻 Referencia técnica para el desarrollador

## Arquitectura

```text
FÉNIX
  ↓
TXT por zona
  ↓
Pandas consolida
  ↓
CON = mano de obra / SUM = materiales
  ↓
Normalización
  ↓
RELACION_MO_MATERIALES.xlsx
  ↓
Reglas especiales Python
  ↓
DataFrames de validación
  ↓
Excel final
  ↓
OpenPyXL aplica formato
```

## Tecnologías

- Python
- Pandas
- OpenPyXL
- Expresiones regulares
- Excel
- Git / GitHub

## Criterio de mantenimiento

Antes de modificar una regla se debe determinar si corresponde a:

1. cambio en la Base Maestra;
2. regla especial ya implementada;
3. nueva validación que requiera Python;
4. excepción operativa.

Esto permite mantener las reglas ordenadas y evita afectar validaciones que ya funcionan.
