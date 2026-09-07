# 📦 NEXUS / Kardex — Manual Funcional y Operativo Completo

> **Propósito de este documento:** servir como guía paso a paso para explicar y operar NEXUS frente al usuario final, sin depender de la memoria del desarrollador.
>
> La regla de validación es simple: **lo que dice este manual debe coincidir con lo que el usuario ve en NEXUS**. Si durante una prueba la pantalla cambia, este documento debe actualizarse.

---

# 1. Objetivo general de NEXUS

NEXUS es una herramienta para controlar inventario, movimientos de materiales, trazabilidad de seriales, inventario por técnico, ajustes y conciliación operativa contra DRACO.

Permite responder preguntas como:

- ¿Qué material ingresó?
- ¿Qué material salió?
- ¿A qué técnico se entregó?
- ¿Qué seriales tiene actualmente cada técnico?
- ¿Qué seriales fueron reintegrados?
- ¿Cuál es el stock actual?
- ¿Qué movimientos presenta un material?
- ¿Qué diferencias existen entre NEXUS y DRACO?
- ¿Qué técnicos o materiales requieren revisión?

---

# 2. Orden recomendado para explicar NEXUS al usuario

Cuando se haga una entrega o capacitación, se recomienda explicar los módulos en este orden:

1. Kardex Inventario
2. Materiales
3. Personal
4. Inventario Técnico
5. Inventario General
6. Ajustes Kardex
7. Seriales
8. Auditoría Seriales
9. Dashboard
10. Conciliación Operativa
11. Manual

---

# 3. 📦 Módulo Kardex Inventario

## 3.1 Objetivo

Registrar los movimientos que afectan o documentan el inventario.

Desde esta pantalla se realizan entradas, salidas, reintegros y otros movimientos definidos por la operación.

---

## 3.2 Campos principales de la pantalla

Los campos pueden cambiar según el tipo de movimiento seleccionado.

Campos habituales:

- **Tipo de almacén**
- **Código material**
- **Tipo de movimiento**
- **Cantidad**
- **Seriales**, cuando el material es serializado
- **Responsable**
- **Número de ACTA**, cuando aplica
- **Confirmación del ACTA**, cuando aplica
- **Bodega origen / destino**, según movimiento
- **Cédula técnico**, cuando aplica
- **Observación**
- **Registrar Movimiento**

---

## 3.3 Seleccionar tipo de almacén

En la pantalla aparece:

```text
Seleccione tipo de almacén
```

Opciones observadas:

```text
ELITE INGENIEROS
EPM
```

El usuario debe seleccionar el tipo de almacén correspondiente antes de continuar.

---

## 3.4 Ingresar código de material

En el campo de código se escribe el código exacto del material.

Material de 10 digitos corresponde al consumo de Elite Ingenieros.
Material de 6 digitos coresponde al consumo de EPM.

Ejemplo:

```text
2100000098
```

NEXUS debe reconocer el material.

Si el material no existe, no se debe continuar con el movimiento.

---

## 3.5 Seleccionar tipo de movimiento

Después de identificar el material, se selecciona el movimiento requerido.

Ejemplos de movimientos existentes en NEXUS:

```text
ENTRADA ELITE
ENTRADA PROVEEDOR
ENTREGA AH
REINTEGRO
DEVOLUCION
DEVOLUCION AHTA
SALIDA ELITE
SALIDA TECNICO
SALIDA EPM
AJUSTE ENTRADA
AJUSTE SALIDA
REINTEGRO SERIAL
```

> El usuario no debe escoger manualmente `AJUSTE ENTRADA` o `AJUSTE SALIDA` desde el módulo de Ajustes Kardex. Ese módulo determina el sentido automáticamente.

---

## 3.6 Cantidad

El usuario ingresa la cantidad correspondiente al movimiento.

Para materiales serializados:

```text
Cantidad = número de seriales que se están procesando
```

---

# 4. Cómo registrar una ENTRADA

## 4.1 Entrada de material no serializado

### Paso a paso

1. Ingresar a **Kardex Inventario**.
2. Seleccionar tipo de almacén.
3. Ingresar código material.
4. Confirmar que NEXUS reconozca el material.
5. Seleccionar un movimiento de entrada.
6. Ingresar cantidad.
7. Seleccionar responsable.
8. Completar los campos adicionales que solicite la pantalla.
9. Ingresar observación.
10. Presionar **Registrar Movimiento**.
11. Confirmar que el movimiento aparezca en el historial.

### Resultado esperado

```text
Stock final > Stock anterior
```

---

## 4.2 Entrada de material serializado

Cuando el material está marcado como serializado, NEXUS muestra:

```text
Este material requiere registro de seriales
```

### Modo manual

1. Seleccionar movimiento de entrada.
2. Ingresar cantidad.
3. Seleccionar **Manual**.
4. Digitar cada serial.
5. Confirmar que el total de seriales coincida con la cantidad.
6. Completar responsable y demás campos.
7. Registrar movimiento.

### Resultado esperado

Los seriales ingresados quedan:

```text
DISPONIBLE
```

---

## 4.3 Entrada serializada por archivo

El usuario puede cargar un Excel con los seriales.

Regla recomendada:

```text
Primera fila = encabezado
Datos desde la fila 2
```

El total de seriales cargados debe coincidir con la cantidad del movimiento.

---

# 5. Cómo registrar una SALIDA

## 5.1 Salida de material no serializado

1. Seleccionar tipo de almacén.
2. Ingresar código.
3. Seleccionar tipo de salida.
4. Ingresar cantidad.
5. Seleccionar responsable.
6. Completar ACTA si aplica.
7. Completar técnico si aplica.
8. Ingresar observación.
9. Registrar movimiento.

Resultado esperado:

```text
Stock final < Stock anterior
```

---

## 5.2 Salida de material serializado

### Regla crítica

Todo serial que pase a:

```text
ASIGNADO
```

debe quedar asociado a un técnico válido.

### Paso a paso

1. Seleccionar movimiento de salida.
2. Ingresar cantidad.
3. Seleccionar o cargar los seriales.
4. Seleccionar responsable.
5. Ingresar número de ACTA cuando corresponda.
6. Confirmar que el movimiento corresponde al ACTA.
7. Ingresar la cédula del técnico.
8. Confirmar que NEXUS reconozca al técnico.
9. Ingresar observación.
10. Registrar movimiento.

### Validación confirmada

Si la cédula queda vacía o no es válida, NEXUS bloquea la salida.

Mensaje observado:

```text
Debe ingresar una cédula válida
```

### Resultado esperado

```text
Serial DISPONIBLE
↓
SALIDA
↓
Serial ASIGNADO
↓
Asociado a técnico
```

---

# 6. 🧱 Módulo Materiales

## 6.1 Objetivo

Administrar el catálogo de materiales utilizados por NEXUS.

---

## 6.2 Crear material

El usuario debe completar los campos disponibles en la pantalla de creación.

Campos relevantes del catálogo:

- Código
- Nombre
- Descripción
- Tipo de material
- Serializado

### Regla

Si el material requiere control individual por número de serie:

```text
Serializado = Sí
```

Si no:

```text
Serializado = No
```

---

## 6.3 Validación del material serializado

Cuando un material serializado se usa en Kardex, NEXUS debe solicitar seriales.

Cuando no es serializado, no debe solicitarlos.

---

# 7. 👥 Módulo Personal

## 7.1 Objetivo

Administrar el personal que puede participar en los movimientos y procesos operativos.

---

## 7.2 Crear personal

1. Ingresar al módulo **Personal**.
2. Seleccionar la pestaña de creación.
3. Ingresar cédula.
4. Ingresar nombre.
5. Seleccionar zona.
6. Guardar.

### Regla

El registro debe quedar disponible también para las operaciones que utilizan la tabla de técnicos.

---

## 7.3 Editar personal

1. Buscar la persona.
2. Editar nombre o zona.
3. Guardar.
4. Confirmar que el cambio se refleje correctamente.

### Validación importante

Se comprobó que la edición debe mantener sincronía entre:

```text
personal
↔
tecnicos
```

---

## 7.4 Responsables

Dentro del módulo Personal existe administración de responsables.

Operaciones:

- Crear
- Editar
- Activar
- Inactivar

### Regla

Un responsable inactivo:

- no debe aparecer en movimientos nuevos;
- sí debe conservarse en registros históricos.

---

# 8. 👷 Inventario Técnico

## 8.1 Objetivo

Consultar qué materiales o seriales están actualmente asignados a un técnico.

---

## 8.2 Consulta

1. Ingresar al módulo.
2. Buscar o seleccionar técnico.
3. Consultar inventario actual.
4. Revisar historial cuando aplique.

---

## 8.3 Regla de seriales

Un serial aparece en inventario técnico cuando:

```text
Estado = ASIGNADO
```

Después de un reintegro:

```text
ASIGNADO
↓
REINTEGRO
↓
DISPONIBLE
```

debe dejar de aparecer en el inventario actual del técnico.

---

# 9. 📊 Inventario General

## 9.1 Objetivo

Consultar el historial general de movimientos de materiales.

---

## 9.2 Información esperada

Según el movimiento, el reporte puede mostrar:

