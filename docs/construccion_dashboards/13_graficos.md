# Capítulo 13 - Gráficos Profesionales

---

# Objetivo

Los gráficos representan visualmente la información calculada mediante los KPIs.

Su propósito es facilitar la identificación de tendencias, comparaciones, distribuciones y comportamientos del negocio, permitiendo que el usuario interprete rápidamente los datos sin necesidad de revisar tablas detalladas.

Dentro del Framework ELITE, todos los gráficos deberán construirse siguiendo criterios de claridad, consistencia visual y rendimiento.

---

# Arquitectura

```

Fuente de Datos

↓

DataFrame

↓

Transformación

↓

KPIs

↓

Gráfico

↓

Dashboard

```

---

# Principios del Framework

Todo gráfico debe responder una pregunta del negocio.

No debe construirse únicamente por razones estéticas.

Antes de agregar un gráfico al Dashboard se debe responder:

- ¿Qué información deseo comunicar?
- ¿Qué decisión ayudará a tomar?
- ¿Existe una forma más simple de mostrarla?

---

# Flujo General

```

Datos

↓

Agrupación

↓

Cálculos

↓

Indicadores

↓

Gráfico

↓

Interpretación

```

---

# Tipos de gráficos soportados

| Tipo | Objetivo |
|-------|----------|
| Barras | Comparar categorías |
| Líneas | Mostrar tendencias |
| Áreas | Evolución acumulada |
| Dona | Participación porcentual |
| Dispersión | Relación entre variables |
| Heatmap | Concentración |
| Treemap | Jerarquías |
| Gauge | Cumplimiento |
| Mapa | Distribución geográfica |

---

# Reglas Visuales

✔ Títulos claros.

✔ Mostrar unidades.

✔ Colores corporativos.

✔ Leyendas visibles.

✔ Escalas correctas.

✔ Evitar saturación de información.

✔ Mantener el mismo estilo en todo el Dashboard.

---

# Estructura de un gráfico

Todo gráfico del Framework deberá estar compuesto por:

Título

↓

Subtítulo (opcional)

↓

Gráfico

↓

Leyenda

↓

Fuente de datos (opcional)

---

# Plantilla Oficial

Todo gráfico deberá documentarse utilizando la siguiente estructura.

| Campo | Descripción |
|--------|-------------|
| Nombre | Nombre del gráfico |
| Objetivo | ¿Qué comunica? |
| Pregunta de negocio | ¿Qué responde? |
| Tipo | Barras, Líneas, Dona... |
| Fuente de datos | DataFrame utilizado |
| Columnas | Campos utilizados |
| Agrupación | groupby() aplicado |
| KPI relacionado | Indicador asociado |
| Librería | Plotly |
| Función | px.bar(), px.line(), etc. |
| Colores | Paleta utilizada |
| Interacción | Hover, Zoom, Leyenda |
| Resultado esperado | Descripción |

---

# Componentes del Capítulo

13.1 Barras

13.2 Líneas

13.3 Áreas

13.4 Dona

13.5 Dispersión

13.6 Heatmap

13.7 Gauge

13.8 Treemap

13.9 Mapas

13.10 Buenas Prácticas

# 13.1 - Barras

---

## Objetivo

Comparar valores entre categorías.

---

## ¿Cuándo utilizarlo?

✔ Comparaciones.

✔ Rankings.

✔ Top N.

✔ Bottom N.

---

## Casos Empresariales

- Ventas por ciudad.

- Horas extras por vehículo.

- Pedidos por técnico.

- Costos por regional.

---

## Función Plotly

```python
px.bar()
```

---

## Buenas prácticas

✔ Ordenar de mayor a menor.

✔ Etiquetas visibles.

✔ Pocos colores.

✔ Evitar demasiadas categorías.

# 13.2 - Líneas

---

## Objetivo

Mostrar tendencias en el tiempo.

---

## Casos

- Ventas mensuales.

- Producción diaria.

- Cumplimiento ANS.

---

## Función

```python
px.line()
```

---

## Buenas prácticas

✔ Orden cronológico.

✔ Marcadores.

✔ Máximo pocas series simultáneas.

# 13.3 - Áreas

---

## Objetivo

Mostrar crecimiento acumulado.

---

## Casos

- Producción.

- Ventas.

- Inventarios.

---

## Función

```python
px.area()
```

---

## Recomendaciones

Utilizar únicamente cuando interese visualizar acumulados.

# 13.4 - Dona

---

## Objetivo

Representar participación porcentual.

---

## Casos

- Regionales.

- Actividades.

- Tipos de servicio.

---

## Función

```python
px.pie(hole=.5)
```

---

## Buenas prácticas

Máximo seis categorías.

# 13.5 - Scatter

---

## Objetivo

Analizar relaciones entre variables.

---

## Casos

- Tiempo vs Costo.

- Distancia vs Consumo.

- Horas vs Producción.

---

## Función

```python
px.scatter()
```

# 13.6 - Heatmap

---

## Objetivo

Detectar patrones.

---

## Casos

- ANS.

- Producción.

- Cumplimiento.

---

## Función

```python
px.imshow()
```

# 13.7 - Gauge

---

## Objetivo

Mostrar cumplimiento de metas.

---

## Casos

- Nivel de servicio.

- Cumplimiento ANS.

- Productividad.

# 13.8 - Treemap

---

## Objetivo

Visualizar jerarquías.

---

## Casos

- Ventas.

- Inventario.

- Costos.

# 13.9 - Mapas

---

## Objetivo

Mostrar información geográfica.

---

## Casos

- Vehículos.

- Pedidos.

- Cobertura.

- Técnicos.

# 13.10 - Buenas Prácticas

---

## Checklist

□ Título claro.

□ Escala correcta.

□ Colores corporativos.

□ Leyenda.

□ Etiquetas.

□ Responsive.

□ Compatible con filtros.

□ Compatible con KPIs.

□ Compatible con el tema del Dashboard.

---

# Filosofía del Framework

Un gráfico debe simplificar la interpretación de los datos.

Si un usuario necesita explicar el gráfico para entenderlo, probablemente el diseño pueda simplificarse.

La prioridad siempre será comunicar información útil antes que incorporar efectos visuales.
