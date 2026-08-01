# Generador de Informes ANS - ATC CHEC

## Centro de Conocimiento Técnico

----

## 1. Entrada a la reunión

El **Generador de Informes ANS - ATC CHEC** es una herramienta orientada al seguimiento operativo de los acuerdos de nivel de servicio asociados a las conexiones gestionadas por ATC CHEC.

Su función principal es transformar el archivo exportado desde el sistema **GIT** en un informe organizado, validado y preparado para el análisis operativo.

## Durante la presentación de la herramienta se recomienda iniciar con la siguiente explicación:

> El sistema toma la información exportada desde GIT, aplica automáticamente las reglas contractuales y operativas definidas por la organización, calcula el estado de cada solicitud y genera un informe consolidado para facilitar la priorización y el seguimiento de los casos.

La herramienta fue diseñada para que la mayor parte de las reglas del negocio puedan administrarse desde archivos de configuración en Excel, evitando depender de modificaciones al software para ajustes funcionales frecuentes.

----

## 2. Objetivo

El objetivo del sistema es facilitar la generación, actualización y análisis del informe de cumplimiento ANS de las solicitudes de conexión.

La herramienta permite:

- Procesar el archivo exportado desde el sistema GIT.
- Calcular automáticamente las fechas límite de atención.
- Determinar los días transcurridos y los días restantes.
- Clasificar cada solicitud según su estado ANS.
- Aplicar reglas especiales de prioridad.
- Generar un archivo consolidado para el seguimiento operativo.
- Actualizar el dashboard de análisis.
- Disminuir el trabajo manual y el riesgo de errores.

----


## 7. Explicación de cada carpeta

## 7.1 Carpeta entrada

La carpeta **entrada** es el punto de inicio del proceso.

En esta ubicación se debe guardar el archivo exportado desde el sistema GIT.

### Recomendaciones

- Utilizar únicamente el archivo correspondiente al corte que se desea analizar.
- Verificar que el archivo no se encuentre abierto antes de iniciar el proceso.
- Confirmar que el archivo contenga la información completa.
- No cambiar los nombres de las columnas requeridas.
- Evitar guardar archivos adicionales que puedan generar confusión.

### Responsabilidad del usuario

El usuario debe asegurarse de que el archivo depositado corresponda a la información oficial exportada desde GIT.

----

## 7.2 Carpeta salida

La carpeta **salida** almacena los archivos generados por la herramienta.

El resultado principal es:

```text
Informe_ANS_ELITE.xlsx
```

Este archivo contiene los registros procesados y los cálculos necesarios para el análisis.

### Información esperada

El informe puede incluir, entre otros:

- Identificación de la solicitud.
- Dirección.
- Municipio.
- Actividad.
- Producto.
- Fecha de inicio del ANS.
- Días contractuales.
- Fecha límite del ANS.
- Días transcurridos.
- Días restantes.
- Estado del ANS.
- Prioridad.
- Observaciones funcionales.

### Recomendaciones

- No editar el archivo mientras se esté generando.
- Evitar reemplazarlo manualmente.
- Conservar copias de los informes históricos cuando el proceso lo requiera.
- Validar la fecha de generación antes de utilizarlo en reuniones o reportes.

----

## 7.3 Carpeta dashboard

La carpeta **dashboard** contiene el archivo de análisis visual:

```text
INFORME_ANS.xlsb
```

Este archivo permite consultar la información mediante:

- Indicadores.
- Tablas dinámicas.
- Segmentadores.
- Filtros.
- Gráficos.
- Resúmenes por estado.
- Análisis por municipio, producto, actividad u otros criterios disponibles.

### Función principal

El dashboard transforma el informe consolidado en una vista ejecutiva y operativa.

### Recomendaciones

- Actualizar el dashboard después de generar el informe.
- Esperar a que finalice la actualización antes de analizar los resultados.
- No cambiar nombres de hojas, tablas o conexiones.
- No eliminar campos utilizados por las visualizaciones.
- Guardar el archivo después de actualizarlo.

----

## 7.4 Carpeta config

La carpeta **config** contiene los archivos de parametrización funcional.

El archivo principal es:

```text
DIAS_CONTRACTUALES.xlsx
```

Este archivo administra las reglas que utiliza el sistema para realizar los cálculos.

### Importancia

La configuración permite realizar ajustes funcionales sin modificar el software.

Desde este archivo se pueden administrar:

- Municipios.
- Días contractuales.
- Parámetros generales.
- Festivos adicionales.
- Reglas especiales de prioridad.

### Recomendación crítica

Antes de modificar el archivo, se debe crear una copia de respaldo.

----

## 7.5 Carpeta logs

