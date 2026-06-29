# 📘 Módulo 10 - Casos Reales y Lecciones Aprendidas en Excel BI

> 📚 **Curso:** Excel BI para Analistas de Datos
>
> 📖 **Módulo:** 10 - Casos Reales y Lecciones Aprendidas en Excel BI
>
> 🎯 **Nivel:** Avanzado
>
> ⏱️ **Duración estimada:** 3 horas

---

# 🎯 Objetivo

Durante los módulos anteriores aprendimos a utilizar:

- Power Query
- Power Pivot
- Modelo de Datos
- Relaciones
- DAX
- Medidas
- Columnas Calculadas
- Tablas Dinámicas
- Dashboards

Sin embargo, en un proyecto real aparecen situaciones que normalmente no se explican en los cursos tradicionales.

Este módulo recopila experiencias reales vividas durante el desarrollo del laboratorio y de proyectos empresariales.

Cada caso presenta:

- El problema.
- Lo que ocurrió.
- La causa.
- La solución.
- La lección aprendida.

El objetivo no consiste únicamente en resolver errores, sino comprender por qué ocurren.

---

# ¿Por qué existe este módulo?

La mayoría de cursos enseñan únicamente cuando todo funciona correctamente.

En la práctica sucede exactamente lo contrario.

Los Analistas BI dedican gran parte de su tiempo a:

- Investigar errores.
- Comprender comportamientos inesperados.
- Validar información.
- Ajustar Modelos de Datos.
- Corregir relaciones.
- Optimizar medidas DAX.

Precisamente esas situaciones son las que construiremos aquí.

---

# Nuestra filosofía

Durante este módulo aprenderemos una regla muy importante.

> Los errores también enseñan.

De hecho, muchos de los conceptos más importantes de Excel BI fueron comprendidos precisamente cuando algo dejó de funcionar.

---

# Cómo utilizar este módulo

No es necesario leer los casos en orden.

Puedes regresar a este documento cada vez que encuentres un comportamiento inesperado.

Con el tiempo este módulo se convertirá en una guía de consulta permanente.

---

# Formato de cada caso

Todos los casos seguirán la misma estructura.

## Situación

¿Qué ocurrió?

---

## Lo que pensé inicialmente

¿Cuál fue la primera hipótesis?

---

## Descubriendo el problema

¿Qué estaba ocurriendo realmente?

---

## Solución

¿Cómo se resolvió?

---

## Lo que aprendimos

¿Cuál fue la enseñanza más importante?

---

# 🏢 Caso Real #1

# No aparece "Campo Calculado"

---

## Situación

Durante el desarrollo de un informe fue necesario calcular el promedio de viáticos dentro de una Tabla Dinámica.

La idea inicial consistía en crear un Campo Calculado.

Sin embargo, al abrir el menú apareció una sorpresa.

La opción **Campo Calculado** estaba deshabilitada.

Parecía un error de Excel.

---

## Lo que pensé inicialmente

Las primeras hipótesis fueron:

- Excel tiene un error.
- La Tabla Dinámica está dañada.
- Debo habilitar alguna opción.
- Falta activar un complemento.

Después de varios minutos el problema continuaba exactamente igual.

---

## Descubriendo el problema

La Tabla Dinámica no era una Tabla Dinámica tradicional.

Había sido creada utilizando:

```text
Agregar estos datos al Modelo de Datos
```

Ese pequeño detalle cambia completamente el funcionamiento de Excel.

Cuando una Tabla Dinámica utiliza el Modelo de Datos:

Excel deja de utilizar los Campos Calculados tradicionales.

En ese momento el motor de cálculo pasa a ser Power Pivot.

Por esta razón los nuevos cálculos deben construirse mediante Medidas DAX.

---

## ¿Por qué ocurre?

Existen dos tipos de Tablas Dinámicas.

### Tabla Dinámica tradicional

Motor de cálculo:

Excel

Permite:

- Campo Calculado
- Elemento Calculado

No utiliza Modelo de Datos.

---

### Tabla Dinámica basada en Modelo de Datos

Motor de cálculo:

Power Pivot

Permite:

- Medidas DAX
- Columnas Calculadas
- Relaciones
- Modelo de Datos

No utiliza Campos Calculados tradicionales.

---

# Comparación

| Tabla Dinámica Tradicional | Modelo de Datos |
|----------------------------|-----------------|
| Campo Calculado | ❌ |
| Medidas DAX | ❌ | ✅ |
| Relaciones | ❌ | ✅ |
| Varias tablas | Limitado | ✅ |
| Modelo Estrella | ❌ | ✅ |

---

## La solución

En lugar de buscar un Campo Calculado fue necesario crear una Medida DAX.

Ejemplo.

```DAX
Promedio Viáticos :=
AVERAGE(tblViaticos[Valor])
```

La medida quedó almacenada dentro del Modelo de Datos y pudo reutilizarse en cualquier Tabla Dinámica.

---

## Lo que aprendimos

Este caso permitió comprender una de las diferencias más importantes de Power Pivot.

Cuando una Tabla Dinámica utiliza el Modelo de Datos:

Ya no debemos pensar en Campos Calculados.

Debemos comenzar a pensar en Medidas DAX.

Ese cambio representa uno de los pasos más importantes para evolucionar desde Excel tradicional hacia Business Intelligence.

---

# 🎯 Regla de Oro

Si una Tabla Dinámica fue creada utilizando el Modelo de Datos y no encuentras la opción **Campo Calculado**, no se trata de un error.

Simplemente significa que el cálculo ahora debe desarrollarse mediante una Medida DAX.

---

# Resumen del Caso

**Problema**

No aparece Campo Calculado.

**Causa**

La Tabla Dinámica utiliza el Modelo de Datos.

**Solución**

Crear una Medida DAX.

**Lección Aprendida**

El Modelo de Datos reemplaza los Campos Calculados por Medidas DAX.

---

# 🚀 Próximo caso

## Caso Real #2

### ¿Es obligatorio tener relaciones para utilizar DAX?

En el siguiente caso descubriremos que una Medida DAX puede funcionar incluso cuando el Modelo de Datos contiene una sola tabla.

---

# 🏢 Caso Real #2

# ¿Es obligatorio tener relaciones para utilizar DAX?

---

## Situación

Durante el desarrollo del laboratorio fue necesario calcular el promedio de viáticos.

La información provenía de una única tabla.

Todavía no existían relaciones.

Surgió entonces una pregunta muy común.

> ¿Puedo utilizar DAX si solamente tengo una tabla?

Inicialmente parecía que la respuesta era NO.

---

## Lo que pensé inicialmente

Las primeras ideas fueron:

- DAX únicamente funciona cuando existen varias tablas.
- Primero debo crear relaciones.
- Necesito un Modelo Estrella para comenzar a utilizar medidas.

Después de investigar descubrimos que ninguna de esas ideas era completamente correcta.

---

## Descubriendo el problema

Lo importante no es la cantidad de tablas.

Lo importante es dónde están almacenados los datos.

Si la tabla fue agregada al:

```text
Modelo de Datos
```

Power Pivot ya puede utilizar DAX.

Aunque exista solamente una tabla.

---

## Ejemplo

Supongamos la siguiente información.

```text
Viáticos

Empleado

Fecha

Valor
```

No existen:

- Clientes
- Técnicos
- Calendario

Solo existe una tabla.

Aun así podemos crear medidas.

Ejemplo.

```DAX
Promedio Viáticos :=
AVERAGE(tblViaticos[Valor])
```

La medida funcionará correctamente.

---

## Entonces...

¿Para qué sirven las relaciones?

Las relaciones permiten que DAX combine información proveniente de diferentes tablas.

Ejemplo.

```text
Clientes

↓

Pedidos

↓

Materiales
```

Gracias a esas relaciones podremos responder preguntas como:

- Total de materiales por cliente.
- Materiales por ciudad.
- Pedidos por técnico.

Pero para utilizar funciones básicas como:

- SUM
- COUNT
- AVERAGE
- MAX
- MIN

No es obligatorio tener relaciones.

---

# Comparación

## Una sola tabla

```text
Viáticos
```

Podemos crear:

- SUM
- COUNT
- MAX
- MIN
- AVERAGE

Sin ningún problema.

---

## Varias tablas

```text
Clientes

↓

Pedidos

↓

Materiales
```

Ahora DAX puede aprovechar las relaciones para realizar análisis mucho más completos.

---

# ¿Qué aprendimos?

Las relaciones no activan DAX.

DAX ya funciona desde el momento en que una tabla pertenece al Modelo de Datos.

Las relaciones simplemente aumentan las posibilidades de análisis.

---

# Regla de Oro

No esperes a tener un Modelo Estrella para comenzar a utilizar DAX.

Puedes comenzar creando medidas desde una sola tabla.

Posteriormente, cuando el proyecto crezca, agregarás nuevas tablas y relaciones.

Esta estrategia facilita el desarrollo incremental de proyectos BI.

---

# Consejo Profesional

Muchos proyectos empresariales comienzan con una sola tabla.

Con el tiempo aparecen nuevas fuentes de información.

En ese momento el Modelo de Datos evoluciona.

Por esta razón no debes esperar a tener un modelo complejo para comenzar a desarrollar medidas DAX.

---

# Error frecuente

Pensar que:

```text
Sin relaciones

↓

No existe DAX
```

La realidad es diferente.

```text
Modelo de Datos

↓

DAX

↓

Relaciones (opcional al inicio)
```

Las relaciones enriquecen el análisis, pero no son un requisito para comenzar a utilizar DAX.

---

# Resumen del Caso

**Problema**

Pensaba que DAX necesitaba varias tablas relacionadas.

---

**Causa**

Confusión entre Modelo de Datos y Relaciones.

---

**Solución**

Agregar la tabla al Modelo de Datos y crear la medida normalmente.

---

**Lección Aprendida**

Una medida DAX puede funcionar perfectamente con una sola tabla.

Las relaciones permiten realizar análisis más completos, pero no son obligatorias para comenzar.

---

# 🚀 Próximo caso

## 🏢 Caso Real #3

### ¿Por qué mi relación quedó 1:1 cuando esperaba una relación 1:N?

Durante el desarrollo del laboratorio descubrimos que el problema no estaba en Power Pivot.

El problema estaba en el diseño del negocio.

Ese descubrimiento cambió completamente la estructura del Modelo de Datos y nos enseñó una de las lecciones más importantes de Business Intelligence.

---

# 🏢 Caso Real #3

# ¿Por qué mi relación quedó 1:1 cuando esperaba una relación 1:N?

---

## Situación

Durante la construcción del laboratorio Empresa_Telecom_ExcelBI_v3.xlsx fue necesario crear la relación entre:

```text
Pedidos

↓

Instalaciones
```

Inicialmente se esperaba obtener una relación:

```text
1 : N
```

Sin embargo, Power Pivot creó una relación:

```text
1 : 1
```

En ese momento parecía un problema del Modelo de Datos.

---

## Lo que pensé inicialmente

Las primeras hipótesis fueron.

- Power Pivot creó la relación incorrectamente.
- Existe un error en el Modelo de Datos.
- Debo modificar manualmente la cardinalidad.
- Excel está detectando mal la información.

Después de revisar varias veces las tablas descubrimos que el problema no era Power Pivot.

---

## Descubriendo el problema

Power Pivot únicamente refleja la realidad de los datos.

Al revisar la tabla Instalaciones encontramos algo interesante.

Cada Pedido aparecía una sola vez.

Ejemplo.

```text
Pedido

P0001

P0002

P0003

P0004
```

No existían pedidos repetidos.

Eso significa que realmente la relación era:

```text
Pedidos

↓

Instalaciones

1 : 1
```

Power Pivot estaba funcionando correctamente.

---

## Entonces...

¿Dónde estaba el problema?

No estaba en Excel.

El problema estaba en el diseño del laboratorio.

---

## Analizando el negocio

Nos hicimos una pregunta.

> ¿En la vida real un pedido siempre tiene una sola visita?

La respuesta fue:

NO.

Puede ocurrir algo como:

```text
Pedido P0008

↓

Visita 1

↓

Visita 2

↓

Visita 3
```

Eso representa mucho mejor la operación de una empresa de telecomunicaciones.

---

## La solución

En lugar de modificar Power Pivot modificamos los datos.

La tabla Instalaciones fue reconstruida.

Ahora algunos pedidos contienen varias visitas.

Ejemplo.

```text
Pedido

P0008

Visita 1

----------------

P0008

Visita 2

----------------

P0008

Visita 3
```

Después de actualizar el Modelo de Datos ocurrió exactamente lo esperado.

```text
Pedidos (1)

↓

Instalaciones (*)
```

Ahora sí teníamos una relación Uno a Muchos.

---

# Lo importante

Observa que no arreglamos el problema desde Excel.

Arreglamos el modelo del negocio.

Este es uno de los principios más importantes del Business Intelligence.

---

# Regla de Oro

Nunca intentes modificar una relación para que se vea como tú esperas.

Primero pregúntate:

> ¿La información realmente representa el proceso del negocio?

Power Pivot únicamente refleja la estructura de los datos.

