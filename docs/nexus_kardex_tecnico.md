# 🛠️ NEXUS / Kardex — Documentación Técnica para Desarrollo y Soporte

> **Propósito:** conservar arquitectura, reglas, SQL, hallazgos, decisiones y puntos de soporte para poder recuperar o modificar NEXUS sin reconstruir todo desde cero.

---

# 1. Arquitectura general

```text
sigem/
│
├── main.py
├── config/
│   └── db.py
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
    ├── sigem_dev.db
    └── sigem_lista.db
```

---

# 2. Entornos DEV / PROD

`config/db.py`:

```python
BASE_DIR = Path(__file__).resolve().parent.parent
ENV = os.getenv("APP_ENV", "prod")

if ENV == "dev":
    DB_PATH = BASE_DIR / "data" / "sigem_dev.db"
else:
    DB_PATH = BASE_DIR / "data" / "sigem.db"
```

## Ejecutar DEV

```bat
set APP_ENV=dev
streamlit run main.py
```

## Ejecutar PROD

```bat
set APP_ENV=prod
streamlit run main.py
```

La interfaz debe mostrar claramente el entorno actual.

---

# 3. SQLite

## Acceso

```bat
py -m sqlite3 data\sigem_dev.db
```

```bat
py -m sqlite3 data\sigem.db
```

## Tablas principales

```text
almacenes
auditoria_seriales
equivalencias_tecnicos_draco
materiales
movimientos
personal
responsables
seriales
tecnicos
tipos_movimiento
```

---

# 4. Tabla movimientos

Campos observados:

```text
id_movimiento
id_material
id_tipo
cantidad
stock_antes
stock_despues
id_responsable
id_tecnico
id_almacen
fecha
observacion
acta
remision
proveedor
```

---

# 5. Tipos de movimiento

Principales tipos recuperados:

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

`REINTEGRO SERIAL` tiene factor 0 y se utiliza para trazabilidad, no para afectar stock.

---

# 6. Stock Kardex

La consulta de stock utiliza el último `stock_despues` de METROPOLITANA SUR:

```sql
SELECT m.stock_despues
FROM movimientos m
JOIN almacenes a ON m.id_almacen = a.id_almacen
WHERE m.id_material = ?
AND UPPER(a.nombre) = 'METROPOLITANA SUR'
ORDER BY m.fecha DESC, m.id_movimiento DESC
LIMIT 1;
```

Recálculo cronológico:

```text
fecha ASC
id_movimiento ASC
```

### Hallazgo pendiente

`eliminar_movimiento_seguro` utiliza orden por `id_movimiento`. Revisar únicamente si existe una necesidad real de modificar esa función.

---

# 7. Materiales

Campos relevantes:

```text
id_material
codigo
nombre
descripcion
tipo_material
serializado
```

Existe una columna histórica llamada:

```text
COLUMNS
```

No modificar sin análisis específico.

---

# 8. Personal / técnicos

`personal` y `tecnicos` deben permanecer sincronizados por cédula.

SQL de control:

```sql
SELECT cedula,nombre,zona
FROM personal
WHERE cedula = ?;
```

```sql
SELECT cedula,nombre
FROM tecnicos
WHERE cedula = ?;
```

---

# 9. Responsables

Se agregó control activo/inactivo.

Funciones relevantes en `modules/catalogos.py`:

```text
obtener_responsables
obtener_todos_responsables
crear_responsable
actualizar_responsable
cambiar_estado_responsable
```

Un responsable inactivo debe permanecer disponible para histórico.

---

# 10. Seriales

Campos:

```text
id_serial
codigo_material
serial
estado
id_movimiento
fecha
```

Estados:

```text
DISPONIBLE
ASIGNADO
```

La edición manual de estado fue deshabilitada en:

```text
ui/seriales_ui.py
```

porque permitía producir:

```text
ASIGNADO + técnico vacío
```

---

# 11. Reintegros

Flujo esperado:

```text
1. localizar serial
2. identificar técnico anterior
3. cambiar a DISPONIBLE
4. registrar auditoría
5. registrar movimiento REINTEGRO SERIAL cuando aplique
6. recalcular Kardex
```

El reintegro por Excel usa solo:

```text
serial
```

---

# 12. Auditoría Seriales

Tabla:

```text
auditoria_seriales
```

Campos:

```text
serial
codigo_material
id_tecnico
estado_anterior
estado_nuevo
evento
fecha
responsable
observacion
id_movimiento
```

Eventos:

```text
SALIDA
REINTEGRO
AJUSTE
```

`AJUSTE` se mantiene por histórico aunque la función manual esté deshabilitada.

---

# 13. Ajustes Kardex

Lógica:

```python
diferencia = nueva_cantidad - stock_actual
```

```text
diferencia > 0 → AJUSTE ENTRADA
diferencia < 0 → AJUSTE SALIDA
diferencia = 0 → sin movimiento
```

El valor de UI representa:

```text
Stock físico correcto
```

no la cantidad de diferencia.

---

# 14. Conciliación Operativa

Archivo:

```text
ui/conciliacion_operativa.py
```

## NEXUS

Consulta por acta:

```sql
WHERE m.acta = ?
```

Calcula:

```text
SALIDAS
REINTEGROS
```

y consolida técnico/material.

---

## DRACO

Columnas utilizadas:

```text
Técnico
Código
Cantidad
```

Transformaciones:

1. limpieza de nombre
2. limpieza de código
3. normalización de códigos
4. exclusión de códigos no conciliables
5. cruce con equivalencias
6. diagnóstico de sin equivalencia
7. consolidación
8. suma de instalados

