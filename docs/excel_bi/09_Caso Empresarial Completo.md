# 📘 Módulo 09 - Proyecto Empresarial Integrador

> 📚 **Curso:** Excel BI para Analistas de Datos
>
> 📖 **Módulo:** 09 - Proyecto Empresarial Integrador
>
> 🎯 **Nivel:** Avanzado
>
> ⏱️ **Duración estimada:** 120 minutos

---

# 🎯 Objetivo

Aplicar todos los conocimientos adquiridos durante el curso para desarrollar un proyecto de Business Intelligence utilizando Excel, Power Query, Power Pivot y DAX.

Al finalizar este módulo serás capaz de abordar un requerimiento empresarial siguiendo una metodología profesional, desde el análisis del problema hasta la entrega de un Dashboard Ejecutivo.

---

# 🏢 Caso Empresarial

Has sido contratado como Analista BI por una empresa de telecomunicaciones.

La gerencia necesita conocer el comportamiento operativo de la organización para apoyar la toma de decisiones.

Actualmente la información se encuentra distribuida en diferentes tablas y resulta difícil obtener respuestas rápidas.

La empresa solicita construir un Dashboard Ejecutivo que permita analizar la operación desde diferentes perspectivas.

---

# 🎯 Requerimiento del Cliente

Durante la reunión inicial, la gerencia plantea las siguientes preguntas:

- ¿Cuál es el valor total de materiales utilizados?
- ¿Cuántos pedidos fueron ejecutados?
- ¿Cuál es el valor promedio de los materiales?
- ¿Cuál es el material más costoso?
- ¿Cuál es el material de menor valor?
- ¿Cuántos materiales diferentes se utilizan?

Además, desean analizar la información por:

- Cliente
- Técnico
- Ciudad
- Tipo de Servicio
- Mes

También solicitan que el Dashboard permita filtrar la información utilizando controles interactivos.

---

# 📋 Analizando el requerimiento

Antes de abrir Excel debemos comprender qué está solicitando realmente el cliente.

Observemos las preguntas planteadas.

| Pregunta | Tipo de análisis |
|----------|------------------|
| Total de materiales | KPI |
| Total de pedidos | KPI |
| Promedio | KPI |
| Máximo | KPI |
| Mínimo | KPI |
| Materiales diferentes | KPI |
| Cliente | Análisis |
| Técnico | Análisis |
| Ciudad | Análisis |
| Mes | Tendencia |
| Tipo de Servicio | Comparativo |

Este análisis inicial permitirá definir la estructura del Dashboard.

---

# 🧠 Pensando como un Analista BI

Uno de los errores más comunes consiste en abrir Excel inmediatamente.

Un Analista BI primero comprende el problema de negocio.

Después diseña la solución.

Finalmente utiliza las herramientas para implementarla.

Por esta razón, antes de construir cualquier Dashboard debemos responder las siguientes preguntas.

---

# Pregunta 1

## ¿Qué información necesita la gerencia?

La gerencia requiere conocer indicadores que permitan evaluar el comportamiento general de la operación.

Estos indicadores se convertirán posteriormente en KPIs.

---

# Pregunta 2

## ¿Qué dimensiones utilizarán para analizar la información?

Nuestro Modelo de Datos contiene varias dimensiones.

Las principales serán:

- Cliente
- Técnico
- Ciudad
- Tipo de Servicio
- Fecha

Estas dimensiones permitirán responder diferentes preguntas sin modificar las medidas DAX.

---

# Pregunta 3

## ¿Qué información cambiará mediante filtros?

El Dashboard deberá permitir analizar la información utilizando:

- Segmentadores.
- Cronologías.

De esta forma el usuario podrá navegar libremente por los datos.

---

# Arquitectura de la solución

Antes de comenzar el desarrollo definiremos la arquitectura del proyecto.

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

Columnas Calculadas

↓

Tablas Dinámicas

↓

KPIs

↓

