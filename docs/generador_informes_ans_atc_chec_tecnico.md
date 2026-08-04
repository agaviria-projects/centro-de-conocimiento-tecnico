# Documentación Técnica  
# Generador de Informes ANS - ATC CHEC

### Inicio recomendado para explicar el desarrollo

Antes de hablar de la parte técnica, lo primero fue entender el requerimiento y la necesidad operativa.

En este caso, el problema era que la información debía revisarse, validarse y procesarse manualmente para calcular los estados ANS, actualizar el informe y facilitar el seguimiento de los pedidos.

A partir de esa necesidad, primero analicé cómo funcionaba el proceso, cuáles eran las columnas necesarias, qué reglas de negocio debían aplicarse, cómo se calculaban los días laborales y qué resultados necesitaban los usuarios.

Cuando la lógica funcional estuvo clara, diseñé una solución en Python separada por módulos. Cada archivo tiene una responsabilidad específica: leer los Excel, validar la información, transformar los datos, calcular los días ANS, generar el informe, actualizar el Dashboard y construir el mapa.

Para la implementación técnica utilicé librerías y herramientas disponibles para cualquier desarrollador, como documentación, ejemplos, videos, comunidades técnicas e Inteligencia Artificial como apoyo. Sin embargo, el entendimiento del requerimiento, la definición de la lógica, las pruebas y la validación de los resultados fueron realizados directamente sobre la necesidad real del proceso.

## Si te preguntan directamente: “¿Usted cómo creó esto?”

Puedes responder:

Primero entendí el proceso y documenté la lógica que debía cumplir la herramienta. Después dividí el desarrollo en componentes pequeños y fui construyendo cada parte: lectura, validación, transformación, cálculo, generación del Excel, Dashboard e interfaz.

En la parte técnica me apoyé en documentación, librerías de Python, videos, ejemplos e Inteligencia Artificial, como lo haría cualquier desarrollador para investigar y acelerar una solución. Lo importante fue adaptar esas herramientas al proceso real, probar los resultados y asegurar que las reglas del negocio se cumplieran.


## Información del documento

| Campo | Descripción |
|---|---|
| Proyecto | Generador de Informes ANS - ATC CHEC |
| Tipo de documento | Documentación técnica |
| Dirigido a | Área de Tecnología de la Información |
| Tecnología principal | Python |
| Interfaz | Aplicación de escritorio |
| Estado | En desarrollo |
| Versión | 1.0 |

---

## Contenido

1. Introducción técnica  
2. Objetivo del sistema  
3. Alcance actual  
4. Arquitectura general  
5. Separación de responsabilidades  
6. Flujo de ejecución  
7. Estructura de carpetas  
8. Módulos Python  
9. Archivos de configuración  
10. Archivos de entrada y salida  
11. Reglas de negocio  
12. Generación del informe Excel  
13. Actualización del Dashboard  
14. Geocodificación y mapas  
15. Manejo de errores y registros  
16. Dependencias  
17. Ejecución del sistema  
18. Puntos de extensión  
19. Desarrollo futuro de ANS Redes  
20. Recomendaciones de mantenimiento  
21. Riesgos técnicos  
22. Checklist de entrega  

---

## 1. Introducción técnica

El proyecto **Generador de Informes ANS - ATC CHEC** es una aplicación desarrollada en Python para automatizar el procesamiento, cálculo y presentación de información relacionada con los Acuerdos de Nivel de Servicio —ANS—.

El sistema procesa archivos operativos y genera:

- Informe consolidado en Excel.
- Actualización del Dashboard.
- Información para análisis geográfico.
- Mapa de pedidos según su ubicación.

El desarrollo utiliza una estructura modular. Cada archivo Python tiene una responsabilidad específica, facilitando su mantenimiento y evolución.

---

## 2. Objetivo del sistema

El objetivo del sistema es transformar archivos operativos en información ANS validada y lista para análisis.

La aplicación permite:

- Leer archivos de entrada.
- Validar columnas y datos requeridos.
- Aplicar reglas de negocio.
- Calcular fechas y estados ANS.
- Generar el informe final.
- Actualizar el Dashboard.
- Preparar información para mapas.

> **Resultado esperado:** reducir actividades manuales y entregar información confiable para el seguimiento de pedidos.

---

## 3. Alcance actual

Actualmente, el sistema cubre las siguientes funcionalidades:

| Funcionalidad | Estado |
|---|---|
| Lectura de archivos Excel | Implementada |
| Lectura de archivos CSV | Disponible |
| Validación de columnas | Implementada |
| Limpieza y transformación | Implementada |
| Cálculo de fechas ANS | Implementada |
| Clasificación de estados | Implementada |
| Generación del informe Excel | Implementada |
| Actualización del Dashboard | Implementada |
| Normalización de direcciones | Implementada |
| Generación de mapas | En ajuste y validación |
| Módulo ANS Redes | Desarrollo futuro |

El alcance actual está orientado al procesamiento de información ANS de ATC CHEC. La incorporación de nuevas fuentes o reglas debe realizarse mediante módulos separados.

---

## 4. Arquitectura general

La aplicación utiliza una arquitectura modular basada en capas funcionales.

```text
Usuario
   │
   ▼
Interfaz gráfica
   │
   ▼
Procesador principal
   │
   ├── Lectura
   ├── Validación
   ├── Transformación
   ├── Cálculo ANS
   └── Generación de resultados
          │
          ├── Informe Excel
          ├── Dashboard
          └── Mapa ANS
```

### Capas principales

| Capa | Responsabilidad |
|---|---|
| Presentación | Interacción con el usuario mediante la interfaz. |
| Coordinación | Control del flujo completo del proceso. |
| Datos | Lectura y validación de archivos. |
| Negocio | Transformación y cálculo de estados ANS. |
| Salida | Generación de Excel, Dashboard y mapas. |
| Soporte | Configuración, rutas y registros de ejecución. |

---

## 5. Separación de responsabilidades

Cada módulo realiza una tarea concreta:

- La interfaz recibe las acciones del usuario.
- El procesador coordina el flujo general.
- Los lectores cargan los archivos.
- El validador revisa la estructura.
- El transformador limpia los datos.
- El calculador aplica las reglas ANS.
- Los generadores producen los resultados.
- Los módulos geográficos procesan direcciones y mapas.

Esta separación permite identificar rápidamente dónde debe realizarse un cambio.

> **Recomendación:** no incorporar cálculos, lectura de archivos o reglas de negocio directamente dentro de `interfaz.py`.

---

## 6. Flujo de ejecución

El proceso general funciona de la siguiente manera:

```text
iniciar.bat
     │
     ▼
main.py
     │
     ▼
interfaz.py
     │
     ▼
procesador_informe.py
     │
     ├── lector_excel.py / lector_csv.py
     ├── validador.py
     ├── transformador.py
     ├── calculador_ans.py
     ├── generador_excel.py
     ├── actualizador_dashboard.py
     └── módulos de mapas
```

### Secuencia principal

1. El usuario ejecuta `iniciar.bat` o `main.py`.
2. Se abre la interfaz gráfica.
3. El usuario inicia la generación del informe.
4. El sistema identifica el archivo de entrada.
5. Se validan las columnas requeridas.
6. Los datos se limpian y transforman.
7. Se calculan fechas y estados ANS.
8. Se genera el informe Excel.
9. Se actualiza el Dashboard.
10. Cuando corresponde, se genera el mapa.
11. El sistema informa el resultado al usuario.

> `procesador_informe.py` coordina el proceso, pero delega cada actividad al módulo correspondiente.

---

## 7. Estructura de carpetas

```text
Informe_ANS_ATC_CHEC
│
├── dashboard
├── entrada
├── logs
├── mapas
├── salida
├── src
│   ├── __init__.py
│   ├── actualizador_dashboard.py
│   ├── calculador_ans.py
│   ├── config.py
│   ├── generador_excel.py
│   ├── generador_mapa.py
│   ├── geocodificador.py
│   ├── interfaz.py
│   ├── lector_csv.py
│   ├── lector_excel.py
│   ├── logging_config.py
│   ├── normalizador_direcciones.py
│   ├── procesador_informe.py
│   ├── transformador.py
│   └── validador.py
│
├── main.py
├── iniciar.bat
├── requirements.txt
└── README.md
```

### Función de las carpetas

| Carpeta | Función |
|---|---|
| `entrada` | Contiene los archivos que serán procesados. |
| `salida` | Guarda los informes generados. |
| `dashboard` | Contiene el archivo de análisis visual. |
| `mapas` | Guarda recursos y resultados geográficos. |
| `logs` | Almacena registros de ejecución y errores. |
| `src` | Contiene el código fuente del sistema. |

