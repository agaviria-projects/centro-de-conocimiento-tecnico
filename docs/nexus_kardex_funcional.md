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

El módulo **Kardex Inventario** es la pantalla principal para registrar los movimientos de materiales en NEXUS.

Desde aquí el usuario puede registrar:

- Entradas de materiales.
- Salidas.
- Entregas a técnicos.
- Reintegros.
- Traslados ELITE.
- Transferencias EPM.

La información registrada en este módulo alimenta posteriormente:

- Stock actual.
- Inventario Técnico.
- Inventario General.
- Seriales.
- Auditoría.
- Conciliación Operativa.

---

## 3.2 Regla principal del inventario

NEXUS trabaja con dos tipos de material:

```text
ELITE INGENIEROS
Código de 10 dígitos
Ejemplo: 9999999904
No utiliza seriales
```

```text
EPM
Código de 6 dígitos
Ejemplo: 999991
Puede utilizar seriales
```

La bodega que controla el **stock real** es:

```text
METROPOLITANA SUR
```

Las demás zonas, por ejemplo:

```text
ORIENTE
OCCIDENTE
NORDESTE
SUROESTE
```

se utilizan principalmente para conservar trazabilidad de traslados y transferencias.

Por tanto:

```text
METROPOLITANA SUR
→ controla existencias reales

OTRAS ZONAS
→ conservan trazabilidad
→ no generan un segundo stock real
```

---

# 4. Cómo registrar un material ELITE

## 4.1 Identificación

Seleccionar:

```text
Tipo de almacén:
ELITE INGENIEROS
```

Ingresar un código ELITE de 10 dígitos.

Ejemplo utilizado durante las pruebas:

```text
9999999904
MATERIAL DE PRUEBA ELITE
```

Los materiales ELITE trabajan por **cantidad** y no por serial.

---

## 4.2 Movimientos disponibles para ELITE

En Kardex se muestran:

```text
ENTRADA ELITE INGENIEROS
ENTRADA PROVEEDOR
SALIDA ELITE INGENIEROS
TRASLADO
ENTREGA AH
REINTEGRO
```

El usuario debe seleccionar el movimiento de acuerdo con lo que ocurrió físicamente.

---

## 4.3 ENTRADA ELITE INGENIEROS

Se utiliza cuando el material ingresa al inventario ELITE.

### Paso a paso

1. Ingresar a **Kardex Inventario**.
2. Seleccionar **ELITE INGENIEROS**.
3. Seleccionar la fecha real del movimiento.
4. Digitar el código del material.
5. Confirmar que NEXUS reconozca el material.
6. Seleccionar **ENTRADA ELITE INGENIEROS**.
7. Ingresar la cantidad.
8. Seleccionar el responsable.
9. Completar la información adicional mostrada por la pantalla.
10. Escribir una observación cuando corresponda.
11. Presionar **Registrar Movimiento**.

### Resultado esperado

```text
Stock Metropolitana Sur
ANTES < DESPUÉS
```

Ejemplo:

```text
Stock antes: 5
Entrada: 3
Stock después: 8
```

---

## 4.4 ENTRADA PROVEEDOR

Se utiliza cuando el material ingresa directamente desde un proveedor.

Además de la cantidad, NEXUS puede solicitar:

```text
Remisión / Orden
Proveedor
Responsable
Observación
```

El resultado también debe incrementar el stock de Metropolitana Sur.

---

## 4.5 SALIDA ELITE INGENIEROS

Se utiliza cuando material ELITE sale de Metropolitana Sur.

### Paso a paso

1. Seleccionar **ELITE INGENIEROS**.
2. Digitar código del material.
3. Seleccionar **SALIDA ELITE INGENIEROS**.
4. Ingresar cantidad.
5. Seleccionar técnico cuando la pantalla lo solicite.
6. Seleccionar responsable.
7. Ingresar ACTA cuando aplique.
8. Confirmar el ACTA cuando NEXUS lo solicite.
9. Escribir observación.
10. Registrar.