Dashboard Ejecutivo
```

Este flujo será el mismo utilizado en proyectos reales de Business Intelligence.

---

# 📂 Revisando el archivo

Trabajaremos con el archivo:

```text
Empresa_Telecom_ExcelBI_v3.xlsx
```

Este archivo contiene:

- Clientes
- Técnicos
- Pedidos
- Materiales
- Instalaciones
- Calendario

Además del Modelo de Datos construido durante los módulos anteriores.

---

# Verificación inicial

Antes de desarrollar el Dashboard realizaremos una revisión general del proyecto.

Debemos verificar:

- Que todas las tablas se encuentren cargadas en el Modelo de Datos.
- Que las relaciones sean correctas.
- Que las medidas DAX funcionen correctamente.
- Que las columnas calculadas existan.
- Que no existan errores de relaciones.

Esta etapa corresponde al proceso de validación previo al desarrollo.

---

# 📝 Lista de verificación

Antes de continuar verifica que el proyecto cumpla los siguientes requisitos.

| Elemento | Estado |
|----------|---------|
| Modelo de Datos | ✅ |
| Relaciones | ✅ |
| Medidas DAX | ✅ |
| Columnas Calculadas | ✅ |
| Tablas Dinámicas | ✅ |
| Hoja Dashboard | ✅ |

Cuando todos estos elementos estén disponibles podremos comenzar el desarrollo del Dashboard Ejecutivo.

---

# Concepto importante

Observa que todavía no hemos construido ningún gráfico.

Tampoco hemos comenzado el Dashboard.

En un proyecto empresarial, gran parte del trabajo consiste en comprender el problema y validar que la información esté preparada para el análisis.

Un Dashboard construido sobre datos incorrectos producirá decisiones incorrectas.

Por esta razón, la validación del Modelo de Datos es una de las etapas más importantes del proyecto.

---

# 🎯 Objetivo de la siguiente etapa

En la siguiente parte comenzaremos el desarrollo del Dashboard Ejecutivo.

Construiremos:

- Los KPIs.
- La distribución visual del Dashboard.
- Los gráficos principales.
- Los Segmentadores.
- La Cronología.

A partir de ese momento la solución comenzará a tomar forma como un proyecto real de Business Intelligence.

---

# 🏗 Etapa 1 - Diseño de la Solución BI

Después de comprender el requerimiento del cliente debemos definir cómo construiremos la solución.

Uno de los errores más comunes consiste en comenzar creando gráficos sin una planificación previa.

En proyectos reales primero diseñamos la arquitectura del Dashboard.

Posteriormente comenzamos el desarrollo.

---

# ¿Qué debe responder nuestro Dashboard?

Antes de construir cualquier visualización debemos identificar qué preguntas responderá.

Nuestro Dashboard deberá responder, como mínimo, las siguientes preguntas.

## Indicadores Generales

- ¿Cuál es el valor total de materiales?
- ¿Cuántos pedidos fueron ejecutados?
- ¿Cuál es el valor promedio?
- ¿Cuál fue el valor máximo?
- ¿Cuál fue el valor mínimo?
- ¿Cuántos materiales diferentes existen?

Estos indicadores serán los primeros elementos que visualizará la gerencia.

---

## Análisis Operacionales

Posteriormente el Dashboard permitirá analizar la operación mediante diferentes dimensiones.

Queremos responder preguntas como:

- ¿Qué cliente consume más materiales?
- ¿Qué técnico ejecutó más trabajos?
- ¿Qué ciudad registra el mayor consumo?
- ¿Cómo se comporta el consumo durante el año?
- ¿Qué tipo de servicio genera mayor utilización de materiales?

---

# Boceto del Dashboard

Antes de comenzar el desarrollo realizaremos un bosquejo.

No importa si el diseño cambia posteriormente.

Lo importante es tener una idea clara de la distribución.

```text
┌──────────────────────────────────────────────────────────────┐
│        DASHBOARD EJECUTIVO - EMPRESA TELECOM                │
├──────────────────────────────────────────────────────────────┤
│ KPI │ KPI │ KPI │ KPI │ KPI │ KPI │
├──────────────────────────────────────────────────────────────┤
│           Materiales por Cliente                            │
├───────────────────────────────┬──────────────────────────────┤
│ Materiales por Técnico        │ Materiales por Ciudad        │
├───────────────────────────────┼──────────────────────────────┤
│ Materiales por Mes            │ Tipo de Servicio             │
├──────────────────────────────────────────────────────────────┤
│ Segmentadores                 │ Cronología                   │
└──────────────────────────────────────────────────────────────┘
```

Este será nuestro plano de construcción.

---

# ¿Por qué hacer un boceto?

El boceto evita construir elementos sin una organización definida.

En proyectos empresariales normalmente se realiza un diseño previo antes de comenzar el desarrollo.

Esto permite identificar:

- Espacios disponibles.
- Cantidad de gráficos.
- Ubicación de KPIs.
- Distribución de filtros.
- Experiencia del usuario.

---

# Definiendo los KPIs

Los primeros elementos del Dashboard serán los indicadores principales.

Trabajaremos con las siguientes medidas DAX.

| KPI | Medida |
|------|---------|
| Total Materiales | Total Materiales |
| Total Pedidos | Total Pedidos |
| Promedio | Promedio Materiales |
| Valor Máximo | Valor Máximo |
| Valor Mínimo | Valor Mínimo |
| Materiales Diferentes | Materiales Diferentes |

Estos indicadores permitirán conocer el estado general de la operación.

---

# Definiendo los gráficos

Cada gráfico debe responder una única pregunta del negocio.

| Gráfico | Pregunta |
|----------|----------|
| Cliente | ¿Qué cliente consume más materiales? |
| Técnico | ¿Qué técnico ejecuta más pedidos? |
| Ciudad | ¿Qué ciudad presenta mayor consumo? |
| Mes | ¿Cómo evoluciona el consumo durante el tiempo? |
| Tipo de Servicio | ¿Qué servicio representa mayor utilización? |

---

# Definiendo la navegación

Un Dashboard moderno debe permitir explorar la información.

Por esta razón agregaremos controles interactivos.

Utilizaremos:

## Segmentadores

- Cliente
- Ciudad
- Técnico
- Tipo de Servicio

Estos controles permitirán cambiar el análisis con un solo clic.

---

## Cronología

La Cronología permitirá navegar por:

- Año
- Trimestre
- Mes

Esto facilitará el análisis temporal del negocio.

---

# Diseñando la experiencia del usuario

Imagina que eres el gerente y acabas de abrir el Dashboard.

¿Cuál sería el recorrido natural?

## Paso 1

Leer los KPIs.

Pregunta:

> ¿Cómo va la operación?

---

## Paso 2

Observar los gráficos.

Pregunta:

> ¿Dónde están ocurriendo los cambios más importantes?

---

## Paso 3

Aplicar filtros.

Pregunta:

> ¿Qué ocurre si analizo únicamente Medellín?

---

## Paso 4

Analizar el tiempo.

Pregunta:

> ¿Cómo cambió el comportamiento durante el año?

---

## Paso 5

Tomar decisiones.

Un Dashboard no tiene como objetivo mostrar información.

Su verdadero objetivo consiste en facilitar la toma de decisiones.

---

# Concepto BI

Observa que nuestro Dashboard contará una historia.

No será simplemente un conjunto de gráficos.

Responderá un conjunto de preguntas de negocio utilizando información organizada de manera lógica.

Este enfoque recibe el nombre de **Data Storytelling**.

En lugar de mostrar datos, construiremos una historia que ayude a comprender el comportamiento de la operación.

---

# Antes de comenzar el desarrollo

Verifica nuevamente:

✅ Modelo de Datos.

✅ Relaciones.

✅ Medidas DAX.

✅ Columnas Calculadas.

✅ Tablas Dinámicas.

✅ Hoja Dashboard.

Cuando todo esté listo comenzaremos la construcción del Dashboard Ejecutivo.

---

# 🎯 Objetivo de la siguiente etapa

En la tercera parte construiremos el Dashboard paso a paso.

Aprenderemos a:

- Organizar los KPIs.
- Insertar Gráficos Dinámicos.
- Aplicar formato profesional.
- Conectar Segmentadores.
- Configurar la Cronología.
- Preparar el Dashboard para su presentación a la gerencia.

---

# 🧠 Etapa 2 - Traduciendo las preguntas del negocio en información

Hasta este momento ya conocemos el requerimiento del cliente.

Ahora debemos responder una pregunta muy importante.

> ¿Cómo convertimos esas necesidades del negocio en un Dashboard?

Un Dashboard no se construye agregando gráficos al azar.

Cada gráfico, cada KPI y cada filtro debe responder una necesidad específica del usuario.

Por esta razón, antes de abrir Excel realizaremos un ejercicio de análisis.

---

# Pregunta 1

## ¿Qué quiere conocer la gerencia en los primeros 5 segundos?

Normalmente un gerente desea conocer el estado general del negocio.

No necesita revisar el detalle de cada pedido.

Necesita indicadores rápidos.

Por esta razón, la primera fila del Dashboard estará compuesta por KPIs.

Estos responderán preguntas como:

- ¿Cuántos pedidos existen?
- ¿Cuál es el valor total de materiales?
- ¿Cuál es el valor promedio?
- ¿Cuál fue el mayor valor registrado?
- ¿Cuál fue el menor valor?
- ¿Cuántos materiales diferentes utilizamos?

Estos indicadores permitirán obtener una visión general del negocio.

---

# Pregunta 2

## ¿Qué necesita investigar después?

Una vez revisados los indicadores, normalmente surge una segunda necesidad.

Comprender por qué los resultados son así.

Para ello construiremos gráficos que permitan analizar diferentes dimensiones del negocio.

---

# Cliente

Pregunta de negocio:

> ¿Qué clientes generan el mayor consumo de materiales?

Visual recomendado:

Gráfico de columnas.

---

# Técnico

Pregunta de negocio:

> ¿Qué técnicos ejecutan la mayor cantidad de trabajos?

Visual recomendado:

Gráfico de barras.

---

# Ciudad

Pregunta de negocio:

> ¿En qué ciudades se concentra la operación?

Visual recomendado:

Gráfico circular o barras.

---

# Mes

Pregunta de negocio:

> ¿Cómo evoluciona el comportamiento durante el año?

Visual recomendado:

Gráfico de líneas.

---

# Tipo de Servicio

Pregunta de negocio:

> ¿Qué tipo de servicio representa el mayor consumo?

Visual recomendado:

Gráfico de columnas.

---

# Pregunta 3

## ¿Qué pasará si el gerente desea profundizar en la información?

Aquí aparecen los controles interactivos.

No construiremos un Dashboard estático.

Construiremos un Dashboard dinámico.

Utilizaremos:

- Segmentadores.
- Cronología.

De esta manera el usuario podrá realizar su propio análisis.

---

# Un ejemplo

Supongamos que el gerente selecciona:

Ciudad = Medellín

En ese momento cambiarán automáticamente:

- Los KPIs.
- Los gráficos.
- Las Tablas Dinámicas.

No será necesario modificar ninguna fórmula.

Esto ocurre gracias al Modelo de Datos y a las medidas DAX.

---

# Pensando como un Consultor BI

En este punto debemos hacernos una pregunta.

> ¿Cada elemento del Dashboard responde una necesidad del negocio?

Si la respuesta es NO...

Ese elemento probablemente no debería existir.

Un Dashboard profesional muestra únicamente la información necesaria para tomar decisiones.

---

# Definiendo el recorrido del usuario

Todo Dashboard cuenta una historia.

Nuestro recorrido será el siguiente.

```text
1. Observar los KPIs.