### Archivos de la raíz

| Archivo | Función |
|---|---|
| `main.py` | Punto de entrada de la aplicación. |
| `iniciar.bat` | Ejecuta la aplicación en Windows. |
| `requirements.txt` | Lista las dependencias del proyecto. |
| `README.md` | Presenta información general del desarrollo. |

> Las carpetas `venv` y `__pycache__` son generadas por Python y no contienen reglas del negocio.

---

## 8. Módulos Python

### Inicio y coordinación

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Inicia la aplicación y abre la interfaz. |
| `src/interfaz.py` | Contiene la ventana, botones y mensajes al usuario. |
| `src/procesador_informe.py` | Coordina el procesamiento completo. |
| `src/__init__.py` | Identifica `src` como paquete Python. |

### Lectura y validación

| Archivo | Responsabilidad |
|---|---|
| `src/lector_excel.py` | Lee archivos en formato Excel. |
| `src/lector_csv.py` | Lee archivos en formato CSV. |
| `src/validador.py` | Verifica columnas, estructura y datos requeridos. |

### Transformación y cálculo

| Archivo | Responsabilidad |
|---|---|
| `src/transformador.py` | Limpia, organiza y estandariza la información. |
| `src/calculador_ans.py` | Calcula fechas, días restantes y estados ANS. |
| `src/normalizador_direcciones.py` | Estandariza direcciones para su ubicación geográfica. |

### Generación de resultados

| Archivo | Responsabilidad |
|---|---|
| `src/generador_excel.py` | Genera el informe final en Excel. |
| `src/actualizador_dashboard.py` | Actualiza la información utilizada por el Dashboard. |
| `src/geocodificador.py` | Convierte direcciones en coordenadas. |
| `src/generador_mapa.py` | Genera el mapa de pedidos. |

### Configuración y soporte

| Archivo | Responsabilidad |
|---|---|
| `src/config.py` | Centraliza rutas, nombres y parámetros generales. |
| `src/logging_config.py` | Configura los registros de ejecución y errores. |

### Archivos críticos

Los siguientes módulos requieren análisis previo antes de ser modificados:

- `calculador_ans.py`
- `transformador.py`
- `validador.py`
- `procesador_informe.py`
- `actualizador_dashboard.py`

Un cambio en estos archivos puede afectar los cálculos o la estructura del resultado.

---

## 9. Archivos de configuración

La configuración técnica se centraliza principalmente en:

```text
src/config.py
```

Este archivo administra:

- Rutas de las carpetas.
- Nombres de archivos.
- Ubicación del Dashboard.
- Ubicación de entradas y salidas.
- Recursos utilizados por la aplicación.

Las rutas deben construirse de forma relativa desde la raíz del proyecto mediante `pathlib`.

```text
Raíz del proyecto
   ├── entrada
   ├── salida
   ├── dashboard
   ├── mapas
   └── logs
```

> **Advertencia:** no se deben utilizar rutas absolutas asociadas al nombre de un usuario o equipo específico.

Las reglas operativas parametrizables pueden almacenarse en archivos externos de configuración, evitando modificar el código cuando cambien días contractuales, prioridades o festivos.

---

## 10. Archivos de entrada y salida

### Entrada

Los archivos operativos se ubican en:

```text
entrada/
```

El sistema espera columnas relacionadas con:

- Pedido.
- Dirección.
- Municipio.
- Actividad.
- Producto.
- Fecha de inicio ANS.
- Días pactados.
- Observación.

Antes de procesarlos se recomienda:

- Mantener el archivo cerrado.
- No cambiar los encabezados requeridos.
- Evitar archivos adicionales en la carpeta.
- Verificar que las fechas sean válidas.

### Salida

Los resultados se almacenan en:

```text
salida/
```

El archivo principal generado corresponde al informe consolidado ANS.

La información resultante puede incluir:

- Fecha límite ANS.
- Días transcurridos.
- Días restantes.
- Estado del pedido.
- Información operativa original.

### Otros resultados

| Carpeta | Resultado |
|---|---|
| `dashboard` | Archivo utilizado para análisis visual. |
| `mapas` | Archivos geográficos y mapa generado. |
| `logs` | Registro técnico del proceso. |

