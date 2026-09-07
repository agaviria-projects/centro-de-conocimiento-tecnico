# 🧠 Skill Analista de Datos

## 1. ¿Qué es un Skill?

Un **Skill** es una solución especializada que reúne conocimiento, reglas,
metodología y lógica de análisis para resolver un tipo de problema de forma
repetible.

En este proyecto, el Skill está orientado al trabajo de un **Analista de Datos**.

No debe entenderse únicamente como una página HTML ni como un conjunto de
archivos Markdown. El Skill completo surge de la combinación de varias piezas.

---

## 2. ¿Para qué sirve?

El Skill busca ayudar a analizar archivos y problemas empresariales de forma
ordenada.

Entre sus funciones se encuentran:

- inspeccionar archivos Excel o CSV;
- conocer cantidad de filas y columnas;
- detectar celdas vacías;
- detectar duplicados exactos;
- revisar valores repetidos en posibles identificadores;
- identificar fechas dudosas o futuras;
- revisar coherencia entre fechas y períodos;
- detectar posibles claves de negocio;
- aplicar reglas declaradas por el usuario;
- generar hallazgos y recomendaciones;
- orientar la elección entre Excel, Power Query, Python, SQL, Power BI u otras
  tecnologías;
- servir como herramienta de aprendizaje práctico.

---

## 3. ¿Cómo está construido?

El Skill se puede entender en cuatro capas principales.

### 3.1 Archivos `.md` — metodología y conocimiento

Los archivos Markdown contienen el conocimiento de referencia.

Ejemplos:

- calidad de datos;
- ETL;
- Python;
- SQL;
- Excel;
- Power Query;
- Power Pivot;
- Power BI;
- pruebas;
- documentación;
- automatización;
- arquitectura.

Su función principal es indicar:

- qué revisar;
- por qué revisarlo;
- cómo interpretar un hallazgo;
- qué prácticas seguir;
- qué acciones no deben hacerse automáticamente.

Ejemplo:

> Antes de eliminar duplicados, validar si realmente son errores y confirmar la
> clave de negocio.

El archivo `.md` describe el criterio, pero no recorre físicamente las filas
del Excel.

---

### 3.2 HTML — estructura de la aplicación

El HTML construye la estructura visible.

Ejemplos:

- pestañas;
- formularios;
- botones;
- tablas;
- campos para cargar archivos;
- secciones de resultados.

Puede verse como el **cuerpo de la aplicación**.

---

### 3.3 CSS — diseño visual

CSS controla la presentación.

Ejemplos:

- colores;
- tarjetas;
- bordes;
- tamaños;
- botones;
- pestañas;
- diseño adaptable a celular.

Cambiar CSS no debe modificar las reglas de negocio ni el motor de análisis.

---

### 3.4 JavaScript — motor actual de análisis

JavaScript es actualmente el principal motor ejecutable del Skill.

Es quien realmente:

- lee el archivo;
- recorre filas;
- compara valores;
- cuenta vacíos;
- detecta duplicados;
- identifica tipos de columnas;
- revisa fechas;
- busca incoherencias;
- genera alertas;
- presenta resultados.

Ejemplo conceptual:

```text
Fila 18
FACTURA = FV001
PROVEEDOR = SERVITRAVEL
VALOR = 500000

Fila 47
FACTURA = FV001
PROVEEDOR = SERVITRAVEL
VALOR = 500000

↓
JavaScript compara las filas
↓
detecta que son iguales
↓
genera el hallazgo
```

---

## 4. ¿Dónde entra Python?

Python no es actualmente el motor principal del HTML.

Puede incorporarse cuando el Skill necesite:

- procesar volúmenes mayores;
- trabajar con varios archivos;
- ejecutar ETL más complejos;
- conectarse con bases de datos;
- generar archivos de salida;
- automatizar procesos;
- crear validaciones más avanzadas.

Por eso se puede pensar así:

```text
JavaScript
= motor local y directo dentro del navegador

Python
= motor adicional para procesamiento avanzado
```

---

## 5. Relación entre `.md` y el motor

Ambos son importantes, pero hacen cosas distintas.

```text
.md
↓
Dice QUÉ revisar y con qué criterio

JavaScript / Python
↓
EJECUTA la revisión sobre los datos reales
```

Ejemplo:

### Regla documentada

> Una factura repetida no debe eliminarse automáticamente.

### Motor

El JavaScript encuentra que la factura `FV001` aparece en las filas 18 y 47.

### Resultado

El Skill puede advertir:

> Revisar las filas 18 y 47. La factura aparece repetida. Antes de eliminarla,
> confirmar si representa un duplicado real o un evento válido del negocio.

---

# Ruta de aprendizaje del Skill

## NIVEL 1 — Entender la arquitectura

### Objetivo

Comprender qué función cumple cada pieza.

### Debes distinguir

```text
HTML
→ estructura

CSS
→ diseño

JavaScript
→ motor de análisis

.md
→ metodología y conocimiento

Python
→ motor adicional cuando sea necesario
```

### Resultado esperado

Poder abrir el proyecto y explicar qué hace cada capa sin necesidad de entender
todavía cada línea de código.

---