### Resultado esperado

```text
Stock Metropolitana Sur disminuye
```

Ejemplo:

```text
Stock antes: 8
Salida: 1
Stock después: 7
```

NEXUS no debe permitir una salida superior al stock disponible.

---

## 4.6 TRASLADO ELITE

El **TRASLADO** se utiliza para mover material ELITE desde:

```text
METROPOLITANA SUR
↓
otra zona
```

Ejemplo:

```text
METROPOLITANA SUR → ORIENTE
```

NEXUS genera internamente dos registros relacionados.

### Movimiento de origen

```text
SALIDA ELITE INGENIEROS
METROPOLITANA SUR
```

Este movimiento disminuye el stock real.

### Movimiento destino

```text
ENTRADA ELITE INGENIEROS
Zona destino
```

Este movimiento conserva trazabilidad y no genera stock adicional.

Ambos registros utilizan una referencia común:

```text
TRAS-xxxxxxxxxx
```

### Ejemplo validado

```text
METROPOLITANA SUR
Stock 8 → 7

ORIENTE
Stock 0 → 0
```

Esto es correcto.

El material físicamente fue trasladado, pero NEXUS mantiene un único stock real controlado desde Metropolitana Sur.

---

## 4.7 ENTREGA AH

Este movimiento quedó funcionalmente validado como una entrega desde:

```text
METROPOLITANA SUR
↓
TÉCNICO
```

NEXUS solicita un técnico válido.

### Ejemplo validado

```text
Material: 9999999904
Cantidad: 1
Técnico: 12345678
Stock antes: 7
Stock después: 6
```

Resultado:

```text
ENTREGA AH
→ disminuye stock
→ registra el técnico receptor
→ conserva trazabilidad
```

### Nota

El significado operativo exacto de la sigla **AH** debe ser confirmado con la operación antes de documentarlo con otro nombre.

---

# 5. Cómo registrar un material EPM

## 5.1 Identificación

Seleccionar:

```text
Tipo de almacén:
EPM
```

Ingresar un código EPM de 6 dígitos.

Ejemplo utilizado durante las pruebas:

```text
999991
MATERIAL PRUEBA EPM SERIALIZADO
```

Los materiales EPM pueden ser:

```text
No serializados
o
Serializados
```

NEXUS identifica esta condición desde el catálogo de Materiales.

---

## 5.2 Material EPM serializado

Cuando un material requiere seriales, NEXUS muestra los controles correspondientes.

Regla:

```text
1 unidad
=
1 serial
```

Ejemplo:

```text
Cantidad: 3

Seriales:
EPM-PRUEBA-001
EPM-PRUEBA-002
EPM-PRUEBA-003
```

El número de seriales debe coincidir con la cantidad.

---

## 5.3 ENTRADA PROVEEDOR EPM serializada

### Paso a paso

1. Seleccionar **EPM**.
2. Seleccionar la fecha.
3. Digitar código del material.
4. Confirmar que NEXUS indique que requiere seriales.
5. Seleccionar **ENTRADA PROVEEDOR**.
6. Ingresar cantidad.
7. Digitar o cargar los seriales.
8. Seleccionar responsable.
9. Completar Remisión / Orden.
10. Completar Proveedor.
11. Escribir observación.
12. Registrar.

### Resultado esperado

Los seriales nuevos quedan:

```text
DISPONIBLE
```

y ubicados inicialmente en:

```text
METROPOLITANA SUR
```

Ejemplo:

```text
EPM-PRUEBA-004
Estado: DISPONIBLE
Ubicación: METROPOLITANA SUR
```

---

## 5.4 SALIDA EPM serializada

Se utiliza cuando un serial EPM se entrega a un técnico.

### Paso a paso

