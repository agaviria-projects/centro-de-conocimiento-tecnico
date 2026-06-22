## 🎯 Objetivo

Este desarrollo permite comprimir archivos PDF de forma automática, reduciendo su tamaño para facilitar el envío, almacenamiento o cargue en plataformas que tienen límite de peso.

El objetivo principal es disminuir el tamaño de los PDF manteniendo una calidad visual aceptable para lectura y revisión.

---

## 🧩 Problema que resuelve

Algunos archivos PDF pueden quedar demasiado pesados, especialmente cuando contienen imágenes escaneadas, fotografías o documentos digitalizados.

Esto puede generar problemas como:

- Dificultad para enviarlos por correo.
- Demora al cargarlos en plataformas.
- Archivos que superan límites de tamaño.
- Mayor consumo de almacenamiento.

El compresor automatiza este proceso y evita hacerlo manualmente archivo por archivo.

---

## 📂 Carpetas de trabajo

El desarrollo utiliza dos carpetas principales:

### Carpeta de origen

Contiene los archivos PDF originales que se desean comprimir.

### Carpeta de destino

Contiene los PDF comprimidos generados por el sistema.

El usuario solo debe colocar los PDF originales en la carpeta de origen y ejecutar el script.

---

## ⚙️ Proceso del desarrollo

El módulo de Python realiza las siguientes actividades:

1. Busca automáticamente todos los archivos PDF dentro de la carpeta de origen.
2. Abre cada PDF.
3. Convierte cada página en una imagen.
4. Reduce la resolución de la imagen.
5. Ajusta la calidad de compresión JPEG.
6. Reconstruye un nuevo PDF con las páginas comprimidas.
7. Guarda el resultado en la carpeta de destino.
8. Valida si el archivo cumple con el límite definido de 20 MB.
9. Si es necesario, aplica una compresión más agresiva.

---

## 📂 Flujo Completo del Desarrollo

PDF originales

↓

Python

↓

Conversión de páginas a imágenes

↓

Reducción de resolución y calidad

↓

Nuevo PDF comprimido

↓

Validación de tamaño final

↓

Carpeta PDF_COMPRIMIDOS

---

## 🧠 Parámetros principales

El sistema utiliza parámetros de compresión que permiten controlar el equilibrio entre peso del archivo y calidad visual.

### DPI - Puntos por pulgada

DPI (Dots Per Inch o Puntos por pulgada) es una medida que indica el nivel de detalle o resolución de una imagen, osea que define la resolución con la que se convierte cada página del PDF a imagen.

En palabras simples:

- Más DPI = mejor calidad visual, pero archivo más pesado.
- Menos DPI = menor tamaño, pero puede perder nitidez.

En este desarrollo se usa:

- DPI = 110

Esto permite reducir el tamaño del archivo manteniendo una lectura aceptable.

por ejemplo:

- 300 DPI → Muy alta calidad, archivos más pesados.
- 150 DPI → Buena calidad para lectura normal.
- 110 DPI → Calidad media, buen equilibrio entre tamaño y legibilidad.
- 96 DPI → Calidad más baja, archivos más livianos.
---

### JPEG_QUALITY

La calidad JPEG controla el nivel de compresión de las imágenes dentro del PDF.

En palabras simples:

- Mayor calidad JPEG = imagen más nítida, pero archivo más pesado.
- Menor calidad JPEG = archivo más liviano, pero con mayor pérdida de nitidez.

En este desarrollo se usa:

- JPEG_QUALITY = 35

Este valor busca un balance entre reducción de tamaño y legibilidad.

---

### ESCALA_GRISES

Este parámetro define si el PDF se convierte a blanco y negro / escala de grises.

En este desarrollo se usa:

- ESCALA_GRISES = False

Esto significa que el sistema mantiene los colores del documento.

La decisión fue conservar colores porque algunos documentos pueden tener información visual importante, como sellos, resaltados, firmas o marcas.

---

## 🔁 Reintento de compresión agresiva

El sistema tiene una segunda etapa de compresión.

Si la compresión inicial no es suficiente o si el segundo resultado queda mejor, el sistema aplica una versión más agresiva.

Parámetros utilizados:

- DPI_AGRESIVO = 96
- QUALITY_AGRESIVA = 25

Esto significa que el archivo se vuelve a generar con menor resolución y mayor compresión.

El sistema compara el peso del primer resultado contra el segundo resultado y conserva el archivo que quede más liviano.

---

## 🎯 Límite objetivo de peso

El desarrollo tiene definido un límite objetivo de:

- 20 MB

Si el archivo comprimido sigue superando los 20 MB, el sistema realiza un ajuste adicional más fuerte para intentar reducirlo por debajo de ese límite.

Esto ayuda cuando existen plataformas o correos que no aceptan archivos demasiado pesados.

---

## 📄 Resultado final

El sistema genera un nuevo PDF comprimido en la carpeta de destino.

El resultado esperado es:

- Archivo más liviano.
- Colores conservados.
- Ligera pérdida de nitidez.
- Mejor facilidad para envío o cargue.
- Validación automática contra el límite de 20 MB.

---

## ⚠️ Consideraciones importantes

La compresión reduce el peso del archivo, pero puede generar una pequeña pérdida de calidad visual.

El objetivo no es mejorar la imagen, sino reducir el tamaño del PDF manteniendo una lectura aceptable.

En documentos muy pesados o con imágenes de alta resolución, puede que no siempre se logre bajar de 20 MB sin afectar demasiado la calidad.

---

## 🚀 Beneficios del desarrollo

- Comprime varios PDF de forma automática.
- Evita procesar archivos manualmente uno por uno.
- Reduce el peso de documentos escaneados.
- Mantiene colores del documento.
- Genera archivos listos para enviar o cargar.
- Aplica reintento automático si el archivo queda muy pesado.
- Ahorra tiempo operativo.

---

## 🎤 Preguntas que me pueden hacer

### ¿Qué hace este desarrollo?

Comprime automáticamente archivos PDF para reducir su tamaño y facilitar su envío o cargue en plataformas.

### ¿Por qué se usa Python?

Porque permite procesar varios archivos PDF de forma automática, convertir páginas en imágenes, ajustar calidad y generar nuevos archivos comprimidos.

### ¿Qué significa DPI?

El DPI define la resolución utilizada para convertir temporalmente cada página del PDF en una imagen durante el proceso de compresión.

Un DPI alto genera mejor calidad visual, pero archivos más pesados.

Un DPI bajo reduce el tamaño del archivo, aunque puede producir una ligera pérdida de nitidez.

Después de la compresión, las imágenes se reconstruyen nuevamente dentro de un archivo PDF.

### ¿El sistema convierte el PDF a imágenes?

Internamente sí. Cada página del PDF se convierte temporalmente en una imagen para poder aplicar la compresión. Posteriormente esas imágenes se reconstruyen nuevamente en un archivo PDF comprimido.

### ¿Qué significa JPEG_QUALITY?

Es el nivel de calidad de la imagen dentro del PDF. A menor calidad, el archivo pesa menos, pero puede perder algo de nitidez.

### ¿Por qué no se convierte a escala de grises?

Porque se decidió conservar los colores del documento para no perder información visual importante.

### ¿Qué pasa si el PDF sigue pesando más de 20 MB?

El sistema aplica una compresión más agresiva para intentar reducir el archivo por debajo del límite definido.

### ¿Cuál es el mayor beneficio?

Permite reducir el peso de documentos PDF de manera automática, ahorrando tiempo y facilitando su envío o cargue.