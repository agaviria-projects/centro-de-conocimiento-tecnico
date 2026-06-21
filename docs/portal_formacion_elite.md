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

El sistema está construido como una aplicación web desarrollada en Streamlit.

La información se almacena en una base de datos PostgreSQL alojada en Supabase.

El despliegue se realiza en Streamlit Cloud, permitiendo el acceso mediante una URL pública.

Flujo general:

Streamlit Cloud
        ↓
Portal Formación Elite
        ↓
DATABASE_URL
        ↓
PostgreSQL (Supabase)
        ↓
Empleados + Formaciones + Asistencias

### 🔗 Conexión segura mediante DATABASE_URL

La aplicación utiliza una cadena de conexión segura llamada DATABASE_URL, que contiene la información necesaria para conectarse a la base de datos PostgreSQL.

Esta información se almacena de forma protegida en Streamlit Cloud y no se encuentra visible dentro del código fuente.

---

## 🛠️ Tecnologías utilizadas

### 🐍 Python

Lenguaje principal utilizado para desarrollar toda la lógica del sistema.

### 🌐 Streamlit

Framework (herramienta que facilita el desarrollo de aplicaciones, reduciendo el tiempo de construcción) utilizado para crear la interfaz web del sistema, permitiendo desarrollar formularios, tablas, reportes y pantallas interactivas de manera rápida y sencilla.

### 🗄️ PostgreSQL

Sistema gestor de base de datos utilizado para almacenar la información.

### ☁️ Supabase

Plataforma donde se encuentra alojada la base de datos PostgreSQL.

### 🔗 SQLAlchemy

Herramienta utilizada para conectar la aplicación desarrollada en Python con PostgreSQL.

### 📦 GitHub

Plataforma utilizada para almacenar y versionar el código fuente.

### 🚀 Streamlit Cloud

Servicio utilizado para publicar la aplicación en internet y permitir el acceso mediante una URL.

## ☁️ Administración de la Base de Datos en Supabase

La base de datos del Portal Formación Elite se encuentra alojada en Supabase.

Para acceder a la plataforma se debe:

1. Ingresar al sitio oficial de Supabase.
2. Seleccionar la opción **Sign In**.
3. Iniciar sesión utilizando el mismo método empleado durante la creación de la cuenta:

   - Correo electrónico y contraseña.
   - Cuenta Google.
   - Cuenta GitHub: usuario agaviria-projects contraseña 34@7O5}p

Una vez autenticado, la plataforma muestra el Dashboard con todos los proyectos disponibles.

Posteriormente se debe seleccionar el proyecto correspondiente al Portal Formación Elite.

---

## 🛠️ Secciones principales utilizadas en Supabase

### 📋 Table Editor

Permite visualizar, consultar y modificar la información almacenada en las tablas del sistema.

Por ejemplo:

- Empleados.
- Formaciones.
- Asistencias.

---

### 🔍 SQL Editor

Permite ejecutar consultas SQL directamente sobre la base de datos para realizar validaciones, auditorías o mantenimiento de la información.

---

### ⚙️ Project Settings

Permite administrar la configuración general del proyecto, incluyendo:

- Parámetros de conexión.
- Variables de configuración.
- Claves API.
- Información necesaria para la conexión desde la aplicación.

---

## 📌 Módulos más utilizados en este desarrollo

Para la administración cotidiana del Portal Formación Elite, normalmente se utilizan principalmente:

- **Table Editor:** revisión y administración de la información almacenada.
- **SQL Editor:** ejecución de consultas y validaciones SQL.
- **Project Settings:** revisión de la configuración de conexión del sistema.

### 🚀 Streamlit Cloud

Servicio utilizado para desplegar la aplicación en internet y permitir el acceso mediante una URL pública.

## 🚀 Administración de la Aplicación en Streamlit Cloud

La aplicación Portal Formación Elite se encuentra desplegada en Streamlit Cloud.

Para acceder a la plataforma se debe:

1. Ingresar al sitio oficial de Streamlit Cloud.
2. Seleccionar la opción **Sign In**.
3. Iniciar sesión utilizando el mismo método empleado durante la creación de la cuenta:

   - Cuenta GitHub: ingresar con el usuario control.elite.drive@gmail.com contraseña 35@El1te}5
   - Cuenta Google.
   - Correo electrónico (si aplica).

Una vez autenticado, la plataforma muestra el espacio de trabajo (Workspace) y las aplicaciones desplegadas que seria sistema-capacitaciones∙main∙app.py 

Posteriormente se debe seleccionar la aplicación correspondiente al Portal Formación Elite.

---

## 🛠️ Funciones principales utilizadas en Streamlit Cloud

### 📱 Aplicaciones

Permite visualizar todas las aplicaciones desplegadas y acceder a cada una de ellas.

---

### 🔐 Secrets

Permite almacenar información sensible de forma segura, por ejemplo:

- DATABASE_URL.
- Contraseñas administrativas.
- Variables de configuración.

Esta información no queda expuesta dentro del código fuente.

---

### 🔄 Reboot App

Permite reiniciar la aplicación cuando se realizan cambios en el código o se requiere actualizar el servicio.

---

### 📜 Logs

Permite consultar errores, advertencias y mensajes generados durante la ejecución de la aplicación.

Esta funcionalidad es útil para identificar y corregir problemas.

---

## 📌 Flujo de actualización del sistema

Cuando se realizan cambios en el código, el proceso normal es:

GitHub
↓
Push de cambios
↓
Streamlit Cloud detecta la actualización
↓
Despliegue automático
↓
Aplicación actualizada

En algunos casos puede ser necesario realizar un **Reboot App** para reiniciar el servicio.

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