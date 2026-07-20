# 📁 Capítulo 02 - Organización del Proyecto

## Introducción

Una vez creada la arquitectura base del Dashboard en el **Capítulo 01**, el siguiente paso consiste en organizar correctamente el contenido del proyecto.

A partir de este punto **no se crean nuevas carpetas**. Todas las carpetas principales ya existen. Este capítulo define qué archivos deben vivir dentro de cada una y cuál es su responsabilidad.

El objetivo es que **todos los Dashboards desarrollados con este Framework compartan exactamente la misma organización**, facilitando el mantenimiento, la reutilización del código y la incorporación de nuevas funcionalidades.

---

# Objetivo

Establecer la organización oficial del Framework para todos los Dashboards Streamlit.

Cada nuevo proyecto deberá comenzar utilizando esta misma estructura.

---

# Estructura Oficial

```text
Dashboard/

├── app.py
├── requirements.txt
├── README.md
│
├── analytics/
├── assets/
├── components/
├── config/
├── data/
├── docs/
├── output/
└── utils/
```

---

# Organización General

| Elemento | Responsabilidad |
|----------|-----------------|
| app.py | Punto de entrada del Dashboard. |
| requirements.txt | Dependencias del proyecto. |
| README.md | Documentación general del proyecto. |
| analytics | Cálculos e indicadores. |
| assets | Recursos visuales. |
| components | Componentes reutilizables de la interfaz. |
| config | Configuración global. |
| data | Lectura y preparación de datos. |
| docs | Documentación técnica. |
| output | Archivos generados por el Dashboard. |
| utils | Funciones auxiliares reutilizables. |

---

# app.py

## Objetivo

Iniciar y coordinar toda la aplicación.

## Responsabilidad

- Configurar Streamlit.
- Cargar estilos.
- Controlar la navegación.
- Coordinar los componentes.

## No debe contener

- Consultas SQL.
- Lectura de Excel.
- KPIs.
- Gráficos.
- CSS embebido.

---

# requirements.txt

Contiene todas las librerías necesarias para ejecutar el Dashboard.

```text
streamlit
pandas
plotly
openpyxl
streamlit-aggrid
```

Instalación:

```bash
pip install -r requirements.txt
```

---

# README.md

Debe documentar:

- Objetivo.
- Tecnologías.
- Ejecución.
- Estructura.
- Autor.
- Versión.

---

# Carpeta assets

## Objetivo

Centralizar los recursos visuales.

```text
assets/

styles.css
logo.png
```

Solo contendrá el archivo de estilos principal y el logo institucional.

Nunca almacenar código Python.

---

# Carpeta components

## Objetivo

Construir todos los componentes reutilizables de la interfaz.

```text
components/

banner.py
sidebar.py
navigation.py
subnavigation.py
filtros.py
kpis.py
graficos.py
tablas.py
footer.py
```

Cada archivo debe tener una única responsabilidad.

---

# Carpeta analytics

## Objetivo

Desarrollar la lógica de negocio.

```text
analytics/

indicadores.py
estadisticas.py
comparativos.py
```

Aquí se construyen KPIs, métricas, rankings y comparativos.

Nunca dibujar componentes desde esta carpeta.

---

# Carpeta data

## Objetivo

Leer y preparar la información.

```text
data/

entrada/
salida/
```

Responsabilidades:

- Leer Excel.
- Leer CSV.
- Consultar bases de datos.
- Preparar DataFrames.

---

# Carpeta config

## Objetivo

Centralizar la configuración.

```text
config/

config.py
```

---

# Carpeta utils

## Objetivo

Guardar funciones auxiliares reutilizables.

```text
utils/

helpers.py
```

---

# Carpeta docs

## Objetivo

Conservar la documentación técnica del proyecto.

---

# Carpeta output

## Objetivo

Guardar los archivos generados por el Dashboard.

Puede contener Excel, PDF, CSV e imágenes.

---

# Flujo General

```text
Usuario
   │
   ▼
app.py
   │
   ▼
components
   │
   ▼
analytics
   │
   ▼
data
   │
   ▼
Interfaz
```

---

# Reglas Oficiales

- Un archivo = una responsabilidad.
- Una carpeta = un propósito.
- No duplicar código.
- Separar datos, lógica e interfaz.
- Utilizar rutas relativas.
- Mantener la misma estructura en todos los Dashboards.

---

# Errores Comunes

- Colocar imágenes en `components`.
- Mezclar cálculos con la interfaz.
- Leer el mismo archivo desde varios módulos.
- Escribir CSS en `app.py`.

---

# Buenas Prácticas

- Crear primero toda la estructura.
- Mantener nombres consistentes.
- Reutilizar componentes.
- Documentar cambios importantes.

---

## Checklist de validación

□ app.py creado

□ requirements.txt creado

□ README.md creado

□ analytics creada

□ assets creada

□ styles.css creado

□ logo_elite.png agregado

□ components creada

□ config creada

□ data creada

□ entrada creada

□ salida creada

□ docs creada

□ output creada

□ utils creada

□ helpers.py creado

---

# Conclusión

La organización del proyecto es un estándar del Framework. Todos los Dashboards deberán respetar esta estructura para garantizar mantenibilidad, reutilización y escalabilidad.

El siguiente capítulo desarrollará el archivo principal **app.py**.