---

# 15. Equivalencias DRACO ↔ NEXUS

Tabla:

```text
equivalencias_tecnicos_draco
```

Campos recuperados:

```text
id_equivalencia
tecnico_draco
cedula
tecnico_nexus
zona
activo
fecha_creacion
```

Consulta:

```sql
SELECT
    tecnico_draco,
    cedula,
    tecnico_nexus
FROM equivalencias_tecnicos_draco
WHERE activo = 1;
```

---

# 16. Regla técnica de equivalencias

DRACO no trae cédula.

La tabla de equivalencias convierte:

```text
Nombre DRACO
→ Cédula
→ Nombre NEXUS
```

Después se cruza:

```text
Cédula + Código
```

### Hallazgo importante

DRACO y NEXUS pueden manejar el mismo técnico con distinto orden del nombre.

Por eso:

```text
tecnico_draco
```

debe reflejar exactamente el nombre que llega desde DRACO.

La cédula es el identificador confiable.

---

# 17. Diagnóstico de Sin equivalencia

Si aparece:

```text
Sin equivalencia > 0
```

procedimiento:

```text
1. listar técnicos DRACO sin equivalencia
2. buscar en tecnicos
3. buscar en personal
4. obtener cédula
5. consultar equivalencia por cédula
6. UPDATE si ya existe
7. INSERT solo si no existe
8. repetir conciliación
```

Nunca crear equivalencias por parecido visual sin validar la identidad.

---

# 18. SQL de diagnóstico de equivalencias

## Por nombre DRACO

```sql
SELECT
    tecnico_draco,
    cedula,
    tecnico_nexus,
    activo
FROM equivalencias_tecnicos_draco
WHERE UPPER(tecnico_draco) LIKE '%TEXTO%';
```

## Por cédula

```sql
SELECT
    tecnico_draco,
    cedula,
    tecnico_nexus,
    activo
FROM equivalencias_tecnicos_draco
WHERE cedula = ?;
```

## Buscar técnico

```sql
SELECT
    cedula,
    nombre
FROM tecnicos
WHERE UPPER(nombre) LIKE '%TEXTO%';
```

## Buscar personal

```sql
SELECT
    cedula,
    nombre,
    zona
FROM personal
WHERE UPPER(nombre) LIKE '%TEXTO%';
```

---

# 19. Cruce final

```python
df_final = pd.merge(
    df_nexus,
    df_draco,
    on=["cedula", "codigo"],
    how="outer"
)
```

El `outer` conserva:

- coincidencias
- solo NEXUS
- solo DRACO

---

# 20. Fórmula de conciliación

```python
diferencia = salidas - reintegros - instalados
```

Estados:

```text
diferencia == 0
→ OK

salidas == 0 and reintegros == 0 and instalados > 0
→ INSTALACIÓN SIN ENTREGA

salidas == 0 and reintegros > 0
→ REINTEGRO SIN ENTREGA A TÉCNICO

diferencia > 0
→ PENDIENTE DEVOLUCIÓN

otro
→ REVISAR OPERACIÓN
```

---

# 21. Trazabilidad mejorada

La pantalla muestra:

```text
DRACO original
DRACO tras exclusiones
Sin equivalencia
DRACO consolidado
NEXUS consolidado
Conciliación final
```

Indicadores:

```text
Técnicos NEXUS
Técnicos DRACO
Técnicos Cruzados
NEXUS sin DRACO
Cobertura %
```

Técnicos cruzados:

```python
cedulas_cruzadas = cedulas_nexus & cedulas_draco
```

---

# 22. Hallazgo Acta 8

Se detectó un técnico existente en NEXUS cuyo nombre DRACO estaba registrado con orden distinto.

La equivalencia fue corregida.

Efecto observado:

```text
Sin equivalencia: 188 → 0
DRACO consolidado: 457 → 498
Conciliación final: 792 → 809
Técnicos DRACO: 9 → 10
Técnicos Cruzados: 9 → 10
Cobertura: 25,71 % → 28,57 %
```

Este caso debe conservarse como ejemplo técnico de diagnóstico.

---

# 23. Hallazgo Acta 7

Se detectaron:

```text
85 registros sin equivalencia
6 técnicos únicos
```

Los técnicos sí existen en NEXUS, pero con nombre invertido respecto a DRACO.

Antes de realizar cambios:

```text
consultar por cédula
```

para evitar duplicar equivalencias.

---

# 24. Dashboard

Estado técnico:

```text
PENDIENTE DE REVALIDACIÓN
```

Hallazgo a revisar:

```text
posible SUM(stock_despues)
```

No modificar hasta confirmar que exista un error real.

---

# 25. Git

Ramas:

```text
main
dev
feature/mysql-network
```

Regla:

```text
main = estable
dev = pruebas y recuperación
```

No hacer merge de cada cambio pequeño.

Al cierre:

```bat
git checkout main
git pull origin main
git merge dev
git push origin main
git checkout dev
```

---

# 26. Despliegue

Antes de PROD:

1. Backup `sigem.db`
2. Confirmar DEV
3. Listar archivos `.py` modificados
4. Listar migraciones SQL
5. Ejecutar pruebas
6. Ejecutar SQL de control
7. Commit final DEV
8. Merge a main
9. Copiar archivos necesarios
10. Aplicar migraciones
11. Ejecutar pruebas post-despliegue
12. Mantener rollback

Archivos modificados conocidos:

```text
modules/catalogos.py
modules/inventario.py
ui/app.py
ui/seriales_ui.py
ui/conciliacion_operativa.py
```

Verificar siempre con Git antes de entregar.
