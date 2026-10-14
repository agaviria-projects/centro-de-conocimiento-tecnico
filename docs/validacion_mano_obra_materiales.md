# Validación Mano de Obra Vs Materiales

**Actualización documental: 14/10/2026.** Documento original complementado con la hoja de reglas suministrada, fechada 13/10/2026.

## 🎯 Entrada a la reunión

Buenos días a todos.

En esta primera parte les voy a presentar el objetivo del proceso de validación y cómo funciona de manera general.

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

Esta base se fue construyendo de acuerdo con las reglas definidas y validadas con la operación. Por eso, los cruces que realiza el desarrollo se basan en reglas de negocio previamente definidas en la Base Maestra.

Estas reglas no se consideran estáticas: pueden ajustarse cuando en la revisión diaria se detecte una nueva condición, excepción o necesidad operativa.

### Ejemplos sencillos

- `A05`: basta con uno de `200492`, `200410`, `200411`, `200493` o `323739`.

- `A12`: basta con `200092` o `200093`.

- `A18`: los materiales definidos son obligatorios.

---

## 📄 Archivo de simulación y archivo final

Para explicar las diferentes validaciones se utilizará inicialmente un **archivo de simulación**, en el cual se encuentran ejemplos de las alertas que puede generar el proceso.

**Archivo de Simulación:**  

`C:\Users\hector.gaviria\Desktop\Launcher_Elite\Control_ANS_v5\\`  

`Capacitacion_V2_validacion_mo_materiales_20260915_131517.xlsx`

Este archivo permite visualizar de manera sencilla qué significa cada alerta y cómo debe interpretarse.

La finalidad del informe es facilitar la identificación de posibles novedades. La revisión final continúa dependiendo del criterio operativo del analista, especialmente cuando se presenten casos especiales o situaciones que requieran confirmar la regla de negocio.

---

# 📊 ¿Qué hace cada hoja del archivo final?

## 🟢 `VALIDACION`

Realizar la explicación con base al archivo de Excel, consolidado final.

`C:\Users\hector.gaviria\Desktop\Launcher_Elite\Control_ANS_v5\\`
`Capacitacion_V2_validacion_mo_materiales_20260915_131517.xlsx`

Estados principales:

- `OK`: cumple la regla.

- `FALTAN`: faltan materiales requeridos.

- `SOBRAN`: aparecen materiales no asociados a la mano de obra evaluada en la Base Maestra. Pueden corresponder a otra mano de obra del mismo pedido; revisar el pedido completo antes de concluir que sobran.

- `AMBOS`: faltan y sobran materiales.

- `NO EXISTEN EN BD`: la mano de obra no está en la Base Maestra. No permite concluir por sí solo que falten o sobren materiales.

### Alerta de cantidad para manos de obra A, C, D y F

Además del cruce de materiales, la hoja VALIDACION revisa la cantidad registrada para cada mano de obra  y presenta controles independientes para los grupos A, C, D y F, según los códigos controlados de cada grupo.
Igual en la hoja VALIDACION detecta mano de obra registrada más de una vez para el mismo pedido y subzona.

| Columna de alerta | Condición | Ejemplo |
|---|---|---|
| `alerta_cantidad_A` | Código que comienza por A, cantidad mayor a 1. | A21R = 4: `CANTIDAD_A>1`. |
| `alerta_cantidad_C` | Código que comienza por C, cantidad mayor a 1. | C02U = 2: `CANTIDAD>1`. |
| `alerta_cantidad_D` | D01U/R, D02U/R, D03U/R o D04U/R, cantidad mayor a 1. | D01U = 2: `CANTIDAD_D>1`. |
| `alerta_cantidad_F` | F01U o F01R, cantidad mayor a 1. | F01R = 2: `CANTIDAD_F>1`. |
| `alerta_duplicado_MO` | Misma mano de obra repetida para un pedido y subzona. | `MO_DUPLICADA`. |

