# Documentación Técnica  
# Generador de Informes ANS - ATC CHEC

## Información general

| Campo | Descripción |
|---|---|
| Proyecto | Generador de Informes ANS - ATC CHEC |
| Tipo de documento | Documentación técnica |
| Dirigido a | Área de Tecnología de la Información |
| Tecnología principal | Python |
| Tipo de aplicación | Aplicación de escritorio |
| Estado | En desarrollo |
| Versión | 1.0 |

---

## Contenido

1. Cómo explicar el desarrollo  
2. Qué problema resuelve  
3. Cómo está organizado  
4. Flujo general  
5. Estructura de carpetas  
6. Función de cada archivo Python  
7. Archivos de configuración  
8. Archivos de entrada y salida  
9. Reglas de negocio y cálculo ANS  
10. Lectura de `DIAS_CONTRACTUALES.xlsx`  
11. Generación del informe Excel  
12. Actualización del Dashboard  
13. Interfaz gráfica  
14. Librerías utilizadas  
15. Manejo de errores y registros  
16. Ejecución del sistema  
17. Desarrollo futuro de ANS Redes  
18. Guía rápida para una reunión  

---

## 1. Cómo explicar el desarrollo

Antes de hablar del código, lo primero es explicar la necesidad que dio origen a la herramienta.

> Primero entendí el proceso operativo, revisé los archivos de entrada, identifiqué las columnas necesarias y confirmé las reglas para calcular los estados ANS.  
> Después dividí el desarrollo en partes pequeñas: lectura, validación, limpieza, cálculo, generación del informe, actualización del Dashboard e interfaz.  
> Para la implementación utilicé documentación, librerías de Python, ejemplos, videos e Inteligencia Artificial como apoyo. La lógica del proceso, las pruebas y la validación de los resultados se realizaron con base en la necesidad real de la operación.

No es necesario explicar el código línea por línea. Lo importante es saber:

- qué información entra;
- qué proceso se realiza;
- qué archivo se encarga;
- qué resultado se genera.

---

## 2. Qué problema resuelve

El sistema automatiza el procesamiento de la información ANS de ATC CHEC.

Permite:

- Leer archivos Excel de entrada.
- Validar que tengan la estructura requerida.
- Limpiar y organizar la información.
- Aplicar reglas contractuales.
- Calcular fechas límite y estados ANS.
- Generar el informe final en Excel.
- Actualizar el Dashboard.
- Preparar información para mapas.

> **Resultado esperado:** reducir tareas manuales y entregar información confiable para el seguimiento de los pedidos.

---

## 3. Cómo está organizado

El desarrollo está dividido por responsabilidades para evitar que toda la lógica quede en un solo archivo.

| Parte | Responsabilidad |
|---|---|
| Interfaz | Recibe las acciones del usuario. |
| Procesador | Coordina el orden del proceso. |
| Lectores | Cargan los archivos de entrada. |
| Validador | Revisa la estructura de los Excel. |
| Transformador | Limpia y organiza los datos. |
| Calculador | Aplica las reglas ANS. |
| Generadores | Crean el Excel, el Dashboard y el mapa. |
| Configuración | Administra rutas y nombres de archivos. |
| Registros | Guarda eventos y errores. |

> **Regla principal:** la interfaz no debe contener cálculos, filtros ni reglas de negocio.

---

## 4. Flujo general

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
     ├── lector_excel.py
     ├── validador.py
     ├── transformador.py
     ├── calculador_ans.py
     ├── generador_excel.py
     ├── actualizador_dashboard.py
     └── módulos de mapas
```

### Secuencia del proceso

1. El usuario ejecuta `iniciar.bat` o `main.py`.
2. Se abre la interfaz.
3. El usuario genera el informe.
4. El sistema identifica los archivos Excel de entrada.
5. Valida que tengan las columnas requeridas.
6. Limpia y organiza la información.
7. Aplica las reglas contractuales.
8. Calcula fechas y estados ANS.
9. Genera el informe Excel.
10. Actualiza el Dashboard.
11. Cuando aplica, genera el mapa.
12. Muestra el resultado al usuario.

---

## 5. Estructura de carpetas

```text
Informe_ANS_ATC_CHEC
│
├── config
├── dashboard
├── entrada
├── logs
├── mapas
├── salida
│
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
| `config` | Contiene archivos de configuración funcional. |
| `entrada` | Guarda los archivos Excel que serán procesados. |
| `salida` | Guarda los informes generados. |
| `dashboard` | Contiene el archivo de análisis visual. |
| `mapas` | Guarda archivos relacionados con ubicación geográfica. |
| `logs` | Contiene registros de ejecución y errores. |
| `src` | Contiene el código fuente. |