---

# Consejo Profesional

Cuando una relación no es la esperada:

No abras Power Pivot inmediatamente.

Primero revisa los datos.

En la mayoría de los casos el problema se encuentra en el origen de la información.

---

# Error frecuente

Pensar que:

```text
La relación está mal.
```

Cuando en realidad ocurre:

```text
Los datos representan otra realidad.
```

---

# Lo que aprendimos

Este caso nos enseñó una de las lecciones más importantes del curso.

No debemos construir el Modelo de Datos pensando únicamente en Excel.

Debemos construirlo pensando en cómo funciona realmente el negocio.

Cuando el Modelo representa correctamente la operación, Power Pivot crea las relaciones adecuadas de forma natural.

---

# 🎯 ¿Cómo respondería esto en una entrevista?

**Pregunta**

¿Por qué una relación puede quedar 1:1 cuando esperaba una relación 1:N?

**Respuesta**

Porque Power Pivot determina la cardinalidad a partir de los datos.

Si el campo relacionado no contiene valores repetidos en la tabla de detalle, la relación será 1:1.

Antes de modificar el modelo es necesario validar que los datos representen correctamente el proceso del negocio.

---

# Resumen del Caso

**Problema**

La relación quedó 1:1.

---

**Causa**

La tabla Instalaciones tenía un único registro por Pedido.

---

**Solución**

Modificar el diseño de la tabla para representar múltiples visitas por Pedido.

---

**Lección Aprendida**

No siempre el problema está en Power Pivot.

Muchas veces el verdadero problema está en el diseño del negocio.

---

# 🚀 Próximo caso

## 🏢 Caso Real #4

### ¿Por qué una medida cambia sola si nunca modifiqué la fórmula?

En este caso descubriremos el concepto que más confusión genera cuando alguien comienza con DAX: **el Contexto de Filtro**.


---

# 🏢 Caso Real #4

# ¿Por qué mi medida funciona, pero no aparece donde esperaba?

---

## Situación

Después de crear varias medidas DAX correctamente:

- Total Materiales
- Promedio Materiales
- Valor Máximo
- Valor Mínimo

Surgió una duda.

> ¿Dónde quedaron las medidas?

Al revisar la tabla no aparecían como una columna nueva.

Parecía que Excel no había guardado el trabajo realizado.

---

## Lo que pensé inicialmente

Las primeras ideas fueron:

- La medida no se creó.
- Power Pivot presentó un error.
- Debo volver a escribir la fórmula.
- La medida desapareció.

Sin embargo, al abrir **Administrar Medidas** todas las medidas estaban allí.

---

## Descubriendo el problema

Había una confusión entre dos conceptos completamente diferentes.

Una **Columna Calculada** sí forma parte de la tabla.

Una **Medida** no pertenece físicamente a la tabla.

Las medidas se almacenan dentro del Modelo de Datos.

Por esa razón no aparecen como una nueva columna.

---

## ¿Dónde viven realmente las medidas?

Las medidas pertenecen al Modelo de Datos.

Puedes comprobarlo desde:

```text
Power Pivot

↓

Administrar

↓

Medidas

↓

Administrar Medidas
```

Allí aparecerán todas las medidas creadas para el proyecto.

---

## ¿Dónde se utilizan?

Las medidas aparecen cuando construimos una:

- Tabla Dinámica.
- Gráfico Dinámico.
- Dashboard.

En ese momento Excel consulta el Modelo de Datos y muestra las medidas disponibles.

---

## Lo importante

Una medida no genera una nueva columna.

Genera un cálculo dinámico.

Por eso puede reutilizarse en múltiples informes sin duplicar información.

---

## Comparación

### Columna Calculada

```text
Pedido

Material

Cantidad

Valor

Valor Total
```

La columna existe físicamente.

Cada fila tiene un valor almacenado.

---

### Medida

```DAX
Total Materiales :=
SUM(tblMateriales[Valor])
```

No aparece como columna.

Permanece almacenada dentro del Modelo de Datos.

Se calcula únicamente cuando un informe la necesita.

---

## La solución

En lugar de buscar la medida dentro de la tabla, comenzamos a verla desde el lugar correcto.

```text
Modelo de Datos

↓

Administrar Medidas

↓

Tabla Dinámica
```

A partir de ese momento comprendimos que una medida no reemplaza una columna.

Cumple una función completamente diferente.

---

# Regla de Oro

Si acabas de crear una medida y no aparece como columna...

No significa que esté mal.

Significa que las medidas pertenecen al Modelo de Datos.

---

# Consejo Profesional

Cuando un proyecto comienza a crecer, administra todas las medidas desde la ventana:

```text
Administrar Medidas
```

Desde allí podrás:

- Editarlas.
- Cambiar su nombre.
- Revisar la fórmula.
- Eliminar medidas que ya no utilices.

Es mucho más práctico que buscarlas una por una.

---

# Lo que aprendimos

Este caso permitió entender una diferencia fundamental.

Una Columna Calculada amplía la tabla.

Una Medida amplía la capacidad de análisis.

Aunque ambas utilizan DAX, cumplen objetivos completamente distintos.

---

# 🎯 ¿Cómo respondería esto en una entrevista?

**Pregunta**

¿Dónde se almacenan las medidas DAX?

**Respuesta**

Las medidas no se almacenan como columnas dentro de una tabla. Permanecen dentro del Modelo de Datos y se evalúan únicamente cuando una Tabla Dinámica, un gráfico o un Dashboard necesitan calcular su resultado.

---

# Resumen del Caso

**Problema**

Pensaba que la medida aparecería como una nueva columna.

---

**Causa**

Confusión entre una Medida y una Columna Calculada.

---

**Solución**

Comprender que las medidas viven dentro del Modelo de Datos y se administran desde Power Pivot.

---

**Lección Aprendida**

Una medida no agrega datos a la tabla.

Agrega inteligencia al Modelo de Datos.

---

# 🚀 Próximo caso

## 🏢 Caso Real #5

### ¿Por qué una misma medida devuelve resultados diferentes sin cambiar la fórmula?

Este fue uno de los conceptos que más costó comprender al inicio y nos llevó a descubrir el verdadero significado del **Contexto de Filtro**.

---

# 🏢 Caso Real #5

# ¿Por qué una misma medida devuelve resultados diferentes sin cambiar la fórmula?

---

## Situación

Durante el laboratorio creamos la siguiente medida.

```DAX
Total Materiales :=
SUM(tblMateriales[Valor Total])
```

La medida funcionaba correctamente.

Sin embargo, al construir una Tabla Dinámica ocurrió algo que generó mucha confusión.

Cuando agregábamos:

- Cliente

El resultado era uno.

Pero al cambiar por:

- Técnico

La misma medida mostraba otro valor.

Después probamos con:

- Ciudad

Nuevamente el resultado era diferente.

Lo extraño era que la medida nunca había cambiado.

---

## Lo que pensé inicialmente

Las primeras ideas fueron.

- La medida tiene un error.
- Power Pivot está calculando mal.
- La Tabla Dinámica está dañada.
- Debo crear una medida para Cliente y otra para Técnico.

Parecía que Excel modificaba el cálculo automáticamente.

---

## Descubriendo el problema

Después de analizar el comportamiento comprendimos algo muy importante.

La medida nunca cambió.

Lo único que cambió fue la información que la Tabla Dinámica le estaba enviando.

Es decir.

Cambió el contexto de análisis.

---

# Imaginemos una reunión

Supongamos que el gerente pregunta.

> ¿Cuál es el Total de Materiales?

La respuesta puede ser:

```text
$3.750.000
```

Hasta aquí no existe ningún filtro.

---

Ahora el gerente pregunta.

> Muéstreme únicamente Cliente 1.

La medida sigue siendo exactamente la misma.

```DAX
Total Materiales :=
SUM(tblMateriales[Valor Total])
```

Pero ahora el resultado cambia.

¿Por qué?

Porque ya no está sumando toda la tabla.

Solo está sumando los registros de Cliente 1.

---

Después el gerente pregunta.

> Ahora muéstreme únicamente Técnico 6.

La medida continúa siendo exactamente igual.

Sin embargo el resultado vuelve a cambiar.

No porque la fórmula cambió.

Sino porque ahora analiza otro conjunto de registros.

---

# Entonces...

¿Qué cambió realmente?

No cambió la medida.

Cambió el conjunto de datos sobre el cual trabaja la medida.

Ese conjunto de datos recibe el nombre de:

# Contexto de Filtro

---

# Explicándolo de forma sencilla

Imagina una calculadora.

La calculadora siempre suma de la misma manera.

Lo único que cambia son los números que introduces.

Con DAX ocurre exactamente igual.

La medida siempre realiza el mismo cálculo.

Lo único que cambia son los registros que recibe.

---

# Ejemplo

Sin filtros.

```text
Cliente

Todos

↓

Total Materiales

$3.750.000
```

---

Filtrando Cliente 1.

```text
Cliente

Cliente 1

↓

Total Materiales

$250.000
```

---

Filtrando Cliente 8.

```text
Cliente

Cliente 8

↓

Total Materiales

$175.000
```

---

Filtrando Ciudad Medellín.

```text
Ciudad

Medellín

↓

Total Materiales

$925.000
```

---

Observa algo importante.

La medida nunca cambió.

Siempre fue exactamente esta.

```DAX
Total Materiales :=
SUM(tblMateriales[Valor Total])
```

Lo único que cambió fue el grupo de registros utilizados para realizar la suma.

---

# La mejor definición

Durante el laboratorio llegamos a la siguiente conclusión.

> El contexto de filtro es el conjunto de registros que Power Pivot selecciona antes de ejecutar una medida DAX.

Primero filtra.

Después calcula.

Nunca ocurre al contrario.

---

# Lo importante

Cuando agregamos un campo en una Tabla Dinámica.

Por ejemplo.

```text
Cliente
```

No estamos modificando la medida.

Estamos diciéndole a Power Pivot:

> Calcula la misma medida, pero únicamente para este Cliente.

---

# Regla de Oro

Una medida DAX normalmente nunca necesita modificarse.

Lo que cambia es el contexto desde donde se analiza la información.

Por esa razón una sola medida puede reutilizarse en cientos de informes diferentes.

---

# Consejo Profesional

Si una medida devuelve un resultado inesperado.

No revises primero la fórmula.

Primero revisa:

- Los filtros.
- Los Segmentadores.
- La Cronología.
- Los campos ubicados en Filas.
- Los campos ubicados en Columnas.

En la mayoría de los casos el problema no está en DAX.

Está en el contexto de filtro.

---

# Lo que aprendimos

Este caso cambió completamente nuestra forma de pensar.

Comprendimos que una medida no devuelve un resultado fijo.

Devuelve un resultado dependiendo del escenario desde el cual se consulta.

Por esa razón una misma medida puede utilizarse durante años sin necesidad de modificar su fórmula.

---

# 🎯 ¿Cómo respondería esto en una entrevista?

**Pregunta**

¿Por qué una medida DAX devuelve resultados diferentes sin modificar la fórmula?

**Respuesta**

Porque las medidas se evalúan dentro de un contexto de filtro.

La expresión DAX permanece igual.

Lo que cambia es el conjunto de registros que Power Pivot utiliza para realizar el cálculo.

Por eso una misma medida puede producir diferentes resultados según el Cliente, la Ciudad, el Técnico, el Mes o cualquier otro filtro aplicado.

---

# Resumen del Caso

**Problema**

La medida cambiaba de resultado sin cambiar la fórmula.

---

**Causa**

Cambiaba el contexto de filtro.

---

**Solución**

Comprender que DAX siempre calcula sobre los registros visibles después de aplicar los filtros.

---

**Lección Aprendida**

Las medidas no son cálculos estáticos.

Son cálculos dinámicos que dependen del contexto de análisis.

---

# 🚀 Próximo caso

## 🏢 Caso Real #6

### ¿Por qué no podía crear una Columna Calculada desde la Tabla Dinámica?

Este fue otro de los casos que nos hizo detener el desarrollo durante el laboratorio y nos permitió comprender la diferencia entre trabajar dentro del Modelo de Datos y trabajar desde una Tabla Dinámica.

---

# 🏢 Caso Real #6

# ¿Por qué no podía crear una Columna Calculada desde la Tabla Dinámica?

🟡 **Nivel 2 - Error que puede detener un desarrollo**

---

## Situación

Durante el laboratorio necesitábamos crear una nueva columna.

La idea era calcular:

```text
Cantidad × Valor
```

Sin embargo, el cálculo debía quedar almacenado para cada registro.

Al intentar hacerlo desde la Tabla Dinámica no encontramos ninguna opción que permitiera crear la columna.

Parecía que Excel había eliminado esa funcionalidad.

---

## Lo que pensé inicialmente

Las primeras ideas fueron:

- La Tabla Dinámica tiene un error.
- Debo habilitar alguna opción.
- Existe un botón oculto.
- Power Pivot no permite columnas calculadas.

Después de revisar varios menús descubrimos que el problema era otro.

---

## Descubriendo el problema

Estábamos trabajando desde una Tabla Dinámica.