1. Seleccionar **EPM**.
2. Digitar código.
3. Seleccionar **SALIDA EPM**.
4. Indicar cantidad.
5. Digitar o seleccionar los seriales.
6. Ingresar ACTA.
7. Confirmar ACTA.
8. Seleccionar o buscar el técnico.
9. Seleccionar responsable.
10. Escribir observación.
11. Registrar.

### Validaciones

Antes de permitir la salida, el serial debe estar disponible.

```text
DISPONIBLE
↓
SALIDA EPM
↓
ASIGNADO
```

Después de registrar:

```text
Estado = ASIGNADO
Técnico = técnico que recibió el serial
```

El movimiento también disminuye el stock de Metropolitana Sur.

---

# 6. TRANSFERENCIA EPM

## 6.1 Objetivo

La **TRANSFERENCIA** permite mover un material EPM desde Metropolitana Sur hacia otra zona.

Ejemplo:

```text
METROPOLITANA SUR
↓
ORIENTE
```

NEXUS genera dos movimientos relacionados.

---

## 6.2 Movimiento de origen

Internamente se registra:

```text
SALIDA EPM
METROPOLITANA SUR
```

Este movimiento disminuye el stock real.

---

## 6.3 Movimiento destino

Internamente se registra:

```text
ENTRADA TRANSFERENCIA EPM
Zona destino
```

Este movimiento es de trazabilidad.

Su configuración es:

```text
afecta = 0
```

Por tanto, no genera un segundo stock.

---

## 6.4 Referencia de transferencia

Los dos movimientos quedan relacionados mediante:

```text
TR-xxxxxxxxxx
```

Ejemplo validado:

```text
SALIDA EPM
METROPOLITANA SUR
Stock 1 → 0

ENTRADA TRANSFERENCIA EPM
ORIENTE
Stock 0 → 0
```

En **Consultar Movimientos**, ambas filas pueden mostrarse funcionalmente como:

```text
TRANSFERENCIA
```

Esto facilita la lectura para el usuario.

---

## 6.5 Trazabilidad del serial transferido

Esta regla es importante.

Un serial transferido a una zona puede continuar:

```text
Estado = DISPONIBLE
```

porque no está asignado a ningún técnico.

Pero también debe conservar su ubicación física actual.

Ejemplo validado:

```text
Serial:
EPM-PRUEBA-004

Estado:
DISPONIBLE

Último movimiento:
ENTRADA TRANSFERENCIA EPM

Ubicación:
ORIENTE
```

Por tanto:

```text
DISPONIBLE
```

significa:

```text
No está asignado a un técnico
```

y no significa necesariamente:

```text
Está en Metropolitana Sur
```

La ubicación debe consultarse junto con el último movimiento del serial.

---

# 7. REINTEGROS

## 7.1 Objetivo

El reintegro registra material que había salido previamente y posteriormente fue devuelto.

La fecha del reintegro corresponde al día real en que el material regresó.

La **ACTA**, en cambio, debe conservar la ACTA de la salida original.

Esta regla es fundamental para la Conciliación Operativa.

---

## 7.2 Reintegro serializado

En un material serializado, el propio serial permite identificar la salida original.

NEXUS recupera automáticamente:

```text
ACTA original
Técnico original
Fecha de salida
Movimiento original
```

Antes de registrar, muestra la validación al usuario.

### Resultado

```text
ASIGNADO
↓
REINTEGRO
↓
DISPONIBLE
```

El serial deja de estar asignado al técnico.

---

## 7.3 Reintegro no serializado

En materiales sin serial no existe una unidad individual que permita conocer de qué salida provino físicamente la devolución.

Por esto NEXUS consulta el histórico de:

```text
Técnico + Material
```

y calcula cuánto tiene pendiente por devolver.

Posteriormente propone una distribución utilizando las salidas más antiguas primero.

```text
FIFO
```

La distribución se realiza por fecha real de salida.

### Ejemplo

Un técnico tiene:

```text
Salida A
ACTA 11
5 unidades pendientes

Salida B
ACTA 10
6 unidades pendientes
```

Si devuelve:

```text
7 unidades
```

NEXUS puede distribuir:

```text
5 → salida A
2 → salida B
```

generando dos reintegros.

Cada reintegro conserva:

```text
ACTA original
Movimiento original
```

mediante la referencia:

```text
ORIGEN_MOV
```

Esto permite conservar la trazabilidad histórica correctamente.

---

# 8. Cómo verificar un movimiento después de registrarlo

Después de realizar cualquier operación se recomienda utilizar:

```text
Consultar Movimientos
```

y comprobar:

- Fecha.
- Tipo.
- Cantidad.
- Stock antes.
- Stock después.
- Técnico.
- Bodega.
- Observación.
- ACTA cuando corresponda.

Para traslados o transferencias deben aparecer dos filas relacionadas por la misma referencia.

Ejemplo:

```text
TRAS-xxxxxxxx
```

o:

```text
TR-xxxxxxxx
```

---

# 9. Guía rápida para capacitación del usuario

Para una prueba de aceptación con el usuario final se recomienda realizar estos casos.

## Caso A — Material ELITE

```text
Tipo almacén:
ELITE INGENIEROS

Código:
material ELITE de 10 dígitos

Movimiento:
ENTRADA ELITE INGENIEROS

Registrar:
1 unidad
```

Confirmar que aumenta el stock.

Después realizar:

```text
SALIDA ELITE INGENIEROS
```

y confirmar que disminuye.

---

## Caso B — Material EPM serializado

```text
Tipo almacén:
EPM

Código:
material EPM serializado de 6 dígitos

Movimiento:
ENTRADA PROVEEDOR

Cantidad:
1

Serial:
serial nuevo de prueba
```

Confirmar:

```text
Estado = DISPONIBLE
Ubicación = METROPOLITANA SUR
```

Después realizar una:

```text
SALIDA EPM
```

y confirmar:

```text
Estado = ASIGNADO
Técnico = técnico seleccionado
```

---

## Caso C — Transferencia EPM

Con un serial disponible en Metropolitana:

```text
TRANSFERENCIA
METROPOLITANA SUR → ORIENTE
```

Confirmar:

```text
Stock Metropolitana disminuye

Zona destino:
0 → 0

Serial:
DISPONIBLE

Ubicación:
ORIENTE
```

---

## Caso D — Reintegro

Realizar un reintegro de una salida existente.

Confirmar que NEXUS conserve:

```text
ACTA de la salida original
Técnico original
Trazabilidad histórica
```

En serializados:

```text
ASIGNADO → DISPONIBLE
```

---

# 10. Estado de validación del módulo Kardex Inventario

```text
ENTRADA ELITE INGENIEROS       = OK
ENTRADA PROVEEDOR              = OK
SALIDA ELITE INGENIEROS        = OK
SALIDA EPM                     = OK
TRASLADO ELITE                 = OK
TRANSFERENCIA EPM              = OK
UBICACIÓN SERIAL TRANSFERIDO   = OK
ENTREGA AH                     = OK FUNCIONAL
REINTEGRO SERIALIZADO          = OK
REINTEGRO NO SERIALIZADO       = OK

KARDEX INVENTARIO              = APROBADO
```

Nota pendiente exclusivamente documental:

```text
Confirmar con operación el significado exacto de la sigla AH.
```

# 6. 🧱 Módulo Materiales

## 6.1 Objetivo

Administrar el catálogo de materiales utilizados por NEXUS.

Desde este módulo el usuario puede:

- Consultar materiales existentes.
- Crear nuevos materiales.
- Editar el nombre de un material.
- Eliminar materiales cuando corresponda.
- Definir si un material EPM requiere control por serial.

---

## 6.2 Pestañas del módulo

El módulo **Materiales** contiene cuatro pestañas:

```text
Lista
Crear
Editar
Eliminar
```

