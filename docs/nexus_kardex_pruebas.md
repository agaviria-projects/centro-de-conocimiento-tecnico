# ✅ NEXUS / Kardex — Plan Maestro de Revalidación antes de Entrega

> **Objetivo:** volver a ejecutar cada escenario desde cero en DEV y comprobar que la pantalla, el resultado, la base de datos y el manual coincidan.

---

# 1. Preparación

- [ ] Confirmar `APP_ENV=dev`
- [ ] Confirmar indicador DEV en pantalla
- [ ] Backup `sigem_dev.db`
- [ ] Ejecutar `git status`
- [ ] Registrar commit actual
- [ ] No tocar PROD

---

# 2. Kardex Inventario

## Entrada no serializada

- [ ] Seleccionar almacén
- [ ] Ingresar código
- [ ] Seleccionar entrada
- [ ] Ingresar cantidad
- [ ] Seleccionar responsable
- [ ] Ingresar observación
- [ ] Registrar
- [ ] Confirmar aumento de stock
- [ ] Confirmar movimiento en SQLite

## Entrada serializada manual

- [ ] Material serializado
- [ ] Cantidad
- [ ] Seriales manuales
- [ ] Total seriales = cantidad
- [ ] Registrar
- [ ] Confirmar seriales DISPONIBLES

## Entrada serializada Excel

- [ ] Archivo correcto
- [ ] Encabezado correcto
- [ ] Total detectado
- [ ] Registrar
- [ ] Confirmar seriales

## Salida no serializada

- [ ] Seleccionar salida
- [ ] Cantidad
- [ ] Responsable
- [ ] Técnico cuando aplique
- [ ] ACTA cuando aplique
- [ ] Confirmar reducción de stock

## Salida serializada

- [ ] Seleccionar serial
- [ ] Ingresar técnico válido
- [ ] Registrar
- [ ] Confirmar `DISPONIBLE → ASIGNADO`
- [ ] Confirmar inventario técnico

## Validación negativa

- [ ] Intentar salida serializada sin técnico
- [ ] Confirmar bloqueo
- [ ] Confirmar mensaje de cédula válida

---

# 3. Materiales

- [ ] Crear serializado
- [ ] Crear no serializado
- [ ] Consultar
- [ ] Editar
- [ ] Confirmar serializado = comportamiento correcto
- [ ] No tocar columna `COLUMNS`

---

# 4. Personal

- [ ] Crear
- [ ] Consultar
- [ ] Editar
- [ ] Confirmar sincronía `personal` / `tecnicos`
- [ ] Validar zona
- [ ] Revisar eliminación solo en prueba controlada

---

# 5. Responsables

- [ ] Crear responsable
- [ ] Confirmar selector
- [ ] Editar
- [ ] Inactivar
- [ ] Confirmar que no aparece en movimientos nuevos
- [ ] Confirmar histórico
- [ ] Reactivar si aplica

---

# 6. Inventario Técnico

- [ ] Asignar serial
- [ ] Buscar técnico
- [ ] Confirmar serial asignado
- [ ] Reintegrar
- [ ] Confirmar que desaparece del inventario actual
- [ ] Confirmar histórico

---

# 7. Inventario General

- [ ] Buscar material
- [ ] Validar entradas
- [ ] Validar salidas
- [ ] Validar reintegros
- [ ] Validar ajustes
- [ ] Exportar Excel
- [ ] Comparar Excel vs pantalla
- [ ] Comparar contra SQLite

---

# 8. Ajustes Kardex

## Sin diferencia

- [ ] Sistema = físico
- [ ] No genera ajuste

## Ajuste entrada

- [ ] Físico > sistema
- [ ] Genera `AJUSTE ENTRADA`
- [ ] Cantidad = diferencia
- [ ] Stock final correcto

## Ajuste salida

- [ ] Físico < sistema
- [ ] Genera `AJUSTE SALIDA`
- [ ] Cantidad = diferencia absoluta
- [ ] Stock final correcto

---

# 9. Seriales

## Lista

- [ ] Buscar código
- [ ] Total registros
- [ ] Estados
- [ ] Técnico
- [ ] Exportar

## Editar número

- [ ] Corregir serial
- [ ] Confirmar mismo `id_serial`
- [ ] Confirmar estado preservado
- [ ] Confirmar serial anterior eliminado

## Editar estado

- [x] Debe permanecer deshabilitado

## Eliminar

- [ ] Probar únicamente con serial de prueba
- [ ] Validar impacto
- [ ] Decidir si se mantiene para usuario final

---

# 10. Reintegros

## Selección manual

- [ ] Asignar varios seriales
- [ ] Seleccionar uno o varios
- [ ] Reintegrar
- [ ] Confirmar DISPONIBLE
- [ ] Confirmar salida del inventario técnico
- [ ] Confirmar auditoría