Las columnas `detalle_cantidad_A`, `detalle_cantidad_C`, `detalle_cantidad_D`, `detalle_cantidad_F` y `detalle_duplicado_MO` muestran la información que originó cada alerta.

El resultado del cruce de materiales y los controles de cantidad o duplicidad requieren revisión conjunta. Consultar las columnas adicionales aunque el cruce indique `OK`.



---

## 🔴 `MO_DUPLICADAS`

Detecta una misma mano de obra registrada más de una vez para el mismo pedido y subzona.

Ejemplo: `C01 x2`.

**Pregunta que responde:**

> ¿Existe una mano de obra repetida que deba revisarse?

---

## 🟠 `ALERTA_CANTIDADES`

Esta hoja muestra todos los materiales reportados cuya cantidad es mayor a 1.

Incluye la columna **Actividad inmediatamente después de Pedido**, seguida de subzona, material, cantidad, alerta y detalle. Esto permite identificar el contexto operativo de la cantidad reportada.

El código de alerta es `MATERIAL_CANTIDAD>1`.

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

## 🟣 `ALERTA_PAGINA_7MO_DIGITO`

Esta hoja complementa la revisión Rural/Urbano con una validación basada en el campo `pagina`.

Aplica únicamente cuando la página **comienza por 190**. Se cuenta el séptimo dígito desde la izquierda, empezando en 1.

| Séptimo dígito | Clasificación requerida | Cruce que genera alerta |
|---|---|---|
| 1 | U: urbano. | Séptimo dígito 1 con `urbrur = R`. |
| 2 | R: rural. | Séptimo dígito 2 con `urbrur = U`. |

Los cruces 1 con U y 2 con R cumplen esta regla. No extenderla a otros prefijos o séptimos dígitos.

**Ejemplos de capacitación:**

| Página | Clasificación encontrada | Resultado |
|---|---|---|
| `190000100000000001` | R | Alerta: el séptimo dígito es 1 y se espera U. |
| `190000200000000001` | U | Alerta: el séptimo dígito es 2 y se espera R. |
| `190000100000000001` | U | Sin alerta de este cruce. |

La hoja permite consultar pedido, subzona, página, séptimo dígito, clasificación encontrada, valor esperado, estado y detalle.

**Pregunta que responde:**

> ¿La clasificación Rural/Urbano corresponde al séptimo dígito de una página que comienza por 190?

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

La hoja de reglas suministrada establece una relación **bidireccional entre CALE1F y A12U o A12R**: si aparece uno, debe aparecer el otro.

Esta explicación actualiza el texto anterior que describía la regla como pendiente de revisión. A18 y A19 no se presentan como parte de esa relación; A18 tiene el control complementario que se explica a continuación.

### Reglas complementarias de AEJDO

Estas novedades se consultan en la misma hoja `ALERTA_ACTIVIDADES`.

| Condición encontrada | Requisito según la hoja de reglas | Alerta si no cumple |
|---|---|---|
| Suministros 215887 o 219404 con cantidad. | Deben registrar cobro al usuario en `vlr_cliente`. | `COBRO_FALTANTE_AEJDO`. |
| A18U o A18R. | Suministro obligatorio 211357. | `REGLA_AEJDO_A18`. |
| A02U o A02R. | A06U/R o A08U/R con la misma terminación; uno es suficiente. | `REGLA_AEJDO_A02`. |
| A10U o A10R. | A12U/R con la misma terminación. | `REGLA_AEJDO_A10`. |
| A07U o A07R. | Suministro obligatorio 200384. | `REGLA_AEJDO_A07`. |
| Suministro 200092. | 200410 o 200492; uno es suficiente. | `REGLA_AEJDO_200092`. |
| Suministro 200093. | 200411, 200493 o 323739; uno es suficiente. | `REGLA_AEJDO_200093`. |
| A32U o A32R. | Ambos suministros: 200151A y 211319A. | `REGLA_AEJDO_A32`. |

**Ejemplos:** A02U sin A06U ni A08U requiere revisión; A02U con A08U cumple esa relación. A32U con solo 200151A no cumple: también se requiere 211319A.

