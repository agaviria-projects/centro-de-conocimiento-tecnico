## 🎯 Objetivo

Este desarrollo permite automatizar el control operativo de los pedidos reportados por los técnicos mediante WhatsApp y formularios digitales.

El objetivo principal es identificar qué pedidos fueron reportados, cuáles no se encuentran registrados en el formulario y validar si continúan vigentes dentro del Informe ANS.

---

## 🧩 Problema que resuelve

El sistema permite:

- Extraer automáticamente pedidos desde conversaciones de WhatsApp.
- Validar pedidos reportados mediante formularios.
- Verificar si el pedido continúa activo en el Informe ANS.
- Identificar posibles pendientes de cierre en Fénix.
- Generar alertas operativas.

---

## 📥 Fuentes de información

El desarrollo utiliza tres fuentes principales:

## 🧾 Archivos necesarios antes de ejecutar

Antes de ejecutar el proceso, la carpeta de trabajo debe contener:

- Archivo exportado de WhatsApp en formato TXT.
- Archivo del formulario Conexión Clientes(LINK).
- Informe ANS más reciente.

---
### 📱 Exportación del chat de WhatsApp

La aplicación de WhatsApp para PC y WhatsApp Web no incluyen la opción nativa para exportar conversaciones.

Por motivos de seguridad, la exportación del chat debe realizarse desde el dispositivo móvil.

Al exportar el chat se debe seleccionar la opción:

Exportar chat → Sin archivos

Esto genera un archivo de texto (.txt) que contiene todo el historial de mensajes del grupo.

### 📂 Carpeta compartida de trabajo

Se creó una carpeta compartida para la operación.

En esta carpeta se almacenan:

-Archivos exportados de WhatsApp (.txt).
-Archivo del formulario Conexión Clientes.

El usuario únicamente debe reemplazar los archivos por las versiones actualizadas.

### ▶️ Ejecución y consolidación de la información

Después de actualizar los archivos dentro de la carpeta compartida, se ejecuta el script de Python.

El sistema detecta automáticamente los archivos necesarios y comienza el proceso de consolidación y validación de la información.

A continuación, se solicita seleccionar el rango de fechas que se desea analizar.

Seleccionar:

- Fecha desde.
- Fecha hasta.

Esto permite analizar únicamente el periodo requerido, sin necesidad de volver a procesar todo el historial desde el inicio del proyecto.

---

## 🎯 ¿Por qué se usa el rango de fechas?

El rango de fechas permite controlar el análisis sobre un periodo específico.

Esto es útil porque el chat de WhatsApp y el formulario pueden contener información histórica acumulada.

Con esta opción, se puede ejecutar el proceso para un día, una semana o un rango definido, evitando reprocesar información que ya fue revisada anteriormente.

---

### 🔍 Validaciones realizadas

El sistema identifica:

## EN_AMBOS

Pedido encontrado tanto en WhatsApp como en el formulario.

## SOLO_WHATSAPP

Pedido reportado en WhatsApp pero no registrado en el formulario.

## SOLO_FORMULARIO

Pedido registrado en el formulario pero no encontrado en WhatsApp

## ⚙️ Proceso del desarrollo

El módulo de Python realiza las siguientes actividades:

1. Leer conversaciones exportadas desde WhatsApp.
2. Extraer automáticamente los pedidos utilizando expresiones regulares.
3. Filtrar pedidos por rango de fechas.
4. Leer la información registrada en Google Forms.
5. Cruzar pedidos entre WhatsApp y Formulario.
6. Validar si los pedidos continúan activos en el Informe ANS.
7. Generar alertas operativas.
8. Construir un archivo Excel consolidado.

---

### El archivo generado contiene tres hojas:

## Pedidos WhatsApp
Contiene:

- Todos los pedidos detectados en el chat.
- Pedidos repetidos.
- Registros que requieren revisión manual.

Información disponible:

- Fecha reportada.
- Pedido.
- Línea del chat.
- Texto original.
- Requiere revisión.
- Motivo de revisión.

## Cruce Control
Permite identificar:

- Pedidos que están en WhatsApp y formulario.
- Pedidos que están solo en WhatsApp.
- Pedidos que están solo en el formulario.

## Estado Fénix
Consolida la información operativa.

Permite:

- Validar si el pedido continúa presente en el Informe ANS.
- Validar la Fecha limite ANS de un pedido.
- Generar alertas operativas.
- Cuando un pedido reportado por el técnico continúa apareciendo en el Informe ANS, el sistema resalta la celda en color rojo y genera la alerta: VALIDAR CIERRE FÉNIX,indicando que el pedido posiblemente aún no ha sido cerrado en Fénix y debe ser revisado por el usuario.

## ⚠️ Reglas especiales

El sistema identifica palabras sensibles dentro del chat como:

- Serie.
- Medidor.
- Sello.

Cuando estas palabras son detectadas, el registro se marca para revisión manual.

Esto se debe a que los números de serie de medidores o sellos pueden tener la misma longitud que un pedido, lo que podría generar identificaciones incorrectas.

De esta manera, el usuario puede validar manualmente estos casos antes de tomar una decisión operativa.

## ¿Por qué se requiere revisión manual?

Puedes responder:

Porque algunos elementos operativos como medidores, series o sellos contienen secuencias numéricas similares a un pedido. Para evitar errores, el sistema marca estos casos para que el usuario confirme manualmente si realmente corresponde a un pedido reportado.

### 💬 Frase de cierre

Lo más importante de esta herramienta es automatizar la identificación de pedidos reportados por WhatsApp, que es la fuente más compleja de analizar manualmente.

El proceso genera un Excel estructurado que facilita la validación, el seguimiento y el control operativo por parte del usuario final.

### 🎤 Preguntas que me pueden hacer

## ¿Por qué se utiliza Python?

Porque permite procesar grandes volúmenes de información, automatizar cruces y generar alertas operativas de manera automática.

## ¿Qué fuentes utiliza el desarrollo?

WhatsApp, Google Forms e Informe ANS.

## ¿Cómo se extraen los pedidos?

El sistema revisa automáticamente todas las líneas del chat y detecta los números de pedido reportados por los técnicos.

## ¿Qué significa VALIDAR CIERRE FÉNIX?

Que el pedido continúa apareciendo en el Informe ANS y requiere verificar si realmente fue cerrado.

## ¿Cuál es el principal beneficio?

Permite automatizar el seguimiento operativo y reducir el riesgo de omitir pedidos pendientes.