---

## 11. Reglas de negocio

Las reglas de negocio determinan cómo se calculan y clasifican los pedidos.

### Reglas principales

- La fecha de inicio ANS debe ser válida.
- Los días pactados dependen de la actividad o condición contractual.
- El cálculo excluye sábados, domingos y festivos.
- La fecha límite se calcula utilizando días hábiles.
- Los días restantes se obtienen comparando la fecha actual con la fecha límite.
- El estado se asigna según el resultado del cálculo.

### Estados ANS

| Estado | Descripción |
|---|---|
| `VENCIDOS` | La fecha límite ya fue superada. |
| `ALERTA 0 DÍAS` | El pedido se encuentra en el límite de vencimiento. |
| `A TIEMPO` | El pedido todavía se encuentra dentro del plazo. |

### Ubicación técnica

| Tipo de regla | Ubicación recomendada |
|---|---|
| Cálculo de fechas | `calculador_ans.py` |
| Limpieza de datos | `transformador.py` |
| Columnas obligatorias | `validador.py` |
| Parámetros modificables | Archivo externo de configuración |
| Rutas y nombres | `config.py` |

> **Advertencia:** una modificación en los estados, días pactados o calendario laboral debe validarse con el área funcional antes de llevarse a producción.

---

## 12. Generación del informe Excel

La generación del archivo final se realiza desde:

```text
src/generador_excel.py
```

Este módulo recibe la información ya validada y calculada. No debería contener reglas de cálculo ANS.

### Responsabilidades

- Crear el archivo Excel.
- Organizar las columnas.
- Aplicar encabezados y formatos.
- Ajustar anchos de columnas.
- Aplicar filtros.
- Resaltar estados mediante colores.
- Guardar el resultado en la carpeta `salida`.

### Flujo

```text
Datos calculados
      │
      ▼
generador_excel.py
      │
      ├── Organiza columnas
      ├── Aplica formato
      ├── Agrega filtros
      └── Guarda el archivo
```

> **Recomendación:** si se modifica el diseño visual del informe, el cambio debe realizarse en `generador_excel.py`. Si cambia un cálculo, debe revisarse `calculador_ans.py`.

---

## 13. Actualización del Dashboard

La actualización del Dashboard se realiza mediante:

```text
src/actualizador_dashboard.py
```

Su responsabilidad es trasladar la información generada al archivo utilizado para análisis visual.

### Proceso general

1. Verifica la existencia del informe generado.
2. Localiza el archivo del Dashboard.
3. Abre el archivo conservando su estructura.
4. Actualiza la hoja de datos.
5. Mantiene las hojas de visualización.
6. Guarda el archivo actualizado.

```text
Informe generado
       │
       ▼
actualizador_dashboard.py
       │
       ▼
Hoja de datos del Dashboard
       │
       ▼
Indicadores, tablas y gráficos
```

### Consideraciones técnicas

- No cambiar el nombre de la hoja de datos sin actualizar el código.
- No eliminar tablas dinámicas, gráficos o segmentadores.
- Mantener una copia de respaldo antes de modificar el archivo.
- Validar que la cantidad y el orden de las columnas sean compatibles.
- El Dashboard debe estar cerrado durante la actualización.

> **Advertencia:** este módulo modifica un archivo existente. Cualquier cambio debe probarse sobre una copia antes de utilizarse en producción.

---

---

## 14. Construcción de la interfaz gráfica

La interfaz del sistema fue desarrollada con **Tkinter**, librería incluida con Python para crear aplicaciones de escritorio.

El módulo responsable es:

```text
src/interfaz.py
```

### Responsabilidades de la interfaz

- Crear la ventana principal.
- Mostrar títulos, imágenes y botones.
- Recibir las acciones del usuario.
- Ejecutar la generación del informe.
- Ejecutar la generación del mapa.
- Mostrar mensajes de éxito, advertencia o error.

La interfaz no debe contener cálculos ANS ni reglas de negocio. Su función principal es conectar al usuario con los procesos internos.

### Flujo de un botón

```text
Usuario presiona un botón
          │
          ▼
interfaz.py recibe la acción
          │
          ▼
Llama al procesador correspondiente
          │
          ▼
El sistema ejecuta el proceso
          │
          ▼
La interfaz muestra el resultado
```

### Componentes principales de Tkinter

