# 📘 Módulo 06 - Medidas DAX

> 📚 **Curso:** Excel BI para Analistas de Datos  
> 📖 **Módulo:** 06 - Medidas DAX  
> 🎯 **Nivel:** Intermedio  
> ⏱️ **Duración estimada:** 60 minutos

---

# 🎯 Objetivo

Aprender a construir medidas DAX reutilizables utilizando las funciones de agregación más comunes y comprender cómo responden al contexto de filtros dentro del Modelo de Datos.

---

# 📖 Recordando el módulo anterior

En el Módulo 05 aprendimos:

- Qué es DAX.
- Cómo crear una medida.
- Dónde se almacenan las medidas.
- Cómo utilizar una medida en una Tabla Dinámica.

Ahora ampliaremos nuestro conjunto de medidas.

---

# ¿Qué es una medida?

Una medida es un cálculo dinámico que Power Pivot evalúa cada vez que cambian los filtros del informe.

Las medidas no almacenan resultados; los calculan cuando son necesarios.

---

# Laboratorio

Trabajaremos sobre la tabla **tblMateriales**.

---

# Medida 1 - Total Materiales

```DAX
Total Materiales :=
SUM ( tblMateriales[Valor] )
```

---

# Medida 2 - Total Pedidos

```DAX
Total Pedidos :=
COUNT ( tblPedidos[Pedido] )
```

---

# Medida 3 - Promedio Materiales

```DAX
Promedio Materiales :=
AVERAGE ( tblMateriales[Valor] )
```

---

# Medida 4 - Valor Máximo

```DAX
Valor Máximo :=
MAX ( tblMateriales[Valor] )
```

---

# Medida 5 - Valor Mínimo

```DAX
Valor Mínimo :=
MIN ( tblMateriales[Valor] )
```

---

# Medida 6 - Materiales Diferentes

```DAX
Materiales Diferentes :=
DISTINCTCOUNT ( tblMateriales[Material] )
```

---

# Probando las medidas

Crear una Tabla Dinámica basada en el Modelo de Datos.

Agregar como filas:

- Material

Agregar como valores:

- Total Materiales
- Promedio Materiales
- Valor Máximo
- Valor Mínimo

---

# 🛠 Administrando las medidas DAX

Después de crear varias medidas es recomendable administrarlas desde Power Pivot.

Ir a:

```text
Power Pivot
      ↓
Medidas
      ↓
Administrar medidas
```
---

# Contexto de filtro

Cambiar las filas por:

- Cliente
- Técnico
- Mes

Observar que las medidas cambian automáticamente sin modificar la fórmula.

---

# ¿Qué es el contexto de filtro?

El contexto de filtro es el conjunto de campos o filtros que determinan cómo se calcula una medida. La medida no cambia; lo que cambia es la forma en que se analiza la información.

Cuando creamos una medida, la fórmula siempre permanece igual.

Lo que cambia es la forma en que queremos analizar la información.

Por ejemplo, tenemos la siguiente medida:

Total Materiales :=
SUM ( tblMateriales[Valor] )

Ahora imaginemos que en una Tabla Dinámica analizamos esa medida de diferentes maneras.

Primer análisis

Colocamos el campo:

Cliente

La Tabla Dinámica nos mostrará el Total de Materiales por Cliente.

Segundo análisis

Sin cambiar la medida, quitamos Cliente y colocamos:

Técnico

Ahora la Tabla Dinámica mostrará el Total de Materiales por Técnico.

¿Qué cambió?

La medida sigue siendo exactamente la misma.

Total Materiales :=
SUM ( tblMateriales[Valor] )

Lo único que cambió fue el campo utilizado para analizar la información.

Ese cambio recibe un nombre

En DAX, el campo o conjunto de filtros que utilizamos para analizar la información se llama contexto de filtro.

Es decir, el contexto de filtro define sobre qué grupo de datos se va a realizar el cálculo.

## En palabras sencillas

El contexto de filtro es la forma en que decides ver la información.

Puedes ver el mismo dato:

Por Cliente.
Por Técnico.
Por Ciudad.
Por Mes.
Por Año.

La medida no cambia.

Lo único que cambia es el grupo de datos que Power Pivot utiliza para realizar el cálculo.
---

## ¿Cómo se crea un contexto de filtro?

El contexto de filtro puede generarse mediante:

- Los campos ubicados en las Filas de una Tabla Dinámica.
- Los campos ubicados en las Columnas.
- Los filtros del informe.
- Los segmentadores de datos.
- Las cronologías.
- Las relaciones del Modelo de Datos.

Todos estos elementos modifican automáticamente el resultado de una medida.

---

## Ejemplo práctico

Supongamos que tenemos la siguiente medida:

```DAX
Total Materiales :=
SUM ( tblMateriales[Valor] )
```

Si construimos una Tabla Dinámica con:

Filas:

- Cliente

Valores:

- Total Materiales

Obtendremos un total diferente para cada cliente.

La medida es exactamente la misma.

Lo único que cambia es el filtro aplicado por la Tabla Dinámica.

---

## Cambiando el contexto

Ahora quitamos el campo **Cliente** y colocamos:

- Técnico

La medida sigue siendo:

```DAX
Total Materiales :=
SUM ( tblMateriales[Valor] )
```

Sin embargo, el resultado cambia.

¿Por qué?

Porque ahora Power Pivot está calculando el total para cada técnico y no para cada cliente.

La fórmula nunca cambió.

El contexto de filtro sí cambió.

---

## Otro ejemplo

Ahora quitamos **Técnico** y colocamos:

- Mes

Obtendremos nuevamente resultados diferentes.

La medida continúa siendo exactamente la misma.

Esto demuestra que una medida DAX no almacena un valor fijo.

Siempre responde al contexto de análisis.

---

## Ejemplos de elementos que crean contexto de filtro

En Power Pivot el contexto puede cambiar mediante:

- Cliente
- Técnico
- Ciudad
- Zona
- Segmento
- Tipo de Servicio
- Material
- Estado
- Fecha
- Mes
- Año
- Trimestre
- Segmentadores
- Cronologías
- Filtros del informe

Todos estos elementos afectan automáticamente el resultado de las medidas.

---

## ¿Qué ocurre internamente?

Cuando cambiamos un campo en una Tabla Dinámica, Power Pivot utiliza las relaciones del Modelo de Datos para determinar qué registros deben participar en el cálculo.

No modifica la fórmula.

No copia datos.

Simplemente cambia el conjunto de registros que serán evaluados por la medida.

---

## ¿Por qué es tan importante comprender este concepto?

El contexto de filtro es uno de los pilares de DAX.

Funciones como:

- CALCULATE()
- FILTER()
- ALL()
- ALLEXCEPT()
- REMOVEFILTERS()

trabajan modificando el contexto de filtro.

Por esta razón, comprender este concepto facilitará el aprendizaje de las funciones avanzadas que veremos en los siguientes módulos.


# Buenas prácticas

- Crear medidas reutilizables.
- Nombrarlas correctamente.
- Validarlas con diferentes filtros.
- Evitar duplicar cálculos.

---

# Errores frecuentes

- Confundir medidas con columnas calculadas.
- Utilizar SUM cuando se necesita COUNT.
- No validar los resultados.

---

# 📝 Lo que aprendí

Ahora puedo construir medidas reutilizables utilizando las funciones básicas de agregación y comprendo que una misma medida cambia automáticamente según el contexto de filtros del Modelo de Datos.

---

# 🎯 Ejercicio

1. Crear las seis medidas.
2. Construir una Tabla Dinámica.
3. Analizar por Material, Cliente, Técnico y Mes.
4. Agregar un segmentador por Ciudad y observar el comportamiento.

---

# 🚀 Próximo módulo

## 📘 Módulo 07 - Columnas Calculadas

Aprenderemos cuándo utilizar una columna calculada y cuándo utilizar una medida DAX.
