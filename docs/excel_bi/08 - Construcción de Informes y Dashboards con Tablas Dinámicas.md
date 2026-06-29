# 📘 Módulo 08 - Construcción de Informes y Dashboards con Tablas Dinámicas

> 📚 **Curso:** Excel BI para Analistas de Datos
>
> 📖 **Módulo:** 08 - Construcción de Informes y Dashboards con Tablas Dinámicas
>
> 🎯 **Nivel:** Intermedio - Avanzado
>
> ⏱️ **Duración estimada:** 90 minutos

---

# 🎯 Objetivo

Aprender a construir informes profesionales utilizando Tablas Dinámicas basadas en el Modelo de Datos.

Al finalizar este módulo comprenderás que las Tablas Dinámicas no son el producto final, sino el motor que alimenta un Dashboard profesional en Excel.

---

# 📖 Recordando el camino recorrido

Durante los módulos anteriores construimos toda la infraestructura necesaria para realizar análisis profesionales.

Aprendimos a:

- Importar datos con Power Query.
- Crear un Modelo de Datos.
- Relacionar tablas.
- Construir medidas DAX.
- Crear columnas calculadas.

Ahora utilizaremos todo ese trabajo para construir un Dashboard.

---

# Un error muy común

Muchos usuarios creen que un Dashboard comienza creando gráficos.

En realidad ocurre exactamente al contrario.

Primero debemos construir una buena fuente de información.

Después construiremos el Dashboard.

Por esta razón, las Tablas Dinámicas son uno de los componentes más importantes de Excel BI.

---

# ¿Qué es una Tabla Dinámica?

Una Tabla Dinámica es un informe dinámico capaz de resumir grandes cantidades de información sin necesidad de utilizar fórmulas tradicionales.

Cuando trabaja junto al Modelo de Datos puede utilizar:

- Relaciones
- Medidas DAX
- Columnas Calculadas
- Segmentadores
- Cronologías

Esto la convierte en el motor principal de un Dashboard.

---

# La arquitectura de Excel BI

Antes de construir el Dashboard debemos comprender cómo fluye la información dentro de un proyecto BI.

```text
                 Power Query
                      │
                      ▼
              Modelo de Datos
                      │
                      ▼
               Medidas DAX
                      │
                      ▼
         Tablas Dinámicas (Motor)
        ┌─────────┼──────────┐
        ▼         ▼          ▼
      KPIs    Gráficos   Segmentadores
                      │
                      ▼
              Dashboard Final
```

Esta arquitectura será la misma que utilizaremos en proyectos empresariales.

---

# Concepto clave

Las Tablas Dinámicas **NO son el Dashboard**.

Las Tablas Dinámicas son el **motor** que alimenta el Dashboard.

El Dashboard únicamente muestra la información procesada.

---

# ¿Por qué utilizar Tablas Dinámicas?

Supongamos que el gerente pregunta:

- ¿Cuál fue el cliente con mayor consumo?
- ¿Qué técnico realizó más instalaciones?
- ¿Qué ciudad utilizó más materiales?
- ¿Cuál fue el mes con mayor valor instalado?

Todas estas preguntas serán respondidas por diferentes Tablas Dinámicas.

Después utilizaremos esos resultados para construir gráficos e indicadores.

---

# Organización profesional del libro

En proyectos empresariales no es recomendable mezclar todo en una sola hoja.

Una estructura profesional podría ser la siguiente:

```text
Empresa_Telecom_ExcelBI_v3.xlsx

│

├── Clientes
├── Técnicos
├── Pedidos
├── Materiales
├── Instalaciones
├── Calendario

│

├── Pivots

│

└── Dashboard
```

Cada hoja cumple una función específica.

---

# ¿Qué contiene cada hoja?

## Hojas de datos

Contienen la información proveniente de Power Query y del Modelo de Datos.

Ejemplos:

- Clientes
- Técnicos
- Pedidos
- Materiales
- Instalaciones
- Calendario