- Fecha
- Cédula
- Técnico
- Código
- Material
- Tipo
- Acta
- Orden / Remisión
- Proveedor
- Cantidad
- Stock Antes
- Stock Final
- Responsable
- Bodega
- Observación

---

## 9.3 Exportar

El módulo permite exportar la información a Excel.

Antes de entregar el sistema se debe comprobar que lo mostrado en pantalla coincida con el archivo exportado.

---

# 10. 🔨 Ajustes Kardex

## 10.1 Objetivo

Corregir el stock cuando el inventario físico real no coincide con NEXUS.

---

## 10.2 Regla aprobada

El usuario NO decide si es entrada o salida.

Solo ingresa:

```text
Stock físico correcto
```

NEXUS calcula automáticamente la diferencia.

---

## 10.3 Ejemplos

### Caso 1

```text
Sistema = 4
Físico = 4
```

Resultado:

```text
No se genera ajuste
```

### Caso 2

```text
Sistema = 4
Físico = 6
```

Resultado:

```text
AJUSTE ENTRADA = 2
```

### Caso 3

```text
Sistema = 6
Físico = 4
```

Resultado:

```text
AJUSTE SALIDA = 2
```

---

## 10.4 Qué no debe hacer el usuario

No debe seleccionar manualmente:

```text
ENTRADA
SALIDA
```

como sentido del ajuste.

El sistema lo determina comparando:

```text
Stock físico correcto
vs
Stock actual NEXUS
```

---

# 11. 🔢 Módulo Seriales

El módulo contiene:

- Lista
- Editar
- Eliminar
- Reintegros

---

## 11.1 Lista

Permite consultar:

- Serial
- Estado
- Fecha Ingreso
- Fecha Asignación
- Técnico

También permite exportar a Excel.

---

## 11.2 Editar número

Se utiliza únicamente para corregir un serial mal digitado.

Ejemplo:

```text
SERIAL-004
↓
SERIAL-004-CORREGIDO
```

Debe conservarse:

- material
- estado
- relación interna
- histórico

---

## 11.3 Editar estado

### DESHABILITADO

La función fue retirada de la interfaz.

### Motivo

Permitía generar:

```text
ASIGNADO
sin técnico
```

Lo cual podía dejar inconsistente el Inventario Técnico.

---

# 12. 🔁 Reintegros de seriales

## 12.1 Objetivo

Liberar seriales asignados y devolverlos al estado:

```text
DISPONIBLE
```

---

## 12.2 Reintegro por selección manual

1. Ingresar código de material.
2. NEXUS muestra únicamente seriales ASIGNADOS.
3. Marcar uno o varios seriales.
4. Seleccionar responsable.
5. Ejecutar **Reintegrar seleccionados**.

Resultado:

```text
ASIGNADO
↓
REINTEGRO
↓
DISPONIBLE
```

---

## 12.3 Reintegro por Excel

Archivo requerido:

```text
serial
SERIAL001
SERIAL002
SERIAL003
```

### Importante

No se requiere columna de cédula.

NEXUS identifica automáticamente el técnico al que estaba asociado cada serial antes del reintegro.

### Ejemplo

```text
Técnico con 40 seriales
↓
Excel con esos 40 seriales
↓
Reintegro
↓
40 seriales DISPONIBLES
↓
El técnico deja de tenerlos en inventario actual
```

---

# 13. 📋 Auditoría Seriales

## Objetivo

Mostrar la trazabilidad histórica de los cambios de estado de un serial.

Campos:

- Serial
- Código
- Material
- Técnico
- Estado Antes
- Estado Nuevo
- Evento
- Responsable
- Fecha
- Observación

---

## 13.1 Eventos

### SALIDA

```text
DISPONIBLE → ASIGNADO
```

### REINTEGRO

```text
ASIGNADO → DISPONIBLE
```

### AJUSTE

Corrección manual histórica.

La opción que generaba este evento manual fue deshabilitada, pero los registros se conservan para auditoría.

---

## 13.2 Filtros

Se validaron filtros por:

- Serial
- Evento
- Responsable

---

# 14. 📈 Dashboard

## Objetivo

Presentar indicadores generales del inventario.

### Estado actual

Debe revalidarse antes de la entrega definitiva.

Durante la revalidación se deben comparar los KPIs contra consultas SQL para confirmar que no exista doble conteo o suma incorrecta.

---

# 15. ⚖️ Conciliación Operativa NEXUS vs DRACO

## 15.1 Objetivo

Comparar:

```text
NEXUS
Salidas + Reintegros

vs

DRACO
Instalados
```

por técnico y material.

---