---

## 6.3 Crear material

Para crear un material:

1. Ingresar a **Materiales**.
2. Seleccionar la pestaña **Crear**.
3. Ingresar el **Código**.
4. Ingresar el **Nombre**.
5. Ingresar la **Descripción**.
6. Revisar la opción **¿Este material requiere seriales?**
7. Presionar **Crear**.

Todos los campos de texto son obligatorios.

Si el código ya existe, NEXUS debe impedir la creación y mostrar:

```text
Ya existe un material con ese código
```

---

## 6.4 Regla ELITE y EPM

La longitud del código identifica el origen del material:

```text
10 dígitos → Material ELITE
6 dígitos  → Material EPM
```

### Material ELITE

Ejemplo:

```text
2100000098
```

Los materiales ELITE no requieren control por serial.

Cuando NEXUS detecta un código de 10 dígitos:

```text
Código de 10 dígitos
↓
Material ELITE
↓
Serialización deshabilitada
↓
Control por cantidad
```

La opción:

```text
¿Este material requiere seriales?
```

debe permanecer deshabilitada.

NEXUS muestra además un mensaje indicando que el material fue identificado como ELITE.

---

### Material EPM

Ejemplo:

```text
219404
```

Los materiales EPM utilizan códigos de 6 dígitos.

Un material EPM puede requerir control por serial.

Cuando el código tiene 6 dígitos, NEXUS permite utilizar la opción:

```text
¿Este material requiere seriales?
```

Si el material requiere serialización:

```text
Marcado
```

Si no requiere serialización:

```text
Sin marcar
```

La configuración debe corresponder al material real que se está creando.

---

## 6.5 Resultado esperado al crear

Después de presionar **Crear**:

```text
Material creado correctamente
```

El material debe:

- quedar registrado en NEXUS;
- conservar código, nombre y descripción;
- conservar correctamente su condición de serialización;
- aparecer en la pestaña **Lista**;
- quedar disponible para utilizarse en **Kardex Inventario**.

---

## 6.6 Pestaña Lista

La pestaña **Lista** permite consultar los materiales registrados.

La pantalla muestra el total de registros y permite consultar principalmente:

```text
Código
Nombre
```

La tabla permite ordenar y filtrar los registros.

Después de crear un material se recomienda:

```text
Crear
↓
Ir a Lista
↓
Buscar el código
↓
Confirmar código y nombre
```

---

## 6.7 Pestaña Editar

La pestaña **Editar** permite modificar actualmente el **nombre** de un material existente.

Procedimiento:

1. Ingresar a **Editar**.
2. Escribir el **Código material**.
3. Confirmar que NEXUS muestre el **Nombre actual**.
4. Escribir el **Nuevo nombre**.
5. Marcar **Confirmar actualización**.
6. Presionar **Actualizar**.

Resultado esperado:

```text
Material actualizado correctamente
```

### Importante

Actualmente esta pantalla no modifica:

```text
Código
Descripción
Serialización
```

Por lo tanto, el usuario debe utilizar esta opción únicamente para corregir el nombre.

---

## 6.8 Pestaña Eliminar

La pestaña **Eliminar** permite eliminar un material.

Procedimiento:

1. Ingresar a **Eliminar**.
2. Escribir el **Código a eliminar**.
3. Confirmar que NEXUS muestre el nombre correcto.
4. Marcar **Confirmar eliminación**.
5. Presionar **Eliminar**.

Resultado esperado:

```text
Material eliminado correctamente
```

### Precaución

La eliminación debe utilizarse únicamente cuando corresponda.

No se recomienda eliminar materiales reales que ya tengan trazabilidad histórica sin una revisión técnica previa.

Para pruebas funcionales se deben utilizar materiales creados exclusivamente para prueba.

---

## 6.9 Materiales utilizados para las pruebas

Durante la revalidación del sistema se crearon materiales controlados para evitar afectar materiales reales.