Estas hojas normalmente no son utilizadas directamente por el usuario final.

---

## Hoja Pivots

Esta hoja contendrá todas las Tablas Dinámicas utilizadas por el Dashboard.

Aquí construiremos diferentes análisis como:

- Materiales por Cliente.
- Materiales por Técnico.
- Materiales por Ciudad.
- Materiales por Mes.
- Materiales por Tipo de Servicio.

Esta hoja funcionará como el motor del Dashboard.

---

## Hoja Dashboard

Será la única hoja visible para la gerencia.

Aquí colocaremos:

- Indicadores (KPIs).
- Gráficos Dinámicos.
- Segmentadores.
- Cronologías.
- Títulos.
- Diseño corporativo.

La información mostrada provendrá de las Tablas Dinámicas construidas en la hoja **Pivots**.

---

# Laboratorio

## Paso 1

Crear una nueva hoja llamada:

```text
Pivots
```

Esta hoja almacenará todas las Tablas Dinámicas del proyecto.

---

## Paso 2

Crear otra hoja llamada:

```text
Dashboard
```

Por el momento permanecerá vacía.

Más adelante construiremos el Dashboard completo.

---

# ¿Por qué separar Pivots y Dashboard?

Separar ambas hojas facilita:

- El mantenimiento del archivo.
- La actualización de los datos.
- La construcción de nuevos gráficos.
- La reutilización de las Tablas Dinámicas.

Además, evita modificar accidentalmente los elementos visuales del Dashboard.

---

# Concepto importante

Piensa en la hoja **Pivots** como la sala de máquinas de un barco.

Los usuarios nunca la verán.

Sin embargo, todo el funcionamiento del Dashboard dependerá de las Tablas Dinámicas almacenadas allí.

---

# 📝 Lo que aprendí

En este módulo comprendí que las Tablas Dinámicas no representan el Dashboard final.

Su función consiste en procesar y resumir la información proveniente del Modelo de Datos para alimentar indicadores, gráficos y segmentadores que posteriormente conformarán un Dashboard profesional.

---

## 🚀 Continuará...

En la siguiente parte construiremos las primeras Tablas Dinámicas que servirán como fuente de información para el Dashboard.

Crearemos análisis por:

- Cliente
- Técnico
- Ciudad
- Mes
- Tipo de Servicio

A partir de ellas comenzaremos a construir los primeros indicadores del Dashboard.

---

# 🧪 Laboratorio - Construyendo el Motor del Dashboard

Hasta este momento tenemos dos hojas creadas:

- Pivots
- Dashboard

La hoja **Dashboard** permanecerá vacía.

Todo nuestro trabajo se realizará inicialmente en la hoja **Pivots**.

---

# ¿Por qué comenzamos por Pivots?

Porque un Dashboard profesional nunca obtiene la información directamente del Modelo de Datos.

Primero construimos diferentes análisis mediante Tablas Dinámicas.

Posteriormente utilizaremos esos análisis para construir:

- KPIs
- Gráficos
- Indicadores
- Segmentadores
- Cronologías

Las Tablas Dinámicas actuarán como la fuente de información del Dashboard.

---

# Primera Tabla Dinámica

## Objetivo

Responder la siguiente pregunta:

> ¿Cuál es el valor total de materiales utilizado por cada cliente?

---

## Paso 1

Seleccionar cualquier celda del libro.

Ir a:

```text
Insertar

↓

Tabla Dinámica
```

---

## Paso 2

Seleccionar:

```text
Usar el Modelo de Datos de este libro
```

Esta opción es muy importante.

No utilizaremos una tabla de Excel tradicional.

Trabajaremos directamente con el Modelo de Datos construido durante los módulos anteriores.

---

## Paso 3

Ubicar la Tabla Dinámica en la hoja:

```text
Pivots
```

Comenzaremos en la celda:

```text
A3
```

---

## Construcción

Filas