## 15.2 Preparar DRACO

Los archivos DRACO están almacenados por meses, pero un mismo archivo puede contener más de un acta.

Por tanto:

```text
NO cargar directamente un archivo mensual completo
```

Primero se debe preparar el archivo correspondiente al acta específica.

Ejemplo:

```text
Acta 9
↓
Unificar archivos DRACO
↓
Filtrar únicamente Acta 9
↓
Guardar archivo Acta 9
↓
Cargarlo en NEXUS
```

---

## 15.3 Relación acta / periodo usada operativamente

```text
Acta 5  → Enero
Acta 6  → Febrero
Acta 7  → Marzo
Acta 8  → Abril
Acta 9  → Mayo
Acta 10 → Junio
Acta 11 → Julio
Acta 12 → Agosto
```

La conciliación técnica se realiza por número de acta.

---

## 15.4 Cómo se cruza DRACO con NEXUS

DRACO trae:

```text
Técnico
Código
Cantidad
```

DRACO no necesita traer cédula.

NEXUS utiliza:

```text
equivalencias_tecnicos_draco
```

para obtener:

```text
Nombre DRACO
↓
Cédula
↓
Nombre NEXUS
```

El cruce final utiliza:

```text
Cédula + Código
```

---

## 15.5 Sin equivalencia

Significa:

```text
NEXUS recibió un técnico DRACO
pero no pudo relacionarlo con una equivalencia activa
```

No significa necesariamente que el técnico no exista.

### Hallazgo validado

DRACO y NEXUS pueden manejar el mismo técnico con distinto orden del nombre.

Ejemplo conceptual:

```text
DRACO:
NOMBRE APELLIDO1 APELLIDO2

NEXUS:
APELLIDO1 APELLIDO2 NOMBRE
```

La tabla de equivalencias actúa como puente y utiliza la cédula como identificador confiable.

---

## 15.6 Qué hacer cuando aparece Sin equivalencia

1. Copiar el nombre DRACO.
2. Buscarlo en `tecnicos`.
3. Si no aparece exacto, buscar por apellido o palabra clave.
4. Buscar también en `personal`.
5. Identificar la cédula correcta.
6. Consultar si ya existe equivalencia por cédula.
7. Si existe, corregir `tecnico_draco`.
8. Si no existe, crear equivalencia solo después de validar identidad.
9. Repetir conciliación.
10. Confirmar que `Sin equivalencia` disminuya o llegue a 0.

---

# 16. Trazabilidad de registros

La conciliación no compara fila contra fila.

NEXUS muestra:

- DRACO original
- DRACO tras exclusiones
- Sin equivalencia
- DRACO consolidado
- NEXUS consolidado
- Conciliación final

Ejemplo validado:

```text
DRACO original: 14053
DRACO consolidado: 647
NEXUS consolidado: 729
Conciliación final: 812
```

Esto ocurre porque DRACO se consolida por:

```text
Cédula + Técnico NEXUS + Código
```

y luego se cruza por:

```text
Cédula + Código
```

---

# 17. Estados de conciliación

Fórmula:

```text
DIFERENCIA =
SALIDAS - REINTEGROS - INSTALADOS
```

### OK

```text
Diferencia = 0
```

### PENDIENTE DEVOLUCIÓN

Quedó saldo entregado que no aparece instalado ni reintegrado.

### INSTALACIÓN SIN ENTREGA

DRACO reporta instalación, pero NEXUS no registra salida.

### REINTEGRO SIN ENTREGA A TÉCNICO

NEXUS registra reintegro sin una salida previa correspondiente.

### REVISAR OPERACIÓN

Existe un descuadre que requiere análisis manual.

---

# 18. Cobertura

Indicadores:

- Técnicos NEXUS
- Técnicos DRACO
- Técnicos Cruzados
- NEXUS sin DRACO
- Cobertura %

La cobertura es:

```text
Técnicos Cruzados / Técnicos NEXUS
```

No significa por sí sola que la conciliación esté bien o mal.

---

# 19. Posibles causas a validar

Cuando un técnico está en NEXUS pero no en DRACO:

- planilla pendiente
- instalación pendiente de legalización
- archivo DRACO incompleto
- diferencia de registro
- técnico aún no incluido

NEXUS muestra la novedad, pero la causa debe validarse operacionalmente.

---

# 20. Cierre de entrega

Antes de entregar NEXUS:

- volver a probar todos los módulos;
- validar pantalla vs manual;
- corregir solo errores reales;
- actualizar este documento;
- ejecutar SQL de control;
- verificar exportaciones;
- confirmar DEV;
- hacer backup;
- cerrar Git;
- preparar despliegue.
