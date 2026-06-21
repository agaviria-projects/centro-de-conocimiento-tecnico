## 🎯 Objetivo

El Portal de Formación Elite es un sistema web desarrollado para gestionar formaciones, capacitaciones, charlas, empleados, asistencias y reportes corporativos.

El objetivo principal es reemplazar controles manuales por una plataforma centralizada que permita registrar asistencias, validar empleados activos y consultar información de manera organizada.

---

## 🧩 Problema que resuelve

El portal permite:

- Crear formaciones o charlas.
- Registrar asistencia de empleados.
- Validar empleados activos.
- Consultar formaciones creadas.
- Editar información.
- Generar reportes.
- Consultar pendientes por registrar.
- Mantener trazabilidad de la información.

---

## 🏗️ Arquitectura general

El sistema está construido como una aplicación web desarrollada en Streamlit(utilizado para crear la interfaz web del sistema)

La información se almacena en una base de datos PostgreSQL alojada en Supa-beis (Plataforma donde se encuentra alojada la base de datos PostgreSQL.)

El despliegue se realiza en Streamlit Cloud(Servicio utilizado para publicar la aplicación en internet y permitir el acceso mediante una URL).

## 🔐 Acceso y administración de plataformas

El acceso a las plataformas utilizadas en el desarrollo requiere autenticación mediante usuario y contraseña.

Las credenciales de administración son de acceso restringido y únicamente son conocidas por el responsable técnico del sistema.(Gaviria)

Esto garantiza que solo personal autorizado pueda administrar:

- La aplicación desplegada en Streamlit Cloud.
- La base de datos alojada en Supabase.

De esta manera se protege la información corporativa y se evita el acceso no autorizado a la infraestructura del sistema.


## 🏠 Pantalla principal

La pantalla inicial muestra el portal corporativo con el logo de Elite Ingenieros y las opciones principales de navegación.

Opciones disponibles:

- Inicio.
- Administración.

El sistema muestra el estado general como Sistema Activo.

---

## 🔐 Módulo de Administración

El módulo de administración está protegido mediante contraseña.

Su objetivo es permitir que solo usuarios autorizados puedan gestionar la información del sistema.

Desde este módulo se puede acceder a:

- Crear formación.
- Gestión de empleados.
- Asistencias y reportes.

---

## 📚 Crear Formación

Este módulo permite crear una nueva formación o charla.

Información registrada:

- Nombre de la capacitación.
- Fecha de asistencia.
- Formador.
- Tipo de registro:
  - Charla.
  - Capacitación.

Cuando el registro corresponde a capacitación, el sistema permite agregar preguntas de evaluación.

---

## 📝 Preguntas de evaluación

Para las capacitaciones se pueden crear preguntas con varias opciones de respuesta.

El sistema permite registrar:

- Texto de la pregunta.
- Opción A.
- Opción B.
- Opción C.
- Opción D.
- Respuesta correcta.

Estas preguntas permiten evaluar el conocimiento de los asistentes después de la capacitación.

---

## 🔎 Consultar / Editar Formación

El sistema permite consultar las formaciones creadas y seleccionar una para editarla.

La tabla muestra información como:

- ID.
- Fecha de asistencia.
- Nombre de formación.
- Tipo de registro.
- Formador.
- URL de asistencia.

Esta opción permite mantener control y trazabilidad sobre las formaciones creadas.

---

## 📅 Consolidado Mensual

El módulo de consolidado mensual permite consultar formaciones dentro de un rango de fechas.

El usuario puede seleccionar:

- Fecha inicial.
- Fecha final.

El sistema consulta las formaciones registradas en ese periodo y permite validar si existen registros para el rango seleccionado.

---

## 👥 Gestión de Empleados

El módulo de empleados permite administrar la base de personas que pueden registrar asistencia.

Funciones principales:

- Agregar empleado.
- Consultar empleado.
- Activar empleado.
- Inactivar empleado.

Información registrada:

- Cédula.
- Nombre.
- Cargo.
- Zona.
- Proyecto.

Esta validación es importante porque el sistema permite controlar quiénes pueden registrar asistencia.

---

## 📋 Asistencias y Reportes

Este módulo permite consultar la asistencia registrada por formación.

Opciones principales:

- Seleccionar formación.
- Actualizar reporte.
- Ver empleados registrados.
- Ver pendientes por registrar.

Indicadores visibles:

- Total de asistencias.
- Nombre de la formación.
- Estado de registros.

---

## 🌐 Registro público de asistencia

Cada formación genera una URL que puede compartirse con los empleados.

