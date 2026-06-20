## 🎯 Objetivo

El Portal de Formación Elite es un sistema web desarrollado para gestionar formaciones, capacitaciones, charlas, empleados, asistencias y reportes corporativos.

El objetivo principal es reemplazar controles manuales por una plataforma centralizada que permita registrar asistencias, validar empleados activos y consultar información de manera organizada.

---

## 🧩 Problema que resuelve

Antes del desarrollo, el control de capacitaciones podía depender de registros manuales, archivos separados o procesos difíciles de auditar.

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

El sistema está construido como una aplicación web en Streamlit.

La información se almacena en una base de datos PostgreSQL alojada en Supabase.

El despliegue se realiza en Streamlit Cloud, permitiendo el acceso mediante una URL pública.

Flujo general:

Streamlit Cloud  
↓  
Aplicación Portal Formación Elite  
↓  
Conexión segura mediante DATABASE_URL  
↓  
Base de datos PostgreSQL en Supabase  
↓  
Registro y consulta de empleados, formaciones y asistencias

---

## 🛠️ Tecnologías utilizadas

- Python.
- Streamlit.
- PostgreSQL.
- Supabase.
- SQLAlchemy.
- GitHub.
- Streamlit Cloud.

---

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

Tablas principales:

- Empleados.
- Formaciones.
- Asistencias.
- Preguntas.
- Respuestas.

Esta estructura permite separar la información y mantener una base organizada para consultas y reportes.

---

## 🔐 Seguridad básica

El sistema utiliza controles básicos de seguridad:

- Acceso administrativo con contraseña.
- Conexión a base de datos mediante secrets.
- DATABASE_URL protegido en Streamlit Cloud.
- Validación de empleados activos.
- Control de registros duplicados.

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

El acceso administrativo se protege mediante contraseña.

### ¿Cómo se registra un empleado a una formación?

El empleado ingresa a una URL generada por el sistema, registra su cédula y el sistema valida si está activo.

### ¿Qué diferencia hay entre charla y capacitación?

La charla registra asistencia. La capacitación puede incluir preguntas de evaluación para medir conocimiento.

### ¿Qué reportes permite consultar?

Permite consultar asistentes registrados, pendientes por registrar y consolidado mensual por rango de fechas.

### ¿Cuál es el mayor beneficio?

Permite tener trazabilidad completa de las formaciones y asistencias en una plataforma centralizada, accesible desde cualquier lugar.