```text
Cliente
```

Valores

```text
Total Materiales
```

Obtendremos un informe similar a:

| Cliente | Total Materiales |
|----------|-----------------:|
| Cliente 1 | $150.000 |
| Cliente 2 | $225.000 |
| Cliente 3 | $100.000 |

---

# ¿Qué estamos haciendo realmente?

La medida:

```DAX
Total Materiales :=
SUM(tblMateriales[Valor])
```

permanece exactamente igual.

Lo único que hicimos fue analizarla utilizando el campo:

```text
Cliente
```

Esto significa que el contexto de filtro cambió.

La medida sigue siendo la misma.

---

# Segunda Tabla Dinámica

Ahora responderemos otra pregunta.

> ¿Qué técnico ha instalado el mayor valor de materiales?

---

Ubicar una nueva Tabla Dinámica aproximadamente en:

```text
A25
```

Filas

```text
Técnico
```

Valores

```text
Total Materiales
```

Obtendremos un análisis completamente diferente utilizando exactamente la misma medida.

---

# ¿Qué cambió?

No modificamos la medida.

Seguimos utilizando:

```DAX
Total Materiales :=
SUM(tblMateriales[Valor])
```

Lo único que cambió fue el campo utilizado para analizar la información.

Ahora el contexto de filtro corresponde al Técnico.

---

# Tercera Tabla Dinámica

Responderemos ahora la siguiente pregunta.

> ¿Qué ciudad registra el mayor consumo de materiales?

Crear una nueva Tabla Dinámica.

Ubicarla aproximadamente en:

```text
A47
```

Filas

```text
Ciudad
```

Valores

```text
Total Materiales
```

---

# Cuarta Tabla Dinámica

Ahora cambiaremos completamente el enfoque del análisis.

Pregunta:

> ¿Cómo se comporta el consumo de materiales a lo largo del tiempo?

Crear otra Tabla Dinámica.

Filas

```text
Nombre Mes
```

Valores

```text
Total Materiales
```

Esta información posteriormente alimentará un gráfico de tendencias.

---

# Quinta Tabla Dinámica

Construiremos un análisis operativo.

Pregunta:

> ¿Qué tipo de servicio consume más materiales?

Filas

```text
TipoServicio
```

Valores

```text
Total Materiales
```

---

# Resultado esperado

Al finalizar tendremos cinco Tablas Dinámicas.

```text
Pivots

------------------------------------------------

Tabla Dinámica 1

Cliente

↓

Total Materiales

------------------------------------------------

Tabla Dinámica 2

Técnico

↓

Total Materiales

------------------------------------------------

Tabla Dinámica 3

Ciudad

↓

Total Materiales

------------------------------------------------

Tabla Dinámica 4

Mes

↓

Total Materiales

------------------------------------------------

Tabla Dinámica 5

Tipo Servicio

↓

Total Materiales
```

---

# Observación importante

Aunque visualmente parecen cinco informes diferentes, en realidad todos utilizan exactamente la misma medida DAX.

```DAX
Total Materiales :=
SUM(tblMateriales[Valor])
```

Lo único que cambia es el contexto de filtro.

Este es uno de los conceptos más importantes de Power Pivot.

---

# Organización de la hoja Pivots

Procura dejar suficiente espacio entre cada Tabla Dinámica.

Una distribución recomendada sería:

```text
A3

Tabla Dinámica Clientes

A25

Tabla Dinámica Técnicos

A47

Tabla Dinámica Ciudad

A69

Tabla Dinámica Mes

A91

Tabla Dinámica Tipo Servicio
```

Esto facilitará posteriormente la creación del Dashboard y permitirá insertar nuevos análisis sin afectar los existentes.

---

# Concepto BI

Observa que todavía no hemos creado ningún gráfico.

Tampoco hemos construido el Dashboard.

Estamos preparando el motor que alimentará toda la información del proyecto.

En Business Intelligence esta fase suele consumir la mayor parte del tiempo.

