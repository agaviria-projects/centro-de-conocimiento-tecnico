# Documentación Técnica  
# Generador de Informes ANS - ATC CHEC

## Información del documento

| Campo | Descripción |
|---|---|
| Proyecto | Generador de Informes ANS - ATC CHEC |
| Tipo de documento | Documentación técnica |
| Dirigido a | Área de Tecnología de la Información |
| Tecnología principal | Python |
| Interfaz | Aplicación de escritorio |
| Estado | En desarrollo |
| Versión | 1.0 |

---

## Contenido

1. Introducción técnica  
2. Objetivo del sistema  
3. Alcance actual  
4. Arquitectura general  
5. Separación de responsabilidades  
6. Flujo de ejecución  
7. Estructura de carpetas  
8. Módulos Python  
9. Archivos de configuración  
10. Archivos de entrada y salida  
11. Reglas de negocio  
12. Generación del informe Excel  
13. Actualización del Dashboard  
14. Geocodificación y mapas  
15. Manejo de errores y registros  
16. Dependencias  
17. Ejecución del sistema  
18. Puntos de extensión  
19. Desarrollo futuro de ANS Redes  
20. Recomendaciones de mantenimiento  
21. Riesgos técnicos  
22. Checklist de entrega  


---

## 1. Introducción técnica

El proyecto **Generador de Informes ANS - ATC CHEC** es una aplicación desarrollada en Python para automatizar el procesamiento, cálculo y presentación de información relacionada con los Acuerdos de Nivel de Servicio —ANS—.

El sistema toma archivos operativos, valida su estructura, transforma la información, calcula los estados ANS y genera los siguientes resultados:

- Informe consolidado en Excel.
- Actualización del Dashboard.
- Archivo para análisis geográfico.
- Mapa de pedidos según su dirección.

El desarrollo utiliza una arquitectura modular. Cada archivo Python tiene una responsabilidad específica, lo que facilita su mantenimiento, corrección y evolución.

### Resumen de la arquitectura

```text
Archivo de entrada
       │
       ▼
Validación de información
       │
       ▼
Transformación de datos
       │
       ▼
Cálculo de ANS
       │
       ▼
Generación de resultados
       │
       ├── Informe Excel
       ├── Dashboard
       └── Mapa ANS

       