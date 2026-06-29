# 📘 Módulo 05 - Introducción a DAX

> 📚 **Curso:** Excel BI para Analistas de Datos  
> 📖 **Módulo:** 05 - Introducción a DAX  
> 🎯 **Nivel:** Básico - Intermedio  
> ⏱️ **Duración estimada:** 50 minutos

---

# 🎯 Objetivo

Comprender qué es DAX, cómo funciona dentro del Modelo de Datos y crear las primeras medidas utilizando Power Pivot.

Al finalizar este módulo serás capaz de crear medidas básicas y entender por qué DAX es el motor analítico de Power Pivot y Power BI.

---

# 📖 ¿Qué es DAX?

**DAX** significa:

**Data Analysis Expressions**

Es el lenguaje utilizado por:

- Microsoft Power Pivot
- Microsoft Power BI
- SQL Server Analysis Services (Tabular)

Su objetivo consiste en crear cálculos sobre un Modelo de Datos.

A diferencia de Excel tradicional, DAX no trabaja únicamente sobre celdas; trabaja sobre tablas relacionadas.

---

# ¿Por qué existe DAX?

En Excel tradicional utilizamos funciones como:

- SUMA
- PROMEDIO
- CONTAR
- MAX
- MIN

Cuando los datos provienen de varias tablas relacionadas, estas funciones dejan de ser suficientes.

DAX fue creado para realizar cálculos utilizando el Modelo de Datos construido en los módulos anteriores.

---

# Conectando con el laboratorio

Nuestro modelo contiene:

- tblClientes
- tblTecnicos
- tblPedidos
- tblMateriales
- tblInstalaciones
- tblCalendario

Las medidas que construiremos utilizarán estas relaciones automáticamente.

---

# Medida vs Fórmula de Excel

En Excel escribimos:

```excel
=SUMA(D2:D100)
```

En DAX escribimos:

```DAX
Total Materiales :=
SUM(tblMateriales[Valor])
```

La diferencia es que la medida queda almacenada dentro del Modelo de Datos y puede reutilizarse en cualquier Tabla Dinámica.

---

# Anatomía de una medida

```DAX
Total Materiales :=
SUM(tblMateriales[Valor])
```

Partes de la expresión:

- **Total Materiales** → Nombre de la medida.
- **:=** → Inicio de la expresión DAX.
- **SUM** → Función.
- **tblMateriales** → Tabla.
- **Valor** → Columna.

---

# ¿Dónde se crean las medidas?

1. Abrir Power Pivot.
2. Seleccionar una tabla (por ejemplo, tblMateriales).
3. Activar el Área de Cálculo.
4. Escribir la medida en una celda del área inferior.

> **Sugerencia:** Inserta aquí una captura del Área de Cálculo de Power Pivot como Figura 5.1.

---

# Primera medida

Crear la siguiente medida:

```DAX
Total Materiales :=
SUM(tblMateriales[Valor])
```

Esta medida calcula el valor total de los materiales utilizados.

---

# Más medidas básicas

## Total Pedidos

```DAX
Total Pedidos :=
COUNT(tblPedidos[Pedido])
```

---

## Valor Promedio

```DAX
Promedio Materiales :=
AVERAGE(tblMateriales[Valor])
```

---

## Valor Máximo

```DAX
Valor Máximo :=
MAX(tblMateriales[Valor])
```

---

## Valor Mínimo

```DAX
Valor Mínimo :=
MIN(tblMateriales[Valor])
```

---

## Materiales Diferentes

```DAX
Materiales Diferentes :=
DISTINCTCOUNT(tblMateriales[Material])
```

---

# ¿Qué hace una medida?

Una medida no guarda un resultado fijo.

Cada vez que cambian los filtros de una Tabla Dinámica, Power Pivot vuelve a calcular automáticamente el resultado.

Ese comportamiento es una de las principales diferencias frente a una fórmula tradicional de Excel.

---

# Buenas prácticas

- Utilizar nombres descriptivos.
- Crear medidas reutilizables.
- Evitar duplicar cálculos.
- Mantener una nomenclatura consistente.
- Crear primero medidas simples antes de utilizar funciones avanzadas.

---

# Errores frecuentes

- Confundir una medida con una columna calculada.
- Escribir funciones de Excel dentro de DAX.
- Crear medidas sin comprender el Modelo de Datos.
- Utilizar nombres poco descriptivos.

---

# 📝 Lo que aprendí

En este módulo comprendí que DAX es el lenguaje de análisis utilizado por Power Pivot y Power BI. Aprendí que una medida es un cálculo dinámico que se evalúa según el contexto de filtros del Modelo de Datos y que puede reutilizarse en cualquier visualización.

---

# 🎯 Ejercicio

Crear las siguientes medidas:

1. Total Materiales
2. Total Pedidos
3. Promedio Materiales
4. Valor Máximo
5. Valor Mínimo
6. Materiales Diferentes

Después insertar una Tabla Dinámica y comprobar que las medidas cambian al aplicar filtros por Cliente, Técnico y Mes.

---

# 🚀 Próximo módulo

## 📘 Módulo 06 - Medidas DAX

En el siguiente módulo profundizaremos en la creación de medidas profesionales, aprenderemos el contexto de filtro, la función CALCULATE(), DIVIDE(), el uso de VAR y las mejores prácticas para construir indicadores reutilizables.