La carpeta **logs** conserva el registro de las ejecuciones realizadas por la herramienta.

Los logs permiten identificar:

- Fecha y hora de ejecución.
- Inicio y finalización del proceso.
- Cantidad de registros procesados.
- Validaciones realizadas.
- Advertencias.
- Errores encontrados.
- Resultado general de la generación.

### Uso funcional

Cuando el proceso no finalice correctamente, el archivo de log debe revisarse o compartirse con el responsable del soporte.

### Recomendaciones

- No eliminar los logs recientes antes de resolver una novedad.
- Compartir el archivo completo cuando se solicite soporte.
- No modificar manualmente su contenido.

----

## 7.6 Carpeta mapas

La carpeta **mapas** almacena los recursos utilizados para la representación geográfica de la información.

Dependiendo del alcance habilitado, puede contener:

- Archivos de ubicación.
- Recursos cartográficos.
- Resultados de mapas generados.
- Archivos auxiliares para identificar zonas o municipios.

### Objetivo

Facilitar la visualización territorial de las solicitudes y apoyar el análisis operativo.

### Recomendaciones

- No eliminar archivos de referencia.
- No cambiar los nombres de los recursos cartográficos.
- Validar que las direcciones del archivo fuente estén completas.
- Revisar manualmente los registros que no puedan ser ubicados.

----

## 8. Archivo DIAS_CONTRACTUALES.xlsx

El archivo **DIAS_CONTRACTUALES.xlsx** es el centro de parametrización funcional del sistema.

Su objetivo es conservar las reglas del negocio en un formato administrable por los usuarios autorizados.

### Hojas principales

- REGLAS_DE_NEGOCIO
- PARAMETROS
- FESTIVOS_ADICIONALES
- REGLAS_PRIORIDAD

----

## 8.1 Hoja REGLAS_DE_NEGOCIO

Esta hoja contiene las reglas utilizadas para asignar los días contractuales a cada solicitud.

Las reglas pueden estar relacionadas con:

- Municipio.
- Producto.
- Actividad.
- Tipo de conexión.
- Zona.
- Clasificación operativa.
- Combinaciones entre varios criterios.

### Objetivo

Determinar cuántos días hábiles tiene una solicitud para ser atendida.

### Ejemplo funcional

| Municipio | Producto | Actividad | Días contractuales |
|---|---|---|---:|
| Municipio A | Producto 1 | Actividad X | 5 |
| Municipio B | Producto 1 | Actividad X | 7 |
| Municipio C | Producto 2 | Actividad Y | 10 |

Los valores anteriores son ilustrativos. Los días reales deben corresponder a las condiciones contractuales vigentes.

### Modificaciones permitidas

El usuario autorizado puede:

- Agregar nuevos municipios.
- Actualizar días contractuales.
- Crear nuevas combinaciones de criterios.
- Ajustar reglas existentes.
- Inactivar reglas que ya no se utilicen, según el método definido para ello.

### Buenas prácticas

- No duplicar reglas con los mismos criterios.
- Mantener uniformidad en los nombres.
- Evitar espacios adicionales.
- No cambiar los encabezados de las columnas.
- Validar que los días contractuales sean valores numéricos.
- Registrar la fecha y el motivo del cambio cuando exista control documental.

### Riesgo de duplicidad

Si existen dos reglas aplicables al mismo registro, el resultado puede ser ambiguo.

Por esta razón, toda modificación debe revisarse antes de ejecutar el informe oficial.

----

## 8.2 Hoja PARAMETROS

La hoja **PARAMETROS** contiene valores generales utilizados por el sistema.

Puede incluir configuraciones como:

- Nombre esperado del archivo de entrada.
- Nombre del archivo de salida.
- Nombre de la hoja de resultados.
- Rango de días para alertas.
- Colores o etiquetas funcionales.
- Criterios generales de operación.
- Valores predeterminados.
- Controles de activación o desactivación.

### Estructura recomendada

| Parámetro | Valor | Descripción |
|---|---|---|
| NOMBRE_SALIDA | Informe_ANS_ELITE.xlsx | Nombre del informe generado. |
| ALERTA_INICIAL | 2 | Número de días desde el cual se activa una alerta. |
| CONSIDERAR_FESTIVOS | SI | Indica si los festivos deben excluirse del cálculo. |

Los parámetros anteriores son ejemplos funcionales.

### Modificaciones permitidas

El usuario autorizado puede:

- Cambiar valores operativos.
- Actualizar nombres definidos para la operación.
- Ajustar rangos de alerta.
- Activar o desactivar opciones permitidas.

### Recomendaciones