La terminación debe coincidir cuando la regla lo exige: A02U con A06R no satisface la relación indicada para A02U.

El control de cobro tiene una diferencia entre el texto de la hoja y el script recibido. Consultar la nota de conciliación en la referencia técnica antes de afirmar que ambos evalúan exactamente la misma condición.

### DSPRE - A13 incluye la instalación del nuevo pase

Para DSPRE, si aparece A13U debe incluirse A22U; si aparece A13R debe incluirse A22R, según la hoja de reglas.

Si falta el correspondiente, aparece una alerta en `ALERTA_ACTIVIDADES` con el detalle:

> El ítem A13 incluye la instalación del nuevo pase (anterior acometida).

Ejemplo: A13R sin el A22 correspondiente requiere revisión. El script recibido también admite A022 con la misma terminación; esta equivalencia se indica en la nota técnica al final.

### ACAMN y ALECA

Debe existir al menos uno de estos códigos válidos:

`C05U` o `C05R`.

Si no aparece ninguno, se genera `FALTA ÍTEM VÁLIDO`. Si para estas actividades se registra un `item_cont` diferente, se genera `ERROR EN DIGITACIÓN`.

### ALEGA y ALEGN

Debe existir al menos uno de estos códigos válidos:

`C01U/C01R`, `C02U/C02R`, `C03U/C03R` o `C04U/C04R`.

Si no aparece ninguno, se genera `FALTA ÍTEM VÁLIDO`. Si para estas actividades se registra un `item_cont` diferente, se genera `ERROR EN DIGITACIÓN`.

| Actividad | Ítem obligatorio válido | Alerta si falta | Alerta si aparece otro ítem |
|---|---|---|---|
| ACAMN / ALECA | C05U o C05R | `FALTA ÍTEM VÁLIDO` | `ERROR EN DIGITACIÓN` |
| ALEGA / ALEGN | Uno de C01U/R, C02U/R, C03U/R o C04U/R | `FALTA ÍTEM VÁLIDO` | `ERROR EN DIGITACIÓN` |

**Pregunta que responde:**

> ¿Los códigos registrados corresponden con la actividad ejecutada?

---

## 🟠 `LEGALIZACION_NO_COBRO`

Identifica cobros no permitidos para las actividades **ACAMN, ALECA, ALEGA y ALEGN**.

| Suministro | Descripción | Regla |
|---|---|---|
| 215887A | Tornillo. | No debe registrar valor en `vlr_cliente`. |
| 219404A | Sello. | No debe registrar valor en `vlr_cliente`. |

Según la hoja de reglas, un valor mayor a cero genera `COBRO_NO_PERMITIDO`. El analista debe consultar actividad, suministro, cantidad, valor cobrado y detalle.

**Ejemplo:** ALEGA con 215887A y cobro positivo genera una novedad para revisión.

Distinguir este control del cobro AEJDO: aquí se utilizan **215887A y 219404A**, con sufijo A, y se exige no cobrar. En AEJDO se controlan 215887 y 219404.

La comparación exacta del script recibido difiere del texto de la hoja para valores negativos; consultar la nota técnica de conciliación.

**Pregunta que responde:**

> ¿Se registró un cobro no permitido para estos suministros en una legalización?

---

## 🟢 `ALERTA_CANTIDADES_MO`

Presenta de forma detallada las manos de obra  cuya cantidad registrada en una fila es mayor a 1.

Incluye:

- Los códigos que comienzan por `A`;

- Los códigos que comienzan por `C`;

- D01U/R, D02U/R, D03U/R y D04U/R;

- F01U y F01R.

| Cantidad | Resultado |
|---|---|
| <= 1 | Sin alerta |
| > 1 | `CANTIDAD_MO>1` |

La regla se evalúa por registro; no suma filas distintas. La hoja muestra el pedido, la subzona, el `item_cont`, la cantidad, el tipo de alerta y el detalle para facilitar la revisión.

**Ejemplos:**

