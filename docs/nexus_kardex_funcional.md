# 📦 NEXUS / Kardex — Manual Funcional y Operativo

## 1. Objetivo
NEXUS es una herramienta de control de inventario y trazabilidad operativa. Permite registrar entradas, salidas, reintegros, ajustes, materiales serializados, inventario por técnico, auditoría de seriales y conciliación operativa contra DRACO.

Regla de trabajo:
- FUNCIONA → preservar
- FALLA → corregir
- RIESGO REAL → atender
- MEJORA ÚTIL → evaluar
- COMPLEJO Y POCO USADO → no implementar

## 2. Kardex Inventario
- El almacén central controlado es METROPOLITANA SUR.
- Las entradas aumentan existencias.
- Las salidas descuentan existencias.
- Los reintegros devuelven material.
- Los movimientos deben conservar responsable, técnico, almacén, acta, observación y fecha cuando aplique.

### Regla crítica para serializados
Una SALIDA de material serializado exige técnico válido.

```text
ENTRADA → Serial DISPONIBLE
SALIDA → Técnico obligatorio → Serial ASIGNADO
REINTEGRO → Serial DISPONIBLE
```

## 3. Materiales
- Material serializado: solicita seriales y los registra.
- Material no serializado: no debe solicitarlos.
- Se validaron materiales de prueba serializados y no serializados.

## 4. Personal
- La edición de personal/técnico debe conservar sincronía por cédula.
- La eliminación física debe usarse con cautela por el histórico.

## 5. Inventario Técnico
- Un serial aparece en inventario técnico cuando está ASIGNADO.
- Después de un reintegro debe dejar de aparecer como inventario actual.
- El histórico debe conservarse.

## 6. Inventario General
Debe permitir consultar y exportar: fecha, técnico, código, material, tipo, acta, orden/remisión, proveedor, cantidad, stock antes, stock final, responsable, bodega y observación.

## 7. Ajustes Kardex
El usuario ingresa el **stock físico correcto**. NEXUS decide automáticamente:

```text
Físico > Sistema → AJUSTE ENTRADA
Físico < Sistema → AJUSTE SALIDA
Físico = Sistema → no genera ajuste
```

## 8. Seriales

### Lista
Muestra serial, estado, fecha de ingreso, fecha de asignación y técnico. Permite exportar a Excel.

### Editar número
Solo para corregir un serial digitado incorrectamente. Debe conservar material, estado e histórico.

### Editar estado — DESHABILITADO
Se retiró porque podía generar:
```text
Estado = ASIGNADO
Técnico = NO REGISTRADO
```

Flujo oficial:
```text
DISPONIBLE → ASIGNADO: solo SALIDA
ASIGNADO → DISPONIBLE: solo REINTEGRO
```

## 9. Reintegros de seriales

### Manual
1. Ingresar código de material.
2. Seleccionar seriales ASIGNADOS.
3. Seleccionar responsable.
4. Reintegrar.

Resultado:
```text
ASIGNADO → REINTEGRO → DISPONIBLE
```

### Por Excel
El archivo requiere únicamente:
```text
serial
SERIAL001
SERIAL002
```

No requiere cédula. NEXUS identifica automáticamente el técnico anterior del serial.

## 10. Auditoría Seriales — APROBADO
Eventos:
- SALIDA: DISPONIBLE → ASIGNADO
- REINTEGRO: ASIGNADO → DISPONIBLE
- AJUSTE: corrección manual histórica; se conserva aunque la edición manual de estado esté deshabilitada.

Los registros de auditoría no deben borrarse solo porque luego hubo una corrección.

## 11. Conciliación Operativa NEXUS vs DRACO
La conciliación se realiza por ACTA.

Correspondencia operativa:
```text
Acta 5 → Enero
Acta 6 → Febrero
Acta 7 → Marzo
Acta 8 → Abril
Acta 9 → Mayo
Acta 10 → Junio
Acta 11 → Julio
Acta 12 → Agosto
```

El criterio técnico final es el número de acta.

### Cómo se cruza
DRACO aporta:
```text
Técnico
Código
Cantidad
```

NEXUS usa la tabla interna `equivalencias_tecnicos_draco` para convertir:
```text
Nombre DRACO → Cédula → Nombre NEXUS
```

Cruce final:
```text
CÉDULA + CÓDIGO MATERIAL
```

### Sin equivalencia
Significa que el nombre recibido desde DRACO no pudo asociarse a una equivalencia activa en NEXUS. No significa necesariamente que el técnico no exista.

Ejemplo validado:
```text
DRACO: NELSON DARIO LONDOÑO HERRERA
NEXUS: LONDOÑO HERRERA NELSON DARIO
```

### Estados
Fórmula:
```text
DIFERENCIA = SALIDAS - REINTEGROS - INSTALADOS
```

- OK: diferencia = 0
- PENDIENTE DEVOLUCIÓN: saldo entregado no instalado ni reintegrado
- INSTALACIÓN SIN ENTREGA: DRACO reporta instalación sin salida NEXUS
- REINTEGRO SIN ENTREGA A TÉCNICO: existe reintegro sin salida previa
- REVISAR OPERACIÓN: descuadre que requiere revisión manual

### Trazabilidad de registros
La conciliación no compara fila a fila.

Ejemplo Acta 9:
```text
DRACO original: 14053
DRACO tras exclusiones: 14053
Sin equivalencia: 0
DRACO consolidado: 647
NEXUS consolidado: 729
Conciliación final: 812
```

Los registros DRACO se consolidan por:
```text
Cédula + Técnico NEXUS + Código
```

y el cruce final por:
```text
Cédula + Código
```

### Cobertura
Ejemplo Acta 9:
```text
Técnicos NEXUS: 42
Técnicos DRACO: 12
Técnicos Cruzados: 12
NEXUS sin DRACO: 30
Cobertura: 28,57 %
```

La cobertura indica proporción de técnicos NEXUS con presencia en el DRACO cargado. No prueba por sí sola que la conciliación esté mal.

## 12. Antes de entrega
1. Backup de base de datos.
2. Ejecutar DEV.
3. Revalidar cada módulo.
4. Confirmar con SQL cuando aplique.
5. Documentar hallazgos.
6. Corregir solo errores reales o riesgos importantes.
7. Commit en dev.
8. Solo al cierre, evaluar merge a main.
