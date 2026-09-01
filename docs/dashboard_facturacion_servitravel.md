# 📊 Dashboard de Facturación SERVITRAVEL

## 1. Objetivo de este documento

Este documento deja registrado **cómo funciona, cómo se usa, cómo se construyó y por qué se tomaron determinadas decisiones técnicas** en el archivo:

`DASHBOARD_FACTURACION.xlsb`

La finalidad es que, si en el futuro se requiere realizar un ajuste, corregir una novedad o explicar el desarrollo a otro usuario, sea posible retomar el proyecto sin depender de la memoria de quien lo construyó.

## 2. Archivos principales del proceso

### Archivo origen de facturación

El archivo operativo de facturación se encuentra en OneDrive:

`C:\Users\hector.gaviria\Elite Ingenieros SAS\Alejandra Lopez Arango - 7.FACTURACIÓN\Seguimiento facturas.xlsx`

Hoja utilizada: `Vinculaciones`.

### Archivo consolidado

El módulo **Consolidador Excel** del Launcher SERVITRAVEL actualiza:

`C:\Users\hector.gaviria\Desktop\Launcher_Elite\SERVITRAVEL\salida\INFORME_LIQUIDACION.xlsb`

La hoja utilizada para este Dashboard es `FACTURACION`.

Flujo:

```text
Seguimiento facturas.xlsx
        ↓
Consolidador Excel
        ↓
INFORME_LIQUIDACION.xlsb
        ↓
Hoja FACTURACION
```

Durante la validación se comprobó:

```text
Registros origen : 219
Registros destino: 219
```

Esto permitió confirmar que el script de consolidación no estaba duplicando registros.

### Archivo Dashboard

Archivo: `DASHBOARD_FACTURACION.xlsb`

Flujo completo:

```text
Seguimiento facturas.xlsx
        ↓
Python - Consolidador Excel
        ↓
INFORME_LIQUIDACION.xlsb
        ↓
Power Query
        ↓
BASE_LIMPIA
        ↓
Modelo de Datos / Power Pivot
        ↓
Tablas dinámicas + medidas DAX
        ↓
DASHBOARD
```

## 3. Uso normal del archivo por parte del usuario

El usuario final **no necesita ingresar a Power Query ni Power Pivot**.

Procedimiento:

1. Actualizar `INFORME_LIQUIDACION.xlsb` desde el módulo **Consolidador Excel**.
2. Abrir `DASHBOARD_FACTURACION.xlsb`.
3. Ir a **Datos → Actualizar todo**.
4. Esperar a que finalicen consultas y tablas dinámicas.
5. Utilizar los segmentadores:
   - MES
   - CATEGORIA
   - PROVEEDOR

## 4. KPI principales

### TOTAL FACTURADO

Representa el valor total facturado bajo los filtros activos.

### NÚMERO DE FACTURAS

Cantidad de facturas dentro del contexto seleccionado.

### NÚMERO DE PROVEEDORES

Cantidad distinta de proveedores. Para este KPI se utiliza Power Pivot / Modelo de Datos.

### PROMEDIO POR FACTURA

```text
TOTAL FACTURADO / NÚMERO DE FACTURAS
```

### SERVICIOS TEMPORALES

Es un KPI independiente que muestra cuánto del total facturado corresponde a Servicios Temporales aprobados para el análisis.

**No debe sumarse nuevamente al Total Facturado**, porque ese valor ya está contenido dentro del total.

## 5. CATEGORIA_ANALISIS

`CATEGORIA_ANALISIS` es la dimensión principal de las tablas dinámicas.

Contiene:

- METROPOLITANA
- NORDESTE
- OCCIDENTE
- ORIENTE
- SUROESTE
- PARQUEADEROS
- PEAJES
- VIATICOS

Debe permanecer intacta.

## 6. ¿Por qué SERVICIOS TEMPORALES no está dentro de CATEGORIA_ANALISIS?

`CATEGORIA_ANALISIS` y `TIPO_SERVICIO` son dimensiones diferentes.

Ejemplo:

```text
CATEGORIA_ANALISIS = METROPOLITANA
TIPO_SERVICIO      = SERVICIOS TEMPORALES
TOTAL              = $5.000.000
```

La misma factura pertenece a METROPOLITANA y simultáneamente es un Servicio Temporal.

Si se reemplaza METROPOLITANA por SERVICIOS TEMPORALES, se pierde la categoría original.

Si se duplica la fila para mostrar:

```text
METROPOLITANA          $5.000.000
SERVICIOS TEMPORALES   $5.000.000
```

se genera una lectura duplicada del valor.

Por eso se conserva `CATEGORIA_ANALISIS` y Servicios Temporales se presenta mediante un KPI independiente.

### Explicación funcional para el usuario

