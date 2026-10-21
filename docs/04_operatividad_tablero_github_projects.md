# ESTRUCTURA, GESTIÓN Y OPERATIVIDAD DEL TABLERO EN GITHUB PROJECTS

> **Asignatura:** Gestión de Proyectos de Software (SCG-1009)  
> **Unidad Académica:** Unidad 3. Planificación del Proyecto  
> **Criterio Evaluado:** Criterio 4 de la Rúbrica (Estructura, Gestión y Operatividad del Tablero en GitHub Projects - Valor: 5.0 pts)  
> **Iniciativa / Ecosistema:** Open Hub Tec (Instituto Tecnológico de Tlaxiaco)  
> **Marco de Trabajo:** eduScrum (Sprint 3)  
> **Proyecto Oficial:** *Sistema de Apoyo y Protección Integral para Vendedoras y Artesanas de Tenates de Palma en la Región Mixteca ("Cuidar y Proteger a las Artesanas")*  
> **Equipo de Desarrollo (Grupo 5):** Maritza Sánchez García, Paola Rosario Ayala, Ariadna Belén Bernabé Juárez y Mayra González Lita.  
> **URL del Repositorio:** [`gestion-de-proyectos-de-software-tablero-group-5`](https://github.com/SistemasTecTlaxiaco/gestion-de-proyectos-de-software-tablero-group-5.git)  
> **Fecha:** Octubre 2026  

---

## 🧭 Índice del Documento

1. [Configuración y Flujo de Columnas del Tablero Kanban](#1-configuración-y-flujo-de-columnas-del-tablero-kanban)
2. [Sistema de Taxonomía y Convención de Etiquetas (Labels)](#2-sistema-de-taxonomía-y-convención-de-etiquetas-labels)
3. [Criterios de Entrada y Salida: Definition of Ready (DoR) y Definition of Done (DoD)](#3-criterios-de-entrada-y-salida-definition-of-ready-dor-y-definition-of-done-dod)
4. [Catálogo Maestro de Tareas del Sprint 3 (Mapeo Completo de 160 Horas)](#4-catálogo-maestro-de-tareas-del-sprint-3-mapeo-completo-de-160-horas)
5. [Protocolo de Gestión Activa por la eduScrum Master](#5-protocolo-de-gestión-activa-por-la-eduscrum-master)
6. [Integración con GitHub Actions y Automatización del Flujo](#6-integración-con-github-actions-y-automatización-del-flujo)

---

## 1. Configuración y Flujo de Columnas del Tablero Kanban

El tablero de planificación del proyecto se implementa en **GitHub Projects (Projects v2)**, configurado como un tablero Kanban adaptado a la pedagogía de **eduScrum**, estructurado en cinco columnas de flujo continuo:

```
+--------------------------------------------------------------------------------------------------------------------+
|                                    TABLERO KANBAN EDUSCRUM - SPRINT 3 (GRUPO 5)                                    |
+-------------------+-------------------+-------------------+-------------------+------------------------------------+
| 📥 Product Backlog| 📋 Sprint Backlog | ⚙️ In Progress    | 🔍 Review / QA    | ✅ Done                            |
|                   | (To Do)           |                   |                   |                                    |
| • HU01 (8 pts)    | • Tareas listas   | • En desarrollo   | • Revisión de PRs | • DoD cumplida 100%                |
| • HU02 (5 pts)    | • Horas asignadas | • Límite WIP = 2  | • Linteo en CI    | • Criterios CA validados           |
| • HU03 (8 pts)    | • Responsable     |   por integrante  | • Pruebas 2G en   | • Evidencias en doc                |
| • HU04 (5 pts)    | • Tag de CoQ      | • Daily Standup   |   Android Go      | • Aprobado por eduScrum Master     |
+-------------------+-------------------+-------------------+-------------------+------------------------------------+
```

### Descripción de Columnas y Reglas de Flujo:
1. **📥 `Product Backlog`:** Contiene las Historias de Usuario macro priorizadas por su valor social de protección a las artesanas (HU01 a HU04), debidamente estimadas en Puntos de Historia (26 pts base) y vinculadas a sus Criterios de Aceptación (CA-1.1 al CA-4.4).
2. **📋 `Sprint Backlog / To Do`:** Aloja las tareas atómicas de ingeniería (desarrollo, análisis, pruebas y corrección) programadas para ejecutarse en el Sprint 3. Cada tarjeta indica la integrante responsable, las horas estimadas y el tipo de actividad.
3. **⚙️ `In Progress`:** Tareas en ejecución activa. **Política WIP (Work In Progress):** Ninguna integrante puede tener más de **2 tareas activas simultáneamente** para prevenir la sobrecarga y los cuellos de botella.
4. **🔍 `Review / Quality Assurance`:** Tareas cuyo código o entregable ha sido subido a GitHub mediante un *Pull Request*. En esta fase, **Mayra González Lita (QA Lead)** ejecuta la batería de pruebas en dispositivos Android Go simulando condiciones de tianguis rural y verifica el pipeline automatizado en GitHub Actions.
5. **✅ `Done`:** Tareas formalmente terminadas que cumplen al 100% con la *Definition of Done* (DoD) y han sido validadas por la **eduScrum Master (Maritza Sánchez García)**.

---

## 2. Sistema de Taxonomía y Convención de Etiquetas (Labels)

Para mantener una trazabilidad visual inmediata, cada tarjeta e issue en GitHub Projects utiliza un esquema estandarizado de etiquetas:

| Categoría | Nombre de la Etiqueta | Color Hex | Propósito en el Tablero |
| :--- | :--- | :---: | :--- |
| **Iteración** | `sprint-3` | `#0E8A16` (Verde) | Identifica las tareas correspondientes a la Unidad 3 de Planificación. |
| **Historias de Usuario** | `HU-01:precio-digno`<br>`HU-02:tianguis-offline`<br>`HU-03:catalogo-autenticidad`<br>`HU-04:caracteristicas-patrimonio` | `#1D76DB`<br>`#5319E7`<br>`#0052CC`<br>`#006B75` | Vinculación directa con las funcionalidades prioritarias para cuidar a las artesanas. |
| **Costo de Calidad (CoQ)** | `tipo:prevencion-coq`<br>`tipo:evaluacion-coq`<br>`tipo:correccion-coq` | `#FBCA04` (Oro)<br>`#D93F0B` (Naranja)<br>`#B60205` (Rojo) | Trazabilidad exacta con los hallazgos del Sprint 2 (horas de prevención, pruebas y corrección). |
| **Tipo de Trabajo** | `tipo:analisis`<br>`tipo:diseno-ui`<br>`tipo:desarrollo-frontend`<br>`tipo:desarrollo-backend`<br>`tipo:documentacion` | `#C2E0C6`<br>`#BFD4F2`<br>`#D4C5F9`<br>`#E99695`<br>`#CCCCCC` | Clasificación funcional de la disciplina técnica requerida. |
| **Perfiles / Asignación** | `perfil:analista-eduscrum`<br>`perfil:frontend-ui`<br>`perfil:backend-datos`<br>`perfil:qa-seguridad` | `#000000` (Negro) | Perfil técnico responsable de la ejecución según la estimación 3.4. |
| **Prioridad** | `prioridad:alta`<br>`prioridad:critica` | `#E11D48`<br>`#990000` | Urgencia operativa en el marco del sprint eduScrum. |

---

## 3. Criterios de Entrada y Salida: Definition of Ready (DoR) y Definition of Done (DoD)

### Definition of Ready (DoR) — Criterio para entrar a *To Do*:
Una tarea sólo puede ser colocada en el *Sprint Backlog* si cumple con:
* [x] Historia de usuario asociada claramente identificada (HU01 a HU04).
* [x] Criterios de aceptación (CA) redactados sin ambigüedades.
* [x] Estimación precisa en horas hombre (entre 2 y 10 horas por tarea).
* [x] Integrante asignada con perfil técnico compatible.
* [x] Etiqueta de clasificación de actividad y Costo de la Calidad (CoQ).

### Definition of Done (DoD) — Criterio para pasar a *Done*:
Una tarea sólo puede considerarse terminada cuando:
* [x] El código fuente o entregable está subido a la rama principal mediante *Pull Request*.
* [x] El pipeline automatizado de CI (`ci_calidad.yml`) pasa con **cero advertencias** (`eslint --max-warnings=0`).
* [x] Se ejecutaron las pruebas en hardware modesto (Android Go) y se verificó latencia < 1.0 s.
* [x] La tarea fue revisada y aprobada por una compañera de equipo (*Peer Review*) y por la QA Lead.
* [x] La documentación técnica y bitácora del entregable está actualizada en la carpeta `docs/`.
* [x] La eduScrum Master valida el cierre en la reunión de sincronización.

---

## 4. Catálogo Maestro de Tareas del Sprint 3 (Mapeo Completo de 160 Horas)

A continuación se detalla la totalidad de las **24 tareas atómicas de ingeniería** que conforman el tablero del Sprint 3, totalizando exactamente **160.0 horas de trabajo**:

| ID Tarea | Título de la Tarea en el Tablero | Historia | Responsable Asignada | Perfil Técnico | Horas | Clasificación CoQ / Tipo | Columna Tablero | Criterios CA |
| :---: | :--- | :---: | :--- | :--- | :---: | :--- | :---: | :--- |
| `TSK-01` | Modelado de formula de Precio Minimo Digno con artesanas | HU01 | Maritza Sanchez Garcia | Analista / eduScrum | 4.0 h | `tipo:analisis` | **Done** | CA-1.1, CA-1.3 |
| `TSK-08` | Especificacion de flujo de venta rapida en tianguis de Tlaxiaco | HU02 | Maritza Sanchez Garcia | Analista / eduScrum | 3.0 h | `tipo:analisis` | **Done** | CA-2.1, CA-2.2 |
| `TSK-15` | Glosario artesanal y taxonomia bilingue en Tu'un Savi | HU03 | Maritza Sanchez Garcia | Analista / eduScrum | 4.0 h | `tipo:analisis` | **Done** | CA-3.3, CA-3.4 |
| `TSK-22` | Levantamiento de catalogo de tecnicas tradicionales de tejido | HU04 | Maritza Sanchez Garcia | Analista / eduScrum | 4.0 h | `tipo:analisis` | **Done** | CA-4.1, CA-4.2 |
| `TSK-29` | Facilitacion eduScrum, Daily Standups y control del grafico Burndown | Transversal | Maritza Sanchez Garcia | Analista / eduScrum | 13.0 h | `tipo:documentacion` | **In Progress** | Transversal |
| `TSK-31` | Validacion de reglas de negocio y precios minimos con comites de artesanas | HU01 | Maritza Sanchez Garcia | Analista / eduScrum | 6.0 h | `tipo:desarrollo` | **In Progress** | CA-1.3, CA-1.4 |
| `TSK-32` | Pruebas de aceptacion de usuario con vendedoras en el tianguis | HU02 | Maritza Sanchez Garcia | Analista / eduScrum | 6.0 h | `tipo:evaluacion-coq` | **Sprint Backlog (To Do)** | CA-2.2, CA-2.3 |
| `TSK-02` | Diseno UI de fases de tejido e insumos en alto contraste | HU01 | Paola Rosario Ayala | Frontend / UI | 4.0 h | `tipo:diseno-ui` | **Done** | CA-1.1, CA-1.4 |
| `TSK-04` | Implementacion de componentes interactivos y calculo reactivo HU01 | HU01 | Paola Rosario Ayala | Frontend / UI | 7.0 h | `tipo:desarrollo-frontend` | **In Progress** | CA-1.1, CA-1.4 |
| `TSK-10` | Vistas PWA de punto de venta rapido (cobro en dos toques) | HU02 | Paola Rosario Ayala | Frontend / UI | 7.0 h | `tipo:desarrollo-frontend` | **Sprint Backlog (To Do)** | CA-2.2, CA-2.3 |
| `TSK-16` | Diseno de tarjetas de catalogo y fichas de autenticidad cultural | HU03 | Paola Rosario Ayala | Frontend / UI | 4.0 h | `tipo:diseno-ui` | **Done** | CA-3.3, CA-3.4 |
| `TSK-17` | Modulo de compresion local de fotos en Web Workers (< 150 KB WebP) | HU03 | Paola Rosario Ayala | Frontend / UI | 6.0 h | `tipo:desarrollo-frontend` | **Sprint Backlog (To Do)** | CA-3.1, CA-3.4 |
| `TSK-21` | Depuracion de fugas de memoria al procesar rafagas de fotos | HU03 | Paola Rosario Ayala | Frontend / UI | 4.0 h | `tipo:correccion-coq` | **Sprint Backlog (To Do)** | CA-3.1, CA-3.3 |
| `TSK-23` | Formulario accesible de captura tecnica con selectores visuales | HU04 | Paola Rosario Ayala | Frontend / UI | 5.0 h | `tipo:desarrollo-frontend` | **Sprint Backlog (To Do)** | CA-4.1, CA-4.3 |
| `TSK-33` | Pruebas visuales de contraste bajo luz solar en el tianguis | HU04 | Paola Rosario Ayala | Frontend / UI | 3.0 h | `tipo:evaluacion-coq` | **Sprint Backlog (To Do)** | CA-4.3, CA-4.4 |
| `TSK-03` | Programacion del motor de costeo en TypeScript y persistencia | HU01 | Ariadna Belen Bernabe Juarez | Backend / Datos | 8.0 h | `tipo:desarrollo-backend` | **In Progress** | CA-1.2, CA-1.3 |
| `TSK-07` | Depuracion y correccion de bugs numericos en calculo de materias primas | HU01 | Ariadna Belen Bernabe Juarez | Backend / Datos | 3.0 h | `tipo:correccion-coq` | **Sprint Backlog (To Do)** | CA-1.3, CA-1.4 |
| `TSK-09` | Estructuracion de esquemas e indices B-Tree en SQLite local cifrado | HU02 | Ariadna Belen Bernabe Juarez | Backend / Datos | 5.0 h | `tipo:desarrollo-backend` | **Done** | CA-2.1, CA-2.4 |
| `TSK-11` | Manejo transaccional ACID en cliente con SQLCipher AES-256 | HU02 | Ariadna Belen Bernabe Juarez | Backend / Datos | 6.0 h | `tipo:desarrollo-backend` | **Sprint Backlog (To Do)** | CA-2.1, CA-2.4 |
| `TSK-14` | Optimizacion de consultas SQLite para terminales Android Go | HU02 | Ariadna Belen Bernabe Juarez | Backend / Datos | 3.0 h | `tipo:correccion-coq` | **Sprint Backlog (To Do)** | CA-2.1, CA-2.4 |
| `TSK-18` | Generacion de huellas criptograficas SHA-256 y renderizado de QR | HU03 | Ariadna Belen Bernabe Juarez | Backend / Datos | 6.0 h | `tipo:desarrollo-backend` | **Sprint Backlog (To Do)** | CA-3.2, CA-3.4 |
| `TSK-24` | Persistencia e indexacion de taxonomia de grecas y tintes naturales | HU04 | Ariadna Belen Bernabe Juarez | Backend / Datos | 5.0 h | `tipo:desarrollo-backend` | **Sprint Backlog (To Do)** | CA-4.2, CA-4.4 |
| `TSK-28` | Correccion de errores en filtros cruzados de tintes y medidas | HU04 | Ariadna Belen Bernabe Juarez | Backend / Datos | 4.0 h | `tipo:correccion-coq` | **Sprint Backlog (To Do)** | CA-4.3, CA-4.4 |
| `TSK-05` | Pruebas de propiedades matematicas de precios minimos (Invariantes) | HU01 | Mayra Gonzalez Lita | QA / Seguridad | 5.0 h | `tipo:prevencion-coq` | **Review / QA** | CA-1.3, CA-1.4 |
| `TSK-06` | Calibracion y verificacion empirica de pesaje de manojos de palma | HU01 | Mayra Gonzalez Lita | QA / Seguridad | 4.0 h | `tipo:evaluacion-coq` | **Sprint Backlog (To Do)** | CA-1.2, CA-1.3 |
| `TSK-12` | Tipado estatico estricto y validacion de esquemas de inventario | HU02 | Mayra Gonzalez Lita | QA / Seguridad | 4.0 h | `tipo:prevencion-coq` | **Review / QA** | CA-2.1, CA-2.4 |
| `TSK-13` | Simulacion de 500 ventas consecutivas desconectadas en tianguis | HU02 | Mayra Gonzalez Lita | QA / Seguridad | 4.0 h | `tipo:evaluacion-coq` | **Sprint Backlog (To Do)** | CA-2.1, CA-2.2 |
| `TSK-19` | Auditoria de compresion sin degradacion visual en tejidos de palma | HU03 | Mayra Gonzalez Lita | QA / Seguridad | 4.0 h | `tipo:prevencion-coq` | **Review / QA** | CA-3.1, CA-3.2 |
| `TSK-20` | Pruebas de verificacion de hashes y lectura QR bajo luz solar | HU03 | Mayra Gonzalez Lita | QA / Seguridad | 3.0 h | `tipo:evaluacion-coq` | **Sprint Backlog (To Do)** | CA-3.2, CA-3.4 |
| `TSK-26` | Validacion de integridad referencial de grecas ancestrales | HU04 | Mayra Gonzalez Lita | QA / Seguridad | 3.0 h | `tipo:prevencion-coq` | **Review / QA** | CA-4.1, CA-4.2 |
| `TSK-27` | Benchmarks de latencia de busqueda en hardware Android Go real | HU04 | Mayra Gonzalez Lita | QA / Seguridad | 3.0 h | `tipo:evaluacion-coq` | **Sprint Backlog (To Do)** | CA-4.4 |
| `TSK-30` | Documentacion tecnica integral, bitacora de calidad y reporte de Sprint 3 | Transversal | Mayra Gonzalez Lita | QA / Seguridad | 10.0 h | `tipo:documentacion` | **In Progress** | Transversal |
| **TOTAL** | **Consolidación General de Tareas Sprint 3** | **-** | **4 Integrantes** | **Grupo 5** | **160.0 h** | **100% Carga Cubierta** | **4 Columnas** | **CA-1.1 a CA-4.4** |

---

## 5. Protocolo de Gestión Activa por la eduScrum Master

La gestión ágil del tablero es facilitada proactivamente por **Maritza Sánchez García (eduScrum Master)**, implementando los siguientes mecanismos de control:

1. **Cadencia de Ceremonias Ágiles:**
   * **Sprint Planning (Semana 1):** Desglose colegiado de historias en tareas, verificación de la DoR y asignación equilibrada de horas.
   * **Daily Standup (Lunes, Miércoles y Viernes - 15 min):** Inspección de tarjetas en movimiento, detección temprana de impedimentos técnicos y reasignación de apoyo si una tarea excede su tiempo previsto.
   * **Sprint Review (Fin de Semana 4):** Demostración interactiva de las cuatro funcionalidades a un comité de prueba con artesanas en Tlaxiaco.
   * **Retrospective (Cierre):** Evaluación del bienestar del equipo, análisis de la precisión de las estimaciones y compromisos de mejora.
2. **Registro de Impedimentos (*Impediment Log*):**
   * *Impedimento 1:* Fallo de renderizado en versión antigua de Chrome en terminal Android Go $\rightarrow$ *Acción:* Paola Rosario implementó polyfills ligeros y Tailwind estándar.
   * *Impedimento 2:* Intermitencia eléctrica en laboratorio del Tec $\rightarrow$ *Acción:* Respaldo local de commits y uso de SQLite offline.
3. **Monitoreo del Gráfico Burndown:** Se actualizan las horas restantes de esfuerzo tras cada sesión de trabajo, garantizando que la línea real de avance converja con la línea ideal hacia la hora cero al concluir las 4 semanas.

---

## 6. Integración con GitHub Actions y Automatización del Flujo

El repositorio cuenta con un pipeline de Integración Continua (`.github/workflows/ci_calidad.yml`) que actúa como guardián automatizado del tablero:
* Cada vez que se crea un *Pull Request* referenciando una tarea (ej. `Closes #12`), el workflow ejecuta automáticamente:
  1. Chequeo de sintaxis y tipos (`tsc --noEmit`).
  2. Linteo estricto (`eslint --max-warnings=0`).
  3. Ejecución de pruebas unitarias de cálculo de precios y transacciones offline.
* Si el workflow falla, GitHub bloquea el botón de *Merge*, impidiendo que la tarjeta avance a la columna **Done** hasta que se resuelva la incidencia. Esto garantiza que la calidad se mantenga en el nivel de excelencia exigido por el Instituto Tecnológico de Tlaxiaco.