El empleado ingresa al enlace, registra sus datos y confirma la asistencia.

El sistema valida que la cédula exista y que el empleado esté activo.

Esto evita registros no autorizados o inconsistentes.

---

## 🗃️ Base de datos

La información se almacena en PostgreSQL mediante Supabase.

### 📋 Tablas principales del sistema

- **empleados:** almacena la información de los empleados autorizados para registrar asistencia.

- **formaciones:** almacena la información de las capacitaciones y charlas creadas en el sistema.

- **asistencias:** almacena los registros de asistencia realizados por los empleados.

Esta estructura permite separar la información y mantener una base organizada para consultas y reportes.

La base de datos está compuesta por tres tablas principales: empleados, formaciones y asistencias. Cada tabla almacena información específica y permite mantener la trazabilidad completa del proceso de capacitación

---

## 🔐 Seguridad y tratamiento de datos

El sistema incorpora controles básicos de seguridad para proteger la información registrada por los empleados.

Entre las medidas implementadas se encuentran:

- Acceso administrativo protegido mediante contraseña.
- Credenciales de conexión a la base de datos almacenadas de forma segura en la plataforma de despliegue.
- Validación de empleados activos antes de permitir el registro de asistencia.
- Prevención de registros duplicados.
- Solo los usuarios autorizados pueden acceder a las funciones administrativas del sistema, como crear formaciones, administrar empleados, consultar reportes o modificar información.

La información almacenada en el sistema es utilizada exclusivamente para fines corporativos relacionados con la gestión de capacitaciones, asistencias y generación de reportes internos.

El sistema no comparte ni divulga la información registrada a terceros y únicamente los usuarios autorizados pueden consultar o administrar los datos.

---

## ❓ ¿Cómo se realiza el tratamiento de los datos?

Los datos registrados por los empleados son tratados únicamente para fines administrativos y de gestión de formación dentro de la organización.

La información almacenada permite:

- Validar que el empleado se encuentre activo.
- Registrar la asistencia a capacitaciones o charlas.
- Generar reportes corporativos.
- Mantener trazabilidad de las formaciones realizadas.

El tratamiento de la información se realiza siguiendo las políticas internas definidas por la organización.

El sistema cuenta con un módulo administrativo protegido mediante contraseña. Esto garantiza que únicamente personal autorizado pueda crear formaciones, administrar empleados y consultar reportes, mientras que los demás usuarios solo pueden registrar su asistencia.

---

## 🚀 Beneficios del desarrollo

El Portal Formación Elite aporta:

- Centralización de capacitaciones.
- Reducción del control manual.
- Validación de empleados activos.
- Registro ordenado de asistencias.
- Creación de evaluaciones.
- Consulta y edición de formaciones.
- Reportes por formación.
- Control de pendientes por registrar.
- Acceso desde cualquier lugar mediante URL.

---

## 💬 Cómo explicarlo en reunión

El Portal de Formación Elite es una aplicación web desarrollada en Streamlit para gestionar capacitaciones, charlas, empleados y asistencias.

El administrador puede crear una formación, definir si es charla o capacitación, agregar preguntas de evaluación cuando aplica y generar una URL pública para que los empleados registren su asistencia.

La información se almacena en una base de datos PostgreSQL en Supabase, lo que permite consultar formaciones, gestionar empleados, validar cédulas activas y generar reportes de asistencia.

---

## 🎤 Preguntas que me pueden hacer

### ¿Qué problema resuelve el portal?

Centraliza el control de formaciones, empleados y asistencias, evitando registros manuales dispersos y mejorando la trazabilidad.

### ¿Por qué se usó Streamlit?

Porque permite crear rápidamente una aplicación web en Python con formularios, tablas, navegación y conexión a base de datos.

### ¿Dónde se guarda la información?

La información se guarda en una base de datos PostgreSQL alojada en Supabase.

### ¿Cómo se protege el acceso administrativo?

Mediante credenciales seguras, validaciones y acceso administrativo protegido.

### ¿Cómo se registra un empleado a una formación?

El empleado ingresa a una URL generada por el sistema, registra su cédula y el sistema valida si está activo.

### ¿Qué diferencia hay entre charla y capacitación?

La charla registra asistencia. La capacitación puede incluir preguntas de evaluación para medir conocimiento.

### ¿Qué reportes permite consultar?

Permite consultar asistentes registrados, pendientes por registrar y consolidado mensual por rango de fechas.

### ¿Cuál es el mayor beneficio?

Permite tener trazabilidad completa de las formaciones y asistencias en una plataforma centralizada, accesible desde cualquier lugar.