### Material ELITE de prueba

```text
Código:
9999999904

Nombre:
MATERIAL DE PRUEBA ELITE

Tipo:
ELITE

Serializado:
NO
```

Prueba realizada:

```text
Código de 10 dígitos
↓
NEXUS identifica ELITE
↓
Opción de serialización deshabilitada
↓
PRUEBA OK
```

---

### Material EPM serializado de prueba

```text
Código:
999991

Nombre:
MATERIAL PRUEBA EPM SERIALIZADO

Descripción:
MATERIAL DE PRUEBA PARA VALIDACION FUNCIONAL NEXUS

Tipo:
EPM

Serializado:
SÍ
```

Prueba realizada:

```text
Código de 6 dígitos
↓
NEXUS identifica EPM
↓
Permite marcar serialización
↓
Kardex reconoce que requiere seriales
↓
PRUEBA OK
```

Estos materiales podrán utilizarse posteriormente para probar:

```text
Entradas
Salidas
Stock
Seriales
Asignación a técnico
Inventario Técnico
Reintegros
Auditoría Seriales
Ajustes Kardex
```

---

## 6.10 Validación del módulo

Estado actual:

```text
CREAR MATERIAL ELITE            = OK
RESTRICCIÓN SERIAL ELITE        = OK
CREAR MATERIAL EPM SERIALIZADO  = OK
RECONOCIMIENTO EN KARDEX        = OK

LISTA                           = EN REVALIDACIÓN
EDITAR                          = PENDIENTE DE PRUEBA
ELIMINAR                        = PENDIENTE DE PRUEBA

MÓDULO MATERIALES               = PENDIENTE DE CIERRE
```

El módulo solamente se marcará como **APROBADO** cuando se terminen las pruebas de Lista, Editar y Eliminar.

# 7. 👥 Módulo Personal

## 7.1 Objetivo

Administrar las personas que participan en la operación de NEXUS.

Desde este módulo se puede:

- Consultar personal existente.
- Crear personal.
- Editar personal.
- Eliminar personal cuando corresponda.
- Administrar responsables activos e inactivos.

El personal registrado puede participar posteriormente en procesos como:

```text
Salidas de material
Asignación a técnicos
Inventario Técnico
Conciliación Operativa
```

---

## 7.2 Pestañas del módulo

El módulo **Personal** contiene las siguientes opciones:

```text
Lista
Crear
Editar
Eliminar
Responsables
```

---

## 7.3 Crear personal

Para crear una persona:

1. Ingresar al módulo **Personal**.
2. Seleccionar la pestaña **Crear**.
3. Ingresar la **Cédula**.
4. Ingresar el **Nombre**.
5. Seleccionar la **Zona**.
6. Presionar el botón de creación o guardado mostrado por NEXUS.

### Resultado esperado

Después de crear el registro:

- La persona debe quedar almacenada en `personal`.
- Debe quedar disponible también en `tecnicos`.
- La cédula debe ser la misma en ambas tablas.
- El nombre debe coincidir en ambas tablas.

La relación esperada es:

```text
PERSONAL
Cédula + Nombre + Zona
        ↓
TÉCNICOS
Cédula + Nombre
```

---

## 7.4 Validación después de crear personal

Después de crear una persona:

1. Ir a **Lista**.
2. Buscar la cédula.
3. Confirmar nombre y zona.
4. Verificar que el técnico pueda ser utilizado posteriormente en los módulos que requieren técnico.

Para una validación técnica se puede comprobar además:

```sql
SELECT
    id_personal,
    cedula,
    nombre,
    zona
FROM personal
WHERE cedula = 'Digitar el número de la cedula';
```

y:

```sql
SELECT
    id_tecnico,
    cedula,
    nombre
FROM tecnicos
WHERE cedula = 'Digitar el número de la cedula';
```

Los dos registros deben corresponder a la misma persona.

---

## 7.5 Editar personal

