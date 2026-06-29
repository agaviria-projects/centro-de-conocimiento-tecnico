# 📘 Módulo 03 - Modelo de Datos

> 📚 **Curso:** Excel BI para Analistas de Datos  
> 📖 **Módulo:** 03 - Modelo de Datos  
> 🎯 **Nivel:** Básico  
> ⏱️ **Duración estimada:** 35 minutos

---

# 🎯 Objetivo

Comprender qué es un Modelo de Datos, cómo identificar la tabla principal, las tablas dimensión, las llaves de relación y cómo construir un modelo correctamente antes de crear medidas DAX.

Este módulo corresponde al primer laboratorio práctico del curso utilizando el archivo **Empresa_Telecom_ExcelBI_v3.xlsx**.

---

# 📖 ¿Qué es un Modelo de Datos?

Un Modelo de Datos es un conjunto de tablas relacionadas entre sí mediante campos comunes (llaves).

Gracias al Modelo de Datos es posible analizar información proveniente de diferentes tablas sin utilizar fórmulas como:

- BUSCARV
- BUSCARX
- INDICE
- COINCIDIR

Power Pivot utiliza el Modelo de Datos como base para realizar todos los cálculos con DAX.

---

# 🏢 Caso empresarial

Supongamos una empresa de telecomunicaciones.

Disponemos de seis tablas:

- Clientes
- Técnicos
- Pedidos
- Materiales
- Instalaciones
- Calendario

Cada tabla almacena una parte del proceso del negocio.

La tabla Calendario permitirá posteriormente realizar análisis por fechas, meses, trimestres y funciones de Inteligencia de Tiempo mediante DAX.

El objetivo consiste en relacionarlas correctamente para obtener información consolidada.

---

# 🧪 Laboratorio realizado

Durante este laboratorio realizamos las siguientes actividades.

## Paso 1

Convertimos cada hoja en una Tabla de Excel.

Nombre recomendado:

- tblClientes
- tblTecnicos
- tblPedidos
- tblMateriales
- tblInstalaciones
- tblCalendario

---

## Paso 2

Agregamos todas las tablas al Modelo de Datos.

En este momento Power Pivot únicamente conoce las tablas.

Todavía NO existen relaciones entre ellas.

Visualmente el modelo se encuentra así:

```text
Clientes

Tecnicos

Pedidos

Materiales

Instalaciones

Calendario
```

Todas las tablas están independientes.

---

## Concepto Clave

> Agregar una tabla al Modelo de Datos NO significa que exista una relación entre las tablas.

Las relaciones deben crearse manualmente.

---

# Paso 3

Antes de crear relaciones respondimos tres preguntas.

## 1

¿Cuál es la tabla principal?

Respuesta:

**Pedidos**

---

## ¿Por qué?

Porque conecta toda la información del negocio.

Un pedido:

- pertenece a un cliente
- es atendido por un técnico
- utiliza materiales
- tiene una o varias visitas de instalación

Por esta razón se convierte en la tabla central del modelo.

---

# Tabla de Hechos

La tabla **Pedidos** representa el evento principal del negocio.

En BI esta tabla recibe el nombre de:

## Fact Table (Tabla de Hechos)

Contiene los eventos que ocurren en la operación.

Ejemplos:

- Ventas
- Facturas
- Pedidos
- Movimientos
- Transacciones

En nuestro laboratorio:

**Pedidos** es la Tabla de Hechos.

---

# Tipos de tablas del Modelo de Datos

En nuestro laboratorio existen tres tipos de tablas.

---

## Tablas Dimensión (Dim)

Las dimensiones contienen información descriptiva del negocio.

En nuestro laboratorio son:

- Clientes
- Técnicos
- Calendario

Estas tablas responden preguntas como:

- ¿Quién realizó el pedido?
- ¿Dónde ocurrió?
- ¿Cuándo ocurrió?

---

## Tabla de Hechos (Fact)

La tabla **Pedidos** representa la operación principal del negocio.

Cada fila corresponde a un pedido realizado por un cliente y atendido por un técnico.

Esta tabla conecta toda la información del modelo.

---

# ¿Por qué Pedidos es la Tabla de Hechos?