- No eliminar parámetros existentes.
- No cambiar el nombre técnico del parámetro.
- Modificar únicamente la columna destinada al valor.
- Revisar la descripción antes de realizar cambios.
- Probar el resultado con una muestra controlada.

----

## 8.3 Hoja FESTIVOS_ADICIONALES

Esta hoja permite registrar días no laborables adicionales que deben excluirse del cálculo.

Puede utilizarse para:

- Festivos no incluidos en el calendario general.
- Días institucionales no laborables.
- Cierres operativos autorizados.
- Fechas especiales definidas contractualmente.

### Estructura recomendada

| Fecha | Descripción | Activo |
|---|---|---|
| 2026-12-24 | Jornada institucional no laborable | SI |
| 2026-12-31 | Cierre operativo autorizado | SI |

### Reglas de uso

- La fecha debe ser válida.
- Cada día debe registrarse una sola vez.
- La descripción debe explicar el motivo.
- Solo deben agregarse fechas oficialmente autorizadas.
- Las fechas inactivas no deben afectar el cálculo.

### Efecto en el ANS

Los días registrados como festivos adicionales no se cuentan como días hábiles.

Esto puede modificar:

- La fecha límite.
- Los días transcurridos.
- Los días restantes.
- El estado final de la solicitud.

----

## 8.4 Hoja REGLAS_PRIORIDAD

La hoja **REGLAS_PRIORIDAD** permite definir condiciones especiales que requieren atención preferente.

Estas reglas no necesariamente modifican los días contractuales.

Su función principal es identificar solicitudes que deben destacarse dentro del análisis.

### Criterios posibles

- Municipio específico.
- Producto.
- Actividad.
- Cliente o tipo de cliente.
- Zona operativa.
- Tipo de solicitud.
- Antigüedad.
- Condición contractual.
- Combinación de criterios.

### Ejemplo funcional

| Regla | Criterio | Valor | Prioridad | Observación |
|---|---|---|---|---|
| R001 | Municipio | Municipio A | ALTA | Seguimiento especial. |
| R002 | Producto | Producto 2 | CRÍTICA | Atención prioritaria. |

### Resultado esperado

Cuando una solicitud cumple una regla especial, el informe puede asignarle:

- Nivel de prioridad.
- Etiqueta especial.
- Observación.
- Orden preferente en el análisis.
- Marcación visual.

### Modificaciones permitidas

El usuario autorizado puede:

- Crear nuevas reglas.
- Cambiar el nivel de prioridad.
- Modificar condiciones existentes.
- Actualizar observaciones.
- Activar o desactivar reglas.

### Buenas prácticas

- Utilizar nombres claros.
- Evitar reglas demasiado generales.
- No crear criterios contradictorios.
- Revisar el impacto antes de aplicarlas en producción.
- Documentar el motivo de cada nueva prioridad.

----

## 9. Funcionamiento del cálculo ANS

El cálculo ANS determina la fecha máxima de atención y el estado actual de cada solicitud.

### Información mínima requerida

El archivo fuente debe contener los campos necesarios para identificar y calcular cada registro.

Entre los campos principales se encuentran:

- Pedido o identificador de la solicitud.
- Dirección.
- Municipio.
- Actividad.
- Producto.
- Fecha de inicio del ANS.
- Información necesaria para identificar la regla contractual.

### Etapas del cálculo

1. Se identifica la solicitud.
2. Se valida la fecha de inicio del ANS.
3. Se busca la regla contractual aplicable.
4. Se asignan los días contractuales.
5. Se consultan fines de semana y festivos.
6. Se calcula la fecha límite.
7. Se calculan los días transcurridos.
8. Se calculan los días restantes.
9. Se determina el estado del ANS.
10. Se aplican reglas especiales de prioridad.

### Días hábiles

El sistema no cuenta como días hábiles:

- Sábados.
- Domingos.
- Festivos oficiales aplicables.
- Festivos adicionales registrados en la configuración.

### Fecha de inicio

La fecha de inicio corresponde al momento desde el cual comienza a contabilizarse el ANS, de acuerdo con la información exportada desde GIT y las reglas operativas definidas.

### Fecha límite

La fecha límite representa el último día permitido para atender la solicitud dentro del acuerdo de nivel de servicio.

### Días transcurridos

Corresponden a los días hábiles contabilizados desde el inicio del ANS hasta la fecha de corte del informe.

### Días restantes

Corresponden a la diferencia entre la fecha de corte y la fecha límite, expresada en días hábiles.

### Resultado del cálculo

Cada solicitud queda clasificada con información suficiente para responder:

- ¿Cuánto tiempo contractual tenía?
- ¿Cuánto tiempo ha transcurrido?
- ¿Cuánto tiempo queda disponible?
- ¿La solicitud está vencida?
- ¿Requiere atención inmediata?
- ¿Tiene una prioridad especial?

