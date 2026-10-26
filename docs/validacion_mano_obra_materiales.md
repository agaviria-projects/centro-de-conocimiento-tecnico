# Validación Mano de Obra vs. Materiales

**Actualización documental: 26/10/2026.**

## Objetivo y alcance

Verificar automáticamente la relación entre la mano de obra y los materiales reportados en Fénix, así como las cantidades, actividades y demás condiciones incluidas en las reglas de negocio, para facilitar la revisión del informe compartido con el equipo técnico.

**La herramienta continúa en desarrollo.** A medida que los analistas e ingenieros identifiquen nuevas reglas, excepciones o necesidades operativas, estas se revisarán e implementarán progresivamente. Este trabajo también se apoya en la revisión de los criterios de EPM para la liquidación de actas, con el acompañamiento de los ingenieros para definir su aplicación en la herramienta.

El proceso consolida archivos TXT exportados de Fénix y utiliza la Base Maestra `RELACION_MO_MATERIALES.xlsx`, junto con validaciones específicas. Las siguientes secciones explican, hoja por hoja, las reglas descritas en la guía del informe del 26/10/2026. Una alerta señala una posible novedad: la conclusión y la corrección correspondiente requieren la revisión del analista.

## 1. GUIA_REGLAS

**¿Para qué sirve?** Explica las validaciones incluidas en el archivo generado y orienta la interpretación de sus alertas.

Contiene la fecha de referencia de las reglas de esa ejecución. Debe consultarse al revisar el informe, especialmente cuando se incorporen nuevas condiciones.

**Qué revisar:** el alcance de la regla, los códigos involucrados y el significado de la alerta antes de concluir que existe un error.

## 2. VALIDACION

**¿Para qué sirve?** Compara la mano de obra reportada con los materiales definidos en la Base Maestra y las reglas especiales aplicables.

Según cada regla, pueden exigirse todos los materiales definidos o ser suficiente uno de los materiales permitidos. Por ejemplo, para A05 basta uno de `200492`, `200410`, `200411`, `200493` o `323739`; para la relación de medidores de A12, uno de `200092` o `200093`. Las condiciones complementarias de A12 en AEJDO se explican en `ALERTA_ACTIVIDADES`.

| Resultado | Interpretación |
|---|---|
| `OK` | Los materiales cumplen el cruce evaluado. |
| `FALTAN` | No se encontraron materiales requeridos por la regla. |
| `SOBRAN` | Hay materiales del pedido que no están asociados a la mano de obra evaluada en la Base Maestra. |
| `AMBOS` | Faltan materiales requeridos y aparecen otros no asociados a esa mano de obra. |
| `NO EXISTEN EN BD` | La mano de obra no tiene una regla en la Base Maestra; este resultado no permite concluir que falten o sobren materiales. |

**Cómo interpretar los sobrantes:** un material puede aparecer como sobrante para una mano de obra y corresponder a otra del mismo pedido. Se debe revisar el pedido completo antes de concluir que realmente sobra.

### Cantidades y duplicidad de mano de obra

La hoja también presenta controles independientes del cruce de materiales:

| Columna | Condición | Alerta |
|---|---|---|
| `alerta_cantidad_A` | Código que comienza por A, con cantidad mayor a 1. | `CANTIDAD_A>1` |
| `alerta_cantidad_C` | Código que comienza por C, con cantidad mayor a 1. | `CANTIDAD>1` |
| `alerta_cantidad_D` | D01U/R, D02U/R, D03U/R o D04U/R, con cantidad mayor a 1. | `CANTIDAD_D>1` |
| `alerta_cantidad_F` | F01U o F01R, con cantidad mayor a 1. | `CANTIDAD_F>1` |
| `alerta_duplicado_MO` | Misma mano de obra repetida para el mismo pedido y subzona. | `MO_DUPLICADA` |

Las columnas `detalle_cantidad_A`, `detalle_cantidad_C`, `detalle_cantidad_D`, `detalle_cantidad_F` y `detalle_duplicado_MO` explican el registro que originó la alerta.

**Qué revisar:** los materiales, las cantidades y las duplicidades conjuntamente. Un resultado `OK` en el cruce de materiales no elimina las alertas de las demás columnas.

## 3. MO_DUPLICADAS

**¿Para qué sirve?** Presenta las manos de obra registradas más de una vez para un mismo pedido y subzona.