Cuando las Tablas Dinámicas están bien construidas, el Dashboard prácticamente se diseña solo.

---

# 💡 Buena práctica

Asigna un título descriptivo sobre cada Tabla Dinámica.

Por ejemplo:

```text
Materiales por Cliente

Materiales por Técnico

Materiales por Ciudad

Materiales por Mes

Materiales por Tipo de Servicio
```

Esto facilitará la identificación de cada análisis durante el desarrollo del Dashboard.

---

## 🚀 Continuará...

En la siguiente parte utilizaremos estas cinco Tablas Dinámicas para construir:

- KPIs.
- Tarjetas de indicadores.
- Gráficos Dinámicos.
- Segmentadores.
- Cronologías.

A partir de ese momento comenzaremos a construir el Dashboard profesional del laboratorio.

---

# 🏗 Construyendo el Dashboard

Hasta este momento ya tenemos:

✔ Modelo de Datos

✔ Relaciones

✔ Medidas DAX

✔ Columnas Calculadas

✔ Cinco Tablas Dinámicas

Ahora construiremos el Dashboard que consumirá toda esa información.

---

# El Dashboard NO comienza con gráficos

Uno de los errores más comunes consiste en insertar gráficos inmediatamente.

Un Dashboard profesional comienza respondiendo una pregunta muy sencilla:

> ¿Qué necesita conocer la gerencia en menos de 10 segundos?

La respuesta normalmente corresponde a los indicadores principales del negocio.

Por esta razón comenzaremos creando los KPIs.

---

# Arquitectura del Dashboard

La distribución recomendada será la siguiente.

```text
┌──────────────────────────────────────────────────────────────┐
│              DASHBOARD EMPRESA TELECOM                      │
├──────────────────────────────────────────────────────────────┤
│ KPI │ KPI │ KPI │ KPI │ KPI │ KPI │
├──────────────────────────────────────────────────────────────┤
│             Gráfico Materiales por Cliente                  │
├───────────────────────────────┬──────────────────────────────┤
│ Materiales por Técnico        │ Materiales por Ciudad        │
├───────────────────────────────┼──────────────────────────────┤
│ Materiales por Mes            │ Tipo de Servicio             │
├──────────────────────────────────────────────────────────────┤
│ Segmentadores                                   Cronología   │
└──────────────────────────────────────────────────────────────┘
```

Esta estructura es utilizada en muchos Dashboards empresariales porque permite visualizar rápidamente la información más importante.

---

# Paso 1

Crear una nueva hoja llamada:

```text
Dashboard
```

Será la hoja que visualizarán los usuarios.

Toda la información provendrá de la hoja **Pivots**.

---

# Paso 2

Ocultar las líneas de cuadrícula.

Ir a:

```text
Vista

↓

Desmarcar

Líneas de cuadrícula
```

Esto mejora considerablemente la apariencia del Dashboard.

---

# Paso 3

Asignar un título.

Ejemplo:

```text
Dashboard Operacional

Empresa Telecom
```

Puede ubicarse en la parte superior.

Se recomienda utilizar:

- Texto grande.
- Negrilla.
- Colores corporativos.

---

# ¿Qué es un KPI?

KPI significa:

**Key Performance Indicator**

o

**Indicador Clave de Desempeño.**

Su objetivo consiste en resumir la información más importante del negocio en un solo valor.

---

# KPIs del laboratorio

Construiremos seis indicadores.

---

## KPI 1

```text
Total Materiales
```

Medida utilizada:

```DAX
Total Materiales
```

---

## KPI 2

```text
Total Pedidos
```

Medida utilizada:

```DAX
Total Pedidos
```

---

## KPI 3

```text
Promedio Materiales
```

---

## KPI 4

```text
Valor Máximo
```

---

## KPI 5

```text
Valor Mínimo
```

---

## KPI 6

```text
Materiales Diferentes
```

---

# Distribución recomendada