----

## 10. Estados del ANS

Los estados permiten identificar rápidamente el nivel de cumplimiento de cada solicitud.

| Estado | Significado | Acción recomendada |
|---|---|---|
| VENCIDO | La fecha límite ya fue superada. | Gestionar inmediatamente y revisar la causa. |
| ALERTA 0 DÍAS | La solicitud vence en la fecha de corte. | Prioridad inmediata. |
| ALERTA 1–2 DÍAS | La solicitud se encuentra próxima a vencer. | Programar y asegurar su atención. |
| A TIEMPO | La solicitud conserva margen dentro del ANS. | Mantener seguimiento preventivo. |

### VENCIDO

Una solicitud se clasifica como vencida cuando los días restantes son negativos o cuando la fecha límite es anterior a la fecha de corte.

### ALERTA 0 DÍAS

Indica que la solicitud vence el mismo día del análisis.

Debe considerarse como una prioridad operativa inmediata.

### ALERTA 1–2 DÍAS

Corresponde a solicitudes con uno o dos días hábiles disponibles antes de vencer.

El rango puede ajustarse mediante parametrización cuando la operación lo requiera.

### A TIEMPO

Corresponde a solicitudes que aún cuentan con margen suficiente dentro del plazo contractual.

Aunque no sean urgentes, deben permanecer dentro del seguimiento.

### Colores de referencia

| Estado | Color recomendado |
|---|---|
| VENCIDO | Rojo |
| ALERTA 0 DÍAS | Naranja |
| ALERTA 1–2 DÍAS | Amarillo |
| A TIEMPO | Verde |

Los colores facilitan la lectura, pero la decisión operativa siempre debe basarse en el estado y la información del registro.

----

## 11. Reglas especiales

Las reglas especiales complementan el cálculo contractual y permiten adaptar el informe a situaciones específicas del negocio.

### Tipos de reglas especiales

- Prioridad por municipio.
- Prioridad por producto.
- Prioridad por actividad.
- Tratamiento especial por zona.
- Condiciones específicas por tipo de conexión.
- Alertas por antigüedad.
- Casos definidos por el área operativa.

### Aplicación

Una regla especial puede:

- Cambiar el nivel de prioridad.
- Agregar una observación.
- Destacar visualmente un registro.
- Ordenar la solicitud en una posición preferente.
- Identificar casos para revisión manual.

### Precedencia de reglas

Cuando una solicitud cumple varias reglas, debe aplicarse el criterio de mayor prioridad definido en la configuración.

Ejemplo:

```text
CRÍTICA
    ↓
ALTA
    ↓
MEDIA
    ↓
NORMAL
```

### Recomendación

Las nuevas reglas deben ser aprobadas funcionalmente antes de incorporarlas al archivo oficial de configuración.

----

## 12. Dashboard

El dashboard permite analizar la información generada por la herramienta.

El archivo principal es:

```text
INFORME_ANS.xlsb
```

### Objetivos del dashboard

- Visualizar el estado general del ANS.
- Identificar solicitudes vencidas.
- Revisar solicitudes próximas a vencer.
- Analizar la distribución por municipio.
- Analizar productos y actividades.
- Priorizar la gestión operativa.
- Facilitar reuniones de seguimiento.

### Indicadores recomendados

- Total de solicitudes.
- Total vencidas.
- Total en alerta 0 días.
- Total en alerta 1–2 días.
- Total a tiempo.
- Porcentaje de cumplimiento.
- Solicitudes por municipio.
- Solicitudes por producto.
- Solicitudes por actividad.
- Solicitudes por prioridad.

### Filtros recomendados

- Estado ANS.
- Municipio.
- Producto.
- Actividad.
- Prioridad.
- Fecha de inicio.
- Fecha límite.
- Zona o clasificación operativa.

### Actualización del dashboard

Después de generar el archivo **Informe_ANS_ELITE.xlsx**, el usuario debe:

1. Abrir el archivo **INFORME_ANS.xlsb**.
2. Ejecutar la opción de actualización definida.
3. Esperar a que finalicen las consultas y tablas dinámicas.
4. Validar que la fecha de corte sea correcta.
5. Revisar los indicadores principales.
6. Guardar el dashboard actualizado.

### Validaciones posteriores

- El total del dashboard debe coincidir con el total del informe generado.
- Los estados deben corresponder con el archivo consolidado.
- Los filtros deben mostrar información.
- Las tablas y gráficos deben estar actualizados.

----

## 13. Flujo completo de operación

## 13.1 Exportar la información desde GIT

