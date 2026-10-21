# VINCULACIÓN Y TRAZABILIDAD CON EL COSTO DE LA CALIDAD (SPRINT 2 A SPRINT 3)

> **Asignatura:** Gestión de Proyectos de Software (SCG-1009)  
> **Unidad Académica:** Unidad 3. Planificación del Proyecto  
> **Criterio Evaluado:** Criterio 1 de la Rúbrica (Vinculación y Trazabilidad con el Costo de la Calidad - Valor: 5.0 pts)  
> **Iniciativa / Ecosistema:** Open Hub Tec (Instituto Tecnológico de Tlaxiaco)  
> **Marco de Trabajo:** eduScrum (Sprint 3)  
> **Proyecto Oficial:** *Sistema de Apoyo y Protección Integral para Vendedoras y Artesanas de Tenates de Palma en la Región Mixteca ("Cuidar y Proteger a las Artesanas")*  
> **Equipo de Desarrollo (Grupo 5):** Maritza Sánchez García, Paola Rosario Ayala, Ariadna Belén Bernabé Juárez y Mayra González Lita.  
> **Fecha:** Octubre 2026  

---

## 🧭 Índice del Documento

1. [Marco Teórico del Costo de la Calidad (CoQ en eduScrum y TecNM)](#1-marco-teórico-del-costo-de-la-calidad-coq-en-eduscrum-y-tecnm)
2. [Consolidación de Métricas del Sprint 2: Prevención vs. Corrección](#2-consolidación-de-métricas-del-sprint-2-prevención-vs-corrección)
3. [Matriz Maestra de Trazabilidad por Historia de Usuario (HU01 a HU04)](#3-matriz-maestra-de-trazabilidad-por-historia-de-usuario-hu01-a-hu04)
4. [Análisis de Impacto Crítico en la Vida y Economía de las Artesanas](#4-análisis-de-impacto-crítico-en-la-vida-y-economía-de-las-artesanas)
5. [Políticas de Aseguramiento de Calidad en el Tablero de GitHub Projects](#5-políticas-de-aseguramiento-de-calidad-en-el-tablero-de-github-projects)

---

## 1. Marco Teórico del Costo de la Calidad (CoQ en eduScrum y TecNM)

El **Costo de la Calidad (Cost of Quality - CoQ)**, estructurado bajo los modelos clásicos de Armand Feigenbaum, Joseph Juran y Philip Crosby, y normado por el estándar internacional **ISO/IEC 25010** y la norma mexicana **MoProSoft (NMX-I-059-NYCE)**, sostiene que la calidad no es un costo adicional prescindible, sino una inversión calculada que evita fallas operativas catastróficas.

El CoQ se divide en dos grandes categorías:
1. **Costos de Conformidad (*Cost of Conformance*):**
   * **Costos de Prevención:** Inversión proactiva en actividades de ingeniería diseñadas para impedir que los defectos se originen (diseño formal de algoritmos, tipado estático estricto, linteo en CI, definición de estándares de codificación y matrices de criterios de aceptación).
   * **Costos de Evaluación / Inspección:** Inversión en verificar, medir y auditar el software para certificar el cumplimiento de los criterios de aceptación antes de la entrega (pruebas unitarias, pruebas de estrés de red, benchmarks de latencia en Android Go y auditorías de usabilidad contextual).
2. **Costos de No Conformidad (*Cost of Non-Conformance*):**
   * **Costos de Fallas Internas (Corrección / Rework):** Esfuerzo técnico dedicado a depurar, corregir y refactorizar código cuando se detectan fallas durante las pruebas internas antes de que el producto llegue a las usuarias finales.

En el marco de la asignatura *Gestión de Proyectos de Software*, el Grupo 5 analizó en el **Sprint 2** que un error de software en este proyecto no es una simple molestia técnica: **un defecto en el algoritmo de cálculo de precios puede provocar que una artesana venda su trabajo por debajo del costo de subsistencia, perdiendo el sustento de su familia; y un fallo en la base de datos durante el tianguis del sábado en Tlaxiaco puede borrar el inventario de una jornada completa**.

---

## 2. Consolidación de Métricas del Sprint 2: Prevención vs. Corrección

A partir de la auditoría de calidad realizada a una tarifa estándar de **$150.00 MXN / hora**, el esfuerzo de calidad se dimensionó en **40.0 horas hombre**, equivalentes a **$6,000.00 MXN** (exactamente el **25.0%** del presupuesto global de 160 horas del proyecto):

```
+---------------------------------------------------------------------------------------------------+
|                         DISTRIBUCIÓN DEL COSTO DE LA CALIDAD (CoQ)                                |
|                                                                                                   |
|  [Prevención (55.0% / 22.0 h)]: $3,300.00 MXN ----> Inversión Proactiva (Diseño y CI)           |
|  [Evaluación (25.0% / 10.0 h)]: $1,500.00 MXN ----> Verificación y Benchmarks Android Go          |
|  [Corrección (20.0% /  8.0 h)]: $1,200.00 MXN ----> Depuración y Refactorización Interna         |
|                                                                                                   |
|  TOTAL COQ: 40.0 Horas Hombre = $6,000.00 MXN (~$315.79 USD)                                     |
+---------------------------------------------------------------------------------------------------+
```

### Justificación de la Proporción Invertida:
* **55% en Prevención ($3,300.00 MXN / 22.0 h):** La mayor parte del presupuesto se destina a evitar defectos en la fase de diseño. En la Mixteca Alta, donde no hay conexión para enviar parches en la nube en tiempo real, el software debe ser correcto por diseño.
* **25% en Evaluación ($1,500.00 MXN / 10.0 h):** Pruebas rigurosas sobre hardware austero real (teléfonos Android Go de 2 GB de RAM) y en condiciones de conectividad degradada (redes 2G/EDGE a 50 kbps).
* **20% en Corrección ($1,200.00 MXN / 8.0 h):** Margen realista de retrabajo para resolver discrepancias numéricas y optimizar consultas en SQLite sin caer en el supuesto utópico de "cero defectos".

---

## 3. Matriz Maestra de Trazabilidad por Historia de Usuario (HU01 a HU04)

La siguiente matriz evidencia la vinculación directa, exacta y trazable entre los aprendizajes del Sprint 2 y las actividades planificadas en el Tablero de GitHub Projects para el Sprint 3:

| Historia de Usuario | Métrica ISO/IEC 25010 | Inversión Prevención (Horas / Costo) | Inversión Evaluación (Horas / Costo) | Inversión Corrección (Horas / Costo) | Total CoQ (Horas / MXN) | Tarea de Calidad Concreta en el Tablero de GitHub |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **HU01: Registro de Tiempo y Costo (Cálculo Digno)** | **Adecuación Funcional (Exactitud)** e **Integridad** | **6.0 h**<br>($900 MXN) | **6.0 h**<br>($900 MXN) | **4.0 h**<br>($600 MXN) | **16.0 h**<br>($2,400 MXN) | • `task-qa-01`: Modelado de invariantes de precio (`proptest`).<br>• `task-qa-02`: Validación de redondeo de centavos y tarifa rural.<br>• `task-dev-01c`: Corrección de desbordamiento en sumatoria de costos. |
| **HU02: Control de Inventario Tianguis (Offline-First)** | **Fiabilidad (Tolerancia a fallos)** y **Rendimiento** | **4.0 h**<br>($600 MXN) | **5.0 h**<br>($750 MXN) | **3.0 h**<br>($450 MXN) | **12.0 h**<br>($1,800 MXN) | • `task-qa-03`: Tipado estático en esquemas SQLite/SQLCipher.<br>• `task-qa-04`: Prueba de corte abrupto de batería durante venta.<br>• `task-dev-02c`: Optimización de transacciones ACID para evitar bloqueos. |
| **HU03: Catálogo Digital y Certificación Autenticidad** | **Seguridad (Autenticidad)** y **Eficiencia** | **6.0 h**<br>($900 MXN) | **5.0 h**<br>($750 MXN) | **7.0 h**<br>($1,050 MXN) | **18.0 h**<br>($2,700 MXN) | • `task-qa-05`: Configuración de linteo estricto (`eslint --max-warnings=0`).<br>• `task-qa-06`: Prueba de generación y colisión de hashes SHA-256.<br>• `task-dev-03c`: Depuración de fugas de memoria en compresión Web Workers. |
| **HU04: Registro de Técnicas y Patrimonio Cultural** | **Usabilidad (Comprensibilidad)** y **Mantenibilidad** | **4.0 h**<br>($600 MXN) | **5.0 h**<br>($750 MXN) | **3.0 h**<br>($450 MXN) | **12.0 h**<br>($1,800 MXN) | • `task-qa-07`: Normalización de tablas relacionales de taxonomía.<br>• `task-qa-08`: Benchmark de filtrado reactivo < 500 ms en Android Go.<br>• `task-dev-04c`: Corrección de filtros combinados de tintes y grecas. |
| **TOTALES CONSOLIDADOS** | **ISO/IEC 25010** | **20.0 h**<br>($3,000 MXN) | **21.0 h**<br>($3,150 MXN) | **17.0 h**<br>($2,550 MXN) | **58.0 h**<br>($8,700 MXN) | *(Nota: Incluye 2 h transversales de pipeline CI en Prevención = 60.0 h globales de CoQ).* |

---

## 4. Análisis de Impacto Crítico en la Vida y Economía de las Artesanas

La inversión en calidad no es un ejercicio académico abstracto; tiene consecuencias humanas inmediatas en el contexto de Tlaxiaco:

### A. Mitigación de Vulnerabilidades en HU01 (Cálculo de Precio Digno):
* **El Riesgo Sin Calidad:** Si el software redondea erróneamente los decimales al dividir el costo de un manojo de palma entre 4 tenates, o si omite el tiempo de secado al sol, el precio sugerido resultará menor al costo de producción. La artesana vendería creyendo que gana, cuando en realidad estaría subsidiando con su propio hambre al intermediario.
* **La Solución con CoQ:** Las **16 horas de CoQ** asignadas a HU01 aseguran mediante pruebas de propiedades matemáticas que **bajo ninguna combinación de insumos el precio calculado sea inferior a la suma estricta de materia prima más salario digno**.

### B. Mitigación de Vulnerabilidades en HU02 (Tianguis Sabatino en Tlaxiaco):
* **El Riesgo Sin Calidad:** En el tianguis del sábado en la explanada de Tlaxiaco, la multitud satura las antenas celulares 3G/4G y la señal cae a 2G/EDGE o desaparece por completo. Si el sistema dependiera de sincronización remota o no manejara transacciones ACID locales, la aplicación se congelaría al momento de registrar una venta rápida, generando confusión con la clientela y pérdida del registro de dinero.
* **La Solución con CoQ:** Las **12 horas de CoQ** dedicadas a HU02 garantizan pruebas de desconexión física forzada, caídas de alimentación y tiempos de respuesta locales **< 800 ms** en SQLite.

### C. Mitigación de Vulnerabilidades en HU03 (Protección contra Plagio Cultural):
* **El Riesgo Sin Calidad:** Si la compresión de fotografías genera artefactos visuales borrosos o si el hash criptográfico SHA-256 no es determinista, la artesana no podrá demostrar la autoría ni la procedencia territorial de su obra frente a intermediarios que plagian sus grecas.
* **La Solución con CoQ:** Las **18 horas de CoQ** aseguran la integridad visual de las fotos en WebP (<150 KB) y la validez matemática del identificador digital.

---

## 5. Políticas de Aseguramiento de Calidad en el Tablero de GitHub Projects

Para asegurar que la trazabilidad del Sprint 2 se refleje activamente en la operatividad diaria del Sprint 3, el Grupo 5 estableció las siguientes reglas innegociables en el tablero Kanban de GitHub Projects:

```
+-----------------------------------------------------------------------------------------------+
|                       POLÍTICAS DE CALIDAD EN EL FLUJO KANBAN                                  |
|                                                                                               |
|  [To Do] -----------> [In Progress] ----------> [Review / QA] ------------> [Done]            |
|     |                       |                          |                       |              |
|     v                       v                          v                       v              |
|  Requiere etiqueta    Límite WIP = 2           Ejecución obligatoria   Aprobación cruzada PR  |
|  de CoQ asignada      tareas por integrante    de checklist de pruebas Cero warnings en CI    |
|  (Prevención/Corr.)                            en terminal Android Go  Criterios CA validados |
+-----------------------------------------------------------------------------------------------+
```

1. **Etiquetado Obligatorio de Calidad:** Toda tarea vinculada al Costo de la Calidad debe portar una de las siguientes etiquetas:
   * 🏷️ `tipo:prevencion-coq` (Inversión en diseño, linteo y esquemas seguros).
   * 🏷️ `tipo:evaluacion-coq` (Inversión en pruebas de estrés 2G, latencia y usabilidad).
   * 🏷️ `tipo:correccion-coq` (Inversión en refactorización y depuración de defectos).
2. **Puerta de Control de Calidad (*Quality Gate* en Pull Requests):** Ningún *Pull Request* puede fusionarse a la rama `main` sin la aprobación formal de **Mayra González Lita (QA Lead)** y el paso exitoso del workflow de GitHub Actions (`ci_calidad.yml`), garantizando cero errores de linteo y cobertura de pruebas.
3. **Validación Contextual con Artesanas:** Antes de marcar como *Done* una historia de usuario, se debe registrar en el issue la evidencia de prueba con artesanas en Tlaxiaco o en simulación de laboratorio con hardware Android Go.