Una Tabla Dinámica únicamente sirve para analizar información.

No sirve para modificar el Modelo de Datos.

Las Columnas Calculadas únicamente pueden crearse dentro de Power Pivot.

---

# Lo importante

Debemos diferenciar claramente dos lugares de trabajo.

## Lugar 1

### Tabla Dinámica

Sirve para:

- Analizar datos.
- Crear informes.
- Insertar gráficos.
- Aplicar filtros.

No permite crear Columnas Calculadas.

---

## Lugar 2

### Power Pivot

Sirve para:

- Crear Medidas.
- Crear Columnas Calculadas.
- Administrar relaciones.
- Administrar el Modelo de Datos.

Aquí sí podemos ampliar el modelo.

---

# ¿Dónde debía crear la columna?

La columna debía construirse dentro de la tabla:

```text
tblMateriales
```

Desde Power Pivot.

Seleccionando la primera columna vacía.

---

## Ejemplo

```DAX
Valor Total =
tblMateriales[Cantidad] *
tblMateriales[Valor]
```

Una vez creada la columna.

Power Pivot calcula automáticamente el valor para cada registro.

---

# ¿Qué ocurrió después?

Regresamos a la Tabla Dinámica.

Actualizamos el Modelo de Datos.

Y la nueva columna apareció disponible dentro de la lista de campos.

Ahora sí podía utilizarse para construir medidas y análisis.

---

# Diferencia fundamental

## Columna Calculada

Se crea en:

```text
Power Pivot
```

Se calcula:

Fila por fila.

Queda almacenada en el Modelo de Datos.

---

## Medida

También se crea en:

```text
Power Pivot
```

Pero no se calcula fila por fila.

Se calcula únicamente cuando una Tabla Dinámica necesita el resultado.

---

# Regla de Oro

Si necesitas agregar un nuevo dato para cada registro.

Utiliza una Columna Calculada.

Si necesitas resumir información.

Utiliza una Medida.

---

# Consejo Profesional

Antes de crear cualquier cálculo pregúntate.

> ¿Necesito un valor para cada fila?

Si la respuesta es:

Sí.

Entonces necesitas una Columna Calculada.

---

Si la respuesta es:

Necesito un total, promedio, máximo, mínimo o indicador.

Entonces necesitas una Medida.

---

# Lo que aprendimos

Este caso nos enseñó que una Tabla Dinámica nunca modifica el Modelo de Datos.

El Modelo de Datos únicamente puede modificarse desde Power Pivot.

Comprender esta diferencia evita perder mucho tiempo buscando opciones que simplemente no existen dentro de una Tabla Dinámica.

---

# 🎯 ¿Cómo respondería esto en una entrevista?

**Pregunta**

¿Por qué una Columna Calculada no puede crearse desde una Tabla Dinámica?

**Respuesta**

Porque la Tabla Dinámica es un componente de análisis y visualización.

Las Columnas Calculadas forman parte del Modelo de Datos y únicamente pueden crearse dentro de Power Pivot, donde se administra la estructura del modelo.

---

# Resumen del Caso

**Problema**

Intentaba crear una Columna Calculada desde una Tabla Dinámica.

---

**Causa**

La Tabla Dinámica no modifica el Modelo de Datos.

---

**Solución**

Abrir Power Pivot y crear la columna directamente sobre la tabla correspondiente.

---

**Lección Aprendida**

Una Tabla Dinámica analiza el Modelo de Datos.

Power Pivot construye el Modelo de Datos.

Nunca debemos confundir ambos entornos.

---

# 🚀 Próximo caso

## 🏢 Caso Real #7

### ¿Por qué creamos una hoja llamada "Pivots" si el usuario nunca la verá?

En este caso descubriremos una de las mejores prácticas utilizadas por Analistas BI para construir Dashboards profesionales en Excel.

---

# 🏢 Caso Real #7

# ¿Por qué creamos una hoja llamada "Pivots" si el usuario nunca la verá?

🟡 **Nivel 2 - Buena práctica que mejora la organización del proyecto**

---

## Situación

Durante la construcción del Dashboard surgió una pregunta.

> ¿Por qué crear una hoja llamada **Pivots** si al final el usuario solo utilizará el Dashboard?

La primera idea fue mucho más sencilla.

Construir directamente:

- Las Tablas Dinámicas.
- Los Gráficos.
- Los KPIs.

Todo dentro de la hoja Dashboard.

Parecía ahorrar tiempo.

---

## Lo que pensé inicialmente

Las primeras ideas fueron:

- Tener menos hojas.
- Construir todo en un solo lugar.
- Evitar cambiar constantemente entre hojas.

En teoría parecía una buena práctica.

En la realidad ocurrió exactamente lo contrario.

---

## Descubriendo el problema

A medida que el Dashboard comenzó a crecer aparecieron varios inconvenientes.

Cada vez que era necesario modificar una Tabla Dinámica:

- Había que mover gráficos.
- Los Segmentadores perdían espacio.
- Los KPIs se desalineaban.
- El Dashboard dejaba de verse limpio.

El área de trabajo comenzó a convertirse en un espacio difícil de mantener.

---

# Entonces comprendimos algo importante

Un Dashboard tiene un único objetivo.

Mostrar información.

No debe utilizarse como área de desarrollo.

---

# La solución

Separar el proyecto en dos hojas.

## Hoja Pivots

Aquí construiremos:

- Todas las Tablas Dinámicas.
- Los cálculos auxiliares.
- Las fuentes de los gráficos.

Esta hoja funcionará como el motor del Dashboard.

---

## Hoja Dashboard

Aquí únicamente mostraremos:

- KPIs.
- Gráficos.
- Segmentadores.
- Cronología.
- Títulos.

El usuario nunca necesitará modificar esta hoja.

---

# Arquitectura obtenida

```text
Empresa_Telecom_ExcelBI_v3.xlsx

│

├── Datos

│

├── Modelo de Datos

│

├── Pivots
│
├── Pivot Clientes
├── Pivot Técnicos
├── Pivot Ciudad
├── Pivot Mes
├── Pivot Tipo Servicio

│

└── Dashboard
      │
      ├── KPIs
      ├── Gráficos
      ├── Segmentadores
      └── Cronología
```

---

# ¿Qué ventajas obtuvimos?

Después de separar ambas hojas descubrimos varias ventajas.

### Desarrollo más ordenado

Las Tablas Dinámicas pueden modificarse sin afectar el Dashboard.

---

### Dashboard más limpio

La hoja principal contiene únicamente la información que verá el usuario.

---

### Mantenimiento más sencillo

Si una Tabla Dinámica necesita cambiar.