El usuario ingresa al sistema GIT y genera el archivo de conexiones correspondiente al corte requerido.

### Validar antes de continuar

- Fecha del corte.
- Cantidad de registros.
- Columnas requeridas.
- Información de municipios.
- Fechas de inicio.
- Productos y actividades.

----

## 13.2 Guardar el archivo en entrada

El archivo exportado debe guardarse en la carpeta:

```text
entrada
```

Antes de iniciar, se debe confirmar que:

- El archivo no esté abierto.
- Corresponda al corte actual.
- No existan archivos antiguos que puedan confundirse con el vigente.

----

## 13.3 Revisar la configuración

Cuando existan cambios contractuales u operativos, el usuario autorizado debe revisar:

```text
config/DIAS_CONTRACTUALES.xlsx
```

Se deben validar especialmente:

- Municipios nuevos.
- Días contractuales modificados.
- Festivos adicionales.
- Parámetros generales.
- Reglas especiales de prioridad.

Si no existen cambios, no es necesario modificar el archivo.

----

## 13.4 Generar el informe ANS

El usuario ejecuta la opción:

```text
Generar Informe ANS
```

Durante el proceso, la herramienta:

- Lee el archivo de entrada.
- Valida la estructura.
- Consulta la parametrización.
- Aplica reglas contractuales.
- Calcula fechas y estados.
- Aplica prioridades.
- Genera el archivo de salida.
- Registra el resultado en los logs.

----

## 13.5 Validar el archivo generado

El resultado se encuentra en:

```text
salida/Informe_ANS_ELITE.xlsx
```

El usuario debe revisar:

- Fecha de generación.
- Cantidad de registros.
- Registros sin municipio.
- Registros sin regla contractual.
- Fechas de inicio inválidas.
- Estados generados.
- Prioridades aplicadas.

----

## 13.6 Actualizar el dashboard

El usuario abre:

```text
dashboard/INFORME_ANS.xlsb
```

Posteriormente actualiza la información y valida los indicadores.

----

## 13.7 Realizar el análisis operativo

El análisis debe iniciar por el siguiente orden:

1. Solicitudes vencidas.
2. Solicitudes con alerta 0 días.
3. Solicitudes con alerta 1–2 días.
4. Solicitudes con prioridad crítica o alta.
5. Solicitudes a tiempo.

### Resultado esperado

El equipo operativo obtiene una lista clara de los casos que requieren gestión prioritaria.

----

## 14. Adaptabilidad del sistema

La herramienta fue diseñada para adaptarse a cambios funcionales sin requerir modificaciones frecuentes al software.

### El usuario puede administrar

- Nuevos municipios.
- Cambios en días contractuales.
- Nuevos productos o actividades, cuando la estructura configurada lo permita.
- Festivos adicionales.
- Parámetros operativos.
- Rangos de alerta.
- Reglas especiales de prioridad.
- Observaciones funcionales.

### Ventaja principal

La parametrización en Excel permite que el conocimiento del negocio permanezca visible y administrable.

### Ejemplo

Cuando se incorpora un nuevo municipio, el usuario autorizado puede agregarlo en la hoja correspondiente, definir sus días contractuales y utilizarlo en la siguiente generación.

No es necesario modificar el software, siempre que el cambio se encuentre dentro de las reglas previstas.

### Cambios que requieren evaluación

Algunas modificaciones sí pueden requerir revisión especializada, por ejemplo:

- Cambio completo del archivo exportado desde GIT.
- Eliminación o cambio de nombres de columnas.
- Nuevas reglas que dependan de información no disponible.
- Cambios en la lógica contractual.
- Nuevos tipos de resultados.
- Modificaciones estructurales del dashboard.

----

## 15. Buenas prácticas

## 15.1 Antes de ejecutar

- Confirmar que el archivo fuente sea el correcto.
- Cerrar los archivos de entrada, salida y dashboard.
- Verificar la fecha del corte.
- Revisar cambios recientes de parametrización.
- Crear una copia de respaldo antes de modificar la configuración.

## 15.2 Durante la ejecución

- No mover archivos.
- No abrir el informe mientras se genera.
- No cerrar la herramienta de forma forzada.
- Esperar el mensaje de finalización.

## 15.3 Después de ejecutar

- Revisar el resultado.
- Validar el total de registros.
- Revisar advertencias.
- Actualizar el dashboard.
- Guardar los archivos.
- Conservar el informe oficial del corte.

## 15.4 Parametrización

- Modificar únicamente los campos permitidos.
- No cambiar encabezados.
- No eliminar hojas.
- No duplicar reglas.
- No registrar fechas inválidas.
- Documentar los cambios importantes.

## 15.5 Control de versiones

