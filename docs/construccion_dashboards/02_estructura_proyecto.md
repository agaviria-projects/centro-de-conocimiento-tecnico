# 📁 Capítulo 02 - Estructura del Proyecto

## Introducción

Una vez definida la arquitectura general del Dashboard, el siguiente paso consiste en construir la estructura física del proyecto.

Esta estructura será la base sobre la cual se desarrollarán todos los componentes de la aplicación.

Una buena organización permite localizar rápidamente cualquier archivo, facilita el mantenimiento y evita mezclar responsabilidades entre diferentes módulos.

En este Framework utilizaremos siempre la misma estructura para todos los proyectos desarrollados con Streamlit.

---

# Objetivo

Construir una estructura estándar que pueda reutilizarse en cualquier Dashboard empresarial.

La idea es que, al iniciar un nuevo proyecto, no sea necesario pensar nuevamente dónde ubicar cada archivo.

Simplemente se reutiliza esta plantilla.

---

# Estructura Base

```text
Dashboard/

│

├── app.py

├── requirements.txt

├── README.md

│

├── assets/

│   ├── css/

│   ├── icons/

│   ├── images/

│   └── logos/

│

├── components/

│

├── analytics/

│

├── data/

│

├── config/

│

├── utils/

│

├── docs/

│

└── output/
```

---

# app.py

Es el punto de entrada del Dashboard.

Desde este archivo inicia toda la aplicación.

Su responsabilidad consiste únicamente en coordinar los diferentes componentes.

Nunca debe contener cálculos complejos.

Nunca debe contener estilos CSS.

Nunca debe contener consultas de datos extensas.

Debe mantenerse lo más limpio posible.

---

# requirements.txt

Contiene todas las librerías necesarias para ejecutar el proyecto.

Ejemplo:

- streamlit
- pandas
- plotly
- openpyxl
- streamlit-aggrid

Gracias a este archivo cualquier persona podrá instalar todas las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

---

# README.md

Describe el proyecto.

Debe incluir:

- Objetivo.
- Tecnologías utilizadas.
- Cómo ejecutar la aplicación.
- Estructura general.
- Autor.
- Versión.

Este archivo será la carta de presentación del Dashboard.

---

# Carpeta assets

Contiene todos los recursos visuales.

Aquí nunca debe existir código Python.

Su función es almacenar únicamente recursos gráficos.

La estructura recomendada es:

```text
assets/

css/

icons/

images/

logos/
```

---

## css

Contendrá todos los archivos de estilos.

Ejemplo:

styles.css

corporativo.css

dark.css

Nunca escribir CSS directamente dentro de app.py cuando el proyecto empiece a crecer.

---

## logos

Logos institucionales.

Por ejemplo:

logo_empresa.png

logo_elite.png

favicon.ico

---

## icons

Iconos personalizados.

PNG

SVG

ICO

---

## images

Capturas de pantalla.

Fondos.

Ilustraciones.

Diagramas.

---

# Carpeta components

Aquí vivirán todos los componentes reutilizables.

Por ejemplo:

```text
components/

banner.py

sidebar.py

kpis.py

tablas.py

filtros.py

graficos.py

footer.py
```

Cada archivo debe tener una única responsabilidad.

---

# Carpeta analytics

Aquí se desarrolla toda la inteligencia del Dashboard.

Ejemplos:

- Indicadores.
- Agrupaciones.
- Comparativos.
- Rankings.
- Métricas.

Mientras components dibuja información, analytics la calcula.

---

# Carpeta data

Su responsabilidad consiste únicamente en obtener información.

Por ejemplo:

- leer_excel.py
- leer_csv.py
- consultas_sql.py
- cargar_datos.py

Nunca generar gráficos aquí.

Nunca construir KPIs aquí.

---

# Carpeta config

Almacena configuraciones generales.

Por ejemplo:

- rutas.py
- constantes.py
- colores.py
- parametros.py

---

# Carpeta utils

Contiene funciones auxiliares reutilizables.

Ejemplos:

- formatear_moneda()
- convertir_fecha()
- limpiar_texto()
- exportar_excel()

---

# Carpeta docs

Contiene toda la documentación técnica del proyecto.

Por ejemplo:

- Manuales.
- Diagramas.
- Arquitectura.
- Capturas.
- Centro de Conocimiento.

---

# Carpeta output

Opcional.

Se utiliza cuando el Dashboard genera archivos.

Ejemplo:

- Excel.
- PDF.
- CSV.
- Imágenes.

---

# Flujo de trabajo

El funcionamiento del proyecto seguirá siempre este recorrido.

```text
Usuario

↓

app.py

↓

components

↓

analytics

↓

data

↓

Resultado

↓

Interfaz
```

---

# Reglas del Framework

Siempre respetaremos estas reglas.

✔ Un archivo = una responsabilidad.

✔ Una carpeta = un propósito.

✔ No duplicar código.

✔ Componentes pequeños.

✔ Código reutilizable.

✔ Separar interfaz de lógica.

✔ Separar datos de presentación.

---

# Errores comunes

Durante el desarrollo de diferentes proyectos se identificaron errores frecuentes.

Los más importantes fueron:

❌ Colocar imágenes dentro de components.

❌ Crear archivos de más de mil líneas.

❌ Escribir CSS dentro de cada componente.

❌ Mezclar cálculos con la interfaz.

❌ Leer el mismo Excel desde diferentes archivos.

---

# Buenas prácticas

Antes de comenzar cualquier Dashboard:

- Crear toda la estructura del proyecto.
- Nombrar correctamente cada carpeta.
- Mantener nombres consistentes.
- Utilizar rutas relativas.
- Reutilizar componentes existentes.

---

# Conclusión

Una buena estructura no acelera únicamente el desarrollo.

También facilita el mantenimiento, mejora la reutilización del código y permite que el proyecto continúe creciendo sin perder organización.

En el siguiente capítulo comenzaremos la configuración inicial del proyecto y construiremos el archivo principal **app.py**.