| Componente | Función |
|---|---|
| `Tk` | Crea la ventana principal. |
| `Frame` | Organiza los componentes visuales. |
| `Label` | Muestra textos, títulos e imágenes. |
| `Button` | Permite ejecutar acciones. |
| `messagebox` | Muestra mensajes al usuario. |
| `PhotoImage` o `ImageTk` | Permite cargar imágenes en la interfaz. |

> **Nota técnica:** si la interfaz utiliza `ttk`, `ttkbootstrap` o `Pillow`, estas librerías también deben incluirse en la documentación y en `requirements.txt`.

---

## 15. Librerías utilizadas

Las dependencias externas del proyecto se encuentran registradas en:

```text
requirements.txt
```

Las librerías estándar de Python no siempre se incluyen en este archivo, pero también hacen parte del funcionamiento del sistema.

### Librerías principales

| Librería | Uso dentro del proyecto |
|---|---|
| `pandas` | Lectura, limpieza, transformación y análisis de datos. |
| `openpyxl` | Creación, edición y formato de archivos Excel. |
| `tkinter` | Construcción de la interfaz gráfica. |
| `pathlib` | Manejo de rutas relativas y portables. |
| `logging` | Registro de eventos, advertencias y errores. |
| `datetime` | Manejo de fechas y tiempos. |

### Librerías que pueden intervenir

| Librería | Uso posible |
|---|---|
| `Pillow` | Carga y redimensionamiento de imágenes. |
| `numpy` | Cálculos relacionados con días hábiles. |
| `folium` | Generación de mapas HTML. |
| `geopy` | Conversión de direcciones en coordenadas. |
| `holidays` | Manejo de festivos oficiales. |
| `xlwings` | Automatización de archivos Excel con macros. |

> **Advertencia:** esta lista debe compararse con los `import` reales del proyecto y con `requirements.txt`. No deben documentarse librerías que no estén siendo utilizadas.

---

## 16. Cálculo de días laborales

La lógica principal del cálculo ANS se encuentra en:

```text
src/calculador_ans.py
```

Este módulo determina fechas límite, días transcurridos, días restantes y estados ANS.

### Días excluidos

El cálculo debe excluir:

- Sábados.
- Domingos.
- Festivos nacionales.
- Festivos adicionales configurados para la operación.

### Flujo del cálculo

```text
Fecha de inicio ANS
        │
        ▼
Cantidad de días pactados
        │
        ▼
Validación de días laborales
        │
        ▼
Cálculo de fecha límite
        │
        ▼
Comparación con la fecha actual
        │
        ▼
Asignación del estado ANS
```

### Ejemplo conceptual

```text
Lunes       → se cuenta
Martes      → se cuenta
Miércoles   → festivo, no se cuenta
Jueves      → se cuenta
Viernes     → se cuenta
Sábado      → no se cuenta
Domingo     → no se cuenta
```

```text
def es_dia_habil(
    fecha: date,
    excluir_sabados: bool,
    excluir_domingos: bool,
    festivos: set[date],
) -> bool:
    """
    Determina si una fecha cuenta como día contractual.
    """

    if (
        excluir_sabados
        and fecha.weekday() == 5
    ):
        return False

    if (
        excluir_domingos
        and fecha.weekday() == 6
    ):
        return False

    if fecha in festivos:
        return False

    return True
```

### Campos calculados

| Campo | Descripción |
|---|---|
| `FECHA_LIMITE_ANS` | Última fecha permitida para atender el pedido. |
| `DIAS_TRANSCURRIDOS` | Días laborales consumidos desde el inicio. |
| `DIAS_RESTANTES` | Días laborales disponibles antes del vencimiento. |
| `ESTADO` | Clasificación actual del pedido. |

### Clasificación general

| Condición | Estado |
|---|---|
| Días restantes menores que cero | `VENCIDOS` |
| Días restantes iguales a cero | `ALERTA 0 DÍAS` |
| Días restantes mayores que cero | `A TIEMPO` |

> **Validación importante:** debe confirmarse en el código si el día inicial se cuenta dentro del plazo o si el cálculo empieza desde el siguiente día laboral.

---

## 17. Validación de los archivos Excel de entrada

```text
src/validador.py
```

Este módulo Verifica que existan archivos Excel en la carpeta entrada,  revisa que el archivo pueda procesarse antes de aplicar transformaciones y cálculos.