> `venv` y `__pycache__` son carpetas generadas por Python. No contienen reglas de negocio.

---

## 6. Función de cada archivo Python

| Pregunta | Archivo principal |
|---|---|
| ¿Dónde inicia la aplicación? | `main.py` |
| ¿Dónde está la interfaz? | `src/interfaz.py` |
| ¿Quién coordina el proceso? | `src/procesador_informe.py` |
| ¿Dónde se leen los Excel? | `src/lector_excel.py` |
| ¿Dónde se leen CSV? | `src/lector_csv.py` |
| ¿Dónde se validan los Excel? | `src/validador.py` |
| ¿Dónde se limpian los datos? | `src/transformador.py` |
| ¿Dónde se calculan los días ANS? | `src/calculador_ans.py` |
| ¿Dónde se genera el Excel? | `src/generador_excel.py` |
| ¿Dónde se actualiza el Dashboard? | `src/actualizador_dashboard.py` |
| ¿Dónde se normalizan direcciones? | `src/normalizador_direcciones.py` |
| ¿Dónde se convierten direcciones en coordenadas? | `src/geocodificador.py` |
| ¿Dónde se genera el mapa? | `src/generador_mapa.py` |
| ¿Dónde están las rutas? | `src/config.py` |
| ¿Dónde se registran errores? | `src/logging_config.py` |

### Archivos que requieren mayor cuidado

Los siguientes archivos pueden afectar directamente los resultados:

- `calculador_ans.py`
- `transformador.py`
- `validador.py`
- `procesador_informe.py`
- `actualizador_dashboard.py`

Antes de modificarlos se debe revisar el impacto y realizar pruebas.

---

## 7. Archivos de configuración

### `src/config.py`

Centraliza:

- rutas del proyecto;
- nombres de archivos;
- ubicación de entrada y salida;
- ubicación del Dashboard;
- ubicación de mapas y registros.

Las rutas deben construirse desde la carpeta raíz usando `pathlib`.

- pathlib es un módulo incluido con Python;
- no necesitas instalarla con pip;
- normalmente no aparece en requirements.txt.

No se deben utilizar rutas fijas como:

```text
C:\Users\NombreUsuario\Desktop\Proyecto
```

### `config/DIAS_CONTRACTUALES.xlsx`

Contiene reglas que pueden ajustarse sin modificar el código, por ejemplo:

- días pactados por municipio;
- parámetros generales;
- festivos adicionales;
- reglas de prioridad.

> Antes de modificar este archivo se recomienda crear una copia de respaldo.

---

## 8. Archivos de entrada y salida

### Entrada

Los archivos se ubican en:

```text
entrada/
```

Antes de ejecutar el proceso:

- el archivo debe estar cerrado;
- no se deben cambiar los encabezados;
- se debe verificar que tenga información;
- se deben evitar archivos adicionales;
- las fechas deben ser válidas.

### Salida

Los resultados se guardan en:

```text
salida/
```

El informe puede incluir:

- información original del pedido;
- fecha límite ANS;
- días transcurridos;
- días restantes;
- estado ANS.

---

## 9. Reglas de negocio y cálculo ANS

La lógica principal se encuentra en:

```text
src/calculador_ans.py
```

El sistema toma:

- fecha de inicio;
- días pactados;
- sábados y domingos;
- festivos nacionales;
- festivos adicionales.

Después calcula:

| Campo | Descripción |
|---|---|
| `FECHA_LIMITE_ANS` | Último día permitido para atender el pedido. |
| `DIAS_TRANSCURRIDOS` | Días laborales consumidos. |
| `DIAS_RESTANTES` | Días laborales disponibles. |
| `ESTADO` | Situación actual del pedido. |

### Estados

| Condición | Estado |
|---|---|
| Días restantes menores que cero | `VENCIDOS` |
| Días restantes iguales a cero | `ALERTA 0 DÍAS` |
| Días restantes mayores que cero | `A TIEMPO` |

### Validación de un día laboral

De forma general, el sistema revisa:

```text
¿Es sábado?        → no se cuenta
¿Es domingo?       → no se cuenta
¿Es festivo?       → no se cuenta
En otro caso       → sí se cuenta
```

