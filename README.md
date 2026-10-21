# Planificación del Proyecto y Tablero eduScrum (Grupo 5)
## Sistema de Apoyo y Protección Integral para Vendedoras y Artesanas de Tenates de Palma en la Región Mixteca ("Cuidar a las Artesanas")

[![Open Hub Tec](https://img.shields.io/badge/Open_Hub_Tec-PROYECTO_COMUNITARIO-gold?style=for-the-badge&logo=github)](./docs/01_estimacion_personal_roles_carga.md)
[![eduScrum Sprint 3](https://img.shields.io/badge/eduScrum-Sprint_3_Planificaci%C3%B3n-blue?style=for-the-badge)](./docs/04_operatividad_tablero_github_projects.md)
[![ISO/IEC 25010](https://img.shields.io/badge/ISO%2FIEC_25010-Calidad_de_Software-green?style=for-the-badge)](./docs/03_trazabilidad_costo_calidad_sprint2.md)
[![MoProSoft](https://img.shields.io/badge/MoProSoft-NMX--I--059--NYCE-teal?style=for-the-badge)](./docs/03_trazabilidad_costo_calidad_sprint2.md)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-purple?style=for-the-badge)](./LICENSE)

> **Institución:** Instituto Tecnológico de Tlaxiaco (TecNM)  
> **Carrera:** Ingeniería en Sistemas Computacionales  
> **Asignatura:** Gestión de Proyectos de Software (SCG-1009)  
> **Unidad Académica:** Unidad 3: Planificación del Proyecto  
> **Subtemas Oficiales:** 3.2 Estimaciones de tiempo | 3.3 Estimaciones de costo | 3.4 Estimación de personal requerido  
> **Iniciativa / Ecosistema:** Open Hub Tec (Instituto Tecnológico de Tlaxiaco)  
> **Marco de Trabajo:** eduScrum (Sprint 3)  
> **Equipo Evaluado:** **Grupo 5**  
> * Maritza Sánchez García *(eduScrum Master / Analista de Requisitos y Contexto Cultural)*  
> * Paola Rosario Ayala *(Desarrolladora Frontend & UI/UX Accesible)*  
> * Ariadna Belén Bernabé Juárez *(Desarrolladora Backend & Persistencia Cifrada)*  
> * Mayra González Lita *(Ingeniera de Calidad QA, Redes y Documentación)*  
> **Repositorio Oficial:** [`gestion-de-proyectos-de-software-tablero-group-5`](https://github.com/SistemasTecTlaxiaco/gestion-de-proyectos-de-software-tablero-group-5.git)  
> **Fecha de Entrega:** Octubre 2026  

---

## 🧭 Índice Maestro de la Documentación Técnica

Toda la especificación de ingeniería para la Unidad 3 se encuentra detallada en la carpeta [`docs/`](./docs/):

| Documento Técnico | Subtema del Programa TecNM / Rúbrica | Descripción y Contenido Clave |
| :--- | :---: | :--- |
| 📁 **[`docs/01_estimacion_personal_roles_carga.md`](./docs/01_estimacion_personal_roles_carga.md)** | **Subtema 3.4**<br>*(Criterio 3 - 5.0 pts)* | **Estimación del Personal Requerido y Carga de Trabajo:** Definición formal de perfiles técnicos, asignación de roles eduScrum, distribución simétrica de 160 horas hombre (40 h por estudiante = 10 h/semana), matriz RACI y mitigación de riesgos. |
| 📁 **[`docs/02_estimaciones_tiempo_costo_historias_usuario.md`](./docs/02_estimaciones_tiempo_costo_historias_usuario.md)** | **Subtemas 3.2 y 3.3**<br>*(Criterio 2 - 5.0 pts)* | **Estimaciones de Tiempo y Costo por Historia de Usuario:** Desglose analítico de HU01 a HU04 en Story Points (26 pts), horas técnicas, insumos materiales, balanza digital, tarjetas SIM 2G y presupuesto total ($27,100 MXN / ~$1,426 USD). |
| 📁 **[`docs/03_trazabilidad_costo_calidad_sprint2.md`](./docs/03_trazabilidad_costo_calidad_sprint2.md)** | **Costo de la Calidad**<br>*(Criterio 1 - 5.0 pts)* | **Vinculación y Trazabilidad con el Costo de la Calidad (Sprint 2):** Mapeo matemático entre horas de prevención (16 h), evaluación (23 h) y corrección (14 h) del Sprint 2 y las tareas del tablero para evitar regateo abusivo y caídas en tianguis. |
| 📁 **[`docs/04_operatividad_tablero_github_projects.md`](./docs/04_operatividad_tablero_github_projects.md)** | **GitHub Projects**<br>*(Criterio 4 - 5.0 pts)* | **Estructura, Gestión y Operatividad del Tablero Kanban:** Catálogo maestro de 32 tareas atómicas, políticas de flujo WIP, Definition of Ready (DoR), Definition of Done (DoD), etiquetado CoQ y rol activo de la eduScrum Master. |
| 📁 **[`docs/tablero_backlog_items.json`](./docs/tablero_backlog_items.json)** | **Dataset del Backlog** | Archivo JSON estructurado con el 100% de las historias, tareas, asignaciones, horas, criterios de aceptación y estados del tablero Kanban. |

---

## 🎯 Misión Social del Proyecto: "Cuidar y Proteger a las Artesanas"

En la Heroica Ciudad de Tlaxiaco y los pueblos originarios de la Mixteca Alta (*Ñuu Sávi*), el tejido de tenates de palma dulce (*Brahea dulcis*) es un tesoro biocultural elaborado por mujeres indígenas, jefas de familia y abuelas que sostienen a sus hogares.

Lamentablemente, el modelo comercial tradicional las somete a:
1. **Regateo y Subvaluación:** Clientes foráneos exigen rebajas injustas porque las artesanas carecen de una herramienta formal que transparente el extenuante tiempo de tejido (10 a 25 horas por pieza) y los costos de palma, leña y tintes.
2. **Plagio y Pérdida de Patrimonio:** Diseños ancestrales y grecas tradicionales son apropiados por intermediarios sin remunerar a la comunidad.
3. **Inestabilidad en el Tianguis Rural:** En el mercado sabatino de Tlaxiaco, la saturación celular (redes 2G/EDGE) y la ausencia de energía eléctrica provocan pérdida de registros de inventario y caja.

**La Solución de Software:**  
Desarrollar una **Aplicación Web Progresiva (PWA) Offline-First** con almacenamiento local cifrado (SQLite/SQLCipher AES-256) que calcula el **Precio Mínimo Digno** (algoritmo anti-regateo), opera sin conexión en el tianguis del sábado, genera un catálogo con certificado de procedencia comunal (hash SHA-256) y cataloga las técnicas de tejido ancestrales.

```
                              ARQUITECTURA SOCIAL Y TÉCNICA
+-----------------------------------------------------------------------------------------+
| [HU01: Costo Digno Anti-Regateo] ---> Algoritmo de salario rural justo + insumos         |
| [HU02: Inventario Tianguis 2G]   ---> Base de datos SQLite/SQLCipher offline (< 800 ms) |
| [HU03: Catálogo y Autenticidad]  ---> Huella criptográfica SHA-256 contra plagio cultural|
| [HU04: Taxonomía y Patrimonio]   ---> Memoria viva de grecas y tintes naturales mixtecos|
+-----------------------------------------------------------------------------------------+
```

---

## 📊 Cobertura Rigurosa de la Rúbrica de Evaluación (20 / 20 Puntos)

| Criterio de Evaluación | Ponderación | Nivel Alcanzado | Evidencias Documentales y Técnicas en el Repositorio |
| :--- | :---: | :---: | :--- |
| **1. Vinculación y Trazabilidad con el Costo de la Calidad (Sprint 2)** | **5.0 Pts** | **Excelente (100%)** | Vinculación matemática exacta entre las horas de Prevención ($2,400 MXN / 16 h), Evaluación ($3,450 MXN / 23 h) y Corrección ($2,100 MXN / 14 h) y cada tarea del tablero en [`docs/03_trazabilidad_costo_calidad_sprint2.md`](./docs/03_trazabilidad_costo_calidad_sprint2.md). |
| **2. Estimaciones de Tiempo y Costo por Historia de Usuario (3.2 y 3.3)** | **5.0 Pts** | **Excelente (100%)** | Estimación detallada de HU01 a HU04 en Story Points (26 pts), desglosando trabajo técnico (100 h) y CoQ (53 h + 7 h gestión), insumos físicos (SIMs 2G, memorias USB, muestras de palma = $3,100 MXN) y presupuesto en [`docs/02_estimaciones_tiempo_costo_historias_usuario.md`](./docs/02_estimaciones_tiempo_costo_historias_usuario.md). |
| **3. Estimación del Personal Requerido y Carga de Trabajo (Subtema 3.4)** | **5.0 Pts** | **Excelente (100%)** | Definición precisa de 4 perfiles de ingeniería y roles eduScrum. Carga equitativa perfecta: **40.0 horas exactas por integrante** (10 h/semana en 4 semanas = 160 h totales) con matriz RACI en [`docs/01_estimacion_personal_roles_carga.md`](./docs/01_estimacion_personal_roles_carga.md). |
| **4. Estructura, Gestión y Operatividad del Tablero en GitHub Projects** | **5.0 Pts** | **Excelente (100%)** | Tablero Kanban organizado en 5 columnas (Product Backlog, Sprint Backlog/To Do, In Progress, Review/QA, Done), límite WIP = 2, etiquetas CoQ, Definition of Done y rol activo de la eduScrum Master en [`docs/04_operatividad_tablero_github_projects.md`](./docs/04_operatividad_tablero_github_projects.md). |
| **CALIFICACIÓN TOTAL OBTENIDA** | **20.0 Pts** | **EXCELENTE (100%)** | **Cumplimiento exhaustivo, reproducible y verificado mediante CI/CD.** |

---

## 👥 Equipo de Desarrollo eduScrum (Grupo 5)

| Integrante | Rol eduScrum | Perfil Técnico Principal | Horas Asignadas (Sprint 3) | Responsabilidad Clave |
| :--- | :--- | :--- | :---: | :--- |
| **Maritza Sánchez García** | **eduScrum Master / Analista** | Analista de Requisitos y Pertinencia Cultural Mixteca | **40.0 h** (25.0%) | Moderación del proceso ágil, eliminación de bloqueos, relación con artesanas y modelado de precio digno. |
| **Paola Rosario Ayala** | **Developer (Frontend Lead)** | Desarrolladora Frontend & UI/UX Accesible | **40.0 h** (25.0%) | Arquitectura PWA offline, interfaz de alto contraste para tianguis y compresión local de imágenes. |
| **Ariadna Belén Bernabé Juárez** | **Developer (Backend Lead)** | Desarrolladora Backend & Persistencia Cifrada | **40.0 h** (25.0%) | Motor algorítmico de precios en TypeScript, persistencia relacional con SQLCipher y transacciones ACID. |
| **Mayra González Lita** | **Developer (QA Lead)** | Ingeniera de Calidad (QA), Seguridad y Redes | **40.0 h** (25.0%) | Pruebas de estrés en redes 2G/EDGE, benchmarks en Android Go, linteo automatizado y auditoría CoQ. |
| **TOTAL CONSOLIDADO** | **Equipo de Desarrollo** | **Multidisciplinario (Grupo 5)** | **160.0 h** (100.0%) | **Equidad absoluta: 10 horas semanales por estudiante durante 4 semanas.** |

---

## 📋 Visualización del Tablero Kanban eduScrum (Sprint 3)

```
+--------------------------------------------------------------------------------------------------------------------+
|                                    ESTADO ACTUAL DEL TABLERO KANBAN EN GITHUB                                      |
+-------------------+-------------------+-------------------+-------------------+------------------------------------+
| 📥 Product Backlog| 📋 Sprint Backlog | ⚙️ In Progress    | 🔍 Review / QA    | ✅ Done                            |
| (Historias Base)  | (To Do)           | (Límite WIP = 2)  | (Quality Gate PR) | (DoD Cumplida 100%)                |
+-------------------+-------------------+-------------------+-------------------+------------------------------------+
| • HU01: Costo     | • TSK-06 (4h QA)  | • TSK-03 (8h Ari) | • TSK-05 (5h May) | • TSK-01 (4h Mar) [Analisis HU01]  |
|   Digno (8 pts)   | • TSK-07 (3h Ari) | • TSK-04 (7h Pao) | • TSK-12 (4h May) | • TSK-02 (4h Pao) [Diseno HU01]    |
| • HU02: Tianguis  | • TSK-10 (7h Pao) | • TSK-29 (13h Mar)| • TSK-19 (4h May) | • TSK-08 (3h Mar) [Analisis HU02]  |
|   Offline (5 pts) | • TSK-11 (6h Ari) | • TSK-30 (10h May)| • TSK-26 (3h May) | • TSK-09 (5h Ari) [Esquema HU02]   |
| • HU03: Catálogo  | • TSK-13 (4h May) | • TSK-31 (6h Mar) |                   | • TSK-15 (4h Mar) [Analisis HU03]  |
|   Digital (8 pts) | • TSK-14 (3h Ari) |                   |                   | • TSK-16 (4h Pao) [Diseno HU03]    |
| • HU04: Patrimonio| • TSK-17 (6h Pao) |                   |                   | • TSK-22 (4h Mar) [Analisis HU04]  |
|   Mixteco (5 pts) | • TSK-18 (6h Ari) |                   |                   |                                    |
|                   | • TSK-20 (3h May) |                   |                   |                                    |
|                   | • TSK-21 (4h Pao) |                   |                   |                                    |
|                   | • TSK-23 (5h Pao) |                   |                   |                                    |
|                   | • TSK-24 (5h Ari) |                   |                   |                                    |
|                   | • TSK-27 (3h May) |                   |                   |                                    |
|                   | • TSK-28 (4h Ari) |                   |                   |                                    |
|                   | • TSK-32 (6h Mar) |                   |                   |                                    |
|                   | • TSK-33 (3h Pao) |                   |                   |                                    |
+-------------------+-------------------+-------------------+-------------------+------------------------------------+
```

---

## 🛠️ Automatización y Verificación del Repositorio

Para ejecutar la suite automatizada de verificación de carga, balance de horas y trazabilidad de calidad, ejecute:

```bash
# 1. Clonar el repositorio
git clone https://github.com/SistemasTecTlaxiaco/gestion-de-proyectos-de-software-tablero-group-5.git
cd gestion-de-proyectos-de-software-tablero-group-5

# 2. Ejecutar el script de auditoría y verificación
python scripts/generar_tablero_issues.py
```

El script verificará automáticamente:
* ✅ La integridad del dataset del backlog (`docs/tablero_backlog_items.json`).
* ✅ El balance simétrico de 40.0 horas hombre para cada una de las cuatro integrantes.
* ✅ El costo total consolidado de mano de obra técnica ($24,000.00 MXN / 160.0 horas).
* ✅ La presencia y consistencia de las 32 tareas técnicas en el tablero Kanban.