### Validaciones principales

- Existencia del archivo.
- Formato permitido.
- Presencia de columnas obligatorias.
- Archivo con registros.
- Fechas válidas.
- Campos requeridos no vacíos.
- Ausencia de columnas duplicadas.
- Existencia de valores necesarios para el cálculo.

### Flujo de validación

```text
Carpeta entrada
      │
      ▼
Búsqueda de archivos Excel
      │
      ▼
Lectura de cada archivo
      │
      ▼
Validación de columnas
      │
      ├── Archivo válido → continúa
      │
      └── Archivo inválido → se detiene y muestra el error
```

### Columnas esperadas

Las columnas pueden variar según la fuente, pero el sistema trabaja principalmente con:

```text
PEDIDO
DIRECCION
MUNICIPIO
ACTIVIDAD
PRODUCTO
FECHA_INICIO_ANS
DIAS_PACTADOS
OBSERVACION
```

> **Recomendación:** las columnas obligatorias deben definirse en un único lugar para evitar diferencias entre el lector, el validador y el transformador.

---

## 18. Coordinación del procesamiento

El módulo:

```text
src/procesador_informe.py
```

actúa como coordinador general del sistema.

Su función no es realizar todas las tareas directamente, sino llamar cada módulo en el orden correcto.

```text
procesador_informe.py
        │
        ├── Localiza el archivo
        ├── Llama al lector
        ├── Llama al validador
        ├── Llama al transformador
        ├── Llama al calculador ANS
        ├── Llama al generador Excel
        ├── Llama al actualizador del Dashboard
        └── Devuelve el resultado a la interfaz
```

### Responsabilidad técnica

`procesador_informe.py` debe concentrarse en:

- Coordinar el flujo.
- Controlar el orden de ejecución.
- Gestionar resultados.
- Propagar mensajes o errores.
- Evitar duplicar lógica de otros módulos.

> **Regla técnica:** el procesador coordina; los demás módulos ejecutan tareas especializadas.

---

## 19. Transformación de la información

La limpieza y preparación de los datos se realiza en:

```text
src/transformador.py
```

Este módulo recibe la información leída desde Excel o CSV y la prepara antes de los cálculos ANS.

### Responsabilidades principales

- Limpiar nombres de columnas.
- Eliminar espacios innecesarios.
- Normalizar textos.
- Convertir fechas.
- Convertir valores numéricos.
- Estandarizar campos operativos.
- Preparar la estructura final de datos.

### Flujo

```text
Datos originales
      │
      ▼
transformador.py
      │
      ├── Limpieza
      ├── Conversión de tipos
      ├── Normalización
      └── Preparación para cálculo
```

> **Advertencia:** cualquier cambio en la transformación puede afectar la validación, los cálculos y la estructura del informe final.

---

## 20. Manejo de rutas portables

La administración de rutas se centraliza en:

```text
src/config.py
```

El proyecto debe utilizar rutas relativas construidas desde la carpeta raíz.

### Estructura esperada

```text
Raíz del proyecto
   ├── entrada
   ├── salida
   ├── dashboard
   ├── mapas
   ├── logs
   └── src
```

### Principio técnico

Las rutas deben construirse con `pathlib`, evitando referencias fijas como:

```text
C:\Users\NombreUsuario\Desktop\Proyecto
```

Esto permite instalar el proyecto en diferentes equipos sin modificar el código.

> **Recomendación:** cualquier nueva carpeta o archivo permanente debe registrarse en `config.py`.

---

## 21. Manejo de errores y registros

La configuración de registros se encuentra en:

```text
src/logging_config.py
```

Este módulo permite guardar información técnica sobre la ejecución.

### Información que debe registrarse

- Inicio del proceso.
- Archivo procesado.
- Cantidad de registros.
- Validaciones realizadas.
- Errores encontrados.
- Archivo generado.
- Actualización del Dashboard.
- Inicio y finalización del mapa.

### Flujo de registro

```text
Proceso ejecutado
       │
       ▼
Evento o error
       │
       ▼
logging_config.py
       │
       ▼
Archivo dentro de logs
```

Los registros facilitan la identificación de errores sin depender únicamente de los mensajes mostrados en pantalla.

> **Recomendación:** no almacenar información sensible o innecesaria dentro de los archivos de log.

---

## 22. Ejecución del sistema