> Un cambio en días pactados, estados o calendario laboral debe validarse con el área responsable antes de usarlo en producción.

---

## 10. Lectura de `DIAS_CONTRACTUALES.xlsx`

El archivo se lee principalmente desde:

```text
src/calculador_ans.py
```

No se lee desde `validador.py`.

El proceso utiliza Pandas:

```python
pd.read_excel(
    ruta_archivo,
    sheet_name=nombre_hoja,
    dtype=object,
    engine="openpyxl",
)
```

### Qué significa

| Elemento | Función |
|---|---|
| `ruta_archivo` | Ubicación de `DIAS_CONTRACTUALES.xlsx`. |
| `sheet_name` | Nombre de la hoja que se va a leer. |
| `dtype=object` | Carga los datos sin forzar inicialmente su tipo. |
| `engine="openpyxl"` | Utiliza OpenPyXL para abrir el archivo `.xlsx`. |

### Flujo

```text
config/DIAS_CONTRACTUALES.xlsx
               │
               ▼
      calculador_ans.py
               │
               ├── valida que exista
               ├── lee REGLAS_DE_NEGOCIO
               ├── lee PARAMETROS
               └── lee FESTIVOS_ADICIONALES
               │
               ▼
      aplica los cálculos ANS
```

Cuando el usuario modifica y guarda el archivo, los cambios se aplican en la siguiente generación del informe.

> **Frase clave:** `calculador_ans.py` no solo calcula; también carga las reglas que necesita para realizar el cálculo.

---

## 11. Generación del informe Excel

El archivo final se genera desde:

```text
src/generador_excel.py
```

Este módulo:

- recibe los datos ya calculados;
- organiza las columnas;
- aplica encabezados y formatos;
- ajusta anchos;
- agrega filtros;
- resalta estados;
- guarda el resultado en `salida`.

> Si cambia el diseño del Excel, se revisa `generador_excel.py`.  
> Si cambia un cálculo, se revisa `calculador_ans.py`.

---

## 12. Actualización del Dashboard

La actualización se realiza desde:

```text
src/actualizador_dashboard.py
```

El módulo:

1. localiza el informe generado;
2. localiza el archivo del Dashboard;
3. actualiza la hoja de datos;
4. conserva gráficos, tablas y segmentadores;
5. guarda el archivo actualizado.

### Cuidados

- El Dashboard debe estar cerrado.
- No se debe cambiar el nombre de la hoja de datos sin revisar el código.
- No se deben eliminar tablas dinámicas ni segmentadores.
- Se recomienda trabajar primero sobre una copia.

### 12.1 Macro para abrir el mapa ANS

El archivo del Dashboard contiene una macro llamada:

```text
AbrirMapaANS_ATC_CHEC
```

Su función es localizar y abrir el archivo:

```text
mapas/Mapa_ANS_ELITE.html
```

en el navegador predeterminado del equipo.

La macro no genera el mapa. El mapa debe haber sido creado previamente desde la aplicación.

### Ubicación esperada

Para que la macro funcione, se debe conservar esta estructura:

```text
Informe_ANS_ATC_CHEC
│
├── dashboard
│   └── INFORME_ANS.xlsb
│
└── mapas
    └── Mapa_ANS_ELITE.html
```

El Dashboard se encuentra dentro de la carpeta `dashboard`, mientras que el mapa se encuentra dentro de la carpeta `mapas`.

---

### Cómo encuentra el mapa

La macro no utiliza una ruta fija asociada al nombre del usuario o al equipo.

Primero obtiene la ubicación del Dashboard mediante:

```vb
rutaDashboard = ThisWorkbook.Path
```

Por ejemplo:

```text
C:\...\Informe_ANS_ATC_CHEC\dashboard
```

Después sube un nivel para obtener la carpeta principal del proyecto:

```vb
rutaProyecto = CreateObject( _
    "Scripting.FileSystemObject" _
).GetParentFolderName(rutaDashboard)
```

El resultado sería:

```text
C:\...\Informe_ANS_ATC_CHEC
```

Luego construye la ruta completa del mapa:

```vb
rutaMapa = _
    rutaProyecto & _
    "\mapas\Mapa_ANS_ELITE.html"
```

La ruta final queda así:

```text
C:\...\Informe_ANS_ATC_CHEC\mapas\Mapa_ANS_ELITE.html
```