## NIVEL 2 — Entender el motor

### Objetivo

Comprender cómo entra un archivo y cómo se convierte en hallazgos.

Estudiar funciones como:

- lectura del Excel;
- análisis de filas;
- normalización;
- conteo de vacíos;
- detección de duplicados;
- detección de repetidos por columna;
- validación de fechas;
- generación de alertas.

### Ejemplo

```text
Excel
↓
lectura
↓
filas y columnas
↓
análisis
↓
hallazgos
↓
resultado visual
```

### Resultado esperado

Poder señalar qué función del motor detecta cada tipo de problema.

---

## NIVEL 3 — Crear reglas nuevas

### Objetivo

Aprender a convertir una necesidad del negocio en una validación automática.

Ejemplos:

```text
Una FACTURA debe pertenecer a un solo PROVEEDOR.

Una FECHA_INICIO no puede ser mayor que FECHA_FIN.

Un PEDIDO debe tener una sola clasificación.

Un ESTADO determinado exige que otra columna tenga información.
```

### Proceso recomendado

```text
1. Definir la regla de negocio.
2. Documentarla.
3. Identificar las columnas necesarias.
4. Programar la validación.
5. Mostrar las filas afectadas.
6. Probar con datos reales.
7. Ajustar si aparecen casos no contemplados.
```

### Resultado esperado

Poder agregar nuevas capacidades sin depender de un archivo específico.

---

## NIVEL 4 — Profesionalizar la arquitectura

Cuando el Skill crezca, conviene separar responsabilidades.

Ejemplo de estructura futura:

```text
ANALISTA_DATOS_EMPRESARIAL/
│
├── index.html
│
├── css/
│   └── nexus.css
│
├── js/
│   ├── lector_excel.js
│   ├── analisis.js
│   ├── validaciones.js
│   ├── reglas_negocio.js
│   └── interfaz.js
│
├── referencias/
│   ├── calidad_datos.md
│   ├── etl.md
│   ├── python.md
│   └── ...
│
└── python/
    └── motor_avanzado.py
```

### Beneficio

- código más fácil de entender;
- menor riesgo al modificar;
- reglas mejor organizadas;
- mantenimiento más sencillo;
- posibilidad de crecer sin convertir el HTML en un archivo gigante.

---

## NIVEL 5 — Evolución avanzada

### Objetivo

Convertir el Skill en una solución analítica cada vez más completa.

Posibles evoluciones:

- analizar varios archivos;
- comparar archivos entre períodos;
- exportar hallazgos;
- generar un Excel de novedades;
- guardar histórico;
- usar Python como motor avanzado;
- integrar SQL;
- parametrizar reglas;
- manejar catálogos;
- crear trazabilidad de cada validación;
- separar ambiente de pruebas y producción;
- registrar cambios y versiones.

### Principio importante

No agregar tecnología por moda.

Cada evolución debe responder a una necesidad real:

```text
Problema real
+
Regla de negocio
+
Evidencia del archivo
+
Pruebas
=
Nueva capacidad del Skill
```

---

# 6. ¿Cómo mejorar el Skill correctamente?

Cuando aparezca un nuevo caso, primero determinar qué debe cambiar.

### Caso A — Cambio metodológico

Ejemplo:

> Nunca eliminar duplicados sin confirmar la clave de negocio.

Normalmente debe documentarse en `.md`.

### Caso B — Nueva detección automática

Ejemplo:

> Detectar facturas que tengan dos proveedores diferentes.

Debe modificarse el motor JavaScript o Python.

### Caso C — Ambas cosas

Cuando la nueva regla necesita:

- quedar documentada;
- ser ejecutada automáticamente.

Se actualizan tanto la documentación como el motor.

---

# 7. Regla de mantenimiento

Cada nueva mejora debe poder responder estas preguntas:

1. ¿Qué problema real intenta detectar o resolver?
2. ¿Es una regla genérica o específica de un proceso?
3. ¿Debe documentarse en `.md`?
4. ¿Debe programarse en JavaScript/Python?
5. ¿Qué evidencia mostrará al usuario?
6. ¿Cómo se probará?
7. ¿Qué cambió después de la mejora?

---

# 8. Resumen rápido

```text
SKILL
│
├── .md
│   └── conocimiento, reglas y metodología
│
├── HTML
│   └── estructura visual
│
├── CSS
│   └── diseño
│
├── JavaScript
│   └── motor actual de análisis
│
└── Python
    └── motor adicional para procesos avanzados
```

La idea central es:

> **El conocimiento dice qué debe hacerse. El motor lo ejecuta sobre los datos.**
> La interfaz muestra el resultado y las pruebas permiten confirmar que la
> solución realmente funciona.

---

## 9. Siguiente tema recomendado

Después de comprender esta introducción, el siguiente aprendizaje recomendado
es estudiar el flujo completo:

```text
Cargar Excel
↓
Leer hoja
↓
Convertir a filas
↓
Analizar filas
↓
Construir perfiles
↓
Ejecutar validaciones
↓
Generar hallazgos
↓
Mostrar resultado
```

Ese recorrido permite comprender cómo funciona internamente el Skill sin
necesidad de memorizar todo el código.
