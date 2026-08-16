# ANS REDES - Guía funcional y reglas de negocio

## 1. Objetivo

El módulo **ANS REDES** permite generar y consultar el informe operativo de redes a partir del archivo exportado, aplicando automáticamente los filtros y reglas de negocio configuradas por el usuario.

La idea principal es que las reglas puedan modificarse desde el archivo:

`config/FILTROS_ANS_REDES.xlsx`

sin necesidad de editar archivos `.py`.

---

## 2. Flujo de trabajo

El proceso operativo es:

1. Ubicar el archivo exportado en la carpeta `entrada_redes`.
2. Ejecutar **GENERAR INFORME ANS REDES**.
3. El sistema aplica los filtros y reglas configuradas en Excel.
4. Se genera `INFORME_ANS_REDES.xlsx`.
5. Ejecutar **ACTUALIZAR DASHBOARD**.
6. El dashboard se actualiza con la información más reciente.
7. Consultar los resultados mediante **ABRIR INFORME** o **ABRIR DASHBOARD**.

---

## 3. Archivo de configuración

El archivo `FILTROS_ANS_REDES.xlsx` concentra las reglas funcionales del módulo.

Contiene tres hojas:

- `PARAMETROS_REDES`
- `DIAS_CONTRACTUALES_REDES`
- `CONFIGURACION_REDES`

Estas hojas permiten modificar filtros, tiempos contractuales y reglas de calendario sin intervenir el código.

---

# 4. Hoja PARAMETROS_REDES

Esta hoja controla qué registros deben ingresar al informe.

Columnas:

| CAMPO | VALOR | ACTIVO |
|---|---|---|
| PROCESO | 4109 | SI |
| REV_ESTADO | P | SI |
| REV_RESPONSABLE | CHEC\AHERRERV | SI |

## Cómo agregar un responsable

Para incluir un nuevo responsable:

1. Agregar una nueva fila.
2. En `CAMPO` escribir `REV_RESPONSABLE`.
3. En `VALOR` escribir el usuario exactamente como aparece en el exporte.
4. En `ACTIVO` escribir `SI`.

Ejemplo:

| CAMPO | VALOR | ACTIVO |
|---|---|---|
| REV_RESPONSABLE | CHEC\NUEVOUSUARIO | SI |

En la siguiente generación, los registros de ese responsable podrán ingresar al informe.

## Cómo deshabilitar un responsable

No es necesario eliminar la fila.

Cambiar:

`ACTIVO = SI`

por:

`ACTIVO = NO`

El responsable deja de participar en el filtro, pero la configuración queda registrada para una posible reactivación.

## Cómo agregar o deshabilitar un proceso

Se aplica la misma lógica.

Agregar:

| CAMPO | VALOR | ACTIVO |
|---|---|---|
| PROCESO | 4200 | SI |

Deshabilitar:

| CAMPO | VALOR | ACTIVO |
|---|---|---|
| PROCESO | 4109 | NO |

---

# 5. Hoja DIAS_CONTRACTUALES_REDES

Esta hoja define cuántos días tiene cada proceso y en qué momento debe iniciar la alerta.

Columnas principales:

| PROCESO | TIPO_ZONA | MUNICIPIO | DIAS_CONTRACTUALES | PORCENTAJE_ALERTA | ACTIVO |
|---|---|---|---:|---:|---|
| 4109 | URBANO | MANIZALES | 15 | 70% | SI |
| 4109 | RURAL | TODOS | 23 | 70% | SI |
| 4133 | TODOS | TODOS | 45 | 70% | SI |

## Reglas actualmente definidas

### Proceso 4109 - zona urbana

Para los municipios configurados como urbanos especiales, se aplican:

`15 días contractuales`

La alerta inicia al:

`70% de los días`

Ejemplo:

`15 x 70% = 10,5`

El sistema toma:

`10 días`

### Proceso 4109 - regla general

Para zona rural y los demás municipios que no cumplen la regla urbana especial:

`23 días contractuales`

Alerta:

`23 x 70% = 16,1`

Resultado:

`16 días`

### Procesos 4133, 4166 y 4167

Se aplican:

`45 días contractuales`

sin importar municipio o zona.

Alerta:

`45 x 70% = 31,5`

Resultado:

`31 días`

---

# 6. Cómo cambiar el porcentaje de alerta

El porcentaje se modifica directamente en la columna:

`PORCENTAJE_ALERTA`

Ejemplo actual:

`70%`

Si en el futuro la regla cambia a `80%`, únicamente se modifica el valor en Excel.

Ejemplo para 45 días:

`45 x 80% = 36`

El sistema utilizará el nuevo porcentaje en la siguiente generación.

No es necesario modificar Python.

---

# 7. Hoja CONFIGURACION_REDES

Esta hoja controla cómo se cuentan los días.