---

### Flujo de la macro

```text
INFORME_ANS.xlsb
       │
       ▼
Obtiene la carpeta dashboard
       │
       ▼
Sube a la carpeta principal del proyecto
       │
       ▼
Busca mapas\Mapa_ANS_ELITE.html
       │
       ▼
Valida que el archivo exista
       │
       ▼
Abre el mapa en el navegador
```

---

### Validaciones realizadas

La macro valida dos situaciones antes de abrir el archivo.

#### Dashboard sin guardar

Si el archivo `INFORME_ANS.xlsb` todavía no tiene una ubicación guardada, la macro detiene el proceso y solicita guardar el Dashboard.

```vb
If rutaDashboard = "" Then
```

#### Mapa no encontrado

Antes de abrir el mapa, verifica que el archivo exista:

```vb
If Dir(rutaMapa) = "" Then
```

Si el mapa no se encuentra, informa al usuario la ruta esperada y solicita generar primero el mapa desde la aplicación.

---

### Apertura del mapa

Cuando el archivo existe, se abre mediante:

```vb
ThisWorkbook.FollowHyperlink _
    Address:=rutaMapa, _
    NewWindow:=True
```

Esta instrucción abre `Mapa_ANS_ELITE.html` en el navegador predeterminado de Windows.

---

### Por qué siempre abre el mapa actualizado

La macro busca siempre el mismo nombre:

```text
Mapa_ANS_ELITE.html
```

Cuando Python vuelve a generar el mapa, actualiza o reemplaza el archivo anterior manteniendo el mismo nombre.

Por esta razón, la macro siempre abre la versión que actualmente se encuentra dentro de la carpeta `mapas`.

> **Importante:** si se cambia el nombre del archivo o de la carpeta `mapas`, también se debe actualizar la ruta construida dentro de la macro.

---

### Explicación para una reunión

> La macro toma como punto de referencia la ubicación del Dashboard. Como el Dashboard está dentro de la carpeta `dashboard`, sube un nivel hasta la carpeta principal del proyecto y luego entra a `mapas` para buscar `Mapa_ANS_ELITE.html`. Antes de abrirlo valida que el archivo exista y, si lo encuentra, lo muestra en el navegador predeterminado.

### Frase clave

> La macro no tiene una ruta fija del computador; construye la ubicación del mapa a partir de la carpeta donde está guardado el Dashboard.

---

## 13. Interfaz gráfica

La interfaz fue creada con Tkinter y se encuentra en:

```text
src/interfaz.py
```

Su función es:

- crear la ventana;
- mostrar títulos, imágenes y botones;
- recibir las acciones del usuario;
- mostrar mensajes de éxito o error;
- llamar los procesos internos.

### Flujo de un botón

```text
Usuario presiona un botón
          │
          ▼
interfaz.py recibe la acción
          │
          ▼
llama al procesador
          │
          ▼
el sistema ejecuta el proceso
          │
          ▼
la interfaz muestra el resultado
```

### Componentes habituales

| Componente | Uso |
|---|---|
| `Tk` | Crea la ventana principal. |
| `Frame` | Organiza los elementos. |
| `Label` | Muestra textos e imágenes. |
| `Button` | Ejecuta acciones. |
| `messagebox` | Muestra mensajes. |
| `ImageTk` o `PhotoImage` | Carga imágenes. |

---

## 14. Librerías utilizadas

| Librería | Uso |
|---|---|
| `pandas` | Lectura, limpieza y transformación de datos. |
| `openpyxl` | Lectura, edición y formato de Excel. |
| `tkinter` | Interfaz gráfica. |
| `pathlib` | Manejo de rutas portables. |
| `logging` | Registro de eventos y errores. |
| `datetime` | Manejo de fechas. |
| `Pillow` | Carga de imágenes, si aplica. |
| `folium` | Generación de mapas, si aplica. |
| `geopy` | Conversión de direcciones en coordenadas, si aplica. |

Las dependencias externas deben estar registradas en:

```text
requirements.txt
```

---

## 15. Manejo de errores y registros

Los registros se configuran desde:

```text
src/logging_config.py
```

Pueden guardar:

- inicio y final del proceso;
- archivo procesado;
- cantidad de registros;
- validaciones realizadas;
- errores encontrados;
- archivo generado;
- actualización del Dashboard;
- generación del mapa.

Los registros se almacenan en:

```text
logs/
```

---