Una forma sencilla de identificar la Tabla de Hechos consiste en responder la siguiente pregunta:

> ¿Qué información conecta a todas las demás tablas?

Observemos algunos ejemplos.

Si queremos conocer:

¿Cuánto material utilizó cada técnico?

El recorrido sería:

```text
Materiales

↓

Pedidos

↓

Técnicos
```

Si queremos saber:

¿Cuántos pedidos realizó cada cliente?

```text
Clientes

↓

Pedidos
```

Si queremos conocer:

¿Cuántas visitas se realizaron por pedido?

```text
Pedidos

↓

Instalaciones
```

Todas las consultas pasan por **Pedidos**.

Por esta razón se convierte en la Tabla de Hechos del modelo.


## Tablas de Detalle

También existen tablas que almacenan información adicional relacionada con cada pedido.

En nuestro laboratorio:

- Materiales
- Instalaciones

Estas tablas contienen múltiples registros asociados a un mismo pedido.

Por ejemplo:

Pedido 1001

- Cable UTP
- Router
- Conectores

o

Pedido 1001

- Visita 1
- Visita 2
- Visita 3

Estas tablas no describen el negocio como una dimensión, sino el detalle de la operación.



---

# Concepto Clave

La Tabla de Hechos responde:

> ¿Qué ocurrió?

Las Tablas Dimensión responden:

> ¿Quién?

> ¿Dónde?

> ¿Cuándo?

> ¿Cómo?

---

# Descubriendo relaciones

No comenzamos arrastrando campos.

Primero analizamos el negocio.

---

## Clientes

Pregunta:

¿Un cliente puede tener varios pedidos?

Respuesta:

Sí.

Entonces:

```text
Clientes (1)

↓

Pedidos (*)
```

---

## Técnicos

Pregunta:

¿Un técnico puede realizar varios pedidos?

Respuesta:

Sí.

Entonces:

```text
Tecnicos (1)

↓

Pedidos (*)
```

---

## Materiales

Pregunta:

¿Un pedido puede utilizar varios materiales?

Respuesta:

Sí.

Entonces:

```text
Pedidos (1)

↓

Materiales (*)
```

---

## Instalaciones

En la primera versión del laboratorio observamos que existía una instalación por pedido.

Durante la práctica detectamos que esa relación realmente era 1:1.

Como objetivo del curso era aprender relaciones 1:N, el laboratorio fue mejorado.

Ahora un pedido puede tener varias visitas de instalación.

Ejemplo:

Pedido 1001

- Visita 1
- Visita 2

Pedido 1005

- Visita 1
- Visita 2

La relación correcta quedó:

```text
Pedidos (1)

↓

Instalaciones (*)
```

---

# ¿Qué aprendimos?

Antes de crear una relación debemos analizar el negocio.

No basta con que dos tablas tengan un campo con el mismo nombre.

La relación debe representar una situación real.

---

# Llave Primaria

Una Llave Primaria identifica un registro de manera única.

Ejemplo:

Clientes

```text
IdCliente

1

2

3

4

5
```

No existen valores repetidos.

---

# Llave Foránea

Una Llave Foránea contiene el mismo valor pero puede repetirse.

Ejemplo:

Pedidos

```text
IdCliente

1

2

1

4

5

1
```

Un mismo cliente puede realizar muchos pedidos.

---

# Relación Uno a Muchos (1:N)

Es la relación más utilizada en BI.

Regla:

La tabla donde la llave es única corresponde al lado **1**.

La tabla donde la llave puede repetirse corresponde al lado **\***.

Ejemplo:

```text
Clientes (1)

──────────────

Pedidos (*)
```

---

# Relación Uno a Uno (1:1)

También existe.

Sin embargo normalmente indica que ambas tablas podrían unirse en una sola.

Durante el laboratorio detectamos este caso y mejoramos el diseño del modelo para representar una situación real.

---

# Esquema Estrella (Star Schema)

Nuestro modelo final quedó conceptualmente así:

```text
                CLIENTES
                    │
                    │
                    │
              ┌──────────┐
              │ PEDIDOS  │
              └──────────┘
             ╱     │      ╲
            ╱      │       ╲
           ╱       │        ╲
 TÉCNICOS  MATERIALES  INSTALACIONES
```

