**\*\*## 🎯 Entrada a la reunión.\*\***

"Buenos días a todos. En esta primera parte les voy a presentar el objetivo de la herramienta, el problema que busca resolver y cómo funciona de manera general. Posteriormente, mi compañera Astrid, quien es la persona que más utiliza este proceso en la operación, nos mostrará cómo realiza la validación del archivo generado, qué aspectos revisa antes de darlo por correcto.

\\----

**\*\*## 🎯 Objetivo\*\***

La herramienta de Validación Mano de Obra Vs Materiales fue desarrollada para verificar automáticamente que los materiales reportados en Fénix correspondan correctamente a la mano de obra ejecutada en cada pedido.

El sistema permite procesar uno o múltiples archivos exportados desde Fenix en las diferentes zonas operativas, consolidando automáticamente toda la información en un único informe de auditoría.

(explicar como los exporto).

Una vez finaliza el proceso, el archivo generado se compartirá a través de OneDrive, en la carpeta Relación\\\_MO\\\_Vs\\\_Materiales. El informe quedará almacenado con un nombre que incluye la fecha de generación para facilitar su identificación; por ejemplo: VALIDACION\\\_MO\\\_MATERIALES\\\_ALMACEN\\\_2026-07-27. Posteriormente, cada usuario responsable únicamente deberá filtrar la zona operativa que le corresponda para realizar la validación de su información. Como recomendación, debido a que varios usuarios accederán al mismo archivo, se sugiere descargar una copia en el equipo local antes de iniciar la validación. De esta manera se evitan conflictos por ediciones simultáneas y se garantiza una revisión más estable de la información."

---

## 📘 Base Maestra: de dónde salen los cruces

Cada código de mano de obra tiene asociados materiales definidos en una **Base Maestra de reglas de negocio**:

`RELACION_MO_MATERIALES.xlsx`

Esta base se fue construyendo de acuerdo con las reglas definidas y validadas con la operación. Por eso, Los cruces que realiza el desarrollo se basan en reglas de negocio previamente definidas en la Base Maestra.

### Ejemplos sencillos

- `A05`: basta con uno de `200492`, `200410`, `200411`, `200493` o `323739`.
- `A12`: basta con `200092` o `200093`.
- `A18`: los materiales definidos son obligatorios.
---
# 🎤 Entrega de la palabra a Astrid

Después de mostrar el objetivo, la Base Maestra, puedes cerrar así:

> “Hasta aquí quería mostrarles de dónde salen las reglas. La herramienta automatiza los cruces y clasifica las posibles novedades, pero la revisión final también tiene un componente operativo. Por eso ahora le voy a dar la palabra a mi compañera Astrid, quien trabaja directamente con este informe y nos va a mostrar cómo realiza la revisión de los resultados y qué criterios utiliza para validar cada novedad.”

## EN CASO DE REFORZAR LA EXPLICACIÓN

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

Revisa registros de materiales (`SUM`) cuya `cantidad` sea mayor a 1.

**Pregunta que responde:**  
> ¿Hay materiales con cantidades superiores a 1 que requieran revisión?

---

## 🟣 `ALERTA_RURAL_URBANO`

Cruza `urbrur` con la terminación de `item_cont`.

```text
R → el código debe terminar en R
U → el código debe terminar en U
```

Ejemplo: `urbrur = R` y `item_cont = D01U` genera inconsistencia.

**Pregunta que responde:**  
> ¿El código corresponde correctamente a la clasificación Rural/Urbano?

---

## 🔵 `ALERTA_ACTIVIDADES`

Valida reglas específicas según `actividad`.

### AMRTR - MOVIMENTO DE REDES

Válidos: `D02U`, `D02R`, `D03U`, `D03R`, `D04U`, `D04R`.

Debe existir al menos uno. Otro `Dxx` genera `ERROR EN DIGITACIÓN`.

### ACREV - PUNTOS DE CONEXIÓN

Válidos: `D01U` o `D01R`.

Debe existir al menos uno. Otro `Dxx` genera `ERROR EN DIGITACIÓN`.

### AEJDO - HV(HABILITACIÓN VIVIENDA)

La regla técnica actual revisa `CALE1F`, `A12U`, `A18U` y `A19U`.
proceso de validación de la regla de negocio con el analista.

**Pregunta que responde:**  
> ¿Los códigos registrados corresponden con la actividad ejecutada?

---

## 🟢 `ALERTA_LEGALIZACIONES`

Controla cantidades para:

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

Valida consistencia de `item_cont` para una misma `pagina_base`.

```text
pagina      = 190607100316666202
pagina_base = 19060710031666
```

La `pagina_base` corresponde a los primeros 14 dígitos.

La regla se activa cuando existe al menos uno de:

`C02U`, `C02R`, `C03U`, `C03R`, `C04U`, `C04R`.

Si para la misma página base aparecen `item_cont` diferentes, genera:

`ITEM_CONT_INCONSISTENTE`

Ejemplo:

```text
19060710031666 → C02U
19060710031666 → C02U
19060710031666 → C01U
```

**Pregunta que responde:**  
> ¿Dentro de una misma página base se utilizaron códigos diferentes?

### Nota técnica

Esto **valida** que `pagina` tenga al menos 14 dígitos numéricos:

```python
mask_pagina_valida = df["pagina"].str.match(r"^\d{14,}$", na=False)
```

Esto **extrae** los primeros 14:

```python
df["pagina_base"] = df["pagina"].str[:14]
```

---

## 🧭 Resumen rápido

| Hoja | Qué revisa |
|---|---|
| `VALIDACION` | MO + materiales contra Base Maestra y reglas |
| `MO_DUPLICADAS` | MO repetida por pedido/subzona |
| `ALERTA_CANTIDADES` | Materiales con cantidad > 1 |
| `ALERTA_RURAL_URBANO` | R/U contra terminación del código |
| `ALERTA_ACTIVIDADES` | Reglas AMRTR, ACREV y AEJDO |
| `ALERTA_LEGALIZACIONES` | Cantidad > 1 en legalizaciones controladas |
| `MASIVAS` | Consistencia de `item_cont` por `pagina_base` |

---



La división queda clara:

```text
Mi explicación
→ Objetivo
→ Exportación Fénix
→ Base Maestra
→ Qué automatiza Python
→ Qué significa cada hoja

Astrid
→ Revisión operativa
→ Criterios del usuario
→ Validación de las novedades
```

---

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