Permite consultar el pedido, el código y el número de repeticiones. La novedad también puede aparecer en `VALIDACION`.

**Ejemplo:** C01U registrado en dos filas para el mismo pedido y subzona genera una novedad por duplicidad.

**Qué revisar:** si la repetición corresponde a una duplicación que debe corregirse o a una condición operativa que deba confirmarse con el responsable.

## 4. ALERTA_CANTIDADES

**¿Para qué sirve?** Identifica cantidades de materiales que requieren revisión. Incluye **Actividad inmediatamente después de Pedido**, además de subzona, material, cantidad, alerta y detalle.

| Control | Condición | Alerta |
|---|---|---|
| General | Material tipo `SUM` con cantidad reportada mayor a 1. | `MATERIAL_CANTIDAD>1` |
| Suministros específicos | `200092`, `200093` y `CALE1F`: cuando aparecen en el TXT, su cantidad total debe ser igual a 1 por pedido, subzona y actividad. | `MATERIAL_CANTIDAD_DISTINTA_1` si el total es diferente de 1. |

Para los tres suministros específicos, se revisan también cantidades cero y varias filas cuya suma sea distinta de 1. Esta condición no equivale a exigir que los tres aparezcan en todos los pedidos; su obligatoriedad depende de las reglas de la actividad.

**Ejemplos:** un material general con cantidad 3 requiere revisión; dos filas de `200092` con cantidad 1 cada una suman 2 y no cumplen la regla específica.

**Qué revisar:** si la cantidad corresponde al trabajo realizado. La alerta general de cantidad mayor a 1 no significa automáticamente que exista un error.

## 5. ALERTA_RURAL_URBANO

**¿Para qué sirve?** Verifica que la clasificación del pedido coincida con la terminación del código de mano de obra (`item_cont`).

| Clasificación en Fénix (`urbrur`) | Terminación esperada |
|---|---|
| Rural: `R` | Código terminado en `R`. |
| Urbano: `U` | Código terminado en `U`. |

Si no coincide, se presenta `INCONSISTENCIA_RURAL_URBANO`. Se revisan los códigos cuya terminación corresponda a U o R.

**Ejemplo:** un pedido rural con D01U presenta inconsistencia.

**Qué revisar:** la clasificación del pedido y el código digitado, para determinar cuál requiere ajuste.

## 6. ALERTA_PAGINA_7MO_DIGITO

**¿Para qué sirve?** Complementa la revisión Rural/Urbano con controles sobre el campo `pagina`.

### Páginas que comienzan por 190

Se cuenta el séptimo dígito desde la izquierda, comenzando en 1.

| Séptimo dígito | Clasificación esperada | Caso que genera alerta |
|---|---|---|
| `1` | Urbano: `U`. | Dígito 1 con clasificación R. |
| `2` | Rural: `R`. | Dígito 2 con clasificación U. |
| Diferente de 1 o 2 | Valor no reconocido por esta regla. | Se solicita revisar en MARCOPOLO. |

Los cruces 1 con U y 2 con R cumplen la comparación. Como ejemplos ficticios, `190000100000000001` con R presenta inconsistencia y `190000200000000001` con U también.

### Páginas cuyo inicio está entre 200 y 999

Toda página cuyos primeros tres dígitos estén entre 200 y 999 se muestra en amarillo como `VALIDAR_EN_MARCOPOLO`, para comprobar si existe un error de digitación. También se indica cuando el séptimo dígito es distinto de 1 o 2. Este control aplica a cualquier actividad.

**Qué revisar:** consultar la página en MARCOPOLO antes de decidir si debe corregirse. La marca amarilla indica una consulta pendiente, no confirma por sí sola un error.

## 7. ALERTA_PAGINA_MUNICIPIO

**¿Para qué sirve?** Cruza el municipio, el inicio de la página y la clasificación U/R registrada en Fénix.

Si el prefijo tiene una clasificación definida y no coincide con la registrada, se muestra `INCONSISTENCIA_PAGINA_MUNICIPIO`. Se conservan los ceros iniciales y se compara el prefijo completo.