> Servicios Temporales no se adiciona como una categoría independiente dentro de la tabla dinámica principal porque esas facturas ya están contabilizadas en su categoría de análisis original. Una factura puede pertenecer, por ejemplo, a Metropolitana y simultáneamente ser identificada como Servicio Temporal. Si se reemplazara Metropolitana por Servicios Temporales se perdería la categoría original; si se mostrara nuevamente el mismo valor en ambas categorías se duplicaría visualmente la información. Por esta razón, Servicios Temporales se presenta como un KPI independiente que permite conocer cuánto del total facturado corresponde a este tipo de servicio.

## 7. CONTROL_SERV_TEMP

Hoja:

`CONTROL_SERV_TEMP`

Objetivo: permitir al usuario decidir qué facturas de Servicios Temporales participan en el KPI.

Estructura:

| FACTURA | PROVEEDOR | ACCION |
|---|---|---|
| 10200 | SERVITRAVEL | INCLUIR |
| 593 | SERVITRAVEL | INCLUIR |
| 6001 | MONTOYA | EXCLUIR |

`PROVEEDOR` sirve para facilitar la identificación.

La columna `ACCION` utiliza Validación de Datos con:

- INCLUIR
- EXCLUIR

### Regla de inclusión

Para sumar en el KPI deben cumplirse simultáneamente:

```text
TIPO_SERVICIO = SERVICIOS TEMPORALES
PROVEEDOR     = SERVITRAVEL
ACCION        = INCLUIR
```

`EXCLUIR` no suma.

Si ACCION está vacía, actualmente tampoco suma.

Importante: excluir del KPI **no elimina la factura de la base**, ni la saca de su categoría original, ni modifica el Total Facturado.

## 8. Cómo usa CONTROL_SERV_TEMP el usuario final

1. Ir a `CONTROL_SERV_TEMP`.
2. Identificar la factura.
3. Revisar el proveedor.
4. Seleccionar `INCLUIR` o `EXCLUIR`.
5. Ir a **Datos → Actualizar todo**.
6. Regresar al Dashboard.
7. Validar el KPI de Servicios Temporales.

El usuario no debe modificar Power Query ni Power Pivot.

## 9. Para qué usamos Power Query

Power Query realiza el ETL:

```text
Extraer → Transformar → Cargar
```

Se utiliza para:

- conectarse a `INFORME_LIQUIDACION.xlsb`;
- leer `FACTURACION`;
- limpiar textos;
- normalizar campos;
- corregir tipos de datos;
- preparar fechas;
- construir columnas auxiliares;
- entregar `BASE_LIMPIA`.

### Consulta FACTURACION

Consulta técnica principal. Normalmente queda como **Solo conexión**.

### BASE_LIMPIA

Base preparada para el análisis y para el Modelo de Datos.

Una validación clave después de ajustes es comparar cantidad de registros:

```text
FACTURACION origen
vs
BASE_LIMPIA
```

Si el origen tiene 219 filas y BASE_LIMPIA aumenta sin una regla funcional que lo justifique, debe revisarse Power Query.

## 10. Campos de período creados en Power Query

### NUM_MES

Número del mes.

### PERIODO

Mes + año.

### ORDEN_PERIODO

Orden cronológico, por ejemplo:

```text
202509
202510
202511
202512
202601
```

### PERIODO_FECHA

Fecha real del período:

```text
01/09/2025
01/10/2025
```

### MES_SEGMENTADOR

Campo utilizado para presentar el mes correctamente en segmentadores y tablas dinámicas.

## 11. Para qué usamos Power Pivot

Power Pivot se utiliza para:

- Modelo de Datos;
- medidas DAX;
- recuentos distintos;
- comparación Mes Actual vs Mes Anterior;
- variación porcentual;
- cálculos sensibles a segmentadores;
- KPI Servicios Temporales.

Resumen:

```text
Power Query prepara.
Power Pivot calcula.
Excel presenta.
```

## 12. Medidas principales

### Total Actual

Conceptualmente:

```DAX
Total Actual :=
SUM(BASE_LIMPIA[TOTAL])
```

### Total Mes Anterior

Identifica automáticamente el período anterior al mes seleccionado.

Ejemplo:

```text
ABRIL 2026
vs
MARZO 2026
```

### Variación %

Compara Total Actual contra Total Mes Anterior.

### Servicios Temporales Incluidos

Medida creada para sumar únicamente facturas aprobadas.

Lógica:

```text
TIPO_SERVICIO = SERVICIOS TEMPORALES
+
PROVEEDOR = SERVITRAVEL
+
CONTROL_SERV_TEMP[ACCION] = INCLUIR
```

La tabla `tbl_control_serv_temp` se agregó al Modelo de Datos.

No se utiliza Merge para este control.


### Cómo funciona la medida Servicios Temporales Incluidos

Medida DAX utilizada:

```DAX
Servicios Temporales Incluidos:=
SUMX(
    FILTER(
        BASE_LIMPIA;
        BASE_LIMPIA[TIPO_SERVICIO] = "SERVICIOS TEMPORALES"
            &&
        BASE_LIMPIA[PROVEEDOR] = "SERVITRAVEL"
            &&
        LOOKUPVALUE(
            tbl_control_serv_temp[ACCION];
            tbl_control_serv_temp[FACTURA];
            BASE_LIMPIA[FACTURA]
        ) = "INCLUIR"
    );
    BASE_LIMPIA[TOTAL]
)
```

#### Explicación sencilla

La medida hace lo siguiente:

> Revisa fila por fila `BASE_LIMPIA`, conserva únicamente las facturas que son
> Servicios Temporales, cuyo proveedor es SERVITRAVEL y cuya factura está marcada
> como `INCLUIR` en `CONTROL_SERV_TEMP`. Finalmente suma el campo `TOTAL` de esas
> facturas.

La lógica puede entenderse así:

```text
¿TIPO_SERVICIO = SERVICIOS TEMPORALES?
        ↓ Sí
¿PROVEEDOR = SERVITRAVEL?
        ↓ Sí
¿La factura está marcada INCLUIR?
        ↓ Sí
SUMAR TOTAL
```

Si alguna condición no se cumple:

```text
NO SUMAR EN EL KPI
```

#### Qué hace cada parte

`FILTER(BASE_LIMPIA; ...)`

Revisa las filas de `BASE_LIMPIA` y deja pasar únicamente las que cumplen las
condiciones definidas.

`BASE_LIMPIA[TIPO_SERVICIO] = "SERVICIOS TEMPORALES"`

Valida que el registro corresponda al tipo de servicio requerido.

`BASE_LIMPIA[PROVEEDOR] = "SERVITRAVEL"`

Valida que el proveedor sea SERVITRAVEL.

`LOOKUPVALUE(...) = "INCLUIR"`

Toma el número de factura de la fila actual de `BASE_LIMPIA`, lo busca en
`tbl_control_serv_temp` y consulta el valor de la columna `ACCION`.

Ejemplo:

```text
BASE_LIMPIA
FACTURA = 10200

        ↓ buscar

tbl_control_serv_temp
FACTURA = 10200
ACCION = INCLUIR
```

Si la acción es `INCLUIR`, la factura puede participar en el KPI.

Si la acción es `EXCLUIR` o no existe una inclusión válida, la medida no suma
ese valor.

`SUMX(...; BASE_LIMPIA[TOTAL])`

Después de aplicar todas las condiciones, suma el campo `TOTAL` de las filas
que fueron aprobadas.

#### Ejemplo práctico

| FACTURA | TIPO_SERVICIO | PROVEEDOR | ACCION | TOTAL | ¿SUMA EN KPI? |
|---|---|---|---|---:|---|
| 10200 | SERVICIOS TEMPORALES | SERVITRAVEL | INCLUIR | $23.002.705 | Sí |
| 593 | SERVICIOS TEMPORALES | SERVITRAVEL | EXCLUIR | -$23.002.705 | No |
| 6001 | SERVICIOS TEMPORALES | MONTOYA | INCLUIR | $5.000.000 | No |
| 10115 | VIATICOS | SERVITRAVEL | INCLUIR | $2.000.000 | No |

#### Por qué esta medida es segura

La medida:

- no modifica `BASE_LIMPIA`;
- no elimina registros;
- no cambia `CATEGORIA_ANALISIS`;
- no duplica facturas;
- no modifica el `TOTAL FACTURADO`;
- solamente determina qué valores deben mostrarse en el KPI de Servicios Temporales.

Por esta razón, `INCLUIR` y `EXCLUIR` afectan únicamente el KPI de Servicios
Temporales y no las tablas dinámicas principales del Dashboard.


## 13. Tabla dinámica auxiliar del KPI

La medida `Servicios Temporales Incluidos` se coloca en una tabla dinámica pequeña en:

`TAB_AUXILIAR`

Esa tabla contiene básicamente el valor de la medida.

El KPI visual del Dashboard apunta a esa celda.

Ventaja: el KPI queda vinculado a una celda controlada y no depende de cuántas filas tengan otras tablas dinámicas.

## 14. Segmentadores y KPI Servicios Temporales

La tabla dinámica auxiliar del KPI puede conectarse mediante **Conexiones de informe** a:

- MES
- CATEGORIA
- PROVEEDOR

Así puede responder preguntas como:

```text
¿Cuánto de ABRIL 2026 corresponde a Servicios Temporales incluidos?
```

o:

```text
¿Cuánto de METROPOLITANA corresponde a Servicios Temporales?
```

## 15. Tablas principales del Dashboard

### RESUMEN DEL PERIODO SELECCIONADO