| Registro | Resultado |
|---|---|
| `A19U = 2` | Alerta |
| `C02U = 2` | Alerta |
| `D01U = 2` | Alerta |
| `D05U = 2` | No entra por la regla D01–D04 |
| `F01R = 2` | Alerta del grupo F |


**Pregunta que responde:**

> ¿Hay manos de obra A, C, D o F, dentro de los códigos controlados, con cantidad mayor a 1 que requieran revisión?

---

## 🔷 `MASIVAS`

Para esta validación se utilizan los primeros 14 dígitos del campo `pagina`, con los cuales se genera el campo técnico `pagina_base`. Los últimos cuatro dígitos se entienden operativamente como el interior.

El proceso agrupa por **subzona y pagina_base** y cuenta las instalaciones diferentes usando el valor completo de `pagina`. Si una instalación aparece en varias filas, se cuenta una sola vez.

La mano de obra C esperada depende de la cantidad de instalaciones:

| Instalaciones distintas | Código esperado |
|---|---|
| 1 | C01U o C01R |
| 2 a 12 | C02U o C02R |
| 13 a 24 | C03U o C03R |
| 25 o más | C04U o C04R |

La terminación U/R no cambia el rango. Cuando el código registrado no corresponde con la cantidad de instalaciones, se genera `ITEM_CONT_NO_CORRESPONDE_CANTIDAD` y se muestran la cantidad calculada, el código encontrado y el código esperado.

### ¿Qué representa el campo `pagina`?

En el exporte de Fénix, el campo `pagina` contiene un identificador proveniente del archivo origen.

Para esta regla se utilizan únicamente sus primeros 14 dígitos con el fin de agrupar registros relacionados y validar la consistencia del `item_cont`.

Ejemplo:

```text

pagina       = 190607100316666202

pagina_base  = 19060710031666

```

Ejemplos de validación:

```text

2 instalaciones distintas  + C02U o C02R  → correcto

14 instalaciones distintas + C02U         → alerta; corresponde C03U o C03R

25 instalaciones distintas + C03R         → alerta; corresponde C04U o C04R

```

La alerta se presenta para revisión del analista y no declara automáticamente un error operativo.

**Pregunta que responde:**

> ¿El código C01–C04 corresponde con la cantidad de instalaciones asociadas a la misma `pagina_base`?

---

## 🧭 Resumen de las hojas del archivo Excel

El informe está compuesto por **diez hojas: una guía y nueve hojas de resultados**. Cada una presenta un tipo de validación diferente para facilitar la revisión del analista.

| Hoja | Función | ¿Qué debe revisar el analista? |
|---|---|---|
| `GUIA_REGLAS` | Explica las reglas incluidas en el informe. | Consultar el alcance de cada alerta y la fecha indicada en la guía. |
| `VALIDACION` | Compara las manos de obra y los materiales reportados contra la Base Maestra y las reglas especiales. | Materiales faltantes, sobrantes, cantidades de MO y resultado general del pedido. |
| `MO_DUPLICADAS` | Identifica una misma mano de obra registrada más de una vez para el mismo pedido y subzona. | Confirmar si la repetición corresponde a una novedad o a una condición válida de la operación. |
| `ALERTA_CANTIDADES` | Muestra materiales tipo `SUM` cuya cantidad es mayor a 1. | Verificar si la cantidad reportada del material es correcta. |
| `ALERTA_RURAL_URBANO` | Compara la clasificación Rural/Urbano con la terminación R/U del `item_cont`. | Confirmar que el código corresponda con la clasificación del pedido. |
| `ALERTA_PAGINA_7MO_DIGITO` | Compara el séptimo dígito de páginas 190 con Rural/Urbano. | Revisar los cruces 1 con R y 2 con U. |
| `ALERTA_ACTIVIDADES` | Aplica las reglas específicas de AMRTR, ACREV, AEJDO, ACAMN, ALECA, ALEGA, ALEGN y DSPRE. | Revisar códigos obligatorios, faltantes o no permitidos para cada actividad. |
| `LEGALIZACION_NO_COBRO` | Identifica cobros no permitidos de 215887A y 219404A en ACAMN, ALECA, ALEGA y ALEGN. | Revisar suministro, actividad y valor cobrado. |
| `ALERTA_CANTIDADES_MO` | Muestra las MO controladas de A, C, D01–D04 U/R y F01U/R cuya cantidad es mayor a 1. | Confirmar si la cantidad reportada para cada `item_cont` es correcta. |
| `MASIVAS` | Determina si corresponde utilizar C01, C02, C03 o C04 según la cantidad de instalaciones agrupadas por `pagina_base`. | Verificar que el código registrado corresponda con el número de instalaciones. |