| Municipio | Prefijos urbanos (U) | Prefijos rurales (R) |
|---|---|---|
| Medellín | 04, 05, 06, 08, 70, 116, 136 | 122, 124, 126, 130, 139, 146, 147, 148, 162 |
| Itagüí | 07, 77 | Sin prefijos definidos. |
| Envigado | 02 | 125, 166 |
| La Estrella | 03 | Sin prefijos definidos. |
| Sabaneta | 01 | Sin prefijos definidos. |
| Caldas | 00 | 161, 1901302 |

**Caso particular:** en Caldas, el prefijo completo `1901302` corresponde a rural.

Los siguientes prefijos pueden corresponder a urbano o rural y se presentan como `VALIDAR_EN_MARCOPOLO`:

| Municipio | Prefijos que requieren consulta |
|---|---|
| Medellín | 103, 114, 117, 119 |
| Itagüí | 163 |
| Envigado | 140 |
| La Estrella | 159 |
| Sabaneta | 167 |

Si la página no comienza por ninguno de los prefijos definidos para su municipio, esta hoja no genera alerta por ese cruce. Esto significa que no existe una clasificación definida para ese caso, no que la página haya quedado validada.

La columna `item_cont` reúne las manos de obra tipo `CON` del mismo pedido, subzona y página, separadas por comas y sin repetir códigos.

**Qué revisar:** el municipio, el prefijo completo y la clasificación registrada; consultar MARCOPOLO cuando la alerta lo indique.

## 8. ALERTA_ACTIVIDADES

**¿Para qué sirve?** Revisa los códigos, materiales y condiciones exigidos para actividades específicas. Las columnas `urbrur` y `tipre` permiten interpretar los controles que dependen de la zona o del tipo de prepago.

### Códigos requeridos por actividad

| Actividad | Códigos requeridos | Criterio de revisión |
|---|---|---|
| AMRTR — Movimiento de redes | D02U/R, D03U/R o D04U/R. | Debe existir al menos uno. Otro código Dxx diferente a los permitidos genera error de digitación. |
| ACREV — Puntos de conexión | D01U o D01R. | Debe existir al menos uno. Otro código Dxx diferente a los permitidos genera error de digitación. |
| ACAMN / ALECA | C05U o C05R. | Debe existir uno de los códigos válidos; otros ítems requieren revisión. |
| ALEGA / ALEGN | C01U/R, C02U/R, C03U/R o C04U/R. | Debe existir uno de los códigos válidos; otros ítems requieren revisión. |

La ausencia de códigos válidos se presenta como `FALTA ÍTEM VÁLIDO`; los códigos no permitidos según el alcance de cada regla, como `ERROR EN DIGITACIÓN`.

### Reglas de AEJDO — Habilitación de vivienda

La relación entre `CALE1F` y `A12U/R` es bidireccional: si aparece uno, debe aparecer el otro.

| Condición encontrada en AEJDO | Requisito | Alerta si no cumple |
|---|---|---|
| 215887 o 219404 con cantidad. | Debe registrar cobro al usuario en `vlr_cliente`. | `COBRO_FALTANTE_AEJDO` |
| A18U o A18R. | Suministro obligatorio 211357. | `REGLA_AEJDO_A18` |
| A12U o A12R. | Uno de los medidores 200092/200093 y ambos suministros 215887 y 219404. También requiere CALE1F. | `REGLA_AEJDO_A12_MATERIALES`; la falta de CALE1F se indica en `REGLA_AEJDO`. |
| A02U o A02R. | A06U/R o A08U/R con la misma terminación; uno es suficiente. | `REGLA_AEJDO_A02` |
| A10U o A10R. | A12U/R con la misma terminación. | `REGLA_AEJDO_A10` |
| A07U o A07R. | Suministro obligatorio 200384. | `REGLA_AEJDO_A07` |
| Suministro 200092. | 200410 o 200492; uno es suficiente. | `REGLA_AEJDO_200092` |
| Suministro 200093. | 200411, 200493 o 323739; uno es suficiente. | `REGLA_AEJDO_200093` |
| A32U o A32R. | Ambos suministros: 200151A y 211319A. | `REGLA_AEJDO_A32` |

**Ejemplos:** A02U con A08U cumple esa relación; A02U con A06R no cumple la misma terminación. A32U con solo 200151A requiere también 211319A.

### Relación A18–A19 en AEJDO e INPRE

Si se registra A18U o A18R, debe aparecer A19U o A19R, respectivamente, dentro del mismo pedido, subzona y actividad. Si falta, se genera `REGLA_A18_REQUIERE_A19`.