Filas: `CATEGORIA_ANALISIS`

Valores: `TOTAL`

### COMPARATIVA MES ACTUAL VS MES ANTERIOR

Muestra:

- Total Mes Anterior
- Total Actual
- Variación %
- Estado

### DETALLE HISTÓRICO POR CATEGORÍA Y PERÍODO

Filas: `CATEGORIA_ANALISIS`

Columnas: `MES_SEGMENTADOR`

Valores: `TOTAL`

## 16. Qué no volver a hacer

### No reemplazar CATEGORIA_ANALISIS por SERVICIOS TEMPORALES

Durante las pruebas se creó una clasificación final que trasladaba registros a SERVICIOS TEMPORALES.

Eso hizo que categorías como METROPOLITANA, OCCIDENTE u ORIENTE parecieran desaparecer.

Los valores no se habían perdido: habían sido reclasificados.

Por eso ese enfoque se descartó.

### No duplicar una factura para mostrarla dos veces

Una factura no debe aparecer como una segunda fila solo para mostrar simultáneamente su categoría original y Servicios Temporales, porque puede inflar la lectura de los totales.

### Evitar Merge innecesarios para excepciones manuales

Una combinación mal definida puede multiplicar filas.

La solución final usa una tabla de control independiente en el Modelo de Datos.

## 17. Validaciones después de cualquier cambio

1. Comparar número de filas del origen con `BASE_LIMPIA`.
2. Verificar Total Facturado para un período conocido.
3. Confirmar que sigan apareciendo todas las categorías.
4. Probar varios meses.
5. Probar una factura con `INCLUIR`.
6. Cambiarla a `EXCLUIR`.
7. Confirmar que solo cambie el KPI Servicios Temporales.
8. Confirmar que Total Facturado no cambie por la acción INCLUIR / EXCLUIR.
9. Revisar conexiones de segmentadores.
10. Validar comparativa Mes Actual vs Mes Anterior.

## 18. Si Servicios Temporales muestra $0

Revisar:

1. La factura existe en `DATOS_FACTURACION`.
2. `TIPO_SERVICIO = SERVICIOS TEMPORALES`.
3. `PROVEEDOR = SERVITRAVEL`.
4. La factura existe en `CONTROL_SERV_TEMP`.
5. `ACCION = INCLUIR`.
6. Se ejecutó **Datos → Actualizar todo**.
7. El mes seleccionado corresponde a la factura.
8. La tabla dinámica auxiliar está conectada al segmentador.

## 19. Explicación corta para una reunión

> El Dashboard toma la información consolidada de facturación, la prepara mediante Power Query y la carga en un Modelo de Datos de Power Pivot. Las categorías principales se mantienen en CATEGORIA_ANALISIS. Servicios Temporales se maneja como un KPI independiente porque es un atributo adicional de las mismas facturas y no una categoría exclusiva. De esta forma se evita reclasificar o duplicar valores. El usuario controla las facturas que participan en este KPI desde CONTROL_SERV_TEMP mediante INCLUIR y EXCLUIR.

## 20. Arquitectura resumida

```text
Seguimiento facturas.xlsx
        ↓
Consolidador Excel - Python
        ↓
INFORME_LIQUIDACION.xlsb
        ↓
Power Query
        ↓
BASE_LIMPIA
        ↓
Power Pivot / Modelo de Datos
        ↓
Medidas DAX
        ↓
Tablas dinámicas
        ↓
Dashboard
```

Servicios Temporales:

```text
CONTROL_SERV_TEMP
        ↓
tbl_control_serv_temp
        ↓
Modelo de Datos
        ↓
Medida Servicios Temporales Incluidos
        ↓
TAB_AUXILIAR
        ↓
KPI SERVICIOS TEMPORALES
```

## 21. Principio de mantenimiento

Antes de modificar el archivo recordar:

> `CATEGORIA_ANALISIS` y `TIPO_SERVICIO` no son la misma dimensión.

Una factura puede pertenecer simultáneamente a una categoría principal y a un tipo de servicio.

Esta diferencia explica por qué Servicios Temporales debe analizarse por separado.

## 22. Resumen final

- **Python:** actualiza el consolidado.
- **Power Query:** extrae, limpia y transforma.
- **BASE_LIMPIA:** conserva la base preparada.
- **Power Pivot:** realiza cálculos dinámicos.
- **Tablas dinámicas:** presentan categoría, período y comparativas.
- **CONTROL_SERV_TEMP:** permite al usuario gestionar inclusión/exclusión del KPI.
- **Dashboard:** presenta KPI, segmentadores, resumen, comparativa e histórico.

La decisión central del diseño es conservar `CATEGORIA_ANALISIS` intacta y tratar `SERVICIOS TEMPORALES` como un indicador adicional contenido dentro del Total Facturado.