Se recomienda conservar:

- Copia del archivo de entrada.
- Copia del informe generado.
- Copia del dashboard actualizado.
- Copia del archivo de configuración utilizado.

Esto permite reconstruir el resultado de un corte cuando sea necesario.

----

## 16. Recomendaciones

### Para usuarios operativos

- Revisar primero los estados vencidos y críticos.
- Utilizar filtros para distribuir la gestión.
- Validar los casos atípicos antes de escalar.
- No modificar manualmente los cálculos del informe.

### Para usuarios administradores

- Mantener actualizado el archivo DIAS_CONTRACTUALES.xlsx.
- Revisar periódicamente las reglas duplicadas.
- Validar nuevos municipios antes de utilizarlos.
- Mantener respaldo de la configuración anterior.
- Controlar quién tiene permiso para parametrizar.

### Para reuniones

- Confirmar que el dashboard esté actualizado.
- Presentar la fecha de corte.
- Mostrar primero los indicadores generales.
- Continuar con vencidos y alertas.
- Finalizar con responsables y acciones.

### Para soporte

Cuando se reporte una novedad, se recomienda enviar:

- Archivo de entrada utilizado.
- Archivo de configuración.
- Archivo generado.
- Log de la ejecución.
- Captura del mensaje mostrado.
- Descripción clara del comportamiento esperado.

----

## 17. Beneficios obtenidos

La implementación de la herramienta aporta los siguientes beneficios:

### Estandarización

Todas las solicitudes se calculan utilizando las mismas reglas.

### Reducción de tiempo

Disminuye las actividades manuales necesarias para preparar el informe.

### Menor riesgo de error

Reduce errores asociados con fórmulas manuales, festivos y fechas límite.

### Trazabilidad

Permite identificar el archivo fuente, la configuración y el resultado de cada ejecución.

### Priorización

Facilita la identificación de solicitudes vencidas o próximas a vencer.

### Autonomía funcional

Los usuarios autorizados pueden ajustar reglas del negocio desde Excel.

### Adaptabilidad

El sistema puede incorporar nuevos municipios, parámetros y prioridades.

### Apoyo a la gestión

El dashboard facilita el seguimiento en reuniones y la toma de decisiones.

----

## 18. Preguntas frecuentes

### ¿De dónde proviene la información?

La información proviene del archivo exportado desde el sistema GIT utilizado para gestionar las conexiones.

### ¿Dónde debo guardar el archivo exportado?

Debe guardarse en la carpeta **entrada**.

### ¿Cuál es el archivo generado?

El resultado principal es:

```text
Informe_ANS_ELITE.xlsx
```

### ¿Dónde se encuentra el dashboard?

En la carpeta **dashboard**, dentro del archivo:

```text
INFORME_ANS.xlsb
```

### ¿El dashboard se actualiza automáticamente?

La generación del informe y la actualización del dashboard son etapas diferentes. Después de generar el informe, el usuario debe actualizar el dashboard mediante la opción definida para ello.

### ¿Qué sucede si aparece un municipio nuevo?

El municipio debe agregarse en la hoja correspondiente del archivo **DIAS_CONTRACTUALES.xlsx**, junto con sus días contractuales y demás criterios aplicables.

### ¿Se puede cambiar el número de días contractuales?

Sí. El usuario autorizado puede modificarlo en la hoja **REGLAS_DE_NEGOCIO**.

### ¿Se pueden agregar festivos?

Sí. Deben registrarse en la hoja **FESTIVOS_ADICIONALES**.

### ¿Se pueden crear nuevas prioridades?

Sí. Deben configurarse en la hoja **REGLAS_PRIORIDAD**.

### ¿Es necesario modificar el software para estos cambios?

No. Los cambios previstos en la parametrización pueden realizarse desde Excel.

### ¿Qué ocurre si una solicitud no encuentra regla contractual?

Debe quedar identificada para revisión. El usuario debe validar los datos del registro y agregar o corregir la regla correspondiente.

### ¿Qué ocurre si la fecha de inicio está vacía o es inválida?

El registro no puede calcularse correctamente y debe ser revisado en el archivo fuente.

### ¿Se cuentan sábados y domingos?

No. El cálculo se realiza sobre días hábiles.

### ¿Se cuentan los festivos?

No. Los festivos aplicables se excluyen del cálculo.

### ¿Qué significa ALERTA 0 DÍAS?

Significa que la solicitud vence en la fecha de corte y debe atenderse de forma inmediata.

### ¿Qué significa ALERTA 1–2 DÍAS?

Significa que la solicitud está próxima a vencer y debe programarse prioritariamente.

### ¿Qué debo revisar primero?

