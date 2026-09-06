# 🛠️ NEXUS / Kardex — Documentación Técnica

## 1. Arquitectura
```text
sigem/
├── main.py
├── config/db.py
├── modules/
│   ├── auditoria.py
│   ├── catalogos.py
│   ├── dashboard.py
│   ├── database.py
│   ├── inventario.py
│   ├── migraciones.py
│   └── reportes.py
├── ui/
│   ├── app.py
│   ├── auditoria_ui.py
│   ├── components.py
│   ├── conciliacion_operativa.py
│   ├── dashboard_ui.py
│   ├── materiales_ui.py
│   └── seriales_ui.py
└── data/
    ├── sigem.db
    └── sigem_dev.db
```

## 2. Entornos
```python
ENV = os.getenv("APP_ENV", "prod")
if ENV == "dev":
    DB_PATH = BASE_DIR / "data" / "sigem_dev.db"
else:
    DB_PATH = BASE_DIR / "data" / "sigem.db"
```

DEV:
```bat
set APP_ENV=dev
streamlit run main.py
```

PROD:
```bat
set APP_ENV=prod
streamlit run main.py
```

## 3. SQLite
```bat
py -m sqlite3 data\sigem_dev.db
py -m sqlite3 data\sigem.db
```

Tablas principales:
`almacenes`, `auditoria_seriales`, `equivalencias_tecnicos_draco`, `materiales`, `movimientos`, `personal`, `responsables`, `seriales`, `tecnicos`, `tipos_movimiento`.

## 4. Kardex
Último stock de METROPOLITANA SUR:
```sql
ORDER BY m.fecha DESC, m.id_movimiento DESC
```

Recálculo:
```text
fecha ASC + id_movimiento ASC
```

Hallazgo pendiente: `eliminar_movimiento_seguro` debe revisarse si alguna vez se modifica, porque el orden por id puede no respetar completamente la cronología.

## 5. Responsables
Funciones conocidas:
- obtener_responsables
- obtener_todos_responsables
- crear_responsable
- actualizar_responsable
- cambiar_estado_responsable

Los inactivos deben conservarse para histórico.

## 6. Seriales
Estados operativos:
```text
DISPONIBLE
ASIGNADO
```

La edición manual de estado fue deshabilitada en `ui/seriales_ui.py`.

## 7. Ajustes Kardex
```python
diferencia = nueva_cantidad - stock_actual
```

```text
> 0 → AJUSTE ENTRADA
< 0 → AJUSTE SALIDA
= 0 → sin movimiento
```

## 8. Conciliación Operativa
Archivo:
```text
ui/conciliacion_operativa.py
```

NEXUS filtra:
```sql
WHERE m.acta = ?
```

DRACO utiliza:
```text
Técnico
Código
Cantidad
```

Luego:
1. normaliza nombres
2. normaliza códigos
3. excluye códigos no conciliables
4. cruza equivalencias activas
5. identifica sin equivalencia
6. agrupa por cédula + técnico_nexus + código
7. suma instalados

Equivalencias:
```sql
SELECT tecnico_draco, cedula, tecnico_nexus
FROM equivalencias_tecnicos_draco
WHERE activo = 1;
```

Cruce final:
```python
pd.merge(
    df_nexus,
    df_draco,
    on=["cedula", "codigo"],
    how="outer"
)
```

Fórmula:
```python
diferencia = salidas - reintegros - instalados
```

Estados:
```text
diferencia == 0 → OK
salidas == 0 and reintegros == 0 and instalados > 0 → INSTALACIÓN SIN ENTREGA
salidas == 0 and reintegros > 0 → REINTEGRO SIN ENTREGA A TÉCNICO
diferencia > 0 → PENDIENTE DEVOLUCIÓN
otros → REVISAR OPERACIÓN
```

## 9. Trazabilidad mejorada
Mostrar:
- DRACO original
- DRACO tras exclusiones
- Sin equivalencia
- DRACO consolidado
- NEXUS consolidado
- Conciliación final
- Técnicos NEXUS
- Técnicos DRACO
- Técnicos Cruzados
- NEXUS sin DRACO
- Cobertura %

Técnicos cruzados:
```python
cedulas_cruzadas = cedulas_nexus & cedulas_draco
```

## 10. Hallazgo Acta 8
Equivalencia corregida:
```text
DRACO: NELSON DARIO LONDOÑO HERRERA
Cédula: 3552306
NEXUS: LONDOÑO HERRERA NELSON DARIO
```

Resultado:
```text
Sin equivalencia: 188 → 0
DRACO consolidado: 457 → 498
Conciliación final: 792 → 809
Técnicos DRACO: 9 → 10
Técnicos Cruzados: 9 → 10
Cobertura: 25,71 % → 28,57 %
```

## 11. Acta 7 — pendiente
Se detectaron 85 registros sin equivalencia correspondientes a 6 técnicos. Los 6 sí existen en NEXUS con nombres invertidos respecto a DRACO. Antes de insertar/actualizar se debe consultar por cédula en `equivalencias_tecnicos_draco`.

## 12. SQL útiles
```sql
SELECT tecnico_draco, cedula, tecnico_nexus, activo
FROM equivalencias_tecnicos_draco
WHERE cedula = ?;
```

```sql
SELECT cedula, nombre
FROM tecnicos
WHERE UPPER(nombre) LIKE '%TEXTO%';
```

```sql
SELECT cedula, nombre, zona
FROM personal
WHERE UPPER(nombre) LIKE '%TEXTO%';
```

## 13. Despliegue
Antes de DEV → PROD:
1. backup sigem.db
2. validar sigem_dev.db
3. listar archivos .py modificados
4. listar migraciones SQL
5. ejecutar pruebas funcionales
6. ejecutar SQL de control
7. commit dev
8. merge a main solo al cierre
9. conservar rollback

Archivos modificados durante la recuperación incluyen al menos:
```text
modules/catalogos.py
modules/inventario.py
ui/app.py
ui/seriales_ui.py
ui/conciliacion_operativa.py
```
