# 📘 PARTE II - Casos Reales de Desarrollo en Excel BI

> 📚 Curso: Excel BI para Analistas de Datos  
> 📖 Módulo 10 - Casos Reales y Lecciones Aprendidas  
> 🎯 Sección: Casos 11 al 20

---

# Introducción

Después de comprender los fundamentos de Power Query, Power Pivot, DAX y el Modelo de Datos, es momento de conocer situaciones reales que suelen aparecer durante el desarrollo de proyectos empresariales.

Los siguientes casos no corresponden a teoría.

Son problemas reales que cualquier Analista BI puede enfrentar durante la construcción de Tablas Dinámicas, Dashboards y Modelos de Datos.

El objetivo consiste en reconocer rápidamente el problema, comprender su causa y conocer la solución recomendada.

---

# 🏢 Caso Real #11

## ¿Por qué una Tabla Dinámica no mostraba todas las tablas del Modelo de Datos?

### Situación

Después de crear el Modelo de Datos, algunas tablas no aparecían disponibles dentro de la lista de campos de la Tabla Dinámica.

### Causa

La Tabla Dinámica fue creada utilizando únicamente una tabla de Excel y no el Modelo de Datos.

### Solución

Crear nuevamente la Tabla Dinámica seleccionando:

**Insertar → Tabla Dinámica → Usar este libro de datos (Modelo de Datos).**

### Lección Aprendida

El origen de la Tabla Dinámica determina si podrá utilizar todo el Modelo de Datos.

---

# 🏢 Caso Real #12

## ¿Por qué una medida apareció en otra tabla dentro de Power Pivot?

### Situación

Una medida fue creada en tblMateriales, pero posteriormente apareció ubicada en otra tabla.

### Causa

Las medidas pertenecen al Modelo de Datos y Power Pivot permite administrarlas desde diferentes tablas.

### Solución

Organizar las medidas utilizando una tabla específica o mantenerlas agrupadas según el tema del proyecto.

### Lección Aprendida

La ubicación visual de una medida no afecta su funcionamiento.

---

# 🏢 Caso Real #13

## ¿Por qué no podía calcular el promedio utilizando un Campo Calculado?

### Situación

Era necesario calcular un promedio dentro de una Tabla Dinámica.

La opción Campo Calculado no estaba disponible.

### Causa

La Tabla Dinámica utilizaba el Modelo de Datos.

### Solución

Crear una Medida DAX en Power Pivot.

### Lección Aprendida

Las Tablas Dinámicas basadas en el Modelo de Datos utilizan Medidas DAX en lugar de Campos Calculados.

---

# 🏢 Caso Real #14

## ¿Por qué el Dashboard quedó desordenado?

### Situación

Se intentó construir todo directamente sobre la hoja del Dashboard.

### Causa

Las Tablas Dinámicas, gráficos y Segmentadores ocupaban el mismo espacio.

### Solución

Separar el proyecto en dos hojas:

- Pivots
- Dashboard

### Lección Aprendida

Separar la lógica del Dashboard mejora el mantenimiento del proyecto.

---

# 🏢 Caso Real #15

## ¿Por qué una relación producía resultados incorrectos?

### Situación

Las medidas mostraban valores inesperados.

### Causa

La relación utilizaba una llave incorrecta o la cardinalidad no representaba el negocio.

### Solución

Validar las llaves primarias, las llaves foráneas y la relación 1:N.

### Lección Aprendida

Una medida correcta no puede compensar un Modelo de Datos mal diseñado.

---

# 🏢 Caso Real #16

## ¿Por qué una medida cambiaba al utilizar un Segmentador?

### Situación

La fórmula nunca cambió.

El resultado sí.

### Causa

El Segmentador modificó el Contexto de Filtro.

### Solución

Comprender que la medida permanece igual.

Lo que cambia son los registros utilizados para el cálculo.

### Lección Aprendida

El Contexto de Filtro es uno de los conceptos más importantes de DAX.

---

# 🏢 Caso Real #17

## ¿Por qué la Tabla Dinámica mostraba datos duplicados?

### Situación

Los totales parecían mayores a los esperados.

### Causa

Existían registros duplicados o relaciones incorrectas.

### Solución

Revisar:

- Datos de origen.
- Relaciones.
- Llaves.
- Duplicados.

### Lección Aprendida

Antes de modificar una medida, valida siempre la calidad de los datos.

---

# 🏢 Caso Real #18

## ¿Cómo validar que una medida DAX está correcta?

### Situación

La medida devolvía un resultado diferente al esperado.

### Causa

No existía un proceso de validación.

### Solución

Comparar el resultado utilizando:

- Tabla Dinámica.
- Totales manuales.
- Filtros.
- Diferentes contextos de análisis.

### Lección Aprendida

Toda medida debe validarse antes de utilizarse en un Dashboard.

---

# 🏢 Caso Real #19

## ¿Por qué el Dashboard no respondía a todos los Segmentadores?

### Situación

Algunos gráficos cambiaban.

Otros permanecían iguales.

### Causa

Los Segmentadores no estaban conectados a todas las Tablas Dinámicas.

### Solución

Utilizar:

**Conexiones de informe**

y vincular cada Segmentador con todas las Tablas Dinámicas correspondientes.

### Lección Aprendida

Todos los componentes del Dashboard deben compartir las mismas conexiones.

---

# 🏢 Caso Real #20

## ¿Cómo validar un Dashboard antes de entregarlo?

### Lista de verificación

Antes de presentar un Dashboard profesional verifica:

✔ Relaciones correctas.

✔ Modelo de Datos actualizado.

✔ Medidas DAX validadas.

✔ Tablas Dinámicas actualizadas.

✔ Segmentadores funcionando.

✔ Cronología conectada.

✔ KPIs consistentes.

✔ Gráficos correctamente titulados.

✔ Dashboard limpio.

✔ Hoja Pivots oculta (si aplica).

### Lección Aprendida

Un Dashboard no termina cuando se construye.

Termina cuando ha sido validado completamente.

---

# 🎯 Conclusión

Estos diez casos representan situaciones comunes durante el desarrollo de soluciones con Excel BI.

En la mayoría de ocasiones el problema no está en Excel.

Está en:

- La calidad de los datos.
- El Modelo de Datos.
- Las relaciones.
- El Contexto de Filtro.
- La organización del proyecto.

Comprender estas situaciones permite reducir tiempos de desarrollo, evitar errores frecuentes y construir soluciones más robustas.

---