El orden recomendado es:

1. Vencidos.
2. Alerta 0 días.
3. Alerta 1–2 días.
4. Prioridades críticas o altas.
5. Solicitudes a tiempo.

### ¿Qué debo hacer si el proceso presenta un error?

Revisar el mensaje mostrado y consultar el archivo de log. Si la novedad continúa, compartir el archivo de entrada, la configuración y el log con el responsable del soporte.

### ¿Puedo cambiar los encabezados del archivo de configuración?

No. Los encabezados forman parte de la estructura esperada por la herramienta.

### ¿Puedo eliminar hojas del archivo DIAS_CONTRACTUALES.xlsx?

No. Las hojas requeridas deben conservarse.

### ¿Puedo modificar manualmente el Informe_ANS_ELITE.xlsx?

No se recomienda. El archivo debe conservar el resultado generado para asegurar trazabilidad y consistencia.

### ¿Cómo se conserva un histórico?

Se recomienda guardar una copia por cada fecha de corte, incluyendo:

- Archivo exportado desde GIT.
- Informe generado.
- Dashboard actualizado.
- Configuración utilizada.

----

## 19. Guion sugerido para explicar la herramienta

### Inicio

> La herramienta automatiza la preparación del informe ANS a partir del archivo exportado desde GIT.

### Problema

> Anteriormente era necesario realizar cálculos manuales de fechas, días hábiles, vencimientos y prioridades.

### Solución

> El sistema consulta las reglas contractuales, excluye fines de semana y festivos, determina la fecha límite y clasifica cada solicitud.

### Parametrización

> Las principales reglas del negocio están administradas en el archivo DIAS_CONTRACTUALES.xlsx. Esto permite agregar municipios, cambiar días, registrar festivos y crear prioridades sin modificar el software.

### Resultado

> El proceso genera el archivo Informe_ANS_ELITE.xlsx, que posteriormente actualiza el dashboard INFORME_ANS.xlsb.

### Uso operativo

> El análisis comienza por los vencidos, continúa con las alertas y finaliza con los casos a tiempo.

### Cierre

> La herramienta reduce tiempo, estandariza los cálculos y mejora la priorización de la gestión.

----

## 20. Lista de verificación operativa

### Antes de generar

- [ ] Exportar el archivo correcto desde GIT.
- [ ] Validar la fecha de corte.
- [ ] Guardar el archivo en entrada.
- [ ] Cerrar los archivos abiertos.
- [ ] Revisar cambios de configuración.

### Después de generar

- [ ] Confirmar que se creó Informe_ANS_ELITE.xlsx.
- [ ] Validar el total de registros.
- [ ] Revisar registros sin regla.
- [ ] Revisar fechas inválidas.
- [ ] Consultar advertencias del log.

### Dashboard

- [ ] Abrir INFORME_ANS.xlsb.
- [ ] Actualizar la información.
- [ ] Confirmar la fecha de corte.
- [ ] Validar indicadores.
- [ ] Guardar el dashboard.

### Análisis

- [ ] Revisar vencidos.
- [ ] Revisar alerta 0 días.
- [ ] Revisar alerta 1–2 días.
- [ ] Revisar prioridades especiales.
- [ ] Definir responsables y acciones.

----

## 21. Control funcional de cambios

Toda modificación de las reglas del negocio debe quedar controlada.

### Información recomendada

| Campo | Descripción |
|---|---|
| Fecha del cambio | Día en que se realizó la modificación. |
| Responsable | Usuario que realizó el cambio. |
| Hoja modificada | Hoja del archivo DIAS_CONTRACTUALES.xlsx. |
| Regla anterior | Valor que estaba vigente. |
| Regla nueva | Valor actualizado. |
| Motivo | Razón contractual u operativa. |
| Aprobación | Responsable que autorizó el cambio. |

### Recomendación

Antes de utilizar una nueva parametrización en producción, se debe ejecutar una prueba controlada y comparar los resultados.

----

## 22. Mantenimiento funcional

El mantenimiento funcional consiste en conservar actualizadas las reglas administradas por el negocio.

### Actividades periódicas

- Revisar municipios nuevos.
- Validar cambios contractuales.
- Actualizar festivos adicionales.
- Revisar prioridades vigentes.
- Eliminar duplicidades funcionales.
- Confirmar que los parámetros continúan aplicando.
- Revisar la calidad del archivo exportado desde GIT.

### Frecuencia recomendada

