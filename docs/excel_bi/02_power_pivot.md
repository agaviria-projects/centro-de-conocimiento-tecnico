# 📘 Módulo 02 - ¿Qué es Power Pivot?

> 📚 **Curso:** Excel BI para Analistas de Datos  
> 📖 **Módulo:** 02 - Power Pivot  
> 🎯 **Nivel:** Básico  
> ⏱️ **Duración estimada:** 20 minutos

---

# 🎯 Objetivo

Comprender qué es Power Pivot, por qué fue creado y qué problemas resuelve dentro de Excel.

Al finalizar este módulo podrás diferenciar claramente cuándo utilizar Power Query y cuándo utilizar Power Pivot.

---

# 🤔 Antes de Power Pivot...

Durante muchos años Excel funcionó muy bien para trabajar con una sola tabla.

Por ejemplo:

- Ventas
- Inventario
- Empleados

Cada archivo contenía toda la información necesaria.

Las Tablas Dinámicas funcionaban perfectamente.

---

# 😓 ¿Qué empezó a ocurrir?

Con el paso del tiempo las empresas comenzaron a manejar mucha más información.

Por ejemplo:

## Clientes

| Id | Nombre |
|----|---------|
|1|Juan|
|2|María|

---

## Ventas

| Id Venta | Cliente | Valor |
|----------|----------|-------|
|100|1|250000|
|101|2|80000|

---

## Productos

| Id Producto | Nombre |
|-------------|---------|
|10|Router|
|20|Módem|

---

Ahora la información ya no estaba en una sola tabla.

Estaba distribuida en varias tablas relacionadas.

---

# 😓 El problema

Los usuarios comenzaron a utilizar:

- BUSCARV
- INDICE
- COINCIDIR
- SUMAR.SI
- CONTAR.SI

Una y otra vez.

Los archivos crecían.

Las fórmulas eran difíciles de mantener.

El rendimiento disminuía.

---

# 💡 Aquí aparece Power Pivot

Microsoft creó Power Pivot para permitir que Excel trabajara como una base de datos relacional.

En lugar de unir toda la información mediante fórmulas, ahora las tablas pueden relacionarse entre sí.

---

# 📊 Antes

```text
Clientes

↓

BUSCARV

↓

Ventas

↓

BUSCARV

↓

Productos

↓

BUSCARV

↓

Inventario
```

Muchísimas fórmulas.

Muchos errores.

---

# 🚀 Ahora

```text
Clientes
      │
      │
Ventas │ Productos
      │
      │
Inventario
```

Las tablas quedan relacionadas dentro de un Modelo de Datos.

---

# 📦 ¿Qué hace realmente Power Pivot?

Power Pivot permite:

- Crear Modelos de Datos.
- Relacionar tablas.
- Crear Medidas.
- Utilizar DAX.
- Analizar millones de registros.
- Construir indicadores avanzados.

---

# ❌ ¿Qué NO hace Power Pivot?

Power Pivot NO sirve para:

- Limpiar datos.
- Eliminar columnas.
- Cambiar formatos.
- Importar archivos.
- Corregir errores de origen.

Todo eso corresponde a Power Query.

---

# 🏢 Caso empresarial

Supongamos que tenemos dos archivos:

## DRACO

| Pedido | Técnico | Material |
|---------|----------|-----------|

## Interventoría

| Pedido | Acta | Zona |
|---------|-------|------|

Muchos usuarios usarían BUSCARV para traer el Acta.

Con Power Pivot simplemente relacionamos ambas tablas por el campo **Pedido**.

A partir de ese momento cualquier Tabla Dinámica puede utilizar información de las dos tablas al mismo tiempo.

---

# 💼 Buenas prácticas

✅ Utilizar Power Query para transformar datos.

✅ Utilizar Power Pivot para relacionar tablas.

✅ Evitar BUSCARV cuando ya existe un Modelo de Datos.

---

# ⚠️ Errores frecuentes

❌ Pensar que Power Query reemplaza Power Pivot.

❌ Pensar que Power Pivot limpia datos.

❌ Utilizar BUSCARV para todo.

---

# 🧠 Lo que debes recordar

Si necesitas...

✅ Limpiar datos → Power Query

✅ Relacionar tablas → Power Pivot

✅ Crear indicadores → DAX

✅ Visualizar resultados → Tabla Dinámica

---

# 📝 Resumen

Power Pivot fue creado para permitir que Excel trabajara con múltiples tablas relacionadas, reduciendo el uso excesivo de fórmulas como BUSCARV y facilitando el análisis de grandes volúmenes de información.

---

# 🚀 Próximo módulo

## 📘 Módulo 03 - Modelo de Datos

Aprenderemos qué es un Modelo de Datos y por qué es el corazón de Power Pivot.