Los KPIs pueden organizarse horizontalmente.

```text
┌────────────┐
│ Total Mat. │
│ $3.750.000 │
└────────────┘

┌────────────┐
│ Pedidos    │
│ 30         │
└────────────┘

┌────────────┐
│ Promedio   │
│ $75.000    │
└────────────┘

┌────────────┐
│ Máximo     │
│ $125.000   │
└────────────┘

┌────────────┐
│ Mínimo     │
│ $25.000    │
└────────────┘

┌────────────┐
│ Materiales │
│ 5          │
└────────────┘
```

Los usuarios deben poder interpretar estos indicadores en pocos segundos.

---

# ¿Cómo obtenemos un KPI?

Existen varias formas.

La más sencilla consiste en utilizar una Tabla Dinámica muy pequeña.

Por ejemplo:

```text
Valores

↓

Total Materiales
```

Posteriormente ocultaremos encabezados y conservaremos únicamente el valor.

De esta manera el KPI permanecerá conectado al Modelo de Datos y responderá automáticamente a los filtros.

---

# Concepto importante

Un KPI no contiene fórmulas independientes.

El KPI simplemente muestra el resultado de una medida DAX.

Si cambia la medida...

El KPI cambia.

Si cambia un Segmentador...

El KPI cambia.

Si cambia una Cronología...

El KPI cambia.

Todo ocurre automáticamente gracias al Modelo de Datos.

---

# Agregando los primeros gráficos

Después de construir los KPIs comenzaremos con los gráficos.

No utilizaremos datos escritos manualmente.

Cada gráfico estará conectado a una Tabla Dinámica.

Esto garantiza que toda la información permanezca sincronizada.

---

# Primer gráfico

Origen:

Tabla Dinámica

```text
Materiales por Cliente
```

Tipo recomendado:

```text
Columnas agrupadas
```

Pregunta que responde:

> ¿Qué clientes consumen más materiales?

---

# Segundo gráfico

Origen:

```text
Materiales por Técnico
```

Tipo recomendado:

```text
Barras horizontales
```

Pregunta:

> ¿Qué técnico realizó el mayor consumo de materiales?

---

# Tercer gráfico

Origen:

```text
Materiales por Ciudad
```

Tipo recomendado:

```text
Circular
```

Pregunta:

> ¿Cómo se distribuye el consumo por ciudad?

---

# Cuarto gráfico

Origen:

```text
Materiales por Mes
```

Tipo recomendado:

```text
Líneas
```

Pregunta:

> ¿Cómo evolucionó el consumo durante el año?

---

# Quinto gráfico

Origen:

```text
Tipo Servicio
```

Tipo recomendado:

```text
Columnas
```

Pregunta:

> ¿Qué tipo de servicio representa el mayor consumo de materiales?

---

# Buena práctica

Cada gráfico debe responder únicamente una pregunta del negocio.

Si un gráfico intenta responder varias preguntas al mismo tiempo, probablemente deba dividirse en dos gráficos diferentes.

---

# Observación

Hasta este momento todavía no hemos agregado Segmentadores.

Primero construiremos toda la información visual.

Después agregaremos los controles interactivos.

Esto facilitará el diseño y evitará tener que reorganizar el Dashboard posteriormente.

---

## 🚀 Continuará...

En la siguiente parte conectaremos todo el Dashboard mediante:

- Segmentadores.
- Cronologías.
- Conexiones entre Tablas Dinámicas.
- Diseño profesional.
- Buenas prácticas utilizadas en proyectos empresariales.

Al finalizar tendremos un Dashboard completamente interactivo construido sobre el Modelo de Datos.

---

# 🎛 Haciendo el Dashboard Interactivo

Hasta este momento construimos:

- El Modelo de Datos.
- Las Medidas DAX.
- Las Tablas Dinámicas.
- Los KPIs.
- Los Gráficos Dinámicos.

Sin embargo, todavía falta una característica fundamental.