↓

2. Identificar tendencias.

↓

3. Analizar gráficos.

↓

4. Aplicar filtros.

↓

5. Investigar el detalle.

↓

6. Tomar decisiones.
```

Observa que el usuario nunca comienza revisando tablas.

Comienza comprendiendo el estado general del negocio.

---

# Regla de Oro

Antes de insertar cualquier gráfico pregúntate:

> ¿Qué pregunta del negocio responderá este gráfico?

Si no puedes responder esa pregunta, probablemente el gráfico no sea necesario.

---

# Arquitectura definitiva del Dashboard

```text
                      DASHBOARD

────────────────────────────────────────────

      KPIs (Estado General)

────────────────────────────────────────────

 Cliente          Ciudad

────────────────────────────────────────────

 Técnico          Mes

────────────────────────────────────────────

 Tipo Servicio

────────────────────────────────────────────

 Segmentadores

 Cronología

────────────────────────────────────────────

 Toma de decisiones
```

Este será el diseño que construiremos durante la siguiente etapa.

---

# 🎯 Objetivo de la siguiente etapa

En la cuarta parte construiremos físicamente el Dashboard.

Aprenderemos a:

- Distribuir correctamente los KPIs.
- Crear tarjetas de indicadores.
- Insertar Gráficos Dinámicos.
- Conectar Segmentadores.
- Configurar la Cronología.
- Aplicar formato ejecutivo.
- Preparar el Dashboard para una reunión con gerencia.

---

# 🏗 Etapa 3 - Construcción del Dashboard Ejecutivo

Hasta este momento hemos realizado el trabajo más importante de un Analista BI.

✔ Comprendimos el problema.

✔ Analizamos el requerimiento.

✔ Identificamos los indicadores.

✔ Diseñamos el Dashboard.

Ahora comenzaremos la implementación.

---

# Regla No. 1

## No comenzar por los gráficos

Un error muy frecuente consiste en insertar gráficos inmediatamente.

En un proyecto profesional el desarrollo comienza organizando el espacio de trabajo.

Primero construiremos la estructura.

Después agregaremos la información.

Finalmente aplicaremos el diseño.

---

# Paso 1 - Preparar la hoja Dashboard

Crear una hoja llamada:

```text
Dashboard
```

Aplicar las siguientes configuraciones.

- Ocultar líneas de cuadrícula.
- Ajustar el ancho de columnas.
- Ajustar la altura de filas.
- Definir un espacio para el título.
- Reservar un área para KPIs.
- Reservar un área para gráficos.
- Reservar un área para Segmentadores.

Nuestro Dashboard comenzará completamente vacío.

---

# Paso 2 - Definir la distribución

Trabajaremos siguiendo el siguiente esquema.

```text
┌────────────────────────────────────────────────────────────┐
│               DASHBOARD EJECUTIVO TELECOM                  │
├────────────────────────────────────────────────────────────┤
│ KPI │ KPI │ KPI │ KPI │ KPI │ KPI │
├────────────────────────────────────────────────────────────┤
│                 Cliente                                    │
├───────────────────────────────┬────────────────────────────┤
│ Técnico                       │ Ciudad                     │
├───────────────────────────────┼────────────────────────────┤
│ Mes                           │ Tipo Servicio              │
├────────────────────────────────────────────────────────────┤
│ Segmentadores                 │ Cronología                 │
└────────────────────────────────────────────────────────────┘
```

Este será nuestro plano de construcción.

---

# ¿Por qué este orden?

Porque corresponde al recorrido natural del usuario.

Primero observa el estado general.

Después identifica tendencias.

Finalmente profundiza utilizando filtros.

---

# Paso 3 - Construcción de los KPIs

La primera fila del Dashboard contendrá los indicadores principales.

Trabajaremos con las siguientes medidas.

| KPI | Medida DAX |
|------|------------|
| Total Materiales | Total Materiales |
| Total Pedidos | Total Pedidos |
| Promedio | Promedio Materiales |
| Valor Máximo | Valor Máximo |
| Valor Mínimo | Valor Mínimo |
| Materiales Diferentes | Materiales Diferentes |

Estos indicadores responderán la pregunta:

> ¿Cómo va el negocio?

---

# Paso 4 - Construcción de los gráficos

Cada gráfico responderá únicamente una pregunta del negocio.

| Gráfico | Pregunta |
|----------|----------|
| Cliente | ¿Qué cliente consume más materiales? |
| Técnico | ¿Qué técnico ejecuta más pedidos? |
| Ciudad | ¿Qué ciudad registra mayor consumo? |
| Mes | ¿Cómo evoluciona el consumo durante el año? |
| Tipo Servicio | ¿Qué servicio representa mayor utilización? |

---

# Regla BI

Nunca insertes un gráfico porque "se ve bonito".

Primero responde:

> ¿Qué pregunta resolverá?

Si no existe una pregunta...

El gráfico probablemente no sea necesario.

---

# Paso 5 - Agregar Segmentadores

Insertaremos Segmentadores para permitir el análisis interactivo.

Campos sugeridos.

- Cliente
- Ciudad
- Técnico
- Tipo Servicio

Todos los Segmentadores deberán conectarse a todas las Tablas Dinámicas.

Esto garantizará que el Dashboard permanezca sincronizado.

---

# Paso 6 - Agregar Cronología

Insertaremos una Cronología utilizando el campo:

```text
Fecha
```

La Cronología permitirá navegar fácilmente por:

- Año
- Trimestre
- Mes

Esto facilitará el análisis histórico.

---

# Paso 7 - Aplicar formato ejecutivo

Antes de entregar el Dashboard revisaremos.

- Todos los gráficos tienen título.
- Los KPIs utilizan el mismo tamaño.
- Los colores son consistentes.
- Los Segmentadores están alineados.
- Existe suficiente espacio entre objetos.
- No hay elementos superpuestos.

Un Dashboard limpio facilita la interpretación de la información.

---

# Revisión final

Antes de presentar el proyecto verifica.

□ Los KPIs responden correctamente.

□ Los gráficos muestran información consistente.

□ Los Segmentadores filtran todo el Dashboard.

□ La Cronología funciona correctamente.

□ No existen errores en las medidas DAX.

□ El Dashboard responde todas las preguntas del negocio.

---

# Entrega al cliente

Una vez finalizado el desarrollo ocultaremos la hoja:

```text
Pivots
```

El usuario únicamente visualizará:

```text
Dashboard
```

Toda la lógica permanecerá funcionando porque las Tablas Dinámicas seguirán alimentando los gráficos y KPIs desde la hoja oculta.

---

# 🎯 Resultado esperado

Al finalizar esta etapa tendremos un Dashboard Ejecutivo completamente funcional.

El usuario podrá:

✔ Consultar indicadores.

✔ Analizar tendencias.

✔ Aplicar filtros.

✔ Navegar por períodos.

✔ Obtener respuestas sin modificar ninguna fórmula.

Este es precisamente el objetivo de una solución de Business Intelligence.

---

# 🚀 Continuará...

En la siguiente parte nos pondremos en el papel del Analista BI durante la presentación del proyecto.

Aprenderemos cómo defender técnicamente el Dashboard, responder preguntas de la gerencia y justificar las decisiones de diseño tomadas durante el desarrollo.

---

# 🎤 Etapa 4 - Presentación del Proyecto a la Gerencia

Felicitaciones.

El Dashboard Ejecutivo ha sido finalizado.

Sin embargo, el trabajo de un Analista BI no termina cuando desarrolla la solución.

Ahora comienza una de las etapas más importantes.

Presentar los resultados.

Un Dashboard únicamente genera valor cuando ayuda a tomar decisiones.

Por esta razón, aprenderemos cómo explicar nuestro trabajo durante una reunión.

---

# Antes de comenzar la reunión

Como Analista BI debes asegurarte de que el Dashboard responda correctamente todas las preguntas planteadas por el cliente.

Antes de ingresar a la reunión verifica:

✅ El Dashboard actualiza correctamente.

✅ Todos los KPIs funcionan.

✅ Los Segmentadores filtran toda la información.

✅ La Cronología responde correctamente.

✅ Las medidas DAX producen resultados consistentes.

✅ No existen errores visibles.

---

# Simulación de una reunión

A continuación realizaremos una simulación similar a la que podrías enfrentar durante una presentación real.

---

# 👨‍💼 Gerente

Buenos días.

¿Podría explicarnos qué información estamos observando?

---

# 👨‍💻 Analista BI

Claro.

El Dashboard resume el comportamiento operativo de la empresa utilizando información consolidada dentro del Modelo de Datos.

En la parte superior encontramos los principales indicadores del negocio.

En la parte central se presentan los análisis por Cliente, Técnico, Ciudad, Mes y Tipo de Servicio.

Finalmente contamos con Segmentadores y una Cronología que permiten explorar la información de forma interactiva.

---

# 👨‍💼 Gerente

¿Por qué decidió colocar primero los KPIs?

---

# 👨‍💻 Analista BI

Porque representan el estado general del negocio.

En pocos segundos permiten conocer:

- Total de Materiales.
- Total de Pedidos.
- Promedio.
- Valor Máximo.
- Valor Mínimo.
- Cantidad de Materiales Diferentes.

Una vez comprendido el panorama general, los gráficos ayudan a investigar las causas.

---

# 👨‍💼 Gerente

¿De dónde provienen esos indicadores?

---

# 👨‍💻 Analista BI

Todos los indicadores fueron construidos mediante Medidas DAX.

Las medidas utilizan información del Modelo de Datos.

Por esta razón no existen fórmulas distribuidas por todo el libro.

Toda la lógica permanece centralizada dentro de Power Pivot.

---

# 👨‍💼 Gerente

¿Cómo puedo consultar únicamente la información de Medellín?

---

# 👨‍💻 Analista BI

Simplemente seleccionamos Medellín en el Segmentador de Ciudad.

Automáticamente se actualizan:

- Los KPIs.
- Los gráficos.
- Las Tablas Dinámicas.

Todo ocurre gracias al Modelo de Datos y a las relaciones creadas durante el desarrollo.

---

# 👨‍💼 Gerente

¿Qué ocurre si mañana llegan nuevos pedidos?

---

# 👨‍💻 Analista BI

El proceso de actualización es muy sencillo.

1. Actualizamos los datos mediante Power Query.
2. El Modelo de Datos se actualiza.
3. Las medidas DAX recalculan los indicadores.
4. Las Tablas Dinámicas se actualizan.
5. El Dashboard refleja automáticamente la nueva información.

No es necesario reconstruir el Dashboard.

---

# 👨‍💼 Gerente

¿Cómo sabemos que los resultados son confiables?

---

# 👨‍💻 Analista BI

Porque el proyecto fue construido siguiendo una metodología de Business Intelligence.

Durante el desarrollo:

- Se validó la calidad de los datos.
- Se construyó un Modelo de Datos.
- Se definieron relaciones.
- Se utilizaron medidas DAX.
- Se verificaron los resultados mediante Tablas Dinámicas.

Esto garantiza consistencia en toda la información.

---

# Preguntas técnicas

Además de la gerencia, en algunos proyectos otros desarrolladores pueden realizar preguntas técnicas.

Veamos algunos ejemplos.

---

## Pregunta

¿Por qué utilizó Power Pivot?

### Respuesta

Porque permite trabajar con un Modelo de Datos, crear relaciones entre tablas y desarrollar medidas DAX reutilizables.

Esto mejora considerablemente el rendimiento frente al uso de fórmulas tradicionales.

---

## Pregunta

¿Por qué creó medidas y no únicamente fórmulas?

### Respuesta

Las medidas pueden reutilizarse en cualquier Tabla Dinámica o Dashboard.

Además responden automáticamente al contexto de filtro.

Esto facilita el mantenimiento del proyecto.

---

## Pregunta

¿Por qué utilizó un Modelo de Datos?

### Respuesta

Porque la información se encuentra distribuida en diferentes tablas relacionadas.

El Modelo de Datos permite analizarlas sin necesidad de duplicar información ni utilizar funciones como BUSCARV.

---

## Pregunta

¿Por qué ocultó la hoja Pivots?

### Respuesta

Porque esa hoja corresponde al motor del Dashboard.

El usuario únicamente necesita visualizar el Dashboard.

La lógica del proyecto permanece protegida y organizada.

---

# ¿Qué aprendimos durante este proyecto?

Durante este proyecto desarrollamos una solución completa de Business Intelligence.

El flujo de trabajo fue el siguiente.

```text
Requerimiento del negocio