Las alertas facilitan la identificación de posibles novedades; sin embargo, los resultados continúan siendo verificados por el analista, quien realiza la validación final de acuerdo con los criterios de la operación.

---

## 📘 Consulta de `GUIA_REGLAS` y revisión diaria

La hoja `GUIA_REGLAS` explica las validaciones del informe y contiene la fecha indicada para esa ejecución. Consultarla antes de interpretar las novedades.

1. Elegir el archivo y el corte que se necesita revisar.
2. Descargar una copia local y filtrar la subzona correspondiente.
3. Revisar la hoja de resultados y leer la alerta junto con su detalle.
4. Consultar el pedido completo en Fénix antes de concluir que existe un error.
5. Confirmar con el analista la corrección o excepción que corresponda.

Un filtro aplicado en una hoja no implica que las demás estén filtradas. Una novedad puede aparecer en `VALIDACION` y en una hoja de detalle; no sumar esas apariciones como pedidos distintos.

El archivo de simulación V2 conservado en este documento es una referencia de la capacitación original. Antes de utilizarlo en una sesión nueva, comprobar que incluya los ejemplos de F01, séptimo dígito, AEJDO, DSPRE y legalizaciones sin cobro; si faltan, complementarlos en una copia de práctica.

### Cortes de publicación

| Corte | Información incluida | Nombre del archivo |
|---|---|---|
| Mañana, aproximadamente 6:00 a. m. | Día anterior. | `VALIDACION_MO_MATERIALES_ALMACEN_AAAA-MM-DD.xlsx` |
| Tarde, aproximadamente 2:30 p. m. | Día actual hasta el corte. | `INFORME_VALIDACION_MO_MATERIALES_ALMACEN_AAAA-MM-DD.xlsx` |

Ejemplo: el 22 de septiembre, el corte de la mañana puede llamarse `VALIDACION_MO_MATERIALES_ALMACEN_2026-09-21.xlsx`; el de la tarde, `INFORME_VALIDACION_MO_MATERIALES_ALMACEN_2026-09-22.xlsx`.

---

## ✅ Cierre de la explicación

Hasta aquí se presenta el funcionamiento general del proceso, de dónde salen las reglas de negocio y qué tipo de novedades identifica cada hoja.

El informe automatiza los cruces y facilita la identificación de posibles inconsistencias; sin embargo, los resultados continúan siendo verificados por el analista, quien realiza la validación final de acuerdo con los criterios de la operación.

Las reglas implementadas corresponden a los requerimientos definidos por los analistas y se mantienen abiertas a ajustes cuando, durante la revisión diaria, se identifique una nueva condición, excepción o necesidad de la operación.

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

## Actualización funcional aprobada — 2026-09-15

Versión de referencia en Git: commit `3aa755d`, mensaje `feat: agregar reglas D, actividades y rangos de masivas`.

Alcance incorporado:

1. cantidades mayores a 1 para D01–D04 U/R en `VALIDACION`;
2. inclusión de D01–D04 U/R en `ALERTA_CANTIDADES_MO`, conservando A y C;
3. confirmación de que `MO_DUPLICADAS` ya cubre estos códigos D;
4. reglas de actividades para ACAMN, ALECA, ALEGA y ALEGN;
5. rangos de instalaciones para C01–C04 en `MASIVAS`.