Configuración actual:

| PARAMETRO | VALOR |
|---|---|
| EXCLUIR_SABADOS | SI |
| EXCLUIR_DOMINGOS | SI |
| EXCLUIR_FESTIVOS_COLOMBIA | SI |
| CONTEO_DESDE_MISMO_DIA | SI |
| CONSERVAR_HORA_INICIO | SI |

## EXCLUIR_SABADOS

### SI

Los sábados no cuentan como día contractual.

### NO

Los sábados pasan a considerarse días válidos para el conteo.

Ejemplo:

Si hoy la organización decide que los sábados deben considerarse hábiles, se cambia:

`EXCLUIR_SABADOS = SI`

por:

`EXCLUIR_SABADOS = NO`

En la siguiente generación las fechas límite se recalcularán incluyendo sábados.

---

## EXCLUIR_DOMINGOS

Funciona igual que la regla de sábados.

`SI` = domingo no cuenta.

`NO` = domingo sí cuenta.

---

## EXCLUIR_FESTIVOS_COLOMBIA

`SI` = los festivos oficiales de Colombia no cuentan.

`NO` = los festivos sí participan en el conteo.

---

## CONTEO_DESDE_MISMO_DIA

Con valor `SI`, el ANS comienza desde la misma fecha de:

`PRO_FECHA_SISTEMA_CREACION`

si ese día es válido según las reglas de calendario.

Ejemplo:

`16/07/2026 09:58:24`

El conteo inicia desde el mismo:

`16/07/2026 09:58:24`

Si esa fecha fuera un sábado y `EXCLUIR_SABADOS = SI`, ese día no contaría y el conteo continuaría en el siguiente día permitido.

---

## CONSERVAR_HORA_INICIO

Con valor `SI`, la hora, minutos y segundos originales se conservan en la fecha límite.

Ejemplo:

Inicio:

`16/07/2026 09:58:24`

La fecha límite mantendrá:

`09:58:24`

en el día contractual correspondiente.

Esto permite que el vencimiento no dependa únicamente de la fecha, sino también de la hora exacta de creación.

---

# 8. Estados del ANS

El informe genera los siguientes estados:

## VENCIDO

La fecha y hora límite ya fueron superadas.

Color:

**Rojo**

## ALERTA 0 DIAS

El pedido se encuentra en su último día disponible.

Color:

**Naranja**

## ALERTA

Ya alcanzó el porcentaje definido para iniciar la alerta.

Color:

**Amarillo**

## A TIEMPO

Todavía no alcanza el punto de inicio de alerta.

Color:

**Verde**

---

# 9. Columnas principales de control

El informe genera automáticamente:

- `DIAS_CONTRACTUALES`
- `FECHA_LIMITE_ANS`
- `DIAS_TRANSCURRIDOS`
- `DIAS_PARA_INICIAR_ALERTA`
- `DIAS_RESTANTES`
- `ESTADO`

Estas columnas son el resultado de las reglas configuradas en `FILTROS_ANS_REDES.xlsx`.

---

# 10. Dashboard ANS REDES

El dashboard permite consultar la información mediante:

- Total de pedidos.
- Vencidos.
- Alerta 0 días.
- Alerta.
- A tiempo.
- Distribución por estado.
- Gráfico de cantidad por estado.
- Tabla de detalle.

Segmentadores disponibles:

- Proceso.
- Clasificación o zona.
- Estado.
- Responsable.
- Municipio.

Al seleccionar un filtro, los KPI, gráficos y tabla de detalle se actualizan de forma sincronizada.

---

# 11. Recomendación para mantenimiento

Antes de modificar una regla:

1. Verificar que el cambio haya sido aprobado funcionalmente.
2. Modificar únicamente el Excel de configuración.
3. Guardar el archivo.
4. Cerrar Excel.
5. Generar nuevamente el informe.
6. Actualizar el dashboard.
7. Validar uno o dos casos antes de utilizar el resultado operativo.

No se recomienda eliminar reglas anteriores; cuando sea posible, es preferible utilizar `ACTIVO = NO`.

---

## Resumen para explicar en reunión

> ANS REDES fue diseñado para que las reglas funcionales no dependan del código. Los responsables, procesos, días contractuales, porcentajes de alerta y reglas de calendario se administran desde `FILTROS_ANS_REDES.xlsx`.
>
> Si cambia un responsable, se agrega o se desactiva desde Excel. Si un sábado empieza a considerarse hábil, se cambia `EXCLUIR_SABADOS` de `SI` a `NO`. Si cambia el porcentaje de alerta, se modifica el porcentaje en la tabla contractual.
>
> Al volver a generar el informe, el sistema toma automáticamente la nueva configuración, recalcula fechas límite, días transcurridos, días restantes y estado, y posteriormente el dashboard se actualiza con los nuevos resultados.
