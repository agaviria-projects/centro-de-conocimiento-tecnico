# Tablas Profesionales

---

# Objetivo

Las tablas son el componente encargado de mostrar el detalle de la información utilizada por el Dashboard.

Mientras los KPIs resumen la información y los gráficos muestran tendencias, las tablas permiten validar cada registro que compone los indicadores.

Dentro del Framework ELITE, todas las tablas deberán construirse utilizando AgGrid para ofrecer una experiencia profesional de consulta.

---

# Arquitectura

```

Base de Datos

↓

DataFrame

↓

Limpieza

↓

Transformación

↓

Tabla Profesional (AgGrid)

↓

Usuario

```

---

# Características del Framework

Todas las tablas deberán cumplir como mínimo las siguientes características.

✔ Encabezados claros

✔ Ordenamiento

✔ Filtros por columna

✔ Scroll vertical

✔ Scroll horizontal

✔ Columnas redimensionables

✔ Selección de texto

✔ Paginación

✔ Responsive

✔ Alto rendimiento

---

# Anatomía de una Tabla

```

┌──────────────────────────────────────────────────────────────┐

ENCABEZADOS

──────────────────────────────────────────────────────────────

FILTROS

──────────────────────────────────────────────────────────────

REGISTROS

──────────────────────────────────────────────

PAGINACIÓN

└──────────────────────────────────────────────────────────────┘

```

---

# Componentes

## Encabezado

Contiene el nombre de cada columna.

Debe utilizar tipografía en negrilla.

Debe permanecer visible durante el desplazamiento.

---

## Filtros

Cada columna debe permitir realizar búsquedas independientes.

Ejemplos

- Zona

- Mes

- Placa

- Fecha

- Ciudad

- Técnico

---

## Datos

Representan la información proveniente del DataFrame.

Nunca deben modificarse directamente desde la tabla, salvo que el proyecto lo requiera.

---

## Scroll

Las tablas deben permitir recorrer grandes volúmenes de información sin afectar el rendimiento del Dashboard.

---

## Paginación

Cuando existan miles de registros se recomienda mostrar entre:

20

30

50

registros por página.

---

# Flujo de funcionamiento

```

DataFrame

↓

AgGrid

↓

Filtros

↓

Ordenamiento

↓

Visualización

```

---

# Buenas prácticas

✔ Ordenar automáticamente las columnas.

✔ Mantener el mismo ancho visual.

✔ Mostrar números alineados a la derecha.

✔ Mostrar texto alineado a la izquierda.

✔ Formatear monedas.

✔ Formatear porcentajes.

✔ Formatear fechas.

✔ Evitar columnas innecesarias.

✔ Congelar columnas importantes cuando sea necesario.

---

# Casos Empresariales

## Dashboard Financiero

Detalle de ventas.

---

## Dashboard Logístico

Detalle de vehículos.

---

## Dashboard ANS

Detalle de pedidos.

---

## Dashboard Inventarios

Detalle de materiales.

---

## Dashboard Producción

Detalle de actividades.

---

# Relación con otros componentes

Las tablas siempre trabajan junto con:

• Filtros

↓

• KPIs

↓

• Gráficos

↓

• Exportaciones

---

# Reglas del Framework

Toda tabla deberá:

□ Utilizar AgGrid.

□ Permitir filtros.

□ Permitir ordenamiento.

□ Mantener formato corporativo.

□ Ser consistente con el resto del Dashboard.

□ Mostrar únicamente la información necesaria.

□ Responder a los filtros del Dashboard.

---

# Plantilla Oficial

Antes de desarrollar una nueva tabla responder:

| Campo | Descripción |
|--------|-------------|
| Nombre | Nombre de la tabla |
| Objetivo | ¿Qué información muestra? |
| DataFrame | Fuente de datos |
| Columnas | Campos visibles |
| Columnas ocultas | Campos internos |
| Filtros | Columnas filtrables |
| Orden inicial | Columna principal |
| Formatos | Fecha, moneda, porcentaje, texto |
| Paginación | Registros por página |
| Exportación | Sí / No |

---

# Conclusión

Las tablas representan la evidencia del Dashboard.

Todo KPI y todo gráfico debe poder verificarse consultando el detalle mostrado en la tabla correspondiente, garantizando la trazabilidad y la confiabilidad de la información presentada.