## Excel

- [ ] Crear Excel con columna `serial`
- [ ] Incluir varios seriales asignados
- [ ] Ejecutar
- [ ] Confirmar que no pide cédula
- [ ] Confirmar técnico anterior
- [ ] Confirmar auditoría
- [ ] Confirmar seriales disponibles
- [ ] Confirmar no reproceso de disponibles
- [ ] Confirmar validación si mezcla materiales

---

# 11. Auditoría Seriales

- [x] Filtro Serial
- [x] Filtro Evento
- [x] Filtro Responsable
- [x] SALIDA
- [x] REINTEGRO
- [x] AJUSTE histórico
- [ ] Exportar nuevamente
- [ ] Confirmar que el histórico no se elimina

Estado: **APROBADO funcionalmente**, pendiente revalidación final de entrega.

---

# 12. Dashboard

- [ ] Revisar KPIs
- [ ] Comparar contra SQL
- [ ] Revisar posible `SUM(stock_despues)`
- [ ] Confirmar ausencia de doble conteo
- [ ] Documentar fórmula de cada KPI
- [ ] Aprobar solo después de validación

Estado: **PENDIENTE**.

---

# 13. Conciliación Operativa

## Preparación DRACO

- [ ] Unificar archivos
- [ ] Filtrar exclusivamente el acta
- [ ] Confirmar número de acta
- [ ] Confirmar total DRACO original
- [ ] Guardar archivo preparado

## Carga en NEXUS

- [ ] Seleccionar misma acta
- [ ] Exportar NEXUS consolidado
- [ ] Cargar DRACO preparado

## Trazabilidad

- [ ] DRACO original
- [ ] DRACO tras exclusiones
- [ ] Sin equivalencia
- [ ] DRACO consolidado
- [ ] NEXUS consolidado
- [ ] Conciliación final

## Equivalencias

Si `Sin equivalencia > 0`:

- [ ] Copiar técnico DRACO
- [ ] Buscar en `tecnicos`
- [ ] Buscar en `personal`
- [ ] Identificar cédula
- [ ] Consultar equivalencia por cédula
- [ ] UPDATE si existe
- [ ] INSERT solo si no existe
- [ ] Repetir conciliación
- [ ] Confirmar nueva trazabilidad

## Cobertura

- [ ] Técnicos NEXUS
- [ ] Técnicos DRACO
- [ ] Técnicos Cruzados
- [ ] NEXUS sin DRACO
- [ ] Cobertura %

## Estados

- [ ] OK
- [ ] PENDIENTE DEVOLUCIÓN
- [ ] INSTALACIÓN SIN ENTREGA
- [ ] REINTEGRO SIN ENTREGA A TÉCNICO
- [ ] REVISAR OPERACIÓN

## Validación manual

Elegir mínimo:

1. un caso OK
2. un pendiente devolución
3. un caso negativo

y revisar:

```text
Cédula
Código
Salidas
Reintegros
Instalados
Diferencia
Estado
```

contra fuente NEXUS y DRACO.

---

# 14. SQL de control

## Tablas

```sql
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
```

## Últimos movimientos

```sql
SELECT *
FROM movimientos
ORDER BY fecha DESC, id_movimiento DESC
LIMIT 20;
```

## Serial

```sql
SELECT
    id_serial,
    codigo_material,
    serial,
    estado,
    id_movimiento
FROM seriales
WHERE serial = ?;
```

## Auditoría serial

```sql
SELECT
    serial,
    estado_anterior,
    estado_nuevo,
    evento,
    fecha,
    responsable,
    observacion,
    id_movimiento
FROM auditoria_seriales
WHERE serial = ?
ORDER BY fecha DESC;
```

## Equivalencia

```sql
SELECT
    tecnico_draco,
    cedula,
    tecnico_nexus,
    activo
FROM equivalencias_tecnicos_draco
WHERE cedula = ?;
```

---

# 15. Cierre de cada módulo

Cada módulo debe terminar con:

```text
PRUEBA FUNCIONAL: OK / FALLA
SQL: OK / NO APLICA
EXPORTACIÓN: OK / NO APLICA
HALLAZGOS: ...
CORRECCIÓN: ...
ARCHIVO MODIFICADO: ...
ESTADO: APROBADO / PENDIENTE
```

---

# 16. Cierre final antes de entrega

- [ ] Todos los módulos probados
- [ ] Manual actualizado
- [ ] Técnico actualizado
- [ ] Pruebas actualizado
- [ ] Sin errores críticos
- [ ] Backup DEV
- [ ] Backup PROD
- [ ] Git limpio
- [ ] Commit final dev
- [ ] Lista de `.py` modificados
- [ ] Lista de migraciones SQL
- [ ] Plan de rollback
- [ ] Merge a main aprobado
- [ ] Prueba post-despliegue