### Relación A13–A22 en DSPRE

A13U requiere A22U y A13R requiere A22R. Si falta el correspondiente, la alerta explica que el ítem A13 incluye la instalación del nuevo pase (anterior acometida).

### Condiciones de A22 según zona y tipo de prepago

Estas condiciones se revisan en la línea `CON` del ítem A22.

| Actividad e ítem | Condición encontrada | Resultado |
|---|---|---|
| AEJDO · A22U | Urbano y `tipre` diferente de ENESUB o ENEPIL. | `A22U_TIPO_PREPAGO_NO_VALIDO`: A22U solo es válido para esos dos tipos. |
| DIPRE o DSPRE · A22U | Urbano y `tipre = ENEPRE`. | `A22U_NO_VALIDO_ENEPRE`: revisar el ítem, válido para ENESUB o ENEPIL. |
| DIPRE o DSPRE · A22R | Rural y `tipre` vacío. | `OBSERVACION_A22R_POSTE`: comprobar si el medidor está en poste; si no, cambiar el ítem. |

### Correcciones de ítems según zona

Aplican a **AEJDO, INPRE, DIPRE, REEQU y DSPRE**.

| Condición encontrada | Corrección indicada | Alerta |
|---|---|---|
| Rural (R): A04R y A05R juntos. | Corregir por A06R. | `CORREGIR_A04R_A05R_POR_A06R` |
| Urbano (U): A06R. | Corregir por A04U y A05U. | `CORREGIR_A06R_POR_A04U_A05U` |

**Qué revisar:** la actividad, las manos de obra y suministros del pedido, la zona, el tipo de prepago y el detalle de cada alerta. Las diferencias históricas entre la guía y el código se conservan en la referencia técnica al final del documento.

## 9. LEGALIZACION_NO_COBRO

**¿Para qué sirve?** Identifica cobros no permitidos para las actividades **ACAMN, ALECA, ALEGA y ALEGN**.

| Suministro | Descripción | Regla de la guía |
|---|---|---|
| 215887A | Tornillo. | No debe registrar valor en `vlr_cliente`. |
| 219404A | Sello. | No debe registrar valor en `vlr_cliente`. |

Según la guía, un valor mayor a cero genera `COBRO_NO_PERMITIDO`.

**Ejemplo:** ALEGA con 215887A y cobro positivo presenta una novedad.

**Qué revisar:** actividad, suministro y valor cobrado. Estos códigos llevan sufijo A y se diferencian de 215887 y 219404, cuyo cobro se controla en AEJDO. La referencia técnica conserva la diferencia histórica sobre valores negativos.

## 10. ALERTA_CANTIDADES_MO

**¿Para qué sirve?** Presenta en una hoja de detalle las manos de obra controladas cuya cantidad registrada en una fila es mayor a 1.

| Grupo | Códigos controlados | Ejemplo que genera alerta |
|---|---|---|
| A | Cualquier `item_cont` que comience por A. | A21R con cantidad 4. |
| C | Cualquier `item_cont` que comience por C. | C02U con cantidad 2. |
| D | D01U/R, D02U/R, D03U/R y D04U/R. | D01U con cantidad 2. |
| F | F01U y F01R. | F01R con cantidad 2. |

La alerta es `CANTIDAD_MO>1`. Este control se evalúa por registro, sin sumar filas distintas; por ejemplo, D05U no entra en la lista controlada del grupo D.

**Qué revisar:** pedido, subzona, mano de obra, cantidad y detalle. Esta novedad también puede aparecer en `VALIDACION`; dos apariciones no representan dos casos diferentes.

## 11. MASIVAS

**¿Para qué sirve?** Verifica que la mano de obra C01–C04 corresponda a la cantidad de instalaciones y detecta páginas compartidas por varios pedidos de una misma subzona.

### Cantidad de instalaciones y código esperado

El proceso toma los primeros 14 dígitos de `pagina` para formar `pagina_base`. Agrupa por **subzona y página base**, y cuenta las instalaciones distintas a partir de la página completa. Si una instalación aparece en varias filas, se cuenta una sola vez.

| Instalaciones distintas | Mano de obra esperada |
|---|---|
| 1 | C01U o C01R |
| 2 a 12 | C02U o C02R |
| 13 a 24 | C03U o C03R |
| 25 o más | C04U o C04R |