La interactividad.

Un Dashboard profesional debe permitir que el usuario explore la información sin modificar fórmulas ni construir nuevos informes.

Para ello utilizaremos Segmentadores y Cronologías.

---

# ¿Qué es un Segmentador?

Un Segmentador es un filtro visual que permite interactuar con las Tablas Dinámicas y los Gráficos Dinámicos de forma sencilla.

A diferencia de los filtros tradicionales, el usuario puede identificar rápidamente qué información está seleccionando.

---

# Segmentadores del laboratorio

Crearemos los siguientes Segmentadores:

- Ciudad
- Técnico
- Cliente
- Tipo de Servicio

Estos campos permitirán analizar la información desde diferentes perspectivas.

---

# Insertando un Segmentador

Seleccionar cualquier Tabla Dinámica.

Ir a:

```text
Analizar Tabla Dinámica

↓

Insertar Segmentación de Datos
```

Seleccionar:

- Cliente
- Ciudad
- Técnico
- TipoServicio

Aceptar.

---

# ¿Qué ocurre?

Al seleccionar:

```text
Ciudad = Medellín
```

Todo el Dashboard cambia automáticamente.

Cambian:

- Los KPIs.
- Los gráficos.
- Las Tablas Dinámicas.

La única acción realizada fue cambiar el contexto de filtro.

---

# ¿Cómo es posible?

Recordemos que todos los elementos del Dashboard utilizan:

- El mismo Modelo de Datos.
- Las mismas Medidas DAX.
- Las mismas relaciones.

Por esta razón toda la información permanece sincronizada.

---

# Conectando los Segmentadores

Este es uno de los pasos más importantes.

Si un Segmentador únicamente controla una Tabla Dinámica, el Dashboard perderá gran parte de su utilidad.

Debemos conectarlo a todas las Tablas Dinámicas relacionadas.

Ir a:

```text
Segmentador

↓

Conexiones de informe
```

Seleccionar todas las Tablas Dinámicas.

Aceptar.

Ahora un único Segmentador controlará todo el Dashboard.

---

# ¿Qué es una Cronología?

La Cronología es un control especializado para trabajar con fechas.

Permite filtrar rápidamente por:

- Año
- Trimestre
- Mes
- Día

Resulta mucho más cómoda que un Segmentador tradicional cuando analizamos información temporal.

---

# Insertando una Cronología

Seleccionar una Tabla Dinámica.

Ir a:

```text
Analizar Tabla Dinámica

↓

Insertar Cronología
```

Seleccionar:

```text
Fecha
```

Aceptar.

Ahora podremos navegar fácilmente por los diferentes períodos.

---

# Probando el Dashboard

Realiza las siguientes pruebas.

## Prueba 1

Selecciona:

```text
Ciudad = Medellín
```

Observa cómo cambian:

- Total Materiales.
- Total Pedidos.
- Promedio.
- Gráficos.

---

## Prueba 2

Selecciona:

```text
Técnico = Juan Pérez
```

Todo el Dashboard se actualizará.

---

## Prueba 3

Utiliza la Cronología.

Filtra únicamente:

```text
Enero
```

Observa nuevamente el comportamiento.

---

# Pensando como un Gerente

Cuando un gerente abre un Dashboard normalmente sigue este recorrido.

## Paso 1

Observa los KPIs.

Pregunta:

> ¿Cómo va el negocio?

---

## Paso 2

Observa los gráficos.

Pregunta:

> ¿Dónde están ocurriendo los mayores cambios?

---

## Paso 3

Utiliza los Segmentadores.

Pregunta:

> ¿Qué ocurre si analizo únicamente Medellín?

---

## Paso 4

Utiliza la Cronología.

Pregunta:

> ¿Cómo se comportó el negocio durante el primer trimestre?

---

## Paso 5

Toma decisiones.

Un Dashboard no existe únicamente para mostrar información.