Pruebas de aceptación realizadas:

| Prueba | Resultado esperado |
|---|---|
| D01U = 2 en una fila de un pedido | Alerta en `VALIDACION` y `ALERTA_CANTIDADES_MO` |
| D01U repetido en dos filas del mismo pedido y subzona | Alerta en `MO_DUPLICADAS` |
| ACAMN o ALECA sin C05U/C05R | `FALTA ÍTEM VÁLIDO` |
| ACAMN o ALECA con otro ítem | `ERROR EN DIGITACIÓN` |
| ALEGA o ALEGN sin un C01–C04 U/R válido | `FALTA ÍTEM VÁLIDO` |
| ALEGA o ALEGN con otro ítem | `ERROR EN DIGITACIÓN` |
| 1, 2, 12, 13, 24 y 25 instalaciones en MASIVAS | Asignación C01, C02, C02, C03, C03 y C04 respectivamente |

El formato y los colores del Excel facilitan la lectura de las novedades; no cambian la lógica de validación.


## Actualización documental — 2026-10-14

Se complementó este documento original con la hoja de reglas suministrada. Se conservan el guion de capacitación, los ejemplos anteriores, la referencia al archivo de simulación, el cierre, la arquitectura, las tecnologías y el historial de septiembre.

Contenido incorporado o actualizado:

1. Resumen de diez hojas, incluida `GUIA_REGLAS`.
2. Alcance F01U/R y detalle de cantidades A, C, D y F.
3. Columna Actividad después de Pedido en `ALERTA_CANTIDADES`.
4. Hoja `ALERTA_PAGINA_7MO_DIGITO` y cruces que generan alerta.
5. Relación CALE1F–A12 y controles complementarios de AEJDO.
6. Regla DSPRE A13–A22.
7. Hoja `LEGALIZACION_NO_COBRO`.
8. Interpretación de sobrantes respecto de cada mano de obra.
9. Agrupación de masivas por subzona y página base, contando páginas completas distintas.
10. Orientación para mantener actualizada la documentación.

### Conciliación pendiente entre hoja y script

Se mantiene la hoja suministrada como referencia operativa solicitada. La revisión previa del script detectó diferencias que deben confirmarse antes de presentar ambas fuentes como equivalentes:

| Tema | Texto de la hoja de reglas | Comportamiento detectado en el script recibido |
|---|---|---|
| Cobro AEJDO, 215887 y 219404. | Vincula el cobro a suministros que llevan cantidad. | Evalúa `vlr_cliente == 0` sin exigir cantidad positiva. |
| Legalizaciones sin cobro. | Describe valores mayores a cero. | Alerta por valores convertidos distintos de cero, incluidos negativos. |
| DSPRE, A13–A22. | Menciona A22 con igual terminación. | También acepta A022 con igual terminación. |

Estas diferencias se documentan para revisión; no constituyen nuevas reglas aprobadas ni una modificación del código.

### Control obligatorio de actualización documental

En cada nueva regla aprobada, actualizar conjuntamente:

| Componente | Qué debe quedar actualizado |
|---|---|
| Script o Base Maestra. | Condición, alcance y excepciones aprobadas. |
| Hoja de resultados del Excel. | Alerta, detalle y campos de consulta. |
| `GUIA_REGLAS`. | Explicación comprensible y ejemplos. |
| `docs/validacion_mano_obra_materiales.md`. | Apartado correspondiente, interpretación y ejemplo para capacitación. |
| Archivo de práctica. | Un caso que cumple y otro que activa la alerta. |
| Verificación y Git. | Revisión de reglas afectadas y referencia al cambio. |

Si se agrega una hoja, incorporarla también al resumen. Registrar fecha, alcance y referencia al commit cuando esté disponible.

**Este documento no se sincroniza automáticamente con Python ni con `GUIA_REGLAS`.** Reemplazar el Markdown actualiza la consulta del centro de conocimiento; las siguientes reglas requieren actualizarlo dentro de la misma entrega del cambio.