↓

Análisis del problema

↓

Power Query

↓

Modelo de Datos

↓

Relaciones

↓

Medidas DAX

↓

Columnas Calculadas

↓

Tablas Dinámicas

↓

KPIs

↓

Dashboard

↓

Presentación a Gerencia
```

Observa que Excel representa únicamente una parte del proceso.

Lo más importante consiste en comprender el problema del negocio.

---

# 🏢 Aplicación en proyectos reales

La metodología aprendida puede utilizarse en proyectos como:

- Control ANS.
- Inventarios.
- Conciliaciones.
- DRACO.
- Interventoría.
- Indicadores de Producción.
- Ventas.
- Logística.
- Operaciones.

El flujo de trabajo será exactamente el mismo.

Cambiarán únicamente los datos.

---

# 📝 Lo que aprendí

Durante este proyecto comprendí que desarrollar un Dashboard no consiste únicamente en insertar gráficos.

Un Analista BI debe comprender el problema del negocio, diseñar una solución, construir un Modelo de Datos, crear medidas DAX, desarrollar un Dashboard interactivo y presentar los resultados de manera clara para facilitar la toma de decisiones.

Ahora soy capaz de desarrollar una solución completa de Business Intelligence utilizando Excel.

---

# 🏆 Proyecto Finalizado

¡Felicitaciones!

Has completado el Proyecto Empresarial Integrador.

A partir de este momento cuentas con las bases necesarias para desarrollar Dashboards profesionales utilizando:

- Excel.
- Power Query.
- Power Pivot.
- DAX.
- Tablas Dinámicas.
- KPIs.
- Segmentadores.
- Cronologías.

Más importante aún, has aprendido una metodología de trabajo utilizada por Analistas BI para transformar datos en información útil para la toma de decisiones.

---

# 🚀 Próximo módulo

## 📘 Módulo 10 - Trucos y Casos Reales de Power Pivot

En el siguiente módulo aprenderemos situaciones reales que aparecen durante el desarrollo de proyectos, errores frecuentes, soluciones prácticas y técnicas que aumentarán tu productividad trabajando con Excel BI.