La terminación U/R no cambia estos rangos. Si el código no corresponde a la cantidad, se muestra `ITEM_CONT_NO_CORRESPONDE_CANTIDAD`.

**Ejemplo:** 14 instalaciones con C02U requieren revisión porque el rango corresponde a C03U/R. Como ejemplo de agrupación, `190607100316666202` tiene como página base `19060710031666`.

### Páginas duplicadas entre pedidos

Si una misma página completa aparece en **dos o más pedidos distintos de la misma subzona**, se muestra `PAGINA_DUPLICADA` y se resalta la página en amarillo.

Varias filas de la misma página dentro de un solo pedido no se consideran duplicidad para este control. La alerta puede aparecer aunque el ítem C01–C04 corresponda correctamente a la cantidad de instalaciones.

**Qué revisar:** la página completa, los pedidos involucrados, la subzona, el número de instalaciones y el código registrado.

## Uso del informe compartido

El archivo se comparte en OneDrive, en la carpeta `Relación_MO_Vs_Materiales`. Para revisarlo:

1. Seleccionar el corte correspondiente y, de ser necesario, descargar una copia para evitar conflictos de edición.
2. Filtrar la zona o subzona en cada hoja que se consulte; el filtro de una hoja no se aplica automáticamente a las demás.
3. Leer la alerta junto con su detalle y revisar el pedido completo en Fénix.
4. Confirmar la corrección o excepción con el responsable operativo cuando corresponda.
5. Comunicar las nuevas condiciones detectadas para su revisión con los analistas e ingenieros y su posterior incorporación a las reglas y a esta documentación.

Una misma novedad puede aparecer en varias hojas. El informe facilita la revisión, pero no acredita por sí solo que un pedido ya haya sido revisado por el analista.

### Cortes de revisión

| Hora aproximada | Alcance |
|---|---|
| 6:00 a. m. | Día anterior. |
| 10:00 a. m. | Mes completo hasta el corte. |
| 2:30 p. m. | Día actual hasta el corte. |

La nomenclatura documentada para el día anterior es `VALIDACION_MO_MATERIALES_ALMACEN_AAAA-MM-DD.xlsx`; para el día actual, `INFORME_VALIDACION_MO_MATERIALES_ALMACEN_AAAA-MM-DD.xlsx`. La fecha corresponde al período informado. No se define aquí un nombre nuevo para el corte mensual.

### Material de práctica

Como referencia histórica de capacitación se conserva el archivo `Capacitacion_V2_validacion_mo_materiales_20260915_131517.xlsx`, ubicado originalmente en `C:\Users\hector.gaviria\Desktop\Launcher_Elite\Control_ANS_v5\`.

Antes de usarlo en una capacitación, comprobar que incluya las reglas actuales y complementar los ejemplos que falten. La explicación de este documento se apoya en la guía del 26/10/2026, no en que el archivo de práctica antiguo contenga todas las novedades.

---

# Referencia técnica para mantenimiento

Esta sección se conserva para el desarrollador y no forma parte del recorrido hoja por hoja de la capacitación.

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

****Este documento no se sincroniza automáticamente con Python ni con `GUIA_REGLAS`.**** Reemplazar el Markdown actualiza la consulta del centro de conocimiento; las siguientes reglas requieren actualizarlo dentro de la misma entrega del cambio.

## Actualización documental — 26/10/2026

Se reorganizó la explicación operativa por las once hojas identificadas en los documentos suministrados y se resumió la introducción. Se incorporaron las condiciones de la guía del 26/10/2026: cantidades específicas de materiales; páginas 190 y 200–999; prefijos por municipio; A18–A19 en AEJDO e INPRE; materiales de A12; cruces de A22; correcciones A04/A05/A06 y duplicidad de páginas en MASIVAS. Se actualizaron los tres cortes de revisión conforme al esquema operativo acordado.

Se conserva el historial técnico anterior como referencia histórica. Su mención a diez hojas corresponde a la documentación del 14/10/2026; la organización actual incluye también ALERTA_PAGINA_MUNICIPIO. Las notas de conciliación anteriores quedan pendientes de comprobar contra el script vigente. En esta actualización se revisaron los dos documentos adjuntos; no se recibió ni se ejecutó el script y no se modificaron reglas de Python ni la Base Maestra.