## 16. Ejecución del sistema

El sistema se puede iniciar mediante:

```text
iniciar.bat
```

o directamente:

```bash
python main.py
```

### Requisitos

- Python instalado.
- Entorno virtual creado.
- Dependencias instaladas.
- Estructura de carpetas completa.
- Archivos Excel disponibles.
- Dashboard cerrado.

### Instalación de dependencias

```bash
pip install -r requirements.txt
```

---

## 17. Desarrollo futuro de ANS Redes

ANS Redes se desarrollará dentro del mismo proyecto, pero como un submódulo independiente.

### Decisión

- ANS Conexiones permanece como está.
- No se mueven sus archivos actuales.
- No se modifican sus importaciones.
- Se crea únicamente una nueva carpeta dentro de `src`.

### Estructura propuesta

```text
src
├── archivos actuales de ANS Conexiones
│
└── ans_redes
    ├── __init__.py
    ├── procesador.py
    ├── validador.py
    ├── filtros.py
    ├── calculador_ans.py
    └── generador_excel.py
```

### Qué es un submódulo

Es una carpeta dentro de `src` que reúne los archivos de una funcionalidad específica.

En este caso:

```text
src/ans_redes/
```

contendrá únicamente la lógica de Redes.

### Responsabilidad de sus archivos

| Archivo | Responsabilidad |
|---|---|
| `__init__.py` | Identifica la carpeta como paquete Python. |
| `procesador.py` | Coordina todo el flujo de Redes. |
| `validador.py` | Revisa los Excel de Redes. |
| `filtros.py` | Aplica procesos, códigos, estados y usuarios. |
| `calculador_ans.py` | Calcula los estados ANS de Redes. |
| `generador_excel.py` | Genera el informe final de Redes. |

### Orden para iniciar el desarrollo

```text
Analizar el requerimiento
          │
          ▼
Revisar el archivo fuente
          │
          ▼
Identificar columnas y filtros
          │
          ▼
Confirmar reglas de negocio
          │
          ▼
Crear src/ans_redes
          │
          ▼
Desarrollar y probar cada parte
          │
          ▼
Validar resultados con los usuarios
```

### Integración con la interfaz

El botón se crea en:

```text
src/interfaz.py
```

El botón solo inicia el proceso. La lógica debe permanecer en:

```text
src/ans_redes/procesador.py
```

### Flujo del botón

```text
Usuario presiona “Generar ANS Redes”
                 │
                 ▼
interfaz.py
                 │
                 ▼
procesar_ans_redes()
                 │
                 ▼
src/ans_redes/procesador.py
                 │
                 ├── valida
                 ├── filtra
                 ├── calcula
                 └── genera el informe
```

### Importación esperada

```python
from src.ans_redes.procesador import procesar_ans_redes
```

> **Decisión técnica:** primero se agrega ANS Redes sin reorganizar ANS Conexiones. Una posible estructura común se evaluará después, cuando ambos procesos estén estables.

---

## 18. Guía rápida para una reunión

### Si preguntan: “¿Cómo creó el desarrollo?”

> Primero entendí el proceso y las reglas del negocio. Después dividí la solución en partes: lectura, validación, transformación, cálculo, generación del Excel, Dashboard e interfaz. Para la implementación utilicé documentación, librerías, ejemplos e Inteligencia Artificial como apoyo. Finalmente realicé pruebas y validé que el resultado respondiera a la necesidad real.

### Si preguntan: “¿Cómo está dividido?”

> La interfaz recibe la acción del usuario, el procesador coordina el flujo, el validador revisa los Excel, el transformador organiza los datos, el calculador aplica las reglas ANS y los generadores producen los resultados.

### Si preguntan: “¿Cómo empezaría ANS Redes?”

> Primero analizaría el archivo y confirmaría el requerimiento. Después identificaría columnas, filtros, códigos, estados y reglas. Luego crearía `src/ans_redes` como un submódulo independiente, sin mover ANS Conexiones, y desarrollaría allí la validación, los filtros, el cálculo y la generación del informe.

### Si preguntan algo muy específico

> Entiendo el flujo completo y la responsabilidad de cada módulo. Para un detalle de implementación puntual, revisaría el código correspondiente para dar una respuesta exacta.

### Frase final

> No es necesario memorizar todo el código. Lo importante es entender el problema, saber cómo está organizada la solución y poder ubicar rápidamente dónde se realiza cada proceso.