| Actividad | Frecuencia |
|---|---|
| Revisión de archivo de entrada | En cada ejecución |
| Revisión de advertencias | En cada ejecución |
| Revisión de municipios nuevos | Cuando aparezcan registros sin regla |
| Revisión de festivos | Al inicio de cada año y cuando existan novedades |
| Revisión de reglas contractuales | Cuando cambie el contrato o la operación |
| Revisión de prioridades | Mensual o según necesidad operativa |
| Copia de respaldo de configuración | Antes de cada modificación |

----

## 23. Criterios de aceptación del informe

El informe puede considerarse listo para uso operativo cuando cumple los siguientes criterios:

- El archivo de entrada corresponde al corte oficial.
- No existen errores críticos de estructura.
- La cantidad de registros procesados es coherente.
- Las fechas de inicio son válidas.
- Las reglas contractuales fueron encontradas.
- Las fechas límite fueron calculadas.
- Los estados ANS fueron asignados.
- Las prioridades especiales fueron aplicadas.
- El archivo Informe_ANS_ELITE.xlsx fue generado.
- El dashboard fue actualizado correctamente.
- Los indicadores coinciden con el archivo consolidado.

----

## 24. Responsabilidades funcionales

| Rol | Responsabilidad |
|---|---|
| Usuario operativo | Exportar el archivo, ejecutar el proceso, actualizar el dashboard y analizar resultados. |
| Administrador funcional | Mantener municipios, días contractuales, parámetros, festivos y prioridades. |
| Responsable del proceso | Aprobar cambios de reglas y validar criterios contractuales. |
| Soporte técnico | Atender errores de ejecución o cambios que superen la parametrización disponible. |
| Líder operativo | Revisar indicadores y asignar acciones sobre vencidos y alertas. |

----

## 25. Conclusión

El **Generador de Informes ANS - ATC CHEC** centraliza y estandariza el proceso de seguimiento de los acuerdos de nivel de servicio.

Su funcionamiento se basa en un flujo claro:

```text
GIT
    ↓
Entrada
    ↓
Cálculo y reglas
    ↓
Informe consolidado
    ↓
Dashboard
    ↓
Gestión operativa
```

La parametrización mediante Excel permite que el sistema se mantenga actualizado frente a cambios de municipios, días contractuales, festivos, parámetros y prioridades.

El valor principal de la herramienta se encuentra en:

- La reducción del trabajo manual.
- La uniformidad de los cálculos.
- La visibilidad de los vencimientos.
- La autonomía funcional.
- La trazabilidad de los resultados.
- El apoyo a la toma de decisiones.

----

## Documento oficial

**Nombre del archivo:**

```text
generador_informes_ans_atc_chec.md
```

**Ubicación recomendada:**

```text
docs/generador_informes_ans_atc_chec.md
```

**Proyecto:** Generador de Informes ANS - ATC CHEC  
**Tipo de documento:** Centro de Conocimiento Técnico y Manual Funcional  
**Público objetivo:** Usuarios funcionales, usuarios operativos, administradores del proceso y personal encargado de la entrega y capacitación.


## Arquitectura funcional

La arquitectura funcional representa la forma en que interactúan los usuarios, los archivos y las reglas del negocio.

No corresponde a la arquitectura técnica del software.

### Componentes funcionales

| Componente | Función |
|---|---|
| Fuente de información | Archivo exportado desde el sistema GIT. |
| Módulo de entrada | Recibe el archivo que será procesado. |
| Módulo de validación | Verifica que el archivo tenga la estructura requerida. |
| Motor de reglas | Consulta los días contractuales, parámetros, festivos y prioridades. |
| Motor de cálculo ANS | Calcula fechas límite, días transcurridos, días restantes y estado. |
| Generador de informe | Construye el archivo Informe_ANS_ELITE.xlsx. |
| Dashboard | Presenta indicadores, filtros y vistas para el análisis. |
| Módulo de mapas | Permite representar geográficamente la información cuando aplique. |
| Registro de ejecución | Conserva información sobre el resultado del procesamiento. |

### Principio funcional

La herramienta separa tres elementos principales:

1. **Información de entrada.**
2. **Reglas del negocio.**
3. **Resultados para análisis.**

Esta separación permite actualizar la operación sin alterar el funcionamiento general del sistema.

----

## 6. Estructura del proyecto

La herramienta está organizada en carpetas que representan las diferentes etapas del proceso.

```text
Generador_Informes_ANS_ATC_CHEC/
│
├── entrada/
├── salida/
├── dashboard/
├── config/
├── logs/
├── mapas/
├── assets/
├── docs/
├── main.py
├── iniciar.bat
└── requirements.txt
```

Para el usuario funcional, las carpetas principales son:

- entrada
- salida
- dashboard
- config
- logs
- mapas

Las demás carpetas y archivos hacen parte del funcionamiento interno de la herramienta y no deben modificarse durante la operación normal.

----