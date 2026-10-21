# ESTIMACIÓN DEL PERSONAL REQUERIDO PARA EL PROYECTO (SUBTEMA 3.4)

> **Asignatura:** Gestión de Proyectos de Software (SCG-1009)  
> **Unidad Académica:** Unidad 3. Planificación del Proyecto  
> **Subtema Evaluado:** 3.4 Estimación de personal requerido y carga de trabajo  
> **Iniciativa / Ecosistema:** Open Hub Tec (Instituto Tecnológico de Tlaxiaco)  
> **Marco de Trabajo:** eduScrum (Sprint 3)  
> **Proyecto Oficial:** *Sistema de Apoyo y Protección Integral para Vendedoras y Artesanas de Tenates de Palma en la Región Mixteca ("Cuidar y Dignificar a las Artesanas")*  
> **Lugar de Aplicación:** Heroica Ciudad de Tlaxiaco, Oaxaca  
> **Equipo de Desarrollo:**  
> * Jazlynn Barrios Velasco  
> * Isaías Brayan López Domínguez
> * Alex Antonio Victoria Vazquez 
> * Mayra González Lita  
> **Repositorio Oficial:** [`gestion-de-proyectos-de-software-tablero-group-5`](https://github.com/SistemasTecTlaxiaco/gestion-de-proyectos-de-software-tablero-group-5.git)  
> **Fecha:** Octubre 2026  

---

## 🧭 Índice del Documento

1. [Introducción y Justificación Social](#1-introducción-y-justificación-social)
2. [Objetivo de la Estimación](#2-objetivo-de-la-estimación)
3. [Descripción del Proyecto y Enfoque de Protección al Artesano](#3-descripción-del-proyecto-y-enfoque-de-protección-al-artesano)
4. [Perfiles Profesionales y Roles eduScrum](#4-perfiles-profesionales-y-roles-eduscrum)
5. [Estimación de la Carga de Trabajo Total (160 Horas)](#5-estimación-de-la-carga-de-trabajo-total-160-horas)
6. [Distribución Equitativa de Horas por Integrante y Perfil](#6-distribución-equitativa-de-horas-por-integrante-y-perfil)
7. [Relación entre Historias de Usuario, Actividades Técnicas y Matriz RACI](#7-relación-entre-historias-de-usuario-actividades-técnicas-y-matriz-raci)
8. [Organización y Operatividad del Equipo mediante eduScrum](#8-organización-y-operatividad-del-equipo-mediante-eduscrum)
9. [Evaluación de Capacidad, Factores Humanos y Mitigación de Riesgos](#9-evaluación-de-capacidad-factores-humanos-y-mitigación-de-riesgos)
10. [Conclusiones y Dictamen de Asignación](#10-conclusiones-y-dictamen-de-asignación)

---

## 1. Introducción y Justificación Social

La estimación del personal requerido es una piedra angular en la planificación de proyectos de software bajo el estándar **TecNM** y el marco de trabajo ágil **eduScrum**. Permite determinar con precisión científica y realismo operativo los perfiles de ingeniería, los roles colaborativos y la cantidad de esfuerzo humano indispensable para transformar los requisitos de los usuarios en un producto de software robusto, mantenible y socialmente transformador.

En el contexto de la **Heroica Ciudad de Tlaxiaco y la Región de la Mixteca Alta oaxaqueña**, el tejido de tenates, petates y artesanías de palma dulce (*Brahea dulcis*) es una manifestación cultural viva heredada de la civilización mixteca (*Ñuu Sávi*), practicada predominantemente por mujeres indígenas y personas adultas mayores en comunidades como Santa María Cuquila, San Esteban Atatlahuca, San Mateo Peñasco y los barrios tradicionales de Tlaxiaco.

Sin embargo, las artesanas enfrentan tres condiciones de vulnerabilidad extrema:
1. **El regateo sistemático (*depreciación forzada del trabajo*):** Compradores foráneos e intermediarios (*coyotes*) fuerzan precios irrisorios, debido a que las artesanas no cuentan con un mecanismo formal para registrar las extenuantes horas de tejido (frecuentemente entre 8 y 25 horas por pieza) ni los costos de recolección, blanqueado y teñido de la fibra.
2. **Plagio y apropiación indebida de patrones:** Distribuidores comerciales replican diseños ancestrales sin retribuir a las comunidades originarias.
3. **Brecha digital y desconexión en tianguis rurales:** En el tradicional tianguis de los sábados en Tlaxiaco, la saturación celular (redes 2G/EDGE) y la falta de terminales bancarias causan descontrol en inventarios y pérdidas económicas.

Por ello, el proyecto trasciende el concepto de un simple punto de venta: se concibe como una **herramienta tecnológica de protección, cuidado integral y soberanía comunitaria para las artesanas**. Para lograr este propósito en el marco del **Sprint 3 (Unidad 3: Planificación)**, se requiere dimensionar minuciosamente el personal que asumirá el análisis de requisitos con pertinencia cultural, la arquitectura de software *offline-first*, la implementación técnica, el aseguramiento de la calidad basado en los hallazgos del Sprint 2 (Costo de la Calidad) y la documentación de ingeniería.

---

## 2. Objetivo de la Estimación

Estimar con rigurosidad matemática y metodológica el personal técnico requerido para diseñar, implementar, probar y documentar el **Sistema de Apoyo y Protección Integral para Vendedoras y Artesanas de Tenates de Palma**, especificando:
* Los perfiles profesionales de ingeniería y los roles ágiles bajo **eduScrum**.
* La asignación equitativa y balanceada de la carga de trabajo entre las **cuatro integrantes del Grupo 5** (Maritza Sánchez García, Paola Rosario Ayala, Ariadna Belén Bernabé Juárez y Mayra González Lita).
* La distribución temporal de **160 horas hombre** en un ciclo operativo de 4 semanas de Sprint académico (10 horas semanales por integrante), garantizando compatibilidad con la carga curricular del semestre agosto-diciembre 2026.
* La cobertura integral de las **cuatro Historias de Usuario principales (HU01 a HU04)**, garantizando que el 100% de los criterios de aceptación y las horas de aseguramiento de calidad (Prevención y Corrección) queden debidamente respaldadas por responsables directos.

---

## 3. Descripción del Proyecto y Enfoque de Protección al Artesano

El sistema es una **Aplicación Web Progresiva (PWA) Offline-First**, concebida para operar en teléfonos móviles de gama de entrada (frecuentemente **Android Go** con memoria RAM entre 2 GB y 3 GB) y computadoras comunitarias, capaz de funcionar de manera fluida en el tianguis sabatino de Tlaxiaco sin necesidad de conexión activa a Internet.

```
+---------------------------------------------------------------------------------------------------+
|               ARQUITECTURA DE PROTECCIÓN Y CUIDADO INTEGRAL DE LAS ARTESANAS                      |
|                                                                                                   |
|    [Artesana / Tejedora Mixteca] --------> [Fórmula de Precio Digno Anti-Regateo (HU01)]          |
|                 |                                              |                                  |
|                 v                                              v                                  |
|    [Tianguis Sabatino Tlaxiaco] ---------> [Inventario Local Cifrado SQLCipher (HU02)]            |
|                 |                                              |                                  |
|                 v                                              v                                  |
|    [Turistas y Clientes Justos] ---------> [Catálogo con Sello de Autenticidad (HU03)]            |
|                 |                                              |                                  |
|                 v                                              v                                  |
|    [Memoria Cultural Mixteca] -----------> [Registro de Técnicas, Grecas y Tintes (HU04)]         |
+---------------------------------------------------------------------------------------------------+
```

### Funcionalidades Específicas del Backlog Base:

* **HU01. Registro de tiempo y costo de elaboración (Defensa del Trabajo Digno):**  
  Permite a la artesana o a su acompañante comunitario registrar los minutos y horas invertidos en el corte, desespinado, secado, teñido y tejido de cada tenate, así como los insumos materiales (manojos de palma, anilinas, leña, agua). El sistema aplica una fórmula algorítmica de **Precio Mínimo Digno** que contempla el salario mínimo rural por hora más desgaste físico, dotando a la artesana de una base científica irrefutable para defender su precio y anular el regateo abusivo.
* **HU02. Control de productos para el tianguis de Tlaxiaco (Resiliencia Offline):**  
  Permite registrar altas de inventario matutino, ventas rápidas con un solo toque y arqueo de caja al cierre de plaza, funcionando 100% desconectado de Internet mediante SQLite/SQLCipher local, sin congelamiento de pantalla ni pérdidas de transacciones.
* **HU03. Catálogo digital de tenates y certificación de autenticidad:**  
  Genera una vitrina digital sobria y bilingüe (Español / *Tu'un Sávi* básico) con fotografías comprimidas localmente (<150 KB), dimensiones, tiempo total de tejido dedicado y un identificador único (hash criptográfico SHA-256) que certifica el origen comunal de la pieza para evitar el plagio por marcas industriales.
* **HU04. Registro de características técnicas y patrimonio cultural:**  
  Clasifica y preserva la memoria de cada obra según su técnica de tejido (petatillo liso, calado, doble tejido), tipo de teñido (palma natural, tintes de grana cochinilla, corteza de encino o anilinas comerciales), dimensiones antropométricas y uso tradicional (tortillero, alhajero, tenate de recolección).

---

## 4. Perfiles Profesionales y Roles eduScrum

Para maximizar el aprovechamiento de talentos y garantizar una división científica del trabajo en un equipo universitario multidisciplinario de cuatro integrantes, se definen los siguientes perfiles de ingeniería de software y su correspondiente correspondencia con el marco **eduScrum**:

| Perfil Técnico Requerido | Rol en eduScrum | Integrante Asignada | Justificación Técnica y Competencias Clave |
| :--- | :--- | :--- | :--- |
| **Coordinadora de Proyecto y Analista de Requisitos** | **eduScrum Master / Analista** | **Maritza Sánchez García** | Lidera la facilitación del proceso ágil, eliminación de impedimentos, moderación de ceremonias (Sprint Planning, Daily Standup, Review, Retrospective) y levantamiento de requisitos con enfoque cultural, traduciendo las necesidades de las artesanas mixtecas en especificaciones técnicas formales y criterios de aceptación verificables. |
| **Desarrolladora Frontend & Experiencia de Usuario (UI/UX)** | **Team Member (Developer)** | **Paola Rosario Ayala** | Especialista en diseño de interfaces centradas en personas usuarias con baja alfabetización digital; responsable del desarrollo de la PWA ultraligera, hojas de estilo accesibles de alto contraste para visibilidad bajo la luz solar en el tianguis, e internacionalización preliminar de iconografía y términos en *Tu'un Sávi*. |
| **Desarrolladora Backend & Persistencia Local Cifrada** | **Team Member (Developer)** | **Ariadna Belén Bernabé Juárez** | Responsable de la lógica de negocio, codificación del algoritmo de costeo digno (HU01), indexación en base de datos local SQLite con cifrado en reposo SQLCipher (AES-256), gestión de concurrencia en almacenamiento de terminales modestas y generación determinista de identificadores de autenticidad. |
| **Ingeniera de Calidad de Software (QA) y Redes** | **Team Member (Developer / QA Lead)** | **Mayra González Lita** | Custodia de la calidad técnica; responsable del diseño y ejecución del plan de pruebas unitarias e integrales, simulación de estrés en red celular 2G/EDGE rural, auditoría de linteo automatizado (`eslint`, `cargo clippy`), validación de criterios de aceptación y elaboración de la memoria técnica y evidencias. |

> **Nota de Gobernanza eduScrum:** Todas las integrantes actúan colegiadamente como desarrolladoras (*Developers*), compartiendo la responsabilidad compartida (*Collective Ownership*) sobre el repositorio y la entrega de valor, bajo la premisa de *Tequio Tecnológico*.

---

## 5. Estimación de la Carga de Trabajo Total (160 Horas)

La estimación del esfuerzo de desarrollo se sustenta en el estándar de dimensionamiento ágil y en la necesidad de incorporar el **Costo de la Calidad (CoQ)** aprendido en el Sprint 2 (horas de prevención para evitar bugs de cálculo de precios y horas de evaluación/corrección en condiciones de tianguis):

| Código | Actividad de Ingeniería | Horas Estimadas | % del Esfuerzo | Justificación Técnica y Operativa |
| :---: | :--- | :---: | :---: | :--- |
| **ACT-01** | **Análisis de Requisitos y Contexto Cultural** | 20 h | 12.50% | Entrevistas contextuales con vendedoras de tenates de Tlaxiaco, descomposición de historias de usuario, modelado de variables de costo digno y redacción de criterios de aceptación verificables. |
| **ACT-02** | **Diseño de Arquitectura y UI/UX Accesible** | 20 h | 12.50% | Diseño de mockups accesibles de alto contraste, definición de esquemas relacionales para SQLite/SQLCipher, diseño del algoritmo de depreciación/amortización y arquitectura PWA *offline-first*. |
| **ACT-03** | **Desarrollo de Funcionalidades (HU01 a HU04)** | 60 h | 37.50% | Implementación del motor de cálculo de precio justo (HU01 - 18 h), módulo de punto de venta e inventario offline (HU02 - 16 h), catálogo digital y hashing (HU03 - 14 h) y catálogo de taxonomía artesanal (HU04 - 12 h). |
| **ACT-04** | **Pruebas de Calidad (Evaluación / CoQ)** | 24 h | 15.00% | Pruebas de integración, verificación de latencia < 1.0 s en Android Go, pruebas de estrés en red móvil 2G (50 kbps), pruebas de usabilidad con personas adultas mayores y auditoría de accesibilidad. |
| **ACT-05** | **Corrección de Defectos y Refactorización (CoQ)** | 16 h | 10.00% | Ajustes por fallas de redondeo en precios, optimización de consultas B-tree en SQLite, depuración de anomalías de renderizado en navegadores antiguos y resolución de incidencias detectadas en CI. |
| **ACT-06** | **Documentación Técnica y Evidencias eduScrum** | 20 h | 12.50% | Redacción de bitácoras, actas de Sprint, manual de usuario ilustrado para artesanas, configuración del tablero en GitHub Projects y registro formal de trazabilidad de calidad. |
| **TOTAL** | **Esfuerzo Global del Proyecto (Sprint 3)** | **160 h** | **100.00%** | **Carga consolidada de ingeniería de software para el equipo eduScrum.** |

```
                              DISTRIBUCIÓN DEL ESFUERZO TOTAL (160 HORAS)
          +-------------------------------------------------------------------------------+
          | Desarrollo Funcional (HU01-HU04): 60 h (37.5%)                                |
          +-------------------------------------------------------------------------------+
          | Aseguramiento de Calidad y Corrección (CoQ): 40 h (25.0%)                     |
          +-------------------------------------------------------------------------------+
          | Análisis y Diseño: 40 h (25.0%)                                               |
          +-------------------------------------------------------------------------------+
          | Documentación y eduScrum: 20 h (12.5%)                                        |
          +-------------------------------------------------------------------------------+
```

---

## 6. Distribución Equitativa de Horas por Integrante y Perfil

Para evitar el síndrome de agotamiento estudiantil (*burnout*) y garantizar el cumplimiento pedagógico de la materia en el Tecnológico de Tlaxiaco, la asignación se diseñó de manera estrictamente simétrica: **cada integrante asume exactamente 40 horas de esfuerzo durante el ciclo de 4 semanas** (un promedio exacto de **10 horas semanales por estudiante**), manteniéndose perfectamente dentro del rango reglamentario de 10 a 12 horas semanales.

### A. Matriz de Distribución por Perfil y por Integrante (en Horas Hombre)

| Actividad de Ingeniería | Maritza Sánchez (eduScrum / Analista) | Paola Rosario (Frontend / UI) | Ariadna Belén (Backend / Datos) | Mayra González (QA / Calidad) | Total Horas por Actividad |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **ACT-01. Análisis de Requisitos** | **12 h** | 3 h | 3 h | 2 h | **20 h** |
| **ACT-02. Diseño de Arquitectura / UI** | 4 h | **10 h** | 4 h | 2 h | **20 h** |
| **ACT-03. Desarrollo de Software** | 6 h | **20 h** | **28 h** | 6 h | **60 h** |
| **ACT-04. Pruebas de Calidad (CoQ)** | 3 h | 3 h | 4 h | **14 h** | **24 h** |
| **ACT-05. Corrección de Defectos (CoQ)** | 2 h | 4 h | 4 h | **6 h** | **16 h** |
| **ACT-06. Documentación y Evidencias** | **13 h** | 0 h | - (apoyo 1 h) | **10 h** | **20 h** |
| **TOTAL HORAS POR INTEGRANTE** | **40.0 h** | **40.0 h** | **40.0 h** | **40.0 h** | **160.0 h** |
| **Porcentaje Individual de Carga** | **25.0%** | **25.0%** | **25.0%** | **25.0%** | **100.0%** |

### B. Justificación del Balance de Carga:

1. **Maritza Sánchez García (40 h):** Concentra el esfuerzo directivo y analítico (12 h en requisitos, 13 h en facilitación eduScrum y documentación general), aportando además 6 h de desarrollo en validación de reglas de negocio y 5 h en pruebas y correcciones de usuario final.
2. **Paola Rosario Ayala (40 h):** Concentra su labor en la experiencia de usuario y presentación gráfica (10 h en prototipado de UI accesible y 20 h en programación de vistas y componentes PWA), complementadas con 7 h de pruebas/correcciones visuales y 3 h de afinación de requisitos con artesanas.
3. **Ariadna Belén Bernabé Juárez (40 h):** Representa el motor de backend y lógica pesada (28 h en desarrollo del algoritmo de costeo, modelos relacionales y persistencia SQLCipher), respaldada por 4 h de diseño técnico, 8 h en pruebas unitarias y corrección de bugs en datos.
4. **Mayra González Lita (40 h):** Asume el liderazgo de la calidad del producto (20 h combinadas de ejecución de pruebas y corrección de incidencias de CoQ), 10 h en elaboración de reportes de calidad y bitácoras, 6 h en apoyo a scripts de prueba automatizados y 4 h en análisis y diseño preventivo.

---

## 7. Relación entre Historias de Usuario, Actividades Técnicas y Matriz RACI

Para vincular operativamente la estimación del personal con las tareas concretas del backlog, se establece la asignación de responsabilidades mediante la matriz **RACI** (*Responsible, Accountable, Consulted, Informed*):
* **R (Responsible):** Quien realiza directamente la tarea técnica.
* **A (Accountable):** Quien rinde cuentas del cumplimiento y calidad del entregable.
* **C (Consulted):** Persona con la que se valida o consulta información técnica.
* **I (Informed):** Persona que se mantiene informada del progreso.

| Historia de Usuario / Entregable | Maritza Sánchez (eduScrum / Analista) | Paola Rosario (Frontend / UI) | Ariadna Belén (Backend / Datos) | Mayra González (QA / Calidad) |
| :--- | :---: | :---: | :---: | :---: |
| **HU01: Registro de tiempo y costo (Cálculo Digno Anti-Regateo)** | **A** / C | C | **R** | C / R (Tests) |
| **HU02: Control de productos para el tianguis (Offline-First)** | C | **R** | **R** | **A** / R (Estrés) |
| **HU03: Catálogo digital y certificación de autenticidad** | C | **R** | C / R | **A** / R (Forensia) |
| **HU04: Registro de características y patrimonio cultural** | **A** / R | **R** | C | C / R (Validación) |
| **Configuración de Pipeline CI y Linteo Automatizado** | I | C | C | **A** / **R** |
| **Gobernanza del Tablero GitHub Projects y eduScrum** | **A** / **R** | I | I | C |
| **Auditoría del Costo de la Calidad (Sprint 2 -> Sprint 3)** | C | I | C | **A** / **R** |

---

## 8. Organización y Operatividad del Equipo mediante eduScrum

La adopción de **eduScrum** (metodología ágil orientada al aprendizaje formativo) permite al Grupo 5 mantener un ritmo de desarrollo constante, autogestionado y transparente:

```
+-----------------------------------------------------------------------------------------------+
|                             CICLO OPERATIVO EDUSCRUM - GRUPO 5                                |
|                                                                                               |
|  [Sprint Planning] ------> [Daily Standup 3x/sem] ------> [Sprint Review] ----> [Retrospective]|
|  - Desglose de tareas      - ¿Qué logré hoy?              - Demo con artesanas  - Mejoras de  |
|  - Asignación horas        - ¿Qué haré mañana?            - Validación de C.A.    convivencia |
|  - Verificación CoQ        - ¿Qué impedimento tengo?      - Feedback P.O.       - Ajuste carga|
+-----------------------------------------------------------------------------------------------+
```

### Reglas Operativas del Equipo:

1. **Reunión de Sincronización Diaria (Daily Standup):** Se realiza de manera ágil (máximo 15 minutos) 3 veces por semana de forma híbrida (laboratorio del TecNM y canal virtual de Discord), respondiendo: ¿Qué avancé para cuidar a las artesanas?, ¿Qué tareas del tablero tomaré?, ¿Existe algún bloqueo técnico en 2G o base de datos?
2. **Políticas de Transición en el Tablero de GitHub Projects:**
   * Ninguna tarea puede pasar a *In Progress* sin tener asignada una integrante, estimación en horas y etiqueta de Historia de Usuario.
   * Límite de Trabajo en Proceso (*Work In Progress - WIP*): Máximo 2 tareas simultáneas por integrante para evitar la dispersión.
   * Criterio de Entrada a *Review*: Código subido a GitHub con *Pull Request*, pasando linteo en CI (`eslint` sin advertencias) y pruebas unitarias locales.
3. **Criterio de Terminado (*Definition of Done - DoD*):**
   * El código satisface el 100% de los Criterios de Aceptación especificados en el issue.
   * Se cuenta con evidencia de prueba ejecutada (captura de pantalla o log de consola).
   * La documentación técnica de la tarea está actualizada.
   * El *Pull Request* cuenta con la aprobación cruzada de al menos otra compañera del equipo y la validación de la QA Lead.

---

## 9. Evaluación de Capacidad, Factores Humanos y Mitigación de Riesgos

Para asegurar que la estimación sea realista y no caiga en el optimismo injustificado, se evaluaron los factores de contingencia propios de la vida universitaria y comunitaria en Tlaxiaco:

| Riesgo Operativo Identificado | Probabilidad | Impacto | Estrategia Preventiva y de Mitigación |
| :--- | :---: | :---: | :--- |
| **Cortes imprevistos de energía o Internet en Tlaxiaco** | Alta | Medio | Configuración de entornos de desarrollo 100% locales (SQLite, Node local); repositorios replicados en unidades USB cifradas; trabajo offline nativo. |
| **Saturación académica por periodo de exámenes parciales** | Alta | Alto | Buffer de 2 horas de holgura por integrante en semanas críticas; asignación de tareas de documentación y análisis en días de evaluación teórica. |
| **Resistencia o dificultades de comprensión por brecha digital** | Media | Alto | Pruebas tempranas de usabilidad con artesanas desde la Semana 2 (Sprint 3); simplificación extrema de la UI con iconografía intuitiva de la palma y el tenate. |
| **Complejidad inesperada en consultas SQLCipher en terminales lentas** | Media | Medio | Apoyo técnico cruzado entre Ariadna (Backend) y Mayra (QA); pruebas de rendimiento sintéticas previas con colecciones de prueba antes de la integración final. |

---

## 10. Conclusiones y Dictamen de Asignación

La estimación de personal presentada demuestra que el desarrollo del **Sistema de Apoyo y Protección Integral para Vendedoras y Artesanas de Tenates de Palma** es plenamente viable, sostenible y equitativo:

1. **Rigor Cuantitativo:** Se justifican minuciosamente **160 horas hombre** de esfuerzo técnico, distribuidas simétricamente a razón de **40 horas por estudiante** durante 4 semanas de trabajo (10 h/semana), lo que encaja con total naturalidad en los créditos y horarios de la carrera de Ingeniería en Sistemas Computacionales del TecNM.
2. **Equilibrio entre Desarrollo y Calidad:** Se destina un contundente **25% del esfuerzo total (40 horas = $6,000 MXN)** al Aseguramiento y Costo de la Calidad (CoQ), garantizando que las funcionalidades de cálculo de precio justo y punto de venta rural no fallen en el terreno real.
3. **Impacto Ético y Social:** La organización del equipo pone la ciencia de la ingeniería de software al servicio de la justicia económica y la preservación cultural de las mujeres artesanas de la Mixteca Alta, convirtiendo el Sprint 3 en un testimonio de innovación con sentido social.

> **Dictamen:** **APROBADO POR EL EQUIPO GRUPO 5 PARA SU INTEGRACIÓN INMEDIATA AL TABLERO DE GITHUB PROJECTS.**  
> *Heroica Ciudad de Tlaxiaco, Oaxaca, a 21 de Octubre de 2026.*
