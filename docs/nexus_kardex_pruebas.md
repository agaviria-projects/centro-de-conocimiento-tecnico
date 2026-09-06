# ✅ NEXUS / Kardex — Plan de Revalidación antes de Entrega

## Preparación
- [ ] Confirmar APP_ENV=dev
- [ ] Verificar indicador DEV en pantalla
- [ ] Backup de sigem_dev.db
- [ ] git status
- [ ] Registrar commit actual de dev
- [ ] No tocar PROD

## Kardex Inventario
- [ ] Entrada no serializada
- [ ] Entrada serializada manual
- [ ] Entrada serializada por archivo
- [ ] Salida no serializada
- [ ] Salida serializada
- [ ] Confirmar técnico obligatorio
- [ ] Intentar salida serializada sin técnico y comprobar bloqueo
- [ ] Validar stock antes/después

## Materiales
- [ ] Crear serializado
- [ ] Crear no serializado
- [ ] Editar
- [ ] Confirmar comportamiento según serializado

## Personal
- [ ] Crear persona/técnico
- [ ] Editar nombre
- [ ] Validar sincronía personal ↔ tecnicos
- [ ] Revisar eliminación solo si es necesario

## Responsables
- [ ] Crear
- [ ] Inactivar
- [ ] Confirmar que desaparece de selectores activos
- [ ] Confirmar histórico

## Inventario Técnico
- [ ] Asignar serial
- [ ] Confirmar que aparece
- [ ] Reintegrar
- [ ] Confirmar que desaparece
- [ ] Confirmar histórico

## Inventario General
- [ ] Consultar material
- [ ] Validar entradas/salidas/reintegros/ajustes
- [ ] Exportar
- [ ] Comparar con SQLite

## Ajustes Kardex
- [ ] sistema = físico
- [ ] físico > sistema
- [ ] físico < sistema
- [ ] Confirmar ajuste automático
- [ ] Confirmar stock final

## Seriales
- [ ] Lista y exportación
- [ ] Editar número
- [x] Editar estado debe permanecer deshabilitado
- [ ] Revisar eliminación de serial en prueba controlada

## Reintegros
- [ ] Manual
- [ ] Excel con columna serial
- [ ] Confirmar que no pide cédula
- [ ] Confirmar técnico anterior
- [ ] Confirmar auditoría
- [ ] Confirmar que disponibles no se reprocesan

## Auditoría Seriales
- [x] Filtro serial
- [x] Filtro evento
- [x] Filtro responsable
- [x] SALIDA
- [x] REINTEGRO
- [x] AJUSTE histórico
- [ ] Exportar nuevamente

Estado: APROBADO funcionalmente, sujeto a revalidación final.

## Dashboard
- [ ] Revisar KPIs
- [ ] Validar consultas
- [ ] Revisar posible SUM(stock_despues)
- [ ] Aprobar o corregir solo si existe error real

Estado: PENDIENTE DE REVALIDACIÓN.

## Conciliación Operativa
- [ ] Unificar DRACO
- [ ] Filtrar exclusivamente el acta
- [ ] Confirmar DRACO original
- [ ] Revisar Sin equivalencia
- [ ] Buscar técnico en tecnicos
- [ ] Buscar técnico en personal
- [ ] Buscar equivalencia por cédula
- [ ] Actualizar/crear solo tras validar identidad
- [ ] Confirmar DRACO consolidado
- [ ] Confirmar NEXUS consolidado
- [ ] Confirmar Conciliación final
- [ ] Confirmar Técnicos Cruzados
- [ ] Confirmar Cobertura
- [ ] Revisar estados OK / PENDIENTE DEVOLUCIÓN / INSTALACIÓN SIN ENTREGA / REINTEGRO SIN ENTREGA / REVISAR OPERACIÓN
- [ ] Validar manualmente al menos 3 casos contra las fuentes

## Cierre
- [ ] Todos los módulos revisados
- [ ] Hallazgos cerrados o documentados
- [ ] Sin errores críticos
- [ ] SQL de control ejecutado
- [ ] Exportaciones verificadas
- [ ] DEV respaldado
- [ ] Git limpio
- [ ] Commit final dev
- [ ] Lista de archivos a desplegar
- [ ] Lista de migraciones SQL
- [ ] Plan de rollback
- [ ] Aprobación para merge a main