La pestaña **Editar** permite modificar información de una persona existente.

Procedimiento general:

1. Buscar la persona por cédula.
2. Confirmar que NEXUS identifique el registro correcto.
3. Modificar la información permitida por la pantalla.
4. Confirmar la actualización.
5. Guardar los cambios.

### Regla importante

Cuando se modifica el nombre de una persona, NEXUS debe mantener sincronizado el registro correspondiente en:

```text
personal
↔
tecnicos
```

Esto evita que una misma cédula aparezca con nombres diferentes dentro del sistema.

---

## 7.6 Validación de edición

Después de editar una persona:

1. Consultarla nuevamente en **Personal**.
2. Confirmar el cambio realizado.
3. Consultar posteriormente el técnico en los módulos operativos.
4. Si se requiere validación técnica, comparar `personal` y `tecnicos` por cédula.

Resultado esperado:

```text
Misma cédula
↓
Nombre actualizado en Personal
↓
Nombre actualizado en Técnicos
```

---

## 7.7 Pestaña Eliminar

La pestaña **Eliminar** permite eliminar una persona cuando corresponda.

Esta opción debe utilizarse con precaución.

Antes de eliminar una persona se debe revisar si tiene relación con:

```text
Movimientos
Seriales
Inventario Técnico
Histórico
Conciliaciones
```

No se recomienda eliminar personal real con trazabilidad histórica sin una revisión técnica previa.

Para pruebas funcionales se debe utilizar únicamente personal creado para prueba.

---

## 7.8 Responsables

Dentro del módulo **Personal** existe la pestaña **Responsables**.

Los responsables se utilizan en los movimientos de NEXUS para identificar quién registra o responde por una operación.

Desde esta sección se puede:

```text
Crear
Editar
Activar
Inactivar
```

---

## 7.9 Regla de responsables activos e inactivos

Un responsable activo:

```text
Debe aparecer en los movimientos nuevos
```

Un responsable inactivo:

```text
No debe aparecer en los movimientos nuevos
```

pero debe conservarse en los registros históricos donde ya fue utilizado.

Esto permite mantener la trazabilidad sin permitir que una persona inactiva siga siendo seleccionada para nuevas operaciones.

---

## 7.10 Validación de responsables

Después de crear o modificar un responsable se debe comprobar:

### Responsable activo

```text
Responsable activo
↓
Aparece en selector de Kardex
```

### Responsable inactivo

```text
Responsable inactivo
↓
No aparece en movimientos nuevos
↓
Permanece visible en el histórico
```

---

## 7.11 Técnico utilizado para pruebas

Durante la revalidación se utilizará el siguiente técnico de prueba ya existente en DEV:

```text
Cédula:
12345678

Nombre:
PRUEBA TECNICO EDITADO

Zona:
METROPOLITANO
```

Se comprobó que el registro existe en:

```text
personal
tecnicos
```

por lo tanto no es necesario crear otro técnico de prueba.

Este técnico se utilizará posteriormente para validar:

```text
Salida de material
Asignación de seriales
Inventario Técnico
Reintegros
Auditoría de Seriales
```

---

## 7.12 Estado de validación

Estado actual:

```text
EXISTENCIA TÉCNICO DE PRUEBA        = OK
SINCRONÍA PERSONAL / TÉCNICOS       = OK

LISTA                               = PENDIENTE DE REVALIDACIÓN
CREAR                               = PENDIENTE DE REVALIDACIÓN
EDITAR                              = PENDIENTE DE REVALIDACIÓN
ELIMINAR                            = PENDIENTE DE REVALIDACIÓN
RESPONSABLES                        = PENDIENTE DE REVALIDACIÓN

MÓDULO PERSONAL                     = PENDIENTE
```

El módulo solamente debe marcarse como **APROBADO** después de revisar nuevamente las pantallas reales de Lista, Crear, Editar, Eliminar y Responsables.


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