Su objetivo principal consiste en facilitar la toma de decisiones.

---

# Diseño profesional

Antes de entregar un Dashboard verifica:

- Todos los gráficos tienen título.
- Los KPIs utilizan el mismo formato.
- Los colores son consistentes.
- Los Segmentadores están alineados.
- La Cronología es visible.
- No existen Tablas Dinámicas visibles para el usuario.

---

# Buena práctica

Una vez finalizado el Dashboard puedes ocultar la hoja:

```text
Pivots
```

El usuario únicamente visualizará:

```text
Dashboard
```

Toda la lógica permanecerá funcionando porque las Tablas Dinámicas continuarán alimentando el Dashboard.

---

# Arquitectura final

```text
Empresa_Telecom_ExcelBI_v3.xlsx

│

├── Clientes
├── Técnicos
├── Pedidos
├── Materiales
├── Instalaciones
├── Calendario

│

├── Pivots
│      │
│      ├── Pivot Cliente
│      ├── Pivot Técnico
│      ├── Pivot Ciudad
│      ├── Pivot Mes
│      └── Pivot Servicio

│

└── Dashboard
       │
       ├── KPIs
       ├── Gráficos
       ├── Segmentadores
       └── Cronología
```

Esta organización facilita el mantenimiento del archivo y refleja una metodología utilizada en proyectos de Business Intelligence.

---

# ⭐ Buenas prácticas

- Mantener separadas las hojas de datos, Pivots y Dashboard.
- Utilizar nombres descriptivos para las medidas.
- Evitar gráficos innecesarios.
- Responder una pregunta de negocio con cada visualización.
- Conectar todos los Segmentadores al Dashboard completo.
- Ocultar la hoja **Pivots** antes de entregar el archivo.

---

# ⚠️ Errores frecuentes

- Crear gráficos directamente desde tablas de datos.
- Mezclar datos, Tablas Dinámicas y Dashboard en una sola hoja.
- No conectar los Segmentadores a todas las Tablas Dinámicas.
- Utilizar demasiados colores.
- Saturar el Dashboard con información irrelevante.

---

# 🏢 Aplicación en proyectos reales

Esta metodología puede aplicarse a proyectos como:

- Control ANS.
- DRACO.
- Inventarios.
- Conciliaciones.
- Ventas.
- Indicadores operativos.
- Seguimiento de técnicos.
- Consumo de materiales.

El flujo de trabajo será siempre el mismo:

Power Query

↓

Modelo de Datos

↓

Medidas DAX

↓

Tablas Dinámicas

↓

Dashboard

---

# 📝 Lo que aprendí

En este módulo comprendí que las Tablas Dinámicas son el motor que alimenta un Dashboard profesional. Aprendí a construir KPIs, Gráficos Dinámicos, Segmentadores y Cronologías utilizando el Modelo de Datos, logrando que toda la información permanezca sincronizada y responda automáticamente a los filtros del usuario.

---

# 🎯 Proyecto del módulo

Utilizando el archivo **Empresa_Telecom_ExcelBI_v3.xlsx** construye un Dashboard profesional que incluya:

- 6 KPIs.
- 5 Gráficos Dinámicos.
- 4 Segmentadores.
- 1 Cronología.

El Dashboard debe responder, como mínimo, las siguientes preguntas:

1. ¿Qué cliente consume más materiales?
2. ¿Qué técnico ejecuta más pedidos?
3. ¿Qué ciudad registra el mayor consumo?
4. ¿Cuál es el comportamiento mensual?
5. ¿Qué tipo de servicio representa el mayor valor?

---

# 🚀 Próximo módulo

## 📘 Módulo 09 - Caso Empresarial Integrador

En el siguiente módulo aplicaremos todos los conocimientos adquiridos para resolver un caso real de negocio. Construiremos un informe ejecutivo completo, desde la preparación de los datos hasta el Dashboard final, siguiendo la metodología utilizada por un Analista BI en un entorno empresarial.