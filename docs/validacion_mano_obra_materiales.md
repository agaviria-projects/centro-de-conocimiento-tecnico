**## 🎯 Entrada a la reunión**

Buenos días a todos.

En esta primera parte les voy a presentar el objetivo del proceso de validación, el problema que busca resolver y cómo funciona de manera general.

También voy a explicar de dónde salen las reglas de negocio que se aplican al informe y qué tipo de novedades se identifican en cada una de las hojas del archivo final.

Estas reglas se han venido definiendo a partir de los requerimientos y criterios entregados por los analistas que realizan la revisión de la información. Por esta razón, pueden ajustarse posteriormente si durante la operación se identifica una nueva condición, excepción o necesidad de validación.

Para facilitar la explicación, voy a utilizar un archivo de simulación que contiene ejemplos de las diferentes alertas. Al finalizar, les mostraré el archivo final que encontrarán en la carpeta compartida y que será el utilizado para la revisión diaria.

\---

**## 🎯 Objetivo**

El proceso de **\*\*Validación Mano de Obra Vs Materiales\*\*** fue desarrollado para verificar automáticamente que los materiales reportados en Fénix correspondan con la mano de obra ejecutada en cada pedido, de acuerdo con las reglas de negocio definidas para la operación.

El proceso permite trabajar con uno o múltiples archivos exportados desde Fénix para las diferentes zonas operativas y consolidar toda la información en un único informe de validación.

[Aquí explico brevemente cómo realizo los exportes desde Fénix y cuáles archivos utilizo como entrada para el proceso.]

Una vez obtenidos los archivos, se ejecuta el proceso de consolidación y se aplican automáticamente las diferentes reglas de validación definidas para Mano de Obra Vs Materiales.

Las reglas actualmente implementadas corresponden a los requerimientos definidos por los analistas y pueden ser ajustadas cuando se identifique alguna novedad operativa, una excepción o un cambio en la regla de negocio.

Al finalizar el proceso, el archivo generado se comparte a través de OneDrive, en la carpeta:

\`Relación\_MO\_Vs\_Materiales\`

El informe correspondiente a la información del día anterior se almacena utilizando la siguiente nomenclatura:

\`VALIDACION\_MO\_MATERIALES\_ALMACEN\_2026-09-10.xlsx\`

Posteriormente, cada usuario responsable deberá filtrar la zona operativa que le corresponda para realizar la validación de su información.

Como recomendación, debido a que varios usuarios pueden acceder al mismo archivo, se sugiere descargar una copia en el equipo local antes de iniciar la validación. De esta manera se evitan conflictos por ediciones simultáneas y se garantiza una revisión más estable de la información.

Adicionalmente, sobre las **\*\*2:30 p. m.\*\*** se realiza un segundo corte correspondiente a la información digitada durante el día hasta ese momento.

Este segundo archivo se genera con la siguiente nomenclatura:

\`INFORME\_VALIDACION\_MO\_MATERIALES\_ALMACEN\_2026-09-11.xlsx\`

\---

**## 📘 Base Maestra: de dónde salen los cruces**

Cada código de mano de obra tiene asociados materiales definidos en una **\*\*Base Maestra de reglas de negocio\*\***:

\`RELACION\_MO\_MATERIALES.xlsx\`

Esta base se fue construyendo de acuerdo con las reglas definidas y validadas con la operación. Por eso, los cruces que realiza el desarrollo se basan en reglas de negocio previamente definidas en la Base Maestra.

Estas reglas no se consideran estáticas: pueden ajustarse cuando en la revisión diaria se detecte una nueva condición, excepción o necesidad operativa.

**### Ejemplos sencillos**

\- \`A05\`: basta con uno de \`200492\`, \`200410\`, \`200411\`, \`200493\` o \`323739\`.

\- \`A12\`: basta con \`200092\` o \`200093\`.

\- \`A18\`: los materiales definidos son obligatorios.

\---

**## 📄 Archivo de simulación y archivo final**

Para explicar las diferentes validaciones se utilizará inicialmente un **\*\*archivo de simulación\*\***, en el cual se encuentran ejemplos de las alertas que puede generar el proceso.

**\*\*Archivo de Simulación:\*\***  

\`C:\Users\hector.gaviria\Desktop\Launcher\_Elite\Control\_ANS\_v5\\\`  

\`Capacitacion_V2_validacion_mo_materiales_20260915_131517.xlsx\`

Este archivo permite visualizar de manera sencilla qué significa cada alerta y cómo debe interpretarse.

La finalidad del informe es facilitar la identificación de posibles novedades. La revisión final continúa dependiendo del criterio operativo del analista, especialmente cuando se presenten casos especiales o situaciones que requieran confirmar la regla de negocio.

\---

**# 📊 ¿Qué hace cada hoja del archivo final?**

**## 🟢 \`VALIDACION\`**

Realizar la explicación con base al archivo de Excel, consolidado final.

\`C:\Users\hector.gaviria\Desktop\Launcher_Elite\Control_ANS_v5\\\`
\`Capacitacion_V2_validacion_mo_materiales_20260915_131517.xlsx\`

Estados principales:

\- \`OK\`: cumple la regla.

\- \`FALTAN\`: faltan materiales requeridos.

\- \`SOBRAN\`: aparecen materiales no correspondientes.

\- \`AMBOS\`: faltan y sobran materiales.

\- \`NO EXISTEN EN BD\`: la mano de obra no está en la Base Maestra.

**### Alerta de cantidad para manos de obra D**

Además del cruce de materiales, esta hoja identifica las manos de obra de tipo \`CON\` correspondientes a:

\`D01U/D01R\`, \`D02U/D02R\`, \`D03U/D03R\` y \`D04U/D04R\`.

Cuando la cantidad registrada en una sola fila es mayor a 1, el informe muestra:

\- \`alerta_cantidad_D = CANTIDAD_D>1\`;

\- el detalle del código y la cantidad encontrada;

\- el estado \`Presenta novedad en las cantidades (D)\`.

**Regla:**

| Condición | Resultado |
|---|---|
| Código D01–D04, terminación U/R y cantidad <= 1 | Sin alerta de cantidad D |
| Código D01–D04, terminación U/R y cantidad > 1 | \`CANTIDAD_D>1\` |

**Ejemplo:** \`D01U = 2\` para un pedido genera alerta. Esta alerta es informativa y no modifica el resultado del cruce de materiales en \`estado_codigo\`.

**\*\*Pregunta que responde:\*\***

\> ¿La mano de obra y los materiales del pedido cumplen con la regla definida?

\---

**## 🔴 \`MO\_DUPLICADAS\`**

Detecta una misma mano de obra registrada más de una vez para el mismo pedido y subzona.

Ejemplo: \`C01 x2\`.

La regla existente también cubre las manos de obra \`D01U/D01R\` a \`D04U/D04R\`; no fue necesario crear otra validación para estos códigos.

**Regla:** se compara el mismo código exacto de tipo \`CON\` dentro de la combinación \`pedido + subzona\`. Si aparece en dos o más filas, se genera la alerta de duplicidad.

| Caso | Resultado |
|---|---|
| \`D01U\` aparece dos veces en el mismo pedido y subzona | Alerta de MO duplicada |
| \`D01U\` y \`D01R\` aparecen una vez cada uno | No son duplicados entre sí, porque son códigos diferentes |

**\*\*Pregunta que responde:\*\***

\> ¿Existe una mano de obra repetida que deba revisarse?

\---

**## 🟠 \`ALERTA\_CANTIDADES\`**

Esta hoja muestra todos los materiales reportados cuya cantidad es mayor a 1.

No valida una lista específica de materiales. Su función es identificar rápidamente cantidades superiores a 1 para que el analista revise si corresponden realmente a la operación.

La alerta sirve como punto de revisión; no significa automáticamente que exista un error.

**\*\*Pregunta que responde:\*\***

\> ¿Hay materiales con cantidades superiores a 1 que requieran revisión?

\---

**## 🟣 \`ALERTA\_RURAL\_URBANO\`**

Valida que la clasificación Rural/Urbano del pedido coincida con la terminación de \`item\_cont\`.

\`\`\`text

R → el código debe terminar en R

U → el código debe terminar en U

\`\`\`

Ejemplo:

\`urbrur = R\` y \`item\_cont = D01U\` genera inconsistencia.

La regla no aplica a una lista específica de ítems; revisa los códigos cuya terminación corresponda a \`R\` o \`U\`.

**\*\*Pregunta que responde:\*\***

\> ¿El código corresponde correctamente a la clasificación Rural/Urbano?

\---

**## 🔵 \`ALERTA\_ACTIVIDADES\`**

Esta hoja aplica reglas específicas de acuerdo con la actividad reportada.

**### AMRTR - MOVIMIENTO DE REDES**

Códigos válidos:

\`D02U\`, \`D02R\`, \`D03U\`, \`D03R\`, \`D04U\`, \`D04R\`.

Debe existir al menos uno de estos códigos.

Si aparece otro código \`Dxx\` diferente a los permitidos, se genera una alerta de:

\`ERROR EN DIGITACIÓN\`

**### ACREV - PUNTOS DE CONEXIÓN**

Códigos válidos:

\`D01U\` o \`D01R\`.

Debe existir al menos uno.

Si aparece otro código \`Dxx\` diferente a los permitidos, se genera una alerta de:

\`ERROR EN DIGITACIÓN\`

**### AEJDO - HV (HABILITACIÓN VIVIENDA)**

Actualmente se está revisando la regla de negocio asociada a esta actividad.

La validación existente considera los códigos:

\`CALE1F\`, \`A12U\`, \`A18U\` y \`A19U\`.

Sin embargo, esta condición se encuentra en proceso de revisión con los analistas, por lo que las alertas relacionadas con AEJDO deben tomarse como informativas hasta confirmar la regla definitiva.

**### ACAMN y ALECA**

Debe existir al menos uno de estos códigos válidos:

\`C05U\` o \`C05R\`.

Si no aparece ninguno, se genera \`FALTA ÍTEM VÁLIDO\`. Si para estas actividades se registra un \`item_cont\` diferente, se genera \`ERROR EN DIGITACIÓN\`.

**### ALEGA y ALEGN**

Debe existir al menos uno de estos códigos válidos:

\`C01U/C01R\`, \`C02U/C02R\`, \`C03U/C03R\` o \`C04U/C04R\`.

Si no aparece ninguno, se genera \`FALTA ÍTEM VÁLIDO\`. Si para estas actividades se registra un \`item_cont\` diferente, se genera \`ERROR EN DIGITACIÓN\`.

| Actividad | Ítem obligatorio válido | Alerta si falta | Alerta si aparece otro ítem |
|---|---|---|---|
| ACAMN / ALECA | C05U o C05R | \`FALTA ÍTEM VÁLIDO\` | \`ERROR EN DIGITACIÓN\` |
| ALEGA / ALEGN | Uno de C01U/R, C02U/R, C03U/R o C04U/R | \`FALTA ÍTEM VÁLIDO\` | \`ERROR EN DIGITACIÓN\` |

**\*\*Pregunta que responde:\*\***

\> ¿Los códigos registrados corresponden con la actividad ejecutada?

\---

**## 🟢 \`ALERTA\_CANTIDADES\_MO\`**

Presenta de forma detallada las manos de obra de tipo \`CON\` cuya cantidad registrada en una fila es mayor a 1.

Incluye:

\- todos los códigos que comienzan por \`A\`;

\- todos los códigos que comienzan por \`C\`;

\- los códigos \`D01U/D01R\`, \`D02U/D02R\`, \`D03U/D03R\` y \`D04U/D04R\`.

| Cantidad | Resultado |
|---|---|
| <= 1 | Sin alerta |
| > 1 | \`CANTIDAD_MO>1\` |

La regla se evalúa por registro; no suma filas distintas. La hoja muestra el pedido, la subzona, el \`item_cont\`, la cantidad, el tipo de alerta y el detalle para facilitar la revisión.

**Ejemplos:**

| Registro | Resultado |
|---|---|
| \`A19U = 2\` | Alerta |
| \`C02U = 2\` | Alerta |
| \`D01U = 2\` | Alerta |
| \`D05U = 2\` | No entra por la regla D01–D04 |

La hoja \`VALIDACION\` conserva la alerta D dentro de la vista general del pedido. \`ALERTA_CANTIDADES_MO\` ofrece la vista especializada y más visual de las cantidades de mano de obra mayores a 1.

**\*\*Pregunta que responde:\*\***

\> ¿Hay manos de obra A, C o D01–D04 con cantidad mayor a 1 que requieran revisión?

\---

**## 🔷 \`MASIVAS\`**

Para esta validación se utilizan los primeros 14 dígitos del campo \`pagina\`, con los cuales se genera el campo técnico \`pagina_base\`. Los últimos cuatro dígitos se entienden operativamente como el interior. No se asigna una definición oficial adicional a los primeros 14 dígitos.

El proceso agrupa por \`subzona + pagina_base\` y cuenta las instalaciones distintas usando el valor completo de \`pagina\`. De esta forma, varias filas asociadas a una misma instalación no aumentan artificialmente el conteo.

La mano de obra C esperada depende de la cantidad de instalaciones:

| Instalaciones distintas | Código esperado |
|---|---|
| 1 | C01U o C01R |
| 2 a 12 | C02U o C02R |
| 13 a 24 | C03U o C03R |
| 25 o más | C04U o C04R |

La terminación U/R no cambia el rango. Cuando el código registrado no corresponde con la cantidad de instalaciones, se genera \`ITEM_CONT_NO_CORRESPONDE_CANTIDAD\` y se muestran la cantidad calculada, el código encontrado y el código esperado.

**### ¿Qué representa el campo \`pagina\`?**

En el exporte de Fénix, el campo \`pagina\` contiene un identificador proveniente del archivo origen.

Para esta regla se utilizan únicamente sus primeros 14 dígitos con el fin de agrupar registros relacionados y validar la consistencia del \`item\_cont\`.

Ejemplo:

\`\`\`text

pagina       = 190607100316666202

pagina\_base  = 19060710031666

\`\`\`

Ejemplos de validación:

\`\`\`text

2 instalaciones distintas  + C02U o C02R  → correcto

14 instalaciones distintas + C02U         → alerta; corresponde C03U o C03R

25 instalaciones distintas + C03R         → alerta; corresponde C04U o C04R

\`\`\`

La alerta se presenta para revisión del analista y no declara automáticamente un error operativo.

**\*\*Pregunta que responde:\*\***

\> ¿El código C01–C04 corresponde con la cantidad de instalaciones asociadas a la misma \`pagina_base\`?

\---

**## 🧭 Resumen rápido**

\| Hoja | Qué revisa |

\|---|---|

\| \`VALIDACION\` | MO + materiales contra Base Maestra y reglas |

\| \`MO\_DUPLICADAS\` | MO repetida por pedido/subzona |

\| \`ALERTA\_CANTIDADES\` | Materiales con cantidad > 1 para revisión |

\| \`ALERTA\_RURAL\_URBANO\` | R/U contra terminación del código |

\| \`ALERTA\_ACTIVIDADES\` | Reglas AMRTR, ACREV, AEJDO, ACAMN, ALECA, ALEGA y ALEGN |

\| \`ALERTA\_CANTIDADES\_MO\` | MO A, C y D01–D04 con cantidad > 1 |

\| \`MASIVAS\` | Código C01–C04 según cantidad de instalaciones por \`pagina_base\` |

\---

**## ✅ Cierre de la explicación**

Hasta aquí se presenta el funcionamiento general del proceso, de dónde salen las reglas de negocio y qué tipo de novedades identifica cada hoja.

El informe automatiza los cruces y facilita la identificación de posibles inconsistencias, pero la validación final continúa teniendo un componente operativo.

Las reglas implementadas corresponden a los requerimientos definidos por los analistas y se mantienen abiertas a ajustes cuando, durante la revisión diaria, se identifique una nueva condición, excepción o necesidad de la operación.

A continuación, utilizando el archivo de simulación, se pueden revisar ejemplos de las diferentes alertas. Finalmente, se presenta el archivo definitivo que quedará disponible en la carpeta compartida para la validación diaria.

\---

**## NO TENER EN CUENTA PARA LA EXPLICACIÓN**

**# 🧑‍💻 Referencia técnica para el desarrollador**

**## Arquitectura**

\`\`\`text

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

RELACION\_MO\_MATERIALES.xlsx

  ↓

Reglas especiales Python

  ↓

DataFrames de validación

  ↓

Excel final

  ↓

OpenPyXL aplica formato

\`\`\`

**## Tecnologías**

\- Python

\- Pandas

\- OpenPyXL

\- Expresiones regulares

\- Excel

\- Git / GitHub

**## Criterio de mantenimiento**

Antes de modificar una regla se debe determinar si corresponde a:

1\. cambio en la Base Maestra;

2\. regla especial ya implementada;

3\. nueva validación que requiera Python;

4\. excepción operativa.

Esto permite mantener las reglas ordenadas y evita afectar validaciones que ya funcionan.

**## Actualización funcional aprobada — 2026-09-15**

Versión de referencia en Git: commit \`3aa755d\`, mensaje \`feat: agregar reglas D, actividades y rangos de masivas\`.

Alcance incorporado:

1. cantidades mayores a 1 para D01–D04 U/R en \`VALIDACION\`;
2. inclusión de D01–D04 U/R en \`ALERTA_CANTIDADES_MO\`, conservando A y C;
3. confirmación de que \`MO_DUPLICADAS\` ya cubre estos códigos D;
4. reglas de actividades para ACAMN, ALECA, ALEGA y ALEGN;
5. rangos de instalaciones para C01–C04 en \`MASIVAS\`.

Pruebas de aceptación realizadas:

| Prueba | Resultado esperado |
|---|---|
| D01U = 2 en una fila de un pedido | Alerta en \`VALIDACION\` y \`ALERTA_CANTIDADES_MO\` |
| D01U repetido en dos filas del mismo pedido y subzona | Alerta en \`MO_DUPLICADAS\` |
| ACAMN o ALECA sin C05U/C05R | \`FALTA ÍTEM VÁLIDO\` |
| ACAMN o ALECA con otro ítem | \`ERROR EN DIGITACIÓN\` |
| ALEGA o ALEGN sin un C01–C04 U/R válido | \`FALTA ÍTEM VÁLIDO\` |
| ALEGA o ALEGN con otro ítem | \`ERROR EN DIGITACIÓN\` |
| 1, 2, 12, 13, 24 y 25 instalaciones en MASIVAS | Asignación C01, C02, C02, C03, C03 y C04 respectivamente |

El formato y los colores del Excel facilitan la lectura de las novedades; no cambian la lógica de validación.