El sistema puede ejecutarse mediante:

```text
iniciar.bat
```

o directamente con:

```text
python main.py
```

### Flujo de inicio

```text
iniciar.bat
    │
    ▼
Activa el entorno virtual
    │
    ▼
Ejecuta main.py
    │
    ▼
Se abre la interfaz
```

### Requisitos previos

- Python instalado.
- Entorno virtual creado.
- Dependencias instaladas.
- Estructura de carpetas completa.
- Archivo de entrada disponible.
- Dashboard cerrado antes de actualizarlo.

### Instalación de dependencias

```bash
pip install -r requirements.txt
```

> **Advertencia:** el sistema debe ejecutarse desde la carpeta raíz del proyecto para garantizar que las rutas relativas funcionen correctamente.

---


---

## Desarrollo futuro del módulo ANS Redes

El módulo **ANS Redes** puede desarrollarse dentro del mismo proyecto **Informe_ANS_ATC_CHEC**, debido a que hace parte de la misma solución general de seguimiento ANS.

Sin embargo, debe mantenerse separado del módulo **ANS Conexiones** para evitar mezclar:

- Filtros.
- Reglas de negocio.
- Validaciones.
- Estados.
- Usuarios.
- Archivos de salida.

### Estructura recomendada

```text
Informe_ANS_ATC_CHEC
│
├── dashboard
├── entrada
├── logs
├── mapas
├── salida
├── src
│   ├── comunes
│   │   ├── lector_excel.py
│   │   ├── logging_config.py
│   │   ├── normalizador_direcciones.py
│   │   └── utilidades_fechas.py
│   │
│   ├── ans_conexiones
│   │   ├── procesador.py
│   │   ├── validador.py
│   │   ├── calculador_ans.py
│   │   └── generador_excel.py
│   │
│   ├── ans_redes
│   │   ├── procesador.py
│   │   ├── validador.py
│   │   ├── filtros.py
│   │   ├── calculador_ans.py
│   │   └── generador_excel.py
│   │
│   ├── config.py
│   ├── interfaz.py
│   └── actualizador_dashboard.py
│
├── main.py
├── iniciar.bat
└── requirements.txt
```
---

## Responsabilidad de cada grupo

| Componente | Responsabilidad |
|---|---|
| `comunes` | Contiene funciones reutilizables por ANS Conexiones y ANS Redes. |
| `ans_conexiones` | Contiene las reglas y procesos específicos del módulo actual. |
| `ans_redes` | Contendrá los filtros, validaciones y cálculos propios de Redes. |
| `interfaz.py` | Permitirá seleccionar qué proceso ejecutar. |
| `config.py` | Mantendrá las rutas y parámetros generales del proyecto. |
| `actualizador_dashboard.py` | Actualizará el Dashboard común o podrá dividirse si cada módulo utiliza un Dashboard diferente. |

---

```text
Analizar el requerimiento
          │
          ▼
Revisar el archivo de entrada
          │
          ▼
Identificar columnas, filtros y estados
          │
          ▼
Confirmar reglas de negocio
          │
          ▼
Crear la carpeta ans_redes
          │
          ▼
Desarrollar lectura, validación y filtros
          │
          ▼
Aplicar cálculo ANS
          │
          ▼
Generar el informe
          │
          ▼
Validar resultados con los usuarios
```

## Reglas que deben confirmarse

Antes de iniciar el desarrollo se deben validar, como mínimo:

- Procesos que deben incluirse.
- Códigos de proceso válidos.
- Estados permitidos.
- Columnas obligatorias.
- Días pactados.
- Festivos y días no laborales.
- Estructura del archivo de salida.
- Reglas de actualización del Dashboard.

---

## Explicación para una reunión

El módulo ANS Redes puede desarrollarse dentro del mismo proyecto porque hace parte de la misma solución. Sin embargo, lo separaría internamente de ANS Conexiones para no mezclar reglas, filtros, validaciones ni resultados. Ambos módulos podrían reutilizar componentes comunes, como la lectura de Excel, el manejo de fechas y los registros de errores.

La idea es mantener un solo proyecto, pero con responsabilidades claramente separadas para facilitar su mantenimiento y evolución futura.

Recomendación técnica: no duplicar el entorno virtual, la interfaz ni la configuración general. La separación debe realizarse dentro de src, creando módulos específicos para cada proceso.