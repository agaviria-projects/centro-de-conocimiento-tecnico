# 🏗️ Capítulo 01 - Arquitectura del Proyecto

## Introducción

Antes de escribir una sola línea de código es necesario definir la arquitectura del proyecto.

Una buena arquitectura permite que un Dashboard sea fácil de desarrollar, mantener, ampliar y reutilizar.

Por el contrario, comenzar a programar sin una estructura definida suele generar aplicaciones difíciles de entender, con código repetido y componentes mezclados.

En este capítulo construiremos la base sobre la cual se desarrollará todo el Dashboard.

---

# ¿Qué es la arquitectura de un proyecto?

La arquitectura es la forma en que organizamos todos los archivos y carpetas del proyecto.

Cada carpeta tendrá una responsabilidad específica.

Esto permite encontrar rápidamente cualquier archivo, reducir errores y facilitar el mantenimiento del sistema.

Una buena arquitectura responde preguntas como:

- ¿Dónde deben ir las imágenes?
- ¿Dónde debe ir el código de los gráficos?
- ¿Dónde se almacenan los estilos?
- ¿Dónde se encuentra la lógica del negocio?
- ¿Dónde deben ubicarse los datos?

Cuando estas responsabilidades están claramente definidas, el proyecto puede crecer sin perder organización.

---

# Filosofía de este Framework

En este Framework seguiremos una regla muy importante.

## Una carpeta = Una responsabilidad.

Esto significa que cada carpeta tendrá un único propósito.

Por ejemplo:

- Las imágenes solamente estarán en una carpeta.
- Los estilos solamente estarán en una carpeta.
- Los componentes visuales solamente estarán en una carpeta.
- Los datos solamente estarán en una carpeta.

Nunca mezclaremos responsabilidades.

Esta forma de trabajar hace que cualquier desarrollador pueda entender rápidamente el proyecto.

---

# Arquitectura General

La estructura utilizada será la siguiente:

```text
PROYECTO

│

├── app.py

├── assets/

├── components/

├── data/

├── analytics/

├── utils/

├── config/

├── docs/

├── requirements.txt

└── README.md
```

Esta será la base para todos los Dashboards desarrollados con este Framework.

---

# Descripción de cada carpeta

## app.py

Es el punto de entrada de la aplicación.

Desde este archivo se inicia el Dashboard.

Su responsabilidad es únicamente coordinar el funcionamiento general.

No debe contener cálculos complejos ni lógica de negocio.

---

## assets

Almacena todos los recursos visuales utilizados por la aplicación.

Por ejemplo:

- Logos.
- Iconos.
- Imágenes.
- Archivos CSS.
- Tipografías.

---

## components

Contiene todos los componentes visuales reutilizables.

Por ejemplo:

- Sidebar.
- Banner.
- KPIs.
- Filtros.
- Tablas.
- Gráficos.

Cada componente debe tener una única responsabilidad.

---

## data

Contiene la información utilizada por el Dashboard.

Puede incluir:

- Lectores de Excel.
- Lectores CSV.
- Transformaciones iniciales.
- Carga de información.

Su función es preparar los datos para ser utilizados por la aplicación.

---

## analytics

Contiene la lógica de análisis.

Aquí se realizan:

- Indicadores.
- Estadísticas.
- Agrupaciones.
- Cálculos.
- Comparativos.

Toda la inteligencia del Dashboard debe encontrarse aquí.

---

## utils

Incluye funciones reutilizables utilizadas por diferentes componentes.

Por ejemplo:

- Conversión de fechas.
- Formateo de números.
- Funciones auxiliares.
- Validaciones generales.

---

## config

Almacena configuraciones del proyecto.

Por ejemplo:

- Constantes.
- Colores corporativos.
- Variables globales.
- Configuración de rutas.

---

## docs

Contiene la documentación técnica del proyecto.

Aquí pueden almacenarse:

- Manuales.
- Diagramas.
- Explicaciones.
- Capturas de pantalla.

---

# Regla de Oro

Cada archivo debe tener una única responsabilidad.

Si un archivo comienza a realizar muchas tareas diferentes, probablemente deba dividirse en varios componentes más pequeños.

Esta práctica facilita el mantenimiento y mejora la reutilización del código.

---

# Errores comunes

Durante el desarrollo de diferentes proyectos se identificaron algunos errores frecuentes.

Los más importantes son:

❌ Colocar toda la aplicación dentro de `app.py`.

❌ Mezclar estilos CSS con lógica de Python.

❌ Crear componentes demasiado grandes.

❌ Duplicar funciones en diferentes archivos.

❌ Leer archivos Excel desde varios componentes.

❌ Mezclar cálculos con la interfaz gráfica.

Evitar estos errores hace que el proyecto sea mucho más fácil de mantener.

---

# Buenas prácticas

Antes de comenzar cualquier Dashboard:

✔ Definir la arquitectura.

✔ Crear todas las carpetas necesarias.

✔ Asignar una responsabilidad clara a cada carpeta.

✔ Mantener los componentes pequeños.

✔ Reutilizar código siempre que sea posible.

✔ Separar la lógica del negocio de la interfaz gráfica.

---

# Conclusión

Una buena arquitectura no hace que el Dashboard sea más bonito.

Hace que sea más fácil de desarrollar, más sencillo de mantener y mucho más escalable.

Todo el Framework se construirá respetando esta organización.