No es necesario mover gráficos.

---

### Nuevos indicadores

Podemos crear nuevas Tablas Dinámicas sin alterar el diseño del Dashboard.

---

### Mayor seguridad

Al finalizar el proyecto incluso podemos ocultar la hoja **Pivots**.

El usuario únicamente visualizará el Dashboard.

---

# Lo importante

La hoja **Pivots** no existe para el usuario.

Existe para el desarrollador.

Es el lugar donde construimos toda la lógica que posteriormente alimentará el Dashboard.

---

# Regla de Oro

Nunca desarrolles un Dashboard directamente sobre la misma hoja donde mostrarás los resultados.

Primero construye el motor.

Después construye la presentación.

---

# Consejo Profesional

En proyectos grandes incluso puedes separar el archivo en varias zonas.

```text
01_Datos

02_Modelo

03_Pivots

04_Dashboard

05_Documentación
```

Esta organización facilita el mantenimiento y permite que otros desarrolladores comprendan rápidamente la estructura del proyecto.

---

# Lo que aprendimos

Este caso nos enseñó que un Dashboard profesional debe separar claramente la lógica del negocio de la presentación visual.

Las Tablas Dinámicas cumplen el papel de motor.

El Dashboard cumple el papel de interfaz para el usuario.

Esa separación mejora la organización, el mantenimiento y la escalabilidad del proyecto.

---

# 🎯 ¿Cómo respondería esto en una entrevista?

**Pregunta**

¿Por qué decidió crear una hoja llamada **Pivots** en lugar de construir todo directamente en el Dashboard?

**Respuesta**

Porque las Tablas Dinámicas funcionan como la fuente de información del Dashboard. Mantenerlas en una hoja independiente facilita el mantenimiento, permite modificar la lógica sin afectar la presentación y deja un Dashboard mucho más limpio para el usuario final. Además, la hoja Pivots puede ocultarse al entregar el proyecto.

---

# Resumen del Caso

**Problema**

Quería construir todo directamente en el Dashboard.

---

**Causa**

No existía separación entre el desarrollo y la presentación.

---

**Solución**

Crear una hoja independiente llamada **Pivots** para alojar todas las Tablas Dinámicas y utilizar el Dashboard únicamente como capa de visualización.

---

**Lección Aprendida**

Un Dashboard profesional no solo depende de buenos gráficos; también depende de una arquitectura organizada. Separar la lógica del negocio de la presentación facilita el mantenimiento y mejora la calidad del proyecto.

---

# 🚀 Próximo caso

## 🏢 Caso Real #8

### ¿Por qué primero diseñamos el Dashboard en papel antes de abrir Excel?

En este caso descubrirás una práctica utilizada por consultores BI y equipos de desarrollo: diseñar la solución antes de construirla, evitando perder tiempo reorganizando gráficos, KPIs y segmentadores durante el desarrollo.

---

# 🏢 Caso Real #8

# ¿Por qué diseñamos el Dashboard antes de abrir Excel?

🟡 **Nivel 2 - Buena práctica utilizada por Consultores BI**

---

## Situación

Durante el desarrollo del Dashboard surgió una idea aparentemente sencilla.

> Abramos Excel y empecemos a insertar gráficos.

Parecía la forma más rápida de comenzar.

Sin embargo, después de crear los primeros gráficos comenzaron los problemas.

---

## Lo que pensé inicialmente

La idea era muy simple.

1. Crear KPIs.
2. Insertar gráficos.
3. Agregar Segmentadores.
4. Ajustar el diseño al final.

Pensé que sería más rápido.

---

## Descubriendo el problema

A medida que el Dashboard crecía comenzaron a aparecer inconvenientes.

Cada nuevo gráfico obligaba a mover los anteriores.

Los KPIs cambiaban constantemente de posición.

Los Segmentadores ocupaban demasiado espacio.

La Cronología no encontraba un lugar adecuado.

Cada modificación implicaba reorganizar prácticamente todo el Dashboard.

Comenzamos a invertir más tiempo acomodando objetos que analizando información.

---

# Entonces apareció una pregunta

Antes de seguir moviendo gráficos nos preguntamos.

> ¿Cómo queremos que el gerente vea la información?

Ese momento cambió completamente el proyecto.

---

# La solución

Antes de continuar desarrollando el Dashboard decidimos hacer un boceto.

No utilizamos Excel.

Simplemente dibujamos la distribución ideal.

```text
┌──────────────────────────────────────────────────────────────┐
│             DASHBOARD EJECUTIVO TELECOM                      │
├──────────────────────────────────────────────────────────────┤
│ KPI │ KPI │ KPI │ KPI │ KPI │ KPI │
├──────────────────────────────────────────────────────────────┤
│             Cliente                                          │
├───────────────────────────────┬──────────────────────────────┤
│ Técnico                       │ Ciudad                       │
├───────────────────────────────┼──────────────────────────────┤
│ Mes                           │ Tipo Servicio                │
├──────────────────────────────────────────────────────────────┤
│ Segmentadores                 │ Cronología                   │
└──────────────────────────────────────────────────────────────┘
```

A partir de ese momento todo comenzó a tener sentido.

---

# ¿Qué descubrimos?

Un Dashboard no debe organizarse pensando en Excel.

Debe organizarse pensando en el usuario.

---

# El recorrido del gerente

Imaginemos nuevamente la reunión.

Cuando un gerente abre un Dashboard normalmente hace el siguiente recorrido.

```text
1

Observa los KPIs.

↓

2

Observa los gráficos.

↓

3

Comienza a comparar resultados.

↓

4

Utiliza Segmentadores.

↓

5

Analiza el comportamiento en el tiempo.

↓

6

Toma decisiones.
```

Ese recorrido nos permitió definir exactamente dónde debía ubicarse cada elemento.

---

# Lo importante

No diseñamos el Dashboard para nosotros.

Lo diseñamos para quien tomará decisiones.

Ese cambio de perspectiva simplificó completamente el desarrollo.

---

# ¿Qué ventajas obtuvimos?

Después de realizar el boceto encontramos varias ventajas.

- Menos tiempo reorganizando objetos.
- Dashboard más limpio.
- Distribución uniforme.
- Mejor experiencia para el usuario.
- Desarrollo mucho más rápido.

---

# Regla de Oro

Nunca abras Excel sin tener una idea clara del Dashboard que vas a construir.

Primero diseña.

Después desarrolla.

---

# Consejo Profesional

En proyectos empresariales es común que el Dashboard sea aprobado antes de comenzar el desarrollo.

Muchas empresas realizan reuniones únicamente para validar el diseño.

Una vez aprobado el boceto comienza el trabajo técnico.

Esto evita realizar cambios costosos durante el desarrollo.

---

# Lo que aprendimos

El mayor tiempo de un proyecto BI no se invierte escribiendo fórmulas.

Se invierte pensando.

Comprender cómo el usuario consumirá la información es mucho más importante que insertar gráficos rápidamente.

Un buen diseño reduce retrabajos y mejora la comunicación de los resultados.

---

# 🎯 ¿Cómo respondería esto en una entrevista?

**Pregunta**

¿Por qué recomienda diseñar un Dashboard antes de comenzar a desarrollarlo?

**Respuesta**

Porque el diseño permite definir la distribución de KPIs, gráficos y filtros antes de invertir tiempo en la implementación. Esto reduce retrabajos, mejora la experiencia del usuario y garantiza que el Dashboard responda las preguntas del negocio de forma organizada.

---

# Resumen del Caso

**Problema**

Comenzamos a construir el Dashboard sin una planificación.

---

**Causa**

No existía un diseño previo.

---

**Solución**

Realizar un boceto antes de abrir Excel.

---

**Lección Aprendida**

Un Dashboard profesional comienza con un diseño, no con un gráfico.

---

# 🚀 Próximo caso

## 🏢 Caso Real #9

### ¿Por qué una misma Tabla Dinámica puede responder cientos de preguntas diferentes?

En este caso comprenderemos uno de los mayores beneficios del Modelo de Datos: reutilizar las mismas medidas DAX cambiando únicamente el contexto de análisis, sin escribir nuevas fórmulas.

---

# 🏢 Caso Real #9

# ¿Por qué una misma medida puede responder cientos de preguntas diferentes?

🔴 **Nivel 3 - Cambio de mentalidad en Business Intelligence**

---

## Situación

Después de construir la medida:

```DAX
Total Materiales :=
SUM(tblMateriales[Valor Total])
```

comenzamos a crear Tablas Dinámicas.

Primero analizamos:

```text
Cliente
```

Todo funcionó correctamente.

Después surgió una nueva necesidad.

> Ahora quiero analizar por Técnico.

La primera reacción fue pensar:

> Debo crear otra medida.

---

## Lo que pensé inicialmente

Las primeras ideas fueron.

- Una medida para Cliente.
- Otra para Técnico.
- Otra para Ciudad.
- Otra para Mes.
- Otra para Tipo de Servicio.

Parecía lógico.

Si cambia el análisis...

Debe cambiar la medida.

Pero ocurrió exactamente lo contrario.

---

## Descubriendo el problema

La medida nunca necesitó modificarse.

Seguía siendo exactamente la misma.

```DAX
Total Materiales :=
SUM(tblMateriales[Valor Total])
```

Lo único que cambiaba era el campo colocado en la Tabla Dinámica.

---

# Hagamos una prueba

## Primera Tabla Dinámica

Filas

```text
Cliente
```

Valores

```text
Total Materiales
```

---

## Segunda Tabla Dinámica

Filas

```text
Técnico
```

Valores

```text
Total Materiales
```

---

## Tercera Tabla Dinámica

Filas

```text
Ciudad
```

Valores

```text
Total Materiales
```

---

## Cuarta Tabla Dinámica

Filas

```text
Mes
```

Valores

```text
Total Materiales
```

---

## Quinta Tabla Dinámica

Filas

```text
Tipo Servicio
```

Valores

```text
Total Materiales
```

---

# Observa algo importante

¿Cuántas medidas utilizamos?

La respuesta es:

Una sola.

---

# Entonces...

¿Por qué obtenemos cinco informes completamente diferentes?

Porque Power Pivot utiliza el campo colocado en las filas para crear un nuevo contexto de filtro.

La medida permanece igual.

El análisis cambia.

---

# Pensándolo de otra manera

Imagina un contador de dinero.

Siempre suma.

No importa si cuentas:

- Pesos.
- Dólares.
- Euros.

La calculadora nunca cambia.

Lo único que cambian son los billetes.

Con DAX ocurre exactamente igual.

La medida siempre realiza el mismo cálculo.

Lo que cambia es el conjunto de registros sobre el cual trabaja.

---

# Lo importante

La verdadera inteligencia no está en crear muchas medidas.

La verdadera inteligencia consiste en crear medidas reutilizables.

Una buena medida puede alimentar:

- Tablas Dinámicas.
- KPIs.
- Gráficos.
- Dashboards.

Sin necesidad de volver a escribirla.

---

# Ejemplo

Nuestra medida:

```DAX
Total Materiales :=
SUM(tblMateriales[Valor Total])
```

alimentó:

✅ KPI Total Materiales.

✅ Materiales por Cliente.

✅ Materiales por Técnico.

✅ Materiales por Ciudad.

✅ Materiales por Mes.

✅ Materiales por Tipo de Servicio.

Todo utilizando exactamente la misma medida.

---

# ¿Qué cambió?

Nunca cambió la medida.

Cambiaron los campos utilizados para analizar la información.

Ese comportamiento es posible gracias al Modelo de Datos y al Contexto de Filtro.

---

# Regla de Oro

Antes de crear una nueva medida pregúntate.

> ¿Realmente necesito otra medida?

Muchas veces la respuesta será:

No.

Lo único que necesitas es cambiar el contexto de análisis.

---

# Consejo Profesional

Cuando desarrolles un Dashboard intenta construir medidas genéricas.

Por ejemplo.

```text
Total Ventas

Total Costos

Total Utilidad

Cantidad Pedidos

Promedio Ventas
```

Después reutilízalas en todos los informes.

Esto simplifica el mantenimiento y evita duplicar lógica.

---

# Lo que aprendimos

Este caso cambió completamente nuestra forma de trabajar.

Comprendimos que el objetivo no consiste en crear muchas medidas.

El objetivo consiste en crear pocas medidas bien diseñadas.

Una medida correctamente construida puede reutilizarse cientos de veces durante la vida del proyecto.

---

# 🎯 ¿Cómo respondería esto en una entrevista?

**Pregunta**

¿Por qué reutiliza la misma medida DAX en diferentes Tablas Dinámicas?

**Respuesta**

Porque las medidas DAX son cálculos dinámicos. La lógica permanece igual y el resultado cambia automáticamente según el contexto de filtro definido por la Tabla Dinámica, los Segmentadores o la Cronología. Esto permite reutilizar una misma medida en múltiples informes sin duplicar cálculos.

---

# Resumen del Caso

**Problema**

Pensaba que debía crear una medida diferente para cada análisis.

---

**Causa**

Confusión entre la lógica del cálculo y el contexto de análisis.

---

**Solución**

Reutilizar la misma medida y cambiar únicamente los campos utilizados en la Tabla Dinámica.

---

**Lección Aprendida**

Una medida bien diseñada puede alimentar decenas de KPIs, Tablas Dinámicas, gráficos y Dashboards.

La potencia de DAX no está en crear muchas medidas, sino en reutilizar las mismas de forma inteligente.

---

# 🚀 Próximo caso

## 🏢 Caso Real #10

### ¿Por qué el Modelo de Datos terminó siendo más importante que las fórmulas?

En este último caso comprenderemos la mayor lección aprendida durante toda la Academia: el éxito de un proyecto BI no depende de conocer muchas funciones, sino de construir correctamente el Modelo de Datos.

---

# 🏢 Caso Real #10

# ¿Por qué el Modelo de Datos terminó siendo más importante que las fórmulas?

🔴 **Nivel 3 - El mayor aprendizaje de toda la Academia**

---

## Situación

Cuando comenzamos el curso, la mayoría de las dudas estaban relacionadas con las fórmulas.

Preguntas como:

- ¿Qué función DAX debo utilizar?
- ¿Cómo hago un SUM?
- ¿Cómo calculo un promedio?
- ¿Cómo cuento registros?

Parecía que aprender Business Intelligence consistía en memorizar funciones.

Sin embargo, a medida que avanzamos en el laboratorio ocurrió algo inesperado.

Descubrimos que los mayores problemas nunca estaban en las fórmulas.

---

## Lo que pensé inicialmente

Al principio creía que para desarrollar un Dashboard profesional debía aprender muchas funciones DAX.

Pensaba que mientras más funciones conociera, mejores serían mis análisis.

Con el tiempo comprendí que estaba enfocando el problema desde el lugar equivocado.

---

## Descubriendo el problema

Durante el desarrollo del laboratorio aparecieron situaciones como:

- Relaciones 1:1 que realmente debían ser 1:N.
- Tablas que no estaban correctamente relacionadas.
- Medidas que parecían incorrectas.
- Campos Calculados que no aparecían.
- Resultados diferentes utilizando la misma medida.

Al analizarlas descubrimos algo sorprendente.

En casi todos los casos el problema no era DAX.

El problema estaba en el Modelo de Datos.

---

# Ejemplos reales

## Caso 1

La relación entre Pedidos e Instalaciones.

Pensábamos que Power Pivot estaba creando una relación incorrecta.

Después comprendimos que los datos representaban una relación 1:1.

La solución no fue modificar Power Pivot.

La solución fue modificar el modelo del negocio.

---

## Caso 2

No aparecía Campo Calculado.

Inicialmente parecía un error de Excel.

Después descubrimos que la Tabla Dinámica utilizaba el Modelo de Datos.

La solución consistió en crear una Medida DAX.

---

## Caso 3

Una medida devolvía resultados diferentes.

Pensábamos que la fórmula estaba mal.

Después comprendimos que el Contexto de Filtro había cambiado.

La medida era exactamente la misma.

---

## Caso 4

Queríamos crear un Dashboard.

Pensábamos comenzar insertando gráficos.

Finalmente comprendimos que el verdadero trabajo consistía en construir primero el Modelo de Datos.

---

# Entonces apareció una conclusión

Las fórmulas únicamente responden preguntas.

El Modelo de Datos define qué preguntas pueden responderse.

---

# Cambiando la forma de pensar

Antes del curso pensábamos así.

```text
Datos

↓

Fórmulas

↓

Resultado
```

Después del curso comprendimos que un proyecto BI funciona de otra manera.

```text
Datos

↓

Power Query

↓

Modelo de Datos

↓

Relaciones

↓

Medidas DAX

↓

Tablas Dinámicas

↓

Dashboard

↓

Toma de decisiones
```

Observa que DAX representa únicamente una etapa del proceso.

No es el punto de partida.

---

# Lo importante

Si el Modelo de Datos está mal diseñado.

Las mejores medidas DAX producirán resultados incorrectos.

Si el Modelo de Datos representa correctamente el negocio.

Las medidas serán sencillas.

Los Dashboards serán consistentes.

Y la información será confiable.

---

# Regla de Oro

Antes de escribir una nueva fórmula pregúntate.

> ¿Mi Modelo de Datos representa correctamente el negocio?

En muchas ocasiones esa pregunta resolverá el problema antes de escribir una sola línea de DAX.

---

# Consejo Profesional

Un Analista BI no comienza escribiendo medidas.

Comienza comprendiendo el negocio.

Posteriormente diseña el Modelo de Datos.

Solo cuando el modelo está correctamente construido comienza a desarrollar medidas DAX.

Esta metodología reduce errores y facilita el mantenimiento del proyecto.

---

# Lo que aprendimos

Durante toda la Academia descubrimos que el verdadero corazón de una solución BI no son las fórmulas.

Es el Modelo de Datos.

Las medidas, los KPIs, los gráficos y los Dashboards dependen completamente de la calidad del modelo.

Ese cambio de mentalidad representa probablemente la enseñanza más importante de todo el curso.

---

# 🎯 ¿Cómo respondería esto en una entrevista?

**Pregunta**

¿Cuál considera que es el componente más importante de una solución de Business Intelligence?

**Respuesta**

El Modelo de Datos.

Las medidas DAX, los KPIs y los Dashboards dependen de una estructura de datos correctamente diseñada. Un buen modelo simplifica el desarrollo, mejora el rendimiento y garantiza resultados consistentes. Las fórmulas son importantes, pero únicamente pueden ofrecer buenos resultados cuando el Modelo de Datos representa correctamente el negocio.

---

# Resumen del Caso

**Problema**

Pensaba que el éxito de un proyecto BI dependía de aprender muchas funciones DAX.

---

**Causa**

Enfoque centrado en las herramientas y no en el modelo.

---

**Solución**

Comprender que el Modelo de Datos es el núcleo de toda solución BI.

---

**Lección Aprendida**

El mayor aprendizaje de esta Academia no fue memorizar funciones.

Fue aprender a modelar correctamente la información para responder preguntas del negocio.

---

# 🏆 Conclusión de la Primera Parte

Los diez primeros casos demostraron que los problemas más importantes de un proyecto BI rara vez se resuelven aprendiendo una nueva función.

La mayoría se solucionan comprendiendo mejor el negocio, diseñando correctamente el Modelo de Datos y entendiendo cómo trabajan Power Query, Power Pivot y DAX en conjunto.

A partir de este momento ya no verás Excel únicamente como una hoja de cálculo.

Lo verás como una plataforma de Business Intelligence capaz de transformar datos en información para apoyar la toma de decisiones.