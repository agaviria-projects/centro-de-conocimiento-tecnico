# 📘 Módulo 07 - Columnas Calculadas

> 📚 **Curso:** Excel BI para Analistas de Datos  
> 📖 **Módulo:** 07 - Columnas Calculadas  
> 🎯 **Nivel:** Intermedio  
> ⏱️ **Duración estimada:** 60 minutos

---

# 🎯 Objetivo

Comprender qué es una columna calculada, cuándo utilizarla y en qué se diferencia de una medida DAX.

Al finalizar este módulo podrás decidir correctamente cuándo crear una medida y cuándo crear una columna calculada.

---

# 📖 Recordando el módulo anterior

En el Módulo 06 aprendimos a crear medidas DAX que responden automáticamente al contexto de filtros.

Ahora conoceremos otro tipo de cálculo disponible en Power Pivot: las columnas calculadas.

---

# ¿Qué es una columna calculada?

Una columna calculada es una nueva columna que se agrega a una tabla del Modelo de Datos.

Su valor se calcula para **cada fila** y queda almacenado en el modelo.

A diferencia de una medida, no cambia cuando se modifican los filtros de una Tabla Dinámica.

---

# Medida vs Columna Calculada

| Medida DAX | Columna Calculada |
|------------|-------------------|
| Se calcula cuando consultas el modelo. | Se calcula al actualizar el Modelo de Datos. |
| Depende del contexto de filtro. | Tiene un valor fijo por fila. |
| Se utiliza principalmente en Valores. | Puede utilizarse en Filas, Columnas, Filtros y Segmentadores. |
| No crea una nueva columna física. | Agrega una nueva columna al modelo. |

---

# ¿Cuándo utilizar una columna calculada?

Utilízala cuando necesites:

- Combinar columnas.
- Clasificar información.
- Crear categorías.
- Obtener un valor fila por fila.
- Preparar datos para análisis posteriores.

---

# 🧪 Laboratorio

En este laboratorio aprenderemos a crear nuestra primera **Columna Calculada** dentro de Power Pivot.

Trabajaremos sobre la tabla **tblMateriales**.

---

## Paso 1

Abrir la tabla **tblMateriales** en Power Pivot.

---

## Paso 2

Desplazarse hasta la primera columna vacía que aparece con el nombre:

```text
Agregar columna
```

Seleccionarla.

---

## Paso 3

En la barra de fórmulas (Fx) escribir la siguiente expresión:

```DAX
Valor Total :=
tblMateriales[Cantidad] * tblMateriales[Valor]
```

> **Nota:** Al crear una columna calculada en Power Pivot es habitual escribir primero el nombre de la columna seguido de :=, por ejemplo:

Valor Total :=
tblMateriales[Cantidad] * tblMateriales[Valor]

---

## Paso 4

Presionar **Enter**.

Power Pivot creará automáticamente una nueva columna llamada **Valor Total**.

Cada fila mostrará el resultado de multiplicar la cantidad del material por su valor unitario.

Por ejemplo:

| Material | Cantidad | Valor | Valor Total |
|----------|---------:|------:|------------:|
| Cable UTP | 1 | 25.000 | 25.000 |
| Router | 2 | 50.000 | 100.000 |
| Conector | 3 | 75.000 | 225.000 |
| ONT | 4 | 100.000 | 400.000 |

---

# Diferencia práctica

## Medida

```DAX
Total Materiales :=
SUM ( tblMateriales[Valor] )
```

Devuelve un único resultado dependiendo de los filtros.

## Columna Calculada

```DAX
Valor Total :=
tblMateriales[Cantidad] * tblMateriales[Valor]
```

Genera un resultado para cada fila de la tabla.

---

# ¿Qué ocurre al actualizar los datos?

Cuando se actualiza el Modelo de Datos:

- Las columnas calculadas se recalculan completamente.
- Las medidas no almacenan resultados; se calculan únicamente cuando son consultadas.

---

# Buenas prácticas

- Crear columnas calculadas solo cuando realmente sean necesarias.
- Evitar duplicar información ya existente.
- Preferir medidas cuando el cálculo dependa del análisis.
- Utilizar nombres claros y descriptivos.

---

# Errores frecuentes

- Crear una columna calculada cuando bastaba con una medida.
- Esperar que una columna calculada cambie con los filtros.
- Crear demasiadas columnas aumentando el tamaño del modelo.

---

# 📝 Lo que aprendí

Ahora comprendo que una medida y una columna calculada tienen propósitos diferentes. Una medida responde al contexto de análisis, mientras que una columna calculada genera un valor permanente para cada fila del Modelo de Datos.

---

# 🎯 Ejercicio

1. Crear la columna **Valor Total**.
2. Insertarla en una Tabla Dinámica.
3. Comparar su comportamiento con la medida **Total Materiales**.
4. Explicar cuál utilizarías para calcular el valor por fila y cuál para obtener el total general.

---

# 🚀 Próximo módulo

## 📘 Módulo 08 - Tablas Dinámicas con Power Pivot

Aprenderemos a construir informes profesionales utilizando el Modelo de Datos, medidas DAX, columnas calculadas, segmentadores y cronologías.
