# MATRIZ DE RIESGOS DEL PROYECTO — SPRINT 3 (TRABAJO 3)

> **Institución:** Instituto Tecnológico Nacional de México (TecNM)  
> **Campus:** Instituto Tecnológico de Tlaxiaco  
> **Carrera:** Ingeniería en Sistemas Computacionales  
> **Asignatura:** Gestión de Proyectos de Software (SCG-1009)  
> **Unidad Académica:** Unidad 3: Planificación del Proyecto  
> **Entregable Oficial:** Trabajo 3 — Matriz de Riesgos Multidimensional (Temas 3.5.1, 3.5.2, 3.5.3, 3.5.4)  
> **Iniciativa / Ecosistema:** Open Hub Tec (Instituto Tecnológico de Tlaxiaco)  
> **Marco de Trabajo:** eduScrum (Sprint 3)  
> **Proyecto Oficial:** *Infraestructura Descentralizada para la Preservación y Consulta Inmutable de Recursos Jurídicos en la Región Mixteca*  
> **Organización Beneficiaria:** Núcleos Agrarios, Ejidos y Comités de Bienes Comunales de la Mixteca Alta oaxaqueña**  
> **Repositorio Oficial del Entregable:** [`gestion-de-proyectos-de-software-tablero-group-5`](https://github.com/SistemasTecTlaxiaco/gestion-de-proyectos-de-software-tablero-group-5.git)  
> **Repositorios de Referencia Técnica:**  
> * [`gestion-de-proyectos-de-software-informe-de-estandares-de-ca-group-4`](https://github.com/SistemasTecTlaxiaco/gestion-de-proyectos-de-software-informe-de-estandares-de-ca-group-4.git)  
> * [`gestion-de-proyectos-de-software-documento-smart-group-7`](https://github.com/SistemasTecTlaxiaco/gestion-de-proyectos-de-software-documento-smart-group-7.git)  
> **Fecha:** 21 de Octubre de 2026  

---

## 🧭 Índice del Entregable

1. [Introducción y Contexto Territorial del Proyecto](#1-introducción-y-contexto-territorial-del-proyecto)
2. [Objetivo General](#2-objetivo-general)
3. [Clasificación Multidimensional de Riesgos (Temas 3.5.1 y 3.5.2)](#3-clasificación-multidimensional-de-riesgos-temas-351-y-352)
4. [Metodología de Evaluación y Escala Semicuantitativa (Temas 3.5.2 y 3.5.3)](#4-metodología-de-evaluación-y-escala-semicuantitativa-temas-352-y-353)
5. [Matriz Maestra de Identificación y Evaluación de Riesgos](#5-matriz-maestra-de-identificación-y-evaluación-de-riesgos)
6. [Justificación Detallada de las Evaluaciones](#6-justificación-detallada-de-las-evaluaciones)
7. [Diseño de Estrategias de Respuesta, Responsables y Planes de Contingencia (Tema 3.5.4)](#7-diseño-de-estrategias-de-respuesta-responsables-y-planes-de-contingencia-tema-354)
8. [Análisis Profundo de Riesgos Críticos y Prioritarios](#8-análisis-profundo-de-riesgos-críticos-y-prioritarios)
9. [Trazabilidad Integral con Sprints Anteriores (Historias US-01 a US-05 y CoQ)](#9-trazabilidad-integral-con-sprints-anteriores-historias-us-01-a-us-05-y-coq)
10. [Operatividad y Monitoreo del Tablero de Riesgos en GitHub Projects](#10-operatividad-y-monitoreo-del-tablero-de-riesgos-en-github-projects)
11. [Articulación con el Análisis de Viabilidad y Dictamen de Riesgo Residual](#11-articulación-con-el-análisis-de-viabilidad-y-dictamen-de-riesgo-residual)
12. [Conclusiones y Compromiso Ético con la Región Mixteca](#12-conclusiones-y-compromiso-ético-con-la-región-mixteca)

---

## 1. Introducción y Contexto Territorial del Proyecto

La gestión proactiva de riesgos de software, articulada conforme a los estándares internacionales del **Project Management Institute (PMI / PMBOK 7ma Edición)**, la norma **ISO 31000** y el marco ágil de aprendizaje colaborativo **eduScrum**, constituye un componente ineludible durante la **Unidad 3: Planificación del Proyecto**. Su finalidad radica en anticipar, caracterizar, clasificar, cuantificar y mitigar sistemáticamente cualquier evento incierto cuya materialización comprometa el cumplimiento del objetivo SMART, el presupuesto universitario, el calendario académico de 14 semanas o la integridad de las comunidades agrarias receptoras de la tecnología.

El proyecto **"Infraestructura Descentralizada para la Preservación y Consulta Inmutable de Recursos Jurídicos en la Región Mixteca"** aborda una problemática de profunda gravedad social, jurídica y de derechos humanos en el estado de Oaxaca: **la vulnerabilidad, falsificación, alteración y extravío intencional de sentencias agrarias, resoluciones de amparo indirecto, actas de asamblea comunal y peritajes territoriales frente a intereses extractivistas (minería a cielo abierto, proyectos hidroeléctricos, privatización de mantos acuíferos y tala clandestina)**.

Para erradicar esta indefensión, la solución arquitectónica combina:
* Almacenamiento local cifrado en reposo mediante **SQLCipher (AES-256)** con índices B-Tree en SQLite para consultas ultrarrápidas (< 1.5 s).
* Despojo forzoso de metadatos forenses y datos de identificación personal (**PII / EXIF GPS**) en el propio dispositivo de origen.
* Identidades autosoberanas efímeras mediante **W3C DID (`did:key` sobre curvas ed25519)**.
* Registro inmutable de hashes SHA-256 y CIDs v1 en contratos inteligentes en **Soroban (Stellar)** con esquemas de almacenamiento persistente (`Persistent Storage TTL / State Archival`).
* Esquemas de validación multifirma colegiada (**EIP-712 / Soroban Auth**) que subordinan la tecnología al quórum asambleario de los **Usos y Costumbres de los pueblos mixtecos (*Ñuu Sávi*)**, según el Artículo 2 de la Constitución Política de los Estados Unidos Mexicanos.
* Mecanismos de sostenibilidad económica descentralizada vía subvenciones por hitos verificables (**Stellar Community Fund - SCF**) y streaming continuo de capital mediante contratos inteligentes (**Drips Protocol v2**).

No obstante, el despliegue de esta tecnología en la **Mixteca Alta oaxaqueña** se enfrenta a una realidad estructural sumamente adversa:
1. **Orografía accidentada y aislamiento de telecomunicaciones:** Cortes eléctricos y caídas de enlace celular frecuentes de 48 a 96 horas continuas, con redes móviles degradadas a perfil 2G/EDGE (50 kbps) y pérdidas de paquetes de entre 35% y 65%.
2. **Limitaciones severas de hardware rural:** El 85% de las autoridades ejidales y defensores comunitarios utiliza teléfonos inteligentes básicos de gama de entrada (**Android Go con memoria RAM entre 2 GB y 3 GB**) y computadoras donadas o recicladas.
3. **Hostilidad sociopolítica y criminalización de defensores:** La filtración involuntaria de la identidad de un firmante o la localización geográfica de un peritaje territorial puede desencadenar represalias armadas, amenazas de muerte o persecución penal ilegítima.
4. **Incertidumbre en mecanismos de financiamiento Web3:** Si bien Stellar y Drips proveen microtarifas y streaming transparente, la obtención real de subvenciones internacionales está sujeta a comités de evaluación externos y a la volatilidad cambiaria de criptoactivos.

Por consiguiente, la presente **Matriz de Riesgos** no es un ejercicio teórico descontextualizado, sino una herramienta técnica de ingeniería defensiva que garantiza la resiliencia operativa y la protección de la vida en la Región Mixteca.

---

## 2. Objetivo General

Identificar, analizar cualitativa y semicuantitativamente, clasificar, evaluar y formular estrategias formales de respuesta ante los riesgos técnicos, socio-operativos y financieros/Web3 susceptibles de presentarse durante el desarrollo y validación del **MVP de la Infraestructura Descentralizada de Recursos Jurídicos en la Región Mixteca**, estableciendo:
* Asignaciones precisas de responsables directos dentro del equipo multidisciplinario **eduScrum**.
* Planes de mitigación preventiva y planes de contingencia reactivos exhaustivos.
* Trazabilidad directa con las **Historias de Usuario (US-01 a US-05)** del Sprint 1, los costos del aseguramiento de la calidad (**Costo de la Calidad - CoQ**) del Sprint 2 y el **Análisis de Viabilidad Multidimensional** del Sprint 3.
* Un protocolo de monitoreo continuo gestionable a través de **GitHub Projects**.

---

## 3. Clasificación Multidimensional de Riesgos (Temas 3.5.1 y 3.5.2)

Conforme a los lineamientos curriculares del TecNM y las áreas de conocimiento del PMBOK, los riesgos se estructuran en **tres dimensiones críticas**:

```
+---------------------------------------------------------------------------------------------------+
|                        TAXONOMÍA MULTIDIMENSIONAL DE RIESGOS (OPEN HUB TEC)                       |
+---------------------------------------------------------------------------------------------------+
|  1. DIMENSIÓN TÉCNICA (Arquitectura de Software, Seguridad Criptográfica y Redes Locales)          |
|     - Desempeño en hardware modesto Android Go (< 3 GB RAM).                                      |
|     - Inmutabilidad, sobreescritura y colisiones criptográficas en Soroban (Rust / WASM).          |
|     - Expiración de almacenamiento TTL (State Archival) en contratos de Stellar.                  |
|     - Fuga de datos de identificación personal (PII) y metadatos EXIF/GPS en archivos jurídicos.  |
|     - Corrupción transaccional de SQLite/SQLCipher (AES-256) por apagones o reinicios forzados.   |
+---------------------------------------------------------------------------------------------------+
|  2. DIMENSIÓN SOCIAL Y OPERATIVA (Contexto Mixteca, Usos/Costumbres y Dinámica eduScrum)          |
|     - Caída de enlaces y desconexión prolongada (48-96 h) en la Sierra Mixteca.                   |
|     - Brecha lingüística (monolingüismo Tu'un Sávi) y analfabetismo digital en asambleas.        |
|     - Desconfianza comunal hacia tecnologías Web3 y riesgo de cooptación de autoridades.         |
|     - Riesgo a la integridad física de defensores del territorio por filtraciones.                |
|     - Desbalances de carga y picos de exámenes académicos en el equipo eduScrum universitario.    |
+---------------------------------------------------------------------------------------------------+
|  3. DIMENSIÓN FINANCIERA Y WEB3 (Stellar Community Fund, Drips Protocol v2 y Sostenibilidad)      |
|     - No aprobación o demora en los tranches de subvención del Stellar Community Fund (SCF).      |
|     - Volatilidad del token XLM y costo de mantenimiento de nodos comunitarios IPFS/routers.     |
|     - Riesgo de sobre-ingeniería Web3 que incremente el consumo de gas o complique el soporte.    |
|     - Exposición pública de balances o padrones comunales en libros contables distribuidos.       |
|     - Fallas o estancamiento de flujos de streaming continuo en contratos RepoDriver de Drips v2. |
+---------------------------------------------------------------------------------------------------+
```

---

## 4. Metodología de Evaluación y Escala Semicuantitativa (Temas 3.5.2 y 3.5.3)

Para evaluar la magnitud de cada evento con rigor ingenieril, se implementa una escala semicuantitativa matricial de **3 × 3**, definiendo objetivamente los valores asignados:

### A. Escala de Probabilidad de Ocurrencia ($P$)

| Valor | Nivel de Probabilidad | Definición Operativa en el Entorno Mixteco / eduScrum |
| :---: | :--- | :--- |
| **1** | **Baja** | Evento con antecedentes escasos; probabilidad de manifestación inferior al 15% durante el ciclo del proyecto. Mecanismos de protección estándar activos. |
| **2** | **Media** | Evento recurrente o probable; probabilidad de manifestación entre el 15% y el 50%. Típico de condiciones climáticas o limitaciones de hardware rural. |
| **3** | **Alta** | Evento casi certero o altamente frecuente; probabilidad de manifestación superior al 50%. Condiciones endémicas de la Mixteca (cortes de luz, redes 2G colapsadas). |

### B. Escala de Impacto en los Objetivos ($I$)

| Valor | Nivel de Impacto | Consecuencia Técnica, Operativa o Humana |
| :---: | :--- | :--- |
| **1** | **Bajo** | Afectación marginal; retrasos de desarrollo menores a 3 días, degradación imperceptible de UI o variaciones presupuestales inferiores al 5%. No compromete la seguridad. |
| **2** | **Medio** | Afectación moderada; retrasos de sprint de hasta 1 semana, indisponibilidad temporal de consulta local o sobrecostos manejables absorbidos por buffers internos. |
| **3** | **Alto / Crítico** | Afectación catastrófica; vulneración de la vida o libertad de defensores, pérdida irreversible de amparos, sobreescritura de fallos en blockchain o quiebra presupuestal. |

### C. Matriz de Exposición y Severidad del Riesgo ($E = P \times I$)

La severidad del riesgo se calcula mediante el producto escalar:

$$E = P \times I$$

```
                           MATRIZ DE SEVERIDAD DEL RIESGO (3x3)
           +-----------------------------------------------------------------+
           | IMPACTO  \  PROB. |     1 (Baja)    |    2 (Media)    |  3 (Alta)   |
           +-------------------+-----------------+-----------------+-------------+
           | 3 (Alto / Crítico)|    3 (Medio)    |    6 (ALTO)     |  9 (CRÍTICO)|
           +-------------------+-----------------+-----------------+-------------+
           | 2 (Medio)         |    2 (Bajo)     |    4 (Medio)    |  6 (ALTO)   |
           +-------------------+-----------------+-----------------+-------------+
           | 1 (Bajo)          |    1 (Bajo)     |    2 (Bajo)     |  3 (Medio)  |
           +-------------------+-----------------+-----------------+-------------+
```

* **Exposición 1 – 2 (Riesgo Bajo - Verde):** Se acepta o se administra con controles operativos rutinarios.
* **Exposición 3 – 4 (Riesgo Medio - Amarillo):** Requiere medidas preventivas planificadas y seguimiento en los Daily Standups.
* **Exposición 6 – 9 (Riesgo Alto / Crítico - Rojo):** Demanda planes de contingencia obligatorios, asignación de recursos inmediatos y supervisión directa por la eduScrum Master y el Product Owner.

---

## 5. Matriz Maestra de Identificación y Evaluación de Riesgos

La siguiente tabla consolida la identificación exhaustiva de los **15 riesgos críticos** del proyecto, cubriendo las tres dimensiones normativas:

| ID | Riesgo Identificado | Dimensión | Clasificación PMBOK | Prob. ($P$) | Imp. ($I$) | Exp. ($P \times I$) | Nivel de Severidad |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **R-TEC-01** | Fuga forense de datos personales (PII) o metadatos EXIF/GPS en documentos cargados | Técnica | Seguridad / Privacidad | 3 | 3 | **9** | **CRÍTICO** |
| **R-TEC-02** | Expiración prematura del almacenamiento persistente (*State Archival TTL*) en Soroban | Técnica | Arquitectura / Blockchain | 2 | 3 | **6** | **ALTO** |
| **R-TEC-03** | Intento de sobreescritura o colisión maliciosa de CIDs v1 de resoluciones agrarias | Técnica | Integridad / Blockchain | 2 | 3 | **6** | **ALTO** |
| **R-TEC-04** | Bloqueo o cuelgue del hilo de UI en terminales Android Go por cálculo criptográfico pesado | Técnica | Rendimiento / Hardware | 3 | 2 | **6** | **ALTO** |
| **R-TEC-05** | Corrupción transaccional de SQLite/SQLCipher por apagón eléctrico abrupto en terminal | Técnica | Fiabilidad / Datos | 2 | 3 | **6** | **ALTO** |
| **R-SOC-01** | Aislamiento prolongado por cortes de telecomunicaciones celulares y CFE (48 a 96 h) | Social / Regional | Infraestructura Rural | 3 | 2 | **6** | **ALTO** |
| **R-SOC-02** | Rechazo o desconfianza de las Asambleas de Comuneros por tecnicismos incomprensibles | Social / Regional | Adopción / Gobernanza | 2 | 2 | **4** | **MEDIO** |
| **R-SOC-03** | Extravío, cooptación o robo de llaves privadas ed25519 de autoridades comunales | Social / Seguridad | Gobernanza / Identidad | 2 | 3 | **6** | **ALTO** |
| **R-SOC-04** | Barrera idiomática por predominio del mixteco (*Tu'un Sávi*) en personas comuneras ancianas | Social / Regional | Accesibilidad Cultural | 2 | 2 | **4** | **MEDIO** |
| **R-OPE-05** | Desbalance de carga en el equipo eduScrum por exámenes parciales y entrega de materias | Operativa | Gestión de Equipo | 3 | 2 | **6** | **ALTO** |
| **R-FIN-01** | Rechazo o atraso burocrático en la liberación de subvenciones del Stellar Community Fund | Financiera / Web3 | Sostenibilidad / Grants | 3 | 3 | **9** | **CRÍTICO** |
| **R-FIN-02** | Desplome cambiario del token XLM que reduzca el fondo operativo en moneda local | Financiera / Web3 | Riesgo Cambiario | 3 | 2 | **6** | **ALTO** |
| **R-FIN-03** | Sobre-ingeniería Web3 que incremente costos de gas o dependencias complejas innecesarias | Técnica / Web3 | Arquitectura / Costo | 2 | 3 | **6** | **ALTO** |
| **R-FIN-04** | Exposición pública e irreversible de información financiera interna comunal en Stellar | Ética / Web3 | Confidencialidad | 2 | 3 | **6** | **ALTO** |
| **R-FIN-05** | Interrupción o atasco en contratos RepoDriver de Drips v2 para streaming de mantenimiento | Financiera / Web3 | Infraestructura Web3 | 2 | 2 | **4** | **MEDIO** |

---

## 6. Justificación Detallada de las Evaluaciones

A continuación se fundamenta la asignación cualitativa y cuantitativa de cada riesgo:

* **R-TEC-01 (Fuga de PII / GPS - Exp. 9):** Los defensores del territorio en la Mixteca enfrentan amenazas directas contra su vida. Un documento escaneado en PDF que conserve metadatos EXIF con coordenadas GPS de la casa del comunero o marcas del escáner municipal expone a los activistas a ejecuciones o desaparición forzada. Probabilidad Alta (3) por la naturaleza automática de los escáneres modernos; Impacto Crítico (3).
* **R-TEC-02 (Expiración TTL Soroban - Exp. 6):** Soroban implementa el modelo *State Archival*, donde las entradas de almacenamiento expiran si no se paga una renta de extensión de TTL (*time-to-live*). Si el equipo omite programar la renovación automática de las entradas de amparos históricos, el contrato archivará los datos impidiendo la consulta pública. Probabilidad Media (2); Impacto Alto (3).
* **R-TEC-03 (Sobreescritura de CIDs - Exp. 6):** Nuevas autoridades municipales o comunales cooptadas por empresas mineras podrían intentar registrar un documento apócrifo sobreescribiendo el hash de una resolución agraria auténtica ganada hace décadas. Probabilidad Media (2); Impacto Alto (3).
* **R-TEC-04 (Cuelgue en Android Go - Exp. 6):** Si la generación de hashes SHA-256 o firmas ed25519 de archivos PDF de 15 MB se realiza en el hilo principal (*Main UI Thread*) de un procesador quad-core de 1.3 GHz con 2 GB de RAM, el sistema operativo cerrará la aplicación por error ANR (*Application Not Responding*). Probabilidad Alta (3); Impacto Medio (2).
* **R-TEC-05 (Corrupción en SQLite/SQLCipher - Exp. 6):** Durante el paso de tormentas en la sierra, los cortes repentinos de energía en computadoras de los Comisariados o el agotamiento de baterías en celulares mientras se escribe en disco pueden corromper el árbol B-Tree si no se aplican transacciones seguras WAL (*Write-Ahead Logging*). Probabilidad Media (2); Impacto Alto (3).
* **R-SOC-01 (Aislamiento de Red 48-96h - Exp. 6):** La Mixteca Alta sufre cortes recurrentes de fibra óptica sobre la carretera federal 125 y caídas de antenas por deslaves. Es una certeza operativa que el sistema pasará días sin conexión. Probabilidad Alta (3); Impacto Medio (2) al existir arquitectura *offline-first*.
* **R-SOC-02 (Desconfianza Asamblearia - Exp. 4):** Si el equipo presenta el proyecto empleando terminología críptica ("criptomonedas", "smart contracts", "WASM"), las asambleas desconfiarán por temor a estafas digitales. Probabilidad Media (2); Impacto Medio (2).
* **R-SOC-03 (Pérdida de Llaves Comunales - Exp. 6):** Las autoridades de Bienes Comunales cambian cada 3 años por Usos y Costumbres. Si las llaves privadas ed25519 quedan en un teléfono personal que se pierde o se entrega a sucesores sin protocolo formal, se pierde la firma multifirma del núcleo agrario. Probabilidad Media (2); Impacto Alto (3).
* **R-SOC-04 (Barrera Lingüística - Exp. 4):** Gran parte de las autoridades de mayor edad son monolingües o tienen el mixteco (*Tu'un Sávi*) como lengua materna primaria. Una interfaz exclusivamente en español formal genera exclusión operativa. Probabilidad Media (2); Impacto Medio (2).
* **R-OPE-05 (Sobrecarga Académica eduScrum - Exp. 6):** En las semanas 8 y 12 del semestre, los exámenes parciales de la carrera de Ingeniería en Sistemas Computacionales generan cuellos de botella que pueden paralizar el tablero Kanban si no se planifican tareas asíncronas. Probabilidad Alta (3); Impacto Medio (2).
* **R-FIN-01 (Ausencia de Subvención SCF - Exp. 9):** Las subvenciones del Stellar Community Fund son altamente competitivas y no representan capital garantizado. Planificar asumiendo que los $10,000 USD llegarán el día uno puede provocar la suspensión prematura del proyecto. Probabilidad Alta (3); Impacto Crítico (3).
* **R-FIN-02 (Volatilidad de XLM - Exp. 6):** Si los fondos recibidos en XLM sufren una caída del 40% en los mercados globales de criptoactivos, el presupuesto para adquirir hardware de prueba o pagar traslados de campo se verá comprometido. Probabilidad Alta (3); Impacto Medio (2).
* **R-FIN-03 (Sobre-ingeniería Web3 - Exp. 6):** Subir el texto íntegro de resoluciones judiciales de 500 páginas a la cadena de bloques en lugar de almacenar únicamente el hash SHA-256 elevaría los costes de almacenamiento y superaría los límites de gas de Soroban. Probabilidad Media (2); Impacto Alto (3).
* **R-FIN-04 (Exposición de Datos Financieros - Exp. 6):** Revelar en blockchain cuánto dinero recaudó una comunidad por litigios o qué fondos de socorro recibe expone a las autoridades a extorsiones por parte del crimen organizado. Probabilidad Media (2); Impacto Alto (3).
* **R-FIN-05 (Atasco de Streaming en Drips - Exp. 4):** Fallas en el oráculo o en los balances de los donantes de justicia ambiental pueden pausar el flujo segundo a segundo hacia el `RepoDriver`. Probabilidad Media (2); Impacto Medio (2).

---

## 7. Diseño de Estrategias de Respuesta, Responsables y Planes de Contingencia (Tema 3.5.4)

Para cada riesgo evaluado, se formula una estrategia rigurosa acorde a los estándares del **PMBOK (Mitigar, Evitar, Transferir o Aceptar)**, asignando un responsable formal dentro del equipo **eduScrum** y especificando la medida preventiva y el plan de contingencia detallado:

| ID | Estrategia | Responsable eduScrum | Medida Preventiva (Proactiva) | Plan de Contingencia (Reactiva) | Indicador de Activación (*Trigger*) |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **R-TEC-01** | **Mitigar** | **Estudiante 3**<br>*(Ing. QA y Seguridad)* | Algoritmo local forzoso de sanitización de binarios en cliente que purga metadatos EXIF, GPS, marcas de escáner y autoría previa a la generación del hash SHA-256. | Inspección forense automatizada en CI (`exiftool` / scripts de validación); si se detecta un byte de PII, se aborta la carga y se purga el archivo en memoria segura. | Detección de cualquier etiqueta XMP, EXIF o texto identificable en el archivo procesado. |
| **R-TEC-02** | **Evitar** | **Estudiante 1**<br>*(Líder Smart Contracts)* | Configuración en el contrato Soroban de invocaciones automáticas `extend_ttl(persistent_storage)` en cada interacción, garantizando un horizonte mínimo de 100,000 bloques. | Función comunitaria abierta de bajo costo (100 stroops) que permita a cualquier nodo comunal donar gas para extender el TTL de amparos en riesgo de expiración. | El TTL restante de un recurso legal baja de 10,000 bloques (aproximadamente 14 días de vida). |
| **R-TEC-03** | **Evitar** | **Estudiante 1**<br>*(Líder Smart Contracts)* | Inclusión de la invariante criptográfica inmutable en Rust: `require(!env.storage().persistent().has(&cid))` impidiendo matemáticamente la sobreescritura. | Reversión automática de la transacción emitiendo el error determinista `ContractError::AlreadyExists`, alertando al cliente local de intento de colisión. | Retorno de error `AlreadyExists` en RPC de Stellar o intento de registro duplicado. |
| **R-TEC-04** | **Mitigar** | **Estudiante 2**<br>*(Dev. Frontend & Offline)* | Ejecución de tareas criptográficas pesadas (SHA-256, TweetNaCl ed25519) en hilos secundarios desacoplados mediante **Web Workers** sin tocar el hilo de UI. | Si el dispositivo reporta memoria RAM < 2 GB, el cliente procesa el documento en fragmentos (*chunks*) de 1 MB, mostrando un indicador de progreso sobrio. | Uso de CPU superior al 20% en el dispositivo móvil durante más de 1.5 segundos. |
| **R-TEC-05** | **Mitigar** | **Estudiante 2**<br>*(Dev. Frontend & Offline)* | Modo de diario WAL (*Write-Ahead Logging*) en SQLite, transacciones atómicas cerradas con `BEGIN IMMEDIATE` y sincronización con `PRAGMA synchronous = NORMAL`. | Reconstrucción automática del índice a partir de copias locales de seguridad y respaldo en almacenamiento no volátil en formato JSON firmado. | Detección de bloqueo de tabla o código de error `SQLITE_CORRUPT` en inicio del cliente. |
| **R-SOC-01** | **Mitigar** | **Estudiante 2**<br>*(Dev. Frontend & Offline)* | Arquitectura *Offline-First* nativa desacoplada de la red: consultas, búsquedas B-Tree e indexación local 100% funcionales sin Internet. | Sincronización en segundo plano mediante archivos CAR en memoria USB física o transferencia P2P por red LAN comunitaria vía mDNS y Bitswap en routers locales. | Falla de conexión HTTP hacia el nodo RPC durante más de 60 segundos continuos. |
| **R-SOC-02** | **Mitigar** | **Estudiante 4**<br>*(Contexto Agrario)* | Traducción del vocabulario técnico a metáforas asamblearias: el contrato inteligente se explica como *"Acta Comunal Digital Inviolable"* y la firma colegiada como *"Pase de Lista Comisariado"*. | Realización de talleres demostrativos en casas ejidales, mostrando físicamente cómo una sentencia no puede ser borrada desconectando el cable de red. | Expresión de dudas o reservas por parte de más del 30% de los asistentes a la asamblea. |
| **R-SOC-03** | **Mitigar** | **Estudiante 1 y 4**<br>*(Web3 y Contexto)* | Esquema multifirma colegiado M-de-N (ej. 3 de 5 firmas: Comisariado, Secretario, Tesorero y Consejo de Vigilancia). Cero llaves maestras individuales. | Protocolo formal de revocación y reemplazo de llaves por consenso mayoritario de la Asamblea General según Usos y Costumbres. | Notificación de extravío de teléfono o cambio formal de mesa directiva en asamblea. |
| **R-SOC-04** | **Mitigar** | **Estudiante 2 y 4**<br>*(Frontend y Contexto)* | Interfaz visual sobria basada en iconografía cultural accesible y terminología bilingüe esencial en *Tu'un Sávi* (Mixteco de la Mixteca Alta). | Asistencia guiada por jóvenes estudiantes bilingües del Tec de Tlaxiaco (*Tequio Tecnológico*) durante las asambleas comunales. | Dificultad observada de navegación por parte de autoridades tradicionales durante pruebas piloto. |
| **R-OPE-05** | **Mitigar** | **eduScrum Master**<br>*(Lizeth Nallely)* | Planificación de tareas modulares atómicas no mayores a 6 horas; asignación simétrica de 10-12 h semanales por estudiante respetando calendarios escolares. | Rebalanceo ágil del Sprint Backlog en Daily Standup; reprogramación de actividades de documentación en periodos de baja carga de exámenes. | Desviación mayor al 15% entre la línea ideal y real en el gráfico Burndown del sprint. |
| **R-FIN-01** | **Evitar Dep.** | **Estudiante 4 y Equipo**<br>*(Drips y Presupuesto)* | Diseño de arquitectura de costo cero: desarrollo 100% local en sandbox (`soroban-cli`), testnet gratuita de Stellar, nodos IPFS locales y SQLite embebido. | Ejecución del proyecto bajo el modelo de *Tequio Tecnológico Académico* utilizando infraestructura preexistente del TecNM sin necesidad de dinero en efectivo. | Notificación oficial de no selección en la convocatoria abierta de Stellar Community Fund. |
| **R-FIN-02** | **Mitigar** | **Estudiante 4**<br>*(Drips & Finanzas)* | Conversión inmediata de fondos de subvención en tokens estables respaldados en moneda fuerte (**USDC en red Stellar**) al momento de recibir los desembolsos. | Ajuste del presupuesto operativo de campo priorizando asambleas de Tlaxiaco y municipios conurbados de menor gasto de transporte. | Caída superior al 15% en la cotización de XLM frente al dólar en un periodo de 72 horas. |
| **R-FIN-03** | **Evitar** | **Estudiante 1**<br>*(Líder Smart Contracts)* | Modelo híbrido estricto: el contrato inteligente almacena exclusivamente el CID v1 (36 bytes) y el hash SHA-256 (32 bytes). Los documentos residen en IPFS local. | Auditoría del costo de gas con `cargo test` midiendo unidades de CPU de Soroban para garantizar tarifa base de 100 stroops (0.00001 XLM). | Consumo de gas superior a 500,000 instrucciones de CPU en la función de registro. |
| **R-FIN-04** | **Evitar** | **Estudiante 1 y 3**<br>*(Web3 y Seguridad)* | Cero almacenamiento de datos financieros, nombres reales de comuneros o padrones en el estado público de contratos inteligentes en Stellar. | Uso de hashes ciegos unidireccionales y firmas EIP-712 fuera de cadena (*off-chain*), publicando únicamente la prueba criptográfica de validez. | Intento de parametrización de variables con información contable en el contrato Soroban. |
| **R-FIN-05** | **Aceptar/Mit.** | **Estudiante 4**<br>*(Drips y Sostenibilidad)* | Los fondos de Drips se acumulan matemáticamente en el contrato `DripsHub` segundo a segundo, sin caducar si los nodos en la Mixteca están desconectados. | Reclamación acumulada (*claim*) de balances de streaming únicamente cuando se restablezca la conectividad estable en cabecera municipal. | Saldo acumulado en Drips no reclamado durante más de 30 días consecutivos. |

---

## 8. Análisis Profundo de Riesgos Críticos y Prioritarios

De acuerdo con el producto escalar de severidad, se identifican **cinco riesgos de alta prioridad** que concentran el mayor peligro para el éxito del proyecto y la seguridad comunal:

```
+-----------------------------------------------------------------------------------------------+
|                        TOP 5 RIESGOS CRÍTICOS Y ESTRATEGIA DE CONTENCIÓN                      |
+-------------+------------------------------------+------------+-------------------------------+
| ID Riesgo   | Descripción del Evento Crítico     | Severidad  | Impacto Territorial Evitado   |
+-------------+------------------------------------+------------+-------------------------------+
| R-TEC-01    | Fuga forense de metadatos PII/GPS  | 9 (P3 x I3)| Evita atentados o amenazas a  |
|             | en amparos territoriales           | CRÍTICO    | defensores de tierras.        |
+-------------+------------------------------------+------------+-------------------------------+
| R-FIN-01    | No asignación de subvención SCF    | 9 (P3 x I3)| Garantiza culminación del MVP |
|             | de Stellar Community Fund          | CRÍTICO    | con arquitectura de costo $0. |
+-------------+------------------------------------+------------+-------------------------------+
| R-SOC-01    | Aislamiento por caída de red 2G/CFE| 6 (P3 x I2)| Asegura operación continua en |
|             | durante 48 a 96 horas continuas    | ALTO       | asambleas sin internet.       |
+-------------+------------------------------------+------------+-------------------------------+
| R-TEC-02    | Expiración prematura TTL Soroban   | 6 (P2 x I3)| Impide pérdida de inmutabilidad|
|             | (State Archival de contratos)      | ALTO       | de sentencias agrarias.       |
+-------------+------------------------------------+------------+-------------------------------+
| R-SOC-03    | Pérdida o suplantación de llaves   | 6 (P2 x I3)| Preserva la gobernanza según  |
|             | privadas de autoridades ejidales   | ALTO       | Usos y Costumbres mixtecos.   |
+-------------+------------------------------------+------------+-------------------------------+
```

### 1. R-TEC-01: Fuga de PII y Coordenadas GPS en Expedientes Jurídicos (Severidad: 9)
* **Peligro Territorial:** El conflicto por límites de tierras y minería en la Mixteca Alta ha cobrado vidas de defensores comunitarios. Los escáneres e impresoras modernas incrustan metadatos ocultos (número de serie de máquina, coordenadas satelitales, fecha y hora exacta).
* **Solución de Ingeniería de Software:** Antes de invocar el cálculo de hash, el cliente web ejecuta un pipeline de sanitización a nivel de bytes: elimina los diccionarios `/Info` y `/Metadata` en el árbol de objetos PDF, remueve cabeceras EXIF/TIFF en imágenes y neutraliza firmas de software de origen. Esto garantiza que el documento sea **matemáticamente anónimo y forensemente limpio**.

### 2. R-FIN-01: Dependencia Fatal de Subvenciones Web3 Externas (Severidad: 9)
* **Peligro Académico:** Proyectos estudiantiles fracasan al condicionar su código a la obtención de premios o becas internacionales. Si el comité evaluador de SDF rechaza la solicitud, el proyecto queda abandonado.
* **Solución de Ingeniería de Software:** Se implementa el principio de **Frugalidad Tecnológica**: la arquitectura del MVP no tiene costos ocultos en la nube. Corre 100% en localhost con `soroban-cli`, Testnet de Stellar de costo cero, nodos IPFS locales embebidos y SQLite. Los fondos de SCF y Drips se conciben como un acelerador de escalamiento comunitario, pero el 100% del backlog académico (US-01 a US-05) se cumple sin requerir un solo centavo de capital externo.

### 3. R-SOC-01: Resiliencia ante Desconexión Total en la Sierra (Severidad: 6)
* **Peligro Operativo:** En asambleas comunales de San Esteban Atatlahuca o Santa María Cuquila no hay cobertura 4G. Depender de llamadas a servidores web centralizados convertiría la aplicación en una pantalla en blanco.
* **Solución de Ingeniería de Software:** El diseño adopta el patrón *Offline-First* estricto. La interfaz lee y escribe directamente sobre la base de datos local SQLite cifrada con SQLCipher (AES-256). La sincronización se produce mediante **paquetes diferenciales CAR de menos de 25 KB** al detectar una celda 2G o mediante transporte físico en llaves USB cifradas.

---

## 9. Trazabilidad Integral con Sprints Anteriores (Historias US-01 a US-05 y CoQ)

La presente matriz se encuentra rigurosamente enlazada con las evidencias de ingeniería de software construidas en los Sprints 1 y 2:

```
+---------------------------------------------------------------------------------------------------+
|                        TRAZABILIDAD DEL RIESGO A LO LARGO DEL CICLO EDUSCRUM                      |
+------------+-------------------------------+--------------------------------+---------------------+
| ID Riesgo  | Sprint 1: Historias de Usuario| Sprint 2: Costo Calidad (CoQ)  | Sprint 3: Tablero   |
+------------+-------------------------------+--------------------------------+---------------------+
| R-TEC-01   | US-03: Publicación Anónima DID| Prevención: $2,775 MXN (18.5h) | Tareas de purga de  |
|            | CA-3.1 (Depuración PII/EXIF)  | Pruebas forenses inyección GPS | metadatos y DID     |
+------------+-------------------------------+--------------------------------+---------------------+
| R-TEC-02   | US-01: Inmutabilidad Soroban  | Prevención: Diseño de esquemas | Configuración de    |
|            | CA-1.2 (Persistent Storage)   | TTL de expiración State Arch.  | auto-extensión TTL  |
+------------+-------------------------------+--------------------------------+---------------------+
| R-TEC-03   | US-01: Bloqueo Sobreescritura | Corrección: Fuzzing SDK Soroban| Test unitario de    |
|            | CA-1.4 (require(!storage.has))| verificación de colisiones     | invariante anti-dup |
+------------+-------------------------------+--------------------------------+---------------------+
| R-TEC-04   | US-02: Búsqueda Local B-Tree  | Corrección: Optimización SQLite| Migración de cripto |
|            | CA-2.1 (Latencia < 1.5 s)     | en terminales Android Go RAM<3G| a Web Workers       |
+------------+-------------------------------+--------------------------------+---------------------+
| R-SOC-01   | US-05: Sincronización 2G/EDGE | Corrección: $2,175 MXN (14.5h) | Pruebas simuladas   |
|            | CA-5.2 y CA-5.3 (Payload 25KB)| Simulación red 2G/50kbps/50%loss| 2G con NetEm/tc     |
+------------+-------------------------------+--------------------------------+---------------------+
| R-SOC-03   | US-04: Respaldo Colegiado WoT | Prevención: Modelado EIP-712   | Gobernanza comunal  |
|            | CA-4.1 a CA-4.4 (Quórum Usos) | multifirma sin llave master    | quórum M-de-N       |
+------------+-------------------------------+--------------------------------+---------------------+
| R-FIN-01   | Todas las historias (MVP)     | Costo Total CoQ: $4,950 MXN    | Presupuesto $27,100 |
|            | 31 Puntos de Historia base    | (33.0 horas hombre acreditadas)| Tequio Tecnológico  |
+------------+-------------------------------+--------------------------------+---------------------+
```

> **Fundamento Metodológico:** La inversión de **$4,950.00 MXN (33.0 horas hombre)** en el Costo de la Calidad durante el Sprint 2 fue precisamente la herramienta que permitió descubrir e instrumentar las medidas preventivas para R-TEC-01, R-TEC-03 y R-SOC-01 antes de comprometer el desarrollo en el Sprint 3.

---

## 10. Operatividad y Monitoreo del Tablero de Riesgos en GitHub Projects

Para garantizar que la gestión de riesgos no quede en un documento estático, se integra directamente en la operatividad ágil del repositorio mediante **GitHub Projects (Kanban)**:

1. **Campos Personalizados en el Tablero de GitHub:**
   * `Tipo_Riesgo`: [Técnico, Social/Operativo, Financiero/Web3].
   * `Probabilidad`: [1 - Baja, 2 - Media, 3 - Alta].
   * `Impacto`: [1 - Bajo, 2 - Medio, 3 - Alto].
   * `Severidad_Exposicion`: [Fórmula calculada $P \times I$].
   * `Estrategia_Respuesta`: [Mitigar, Evitar, Transferir, Aceptar].
   * `Responsable_eduScrum`: [Estudiante 1, 2, 3 o 4].
   * `Estado_Mitigacion`: [No Iniciado, En Mitigación, Mitigado, Riesgo Residual Controlado].
2. **Vinculación con Issues y Pull Requests:**
   * Cada riesgo prioritario (R-TEC-01 a R-TEC-05, R-FIN-01) cuenta con un *Issue* en GitHub etiquetado con `riesgo:critico` o `riesgo:alto`.
   * Los *Pull Requests* de desarrollo no pueden fusionarse a `main` si no acreditan la mitigación del riesgo asociado mediante pruebas automatizadas en CI (`ci_calidad.yml`).
3. **Cadencia en Ceremonias eduScrum:**
   * **Daily Standup (3 veces por semana):** La eduScrum Master pregunta explícitamente: *¿Ha surgido algún nuevo factor de riesgo en conectividad 2G o hardware Android Go?*
   * **Sprint Review:** Se presenta a los asesores agrarios la evidencia de los riesgos mitigados mediante pruebas de desconexión forzada en vivo.

---

## 11. Articulación con el Análisis de Viabilidad y Dictamen de Riesgo Residual

La Matriz de Riesgos valida de manera concluyente las tres dimensiones del **Análisis de Viabilidad Multidimensional** del proyecto:

1. **Viabilidad Técnica:** Respaldada por la neutralización de los riesgos R-TEC-01 (purga de PII), R-TEC-03 (invariantes de inmutabilidad en Soroban) y R-SOC-01 (arquitectura *offline-first* con paquetes diferenciales ≤ 25 KB).
2. **Viabilidad Operativa:** Respaldada por la adecuación cultural bilingüe en *Tu'un Sávi* (R-SOC-04), el quórum asambleario colegiado M-de-N (R-SOC-03) y la distribución equitativa de 10-12 h semanales por estudiante eduScrum (R-OPE-05).
3. **Viabilidad Financiera:** Respaldada por la total independencia del MVP respecto a financiamiento externo (R-FIN-01), operando con microcostos inmutables de 100 stroops por registro (R-FIN-03) y asegurando el flujo continuo mediante contratos Drips v2 (R-FIN-05).

```
+-----------------------------------------------------------------------------------------------+
|                       EVALUACIÓN DEL RIESGO RESIDUAL DEL PROYECTO                             |
|                                                                                               |
|  [Riesgo Inherente Inicial] = ALTO (Severidad Promedio: 6.2 / 9.0)                            |
|                 |                                                                             |
|                 v  (Aplicación de Mitigaciones Técnicas, eduScrum y Frugalidad)               |
|                                                                                               |
|  [Riesgo Residual Controlado] = BAJO / ACEPTABLE (Severidad Promedio: 2.1 / 9.0)               |
+-----------------------------------------------------------------------------------------------+
```

> ### DICTAMEN DE RIESGO: **VIABLE Y APROBADO CON CONTROLES (GO)**  
> Se confirma formalmente el dictamen **GO** para la ejecución del Sprint 3. El nivel de riesgo residual se sitúa dentro de los umbrales de tolerancia técnica y pedagógica del Instituto Tecnológico de Tlaxiaco. Los planes de contingencia garantizan que, ante el peor escenario de aislamiento de red y falta de fondos internacionales, las comunidades agrarias contarán con un sistema funcional, seguro y soberano.

---

## 12. Conclusiones y Compromiso Ético con la Región Mixteca

La gestión de riesgos desarrollada por el equipo demuestra que la ingeniería de software aplicada a problemáticas reales trasciende la codificación mecánica:
1. **Rigor Metodológico y Pedagógico:** Se identificaron y clasificaron quince riesgos en tres dimensiones requeridas, aplicando una evaluación semicuantitativa objetiva ($P \times I$), formulando estrategias concretas del PMBOK y asignando responsabilidades nominativas.
2. **Pertinencia Territorial:** Cada riesgo técnico fue analizado desde las restricciones reales de la Mixteca Alta: procesadores modestos, redes 2G degradadas, asambleas comunitarias y el deber ético supremo de proteger la vida y la tierra de los pueblos originarios.
3. **Sostenibilidad sin Dependencia:** El proyecto demuestra madurez al erradicar la subordinación económica a subsidios Web3, garantizando que el software continuará funcionando en los Comisariados de Bienes Comunales aun si los servidores remotos se apagan.

> *"La tecnología no es un fin en sí misma, sino un instrumento de justicia territorial, verdad comunal y defensa de la vida en la Región Mixteca."*  
> **Equipo eduScrum — Open Hub Tec — Instituto Tecnológico de Tlaxiaco.**
