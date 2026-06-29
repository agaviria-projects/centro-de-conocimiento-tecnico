# 📘 Glosario de Business Intelligence con Excel

> 📚 Curso: Excel BI para Analistas de Datos
>
> 📖 Módulo 12 - Glosario
>
> 🎯 Objetivo:
>
> Disponer de una guía rápida con los principales conceptos utilizados durante la Academia Excel BI.

---

# Introducción

Durante el desarrollo de esta Academia aparecieron numerosos términos propios del mundo del Business Intelligence.

Este glosario reúne los conceptos más importantes explicados a lo largo del curso para facilitar su consulta.

Cada definición incluye:

- Una explicación sencilla.
- Un ejemplo práctico.
- El módulo donde fue trabajado.

---

# 📖 Business Intelligence (BI)

## Definición

Business Intelligence (BI) es el conjunto de metodologías, procesos y herramientas utilizadas para transformar datos en información útil que apoye la toma de decisiones.

En pocas palabras:

Convierte grandes cantidades de datos en información comprensible para el negocio.

---

## Ejemplo

Una empresa de telecomunicaciones registra diariamente miles de pedidos.

Mediante BI es posible responder preguntas como:

- ¿Qué técnico realizó más instalaciones?
- ¿Qué ciudad presenta más averías?
- ¿Cuál fue el costo promedio por instalación?
- ¿Qué materiales se utilizan con mayor frecuencia?

---

## Se estudió en

Toda la Academia.

---

# 📖 Power Query

## Definición

Power Query es la herramienta de Excel utilizada para importar, limpiar, transformar y preparar datos antes de analizarlos.

Es el primer paso dentro de un proyecto BI.

---

## Ejemplo

Importar cinco archivos CSV de diferentes zonas y consolidarlos automáticamente en una sola tabla.

---

## Se estudió en

Módulo 01.

---

# 📖 Power Pivot

## Definición

Power Pivot es el motor analítico de Excel.

Permite construir el Modelo de Datos, crear relaciones entre tablas y desarrollar medidas DAX.

---

## Ejemplo

Relacionar Clientes, Pedidos y Materiales para analizarlos en una única Tabla Dinámica.

---

## Se estudió en

Módulo 02.

---

# 📖 Modelo de Datos

## Definición

Es la estructura donde se organizan las tablas y las relaciones que representan el funcionamiento del negocio.

El Modelo de Datos es el corazón de cualquier solución BI.

---

## Ejemplo

Clientes

↓

Pedidos

↓

Materiales

↓

Instalaciones

---

## Se estudió en

Módulos 03 y 04.

---

# 📖 Tabla de Hechos

## Definición

Es la tabla principal del Modelo de Datos.

Contiene los eventos que se desean analizar.

Generalmente almacena cantidades, valores o transacciones.

---

## Ejemplo

tblPedidos

Cada registro representa un pedido realizado.

---

## Se estudió en

Módulo 03.

---

# 📖 Tabla Dimensión

## Definición

Es una tabla que describe las características de los datos.

Normalmente contiene información descriptiva utilizada para clasificar o filtrar.

---

## Ejemplo

tblClientes

Permite analizar pedidos por cliente, ciudad o segmento.

---

## Se estudió en

Módulo 03.

---

# 📖 Star Schema

## Definición

Es un modelo donde una Tabla de Hechos se encuentra en el centro y las Tablas Dimensión la rodean.

Es el diseño más utilizado en Business Intelligence.

---

## Ejemplo

             Clientes

                 │

Técnicos ─ Pedidos ─ Materiales

                 │

             Calendario

---

## Se estudió en

Módulos 03 y 04.

---

# 📖 Llave Primaria (Primary Key)

## Definición

Es una columna cuyos valores son únicos.

Permite identificar cada registro sin repetir información.

---

## Ejemplo

IdCliente

Cada cliente posee un identificador diferente.

---

## Se estudió en

Módulo 03.

---

# 📖 Llave Foránea (Foreign Key)

## Definición

Es una columna utilizada para relacionar una tabla con otra.

Puede contener valores repetidos.

---

## Ejemplo

IdCliente dentro de la tabla Pedidos.

Permite identificar a qué cliente pertenece cada pedido.

---

## Se estudió en

Módulos 03 y 04.

---

# 📖 Relación 1:N

## Definición

Representa una relación donde un registro de una tabla puede relacionarse con muchos registros de otra.

Es la relación más utilizada en BI.

---

## Ejemplo

Un cliente puede realizar muchos pedidos.

Un pedido pertenece únicamente a un cliente.

---

## Se estudió en

Módulo 04.

---

# 📖 Cardinalidad

## Definición

Describe cómo se relacionan los registros entre dos tablas.

Las relaciones más comunes son:

- Uno a Uno (1:1)
- Uno a Muchos (1:N)
- Muchos a Muchos (N:N)

---

## Ejemplo

Clientes (1)

↓

Pedidos (*)

---

## Se estudió en

Módulo 04.

---