Este tipo de diseño recibe el nombre de:

## Star Schema

Es el modelo recomendado para Power Pivot y Power BI.

---
# ¿Cómo viaja la información entre las tablas?

Cuando una Tabla Dinámica aplica un filtro, Power Pivot utiliza automáticamente las relaciones del Modelo de Datos.

Por ejemplo.

Si seleccionamos:

Ciudad = Medellín

El filtro sigue el siguiente recorrido:

```text
Clientes

↓

Pedidos

↓

Materiales
```

Power Pivot identifica automáticamente los pedidos pertenecientes a Medellín y filtra únicamente los materiales utilizados en esos pedidos.

Este comportamiento será fundamental cuando comencemos a trabajar con medidas DAX.

# Resumen del Modelo

| Tipo de tabla | Tabla |
|---------------|----------------|
| Tabla de Hechos | Pedidos |
| Dimensión | Clientes |
| Dimensión | Técnicos |
| Dimensión | Calendario |
| Tabla de Detalle | Materiales |
| Tabla de Detalle | Instalaciones |
| Tipo de Modelo | Star Schema |

# ⭐ Reglas de Oro

## Regla 1

Antes de crear relaciones identifica la Tabla de Hechos.

---

## Regla 2

Las Tablas Dimensión deben tener llaves únicas.

---

## Regla 3

No pienses primero en Excel.

Piensa primero en el negocio.

---

## Regla 4

Las relaciones deben representar procesos reales.

No simplemente columnas con el mismo nombre.

---

# ⚠️ Errores frecuentes

## Error 1

Agregar tablas al Modelo de Datos pensando que ya quedaron relacionadas.

---

## Error 2

Crear relaciones únicamente porque las columnas tienen el mismo nombre.

---

## Error 3

Utilizar una columna con valores duplicados como lado **1**.

---

## Error 4

Nombrar las tablas como:

- Tabla1
- Tabla2
- Hoja1

En lugar de utilizar nombres descriptivos.

---

# 🏢 Aplicación en proyectos reales

La misma lógica se aplica a proyectos empresariales como:

- DRACO
- Interventoría
- SIGEM
- Control ANS
- Inventarios

Antes de crear cualquier medida debemos responder:

- ¿Cuál es la Tabla de Hechos?
- ¿Cuáles son las Dimensiones?
- ¿Cuál es la llave de relación?

---

# Pensando como un Analista BI

Un usuario de Excel observa varias hojas con datos.

Un Analista BI observa un modelo de información donde cada tabla cumple una función específica.

- Clientes identifica quién realiza el pedido.
- Técnicos identifica quién ejecuta el trabajo.
- Calendario permite analizar el tiempo.
- Pedidos representa la operación principal.
- Materiales almacena los recursos utilizados.
- Instalaciones registra el seguimiento del servicio.

Comprender el papel de cada tabla es el primer paso para construir modelos escalables en Power Pivot y Power BI.

# 📝 Lo que aprendí

En este módulo comprendí que un Modelo de Datos no consiste únicamente en agregar tablas al Modelo de Datos.

El verdadero trabajo consiste en analizar el negocio, identificar la Tabla de Hechos, descubrir las Tablas Dimensión y construir relaciones que representen correctamente la realidad de la empresa.

A partir de este momento comenzaré a pensar primero en el modelo y después en las herramientas.

---

# 🎯 Ejercicio

Utilizando el archivo **Empresa_Telecom_ExcelBI_v3.xlsx** responde:

1. ¿Cuál es la Tabla de Hechos?

2. ¿Cuáles son las Tablas Dimensión?

3. ¿Qué relaciones existen?

4. ¿Cuál es la llave primaria de cada dimensión?

5. ¿Cuál es la llave foránea en la Tabla de Hechos?

6. ¿Qué relaciones son 1:N?

---

# 🚀 Próximo módulo

## 📘 Módulo 04 - Creando Relaciones en Power Pivot

En el siguiente módulo construiremos el Modelo de Datos completo dentro de Power Pivot, aprenderemos a interpretar la Vista de Diagrama y entenderemos cómo afectan las relaciones a las Tablas Dinámicas y a las futuras medidas DAX.