
# 📘 Módulo 05 - Introducción a DAX

> 📚 **Curso:** Excel BI para Analistas de Datos  
> 📖 **Módulo:** 05 - Introducción a DAX  
> 🎯 **Nivel:** Básico - Intermedio  
> ⏱️ **Duración estimada:** 55 minutos

---

# 🎯 Objetivo

Comprender qué es DAX, cómo funciona dentro del Modelo de Datos y crear la primera medida del laboratorio utilizando Power Pivot.

Al finalizar este módulo comprenderás por qué las medidas son el núcleo del análisis en Power Pivot y Power BI.

---

# 📖 ¿Qué es DAX?

**DAX** significa **Data Analysis Expressions**.

Es el lenguaje de fórmulas utilizado por:

- Microsoft Power Pivot
- Microsoft Power BI
- SQL Server Analysis Services (Tabular)

Su finalidad es crear cálculos dinámicos sobre un Modelo de Datos.

A diferencia de Excel tradicional, DAX no trabaja únicamente sobre celdas, sino sobre tablas relacionadas.

---

# ¿Por qué existe DAX?

En Excel solemos utilizar funciones como:

- SUMA
- PROMEDIO
- CONTAR
- MAX
- MIN

Cuando la información proviene de varias tablas relacionadas, estas funciones ya no son suficientes.

DAX aprovecha el Modelo de Datos construido en los módulos anteriores para realizar cálculos inteligentes.

---

# Conectando con el laboratorio

Nuestro modelo contiene:

- tblClientes
- tblTecnicos
- tblPedidos
- tblMateriales
- tblInstalaciones
- tblCalendario

Las relaciones creadas en el Módulo 4 serán utilizadas automáticamente por las medidas DAX.

---

# Medida vs Fórmula de Excel

En Excel escribimos:

```excel
=SUMA(D2:D100)
```

En DAX escribimos:

```DAX
Total Materiales :=
SUM ( tblMateriales[Valor] )
```

Una fórmula pertenece a una celda.

Una medida pertenece al Modelo de Datos.

---

# Anatomía de una medida

```DAX
Total Materiales :=
SUM ( tblMateriales[Valor] )
```

Cada parte tiene un significado:

- **Total Materiales** → Nombre de la medida.
- **:=** → Inicio de la expresión DAX.
- **SUM** → Función.
- **tblMateriales** → Tabla.
- **Valor** → Columna.

---

# ¿Dónde se crean las medidas?

1. Abrir Power Pivot.
2. Seleccionar la tabla **tblMateriales**.
3. Mostrar el **Área de Cálculo**.
4. Escribir la medida.

---

# Primera medida

Crear la siguiente medida:

```DAX
Total Materiales :=
SUM ( tblMateriales[Valor] )
```

Esta medida calcula el valor total de los materiales utilizados en el laboratorio.

---

# ¿Dónde se utiliza una medida?

Una medida cobra verdadero sentido cuando se utiliza en una Tabla Dinámica.

## Crear una Tabla Dinámica

Ir a:

```text
Power Pivot
      ↓
Tabla Dinámica
      ↓
Nueva Hoja
```

o

```text
Insertar
      ↓
Tabla Dinámica
      ↓
Usar este Modelo de Datos
```

---

# Primer análisis

Arrastrar:

**Filas**

- Material

**Valores**

- Total Materiales

Observa cómo la medida calcula automáticamente el total para cada material.

---

# Cambiando la dimensión

Ahora reemplaza **Material** por:

- Cliente
- Técnico
- Mes

La medida **no cambia**.

Lo único que cambia es la forma de analizar la información.

---

# ¿Qué acaba de ocurrir?

Power Pivot utiliza las relaciones del Modelo de Datos para recalcular automáticamente la medida según el contexto de análisis.

No fue necesario modificar la fórmula.

Esta es una de las principales ventajas de DAX frente a una fórmula tradicional de Excel.

---

# ¿Qué hace una medida?

Una medida:

- No almacena un valor fijo.
- Se recalcula automáticamente.
- Responde a filtros y segmentaciones.
- Puede reutilizarse en múltiples Tablas Dinámicas.

---

# Buenas prácticas

- Utilizar nombres descriptivos.
- Crear primero medidas sencillas.
- Mantener una nomenclatura consistente.
- Aprovechar el Modelo de Datos antes de escribir fórmulas complejas.

---

# Errores frecuentes

- Confundir una medida con una columna calculada.
- Escribir funciones de Excel en lugar de funciones DAX.
- Crear medidas sin comprender las relaciones del modelo.
- Intentar resolver todo con una única fórmula.

---

# 📝 Lo que aprendí

En este módulo comprendí que DAX es el lenguaje de análisis utilizado por Power Pivot y Power BI. Aprendí a crear mi primera medida, a almacenarla en el Modelo de Datos y a utilizarla dentro de una Tabla Dinámica. También observé que una misma medida puede analizar diferentes dimensiones gracias a las relaciones del modelo.

---

# 🎯 Ejercicio

## Ejercicio 1

Crear la medida:

```DAX
Total Materiales :=
SUM ( tblMateriales[Valor] )
```

## Ejercicio 2

Crear una Tabla Dinámica utilizando el Modelo de Datos.

## Ejercicio 3

Mostrar el valor de la medida por:

- Material
- Cliente
- Técnico
- Mes

## Ejercicio 4

Responder:

1. ¿Por qué no fue necesario modificar la medida al cambiar las filas?
2. ¿Qué papel desempeñan las relaciones del Modelo de Datos?
3. ¿Cuál es la diferencia entre una fórmula de Excel y una medida DAX?

---

# 🚀 Próximo módulo

## 📘 Módulo 06 - Medidas DAX

En el siguiente módulo aprenderemos las funciones de agregación más utilizadas:

- SUM
- COUNT
- AVERAGE
- MIN
- MAX
- DISTINCTCOUNT

y construiremos indicadores reutilizables para comenzar a desarrollar análisis profesionales.
