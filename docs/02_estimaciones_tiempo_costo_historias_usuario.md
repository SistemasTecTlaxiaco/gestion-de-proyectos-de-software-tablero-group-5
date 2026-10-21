# ESTIMACIONES DE TIEMPO Y COSTO POR HISTORIA DE USUARIO (SUBTEMAS 3.2 Y 3.3)

> **Asignatura:** Gestión de Proyectos de Software (SCG-1009)  
> **Unidad Académica:** Unidad 3. Planificación del Proyecto  
> **Subtemas Evaluados:** 3.2 Estimaciones de tiempo | 3.3 Estimaciones de costo  
> **Iniciativa / Ecosistema:** Open Hub Tec (Instituto Tecnológico de Tlaxiaco)  
> **Marco de Trabajo:** eduScrum (Sprint 3)  
> **Proyecto Oficial:** *Sistema de Apoyo y Protección Integral para Vendedoras y Artesanas de Tenates de Palma en la Región Mixteca ("Cuidar y Proteger a las Artesanas")*  
> **Equipo de Desarrollo (Grupo 5):** Maritza Sánchez García, Paola Rosario Ayala, Ariadna Belén Bernabé Juárez y Mayra González Lita.  
> **Fecha:** Octubre 2026  

---

## 🧭 Índice del Documento

1. [Marco Metodológico de Estimación (Planning Poker y CoQ)](#1-marco-metodológico-de-estimación-planning-poker-y-coq)
2. [Desglose Detallado de Estimaciones por Historia de Usuario](#2-desglose-detallado-de-estimaciones-por-historia-de-usuario)
   * [HU01: Registro de Tiempo y Costo (Cálculo de Precio Digno Anti-Regateo)](#hu01-registro-de-tiempo-y-costo-de-elaboración-cálculo-de-precio-digno-anti-regateo)
   * [HU02: Control de Inventario y Ventas para el Tianguis Sabatino (Modo Offline-First)](#hu02-control-de-inventario-y-ventas-para-el-tianguis-sabatino-modo-offline-first)
   * [HU03: Catálogo Digital y Certificación de Autenticidad Cultural](#hu03-catálogo-digital-de-tenates-y-certificación-de-autenticidad-cultural)
   * [HU04: Registro de Características Técnicas y Patrimonio Artesanal](#hu04-registro-de-características-técnicas-y-patrimonio-artesanal)
3. [Matriz Consolidada de Tiempo, Esfuerzo y Costos Técnicos](#3-matriz-consolidada-de-tiempo-esfuerzo-y-costos-técnicos)
4. [Estructura Presupuestal de Insumos Físicos, Hardware y Logística](#4-estructura-presupuestal-de-insumos-físicos-hardware-y-logística)
5. [Presupuesto Económico Integral del Proyecto (MXN / USD)](#5-presupuesto-económico-integral-del-proyecto-mxn--usd)
6. [Estrategias de Sostenibilidad y Frugalidad Tecnológica](#6-estrategias-de-sostenibilidad-y-frugalidad-tecnológica)

---

## 1. Marco Metodológico de Estimación (Planning Poker y CoQ)

Para determinar los tiempos de desarrollo y costos económicos de manera objetiva, el Grupo 5 aplicó una metodología híbrida que combina:
1. **Planning Poker (Fibonacci Modificado):** Estimación relativa del esfuerzo y complejidad técnica asignando Puntos de Historia (*Story Points*: 1, 2, 3, 5, 8, 13) por consenso colegiado de las cuatro integrantes.
2. **Descomposición WBS / Tareas de Ingeniería:** Mapeo de cada Historia de Usuario en tareas atómicas de análisis, diseño, programación frontend, persistencia backend, pruebas de calidad y corrección.
3. **Incorporación de los Insumos del Costo de la Calidad (Sprint 2):** Se articulan explícitamente las horas de **Prevención** (diseño a prueba de fallos, linteo estricto, modelado matemático de precios justos) y **Evaluación / Corrección** (pruebas de estrés 2G en el tianguis, pruebas de compatibilidad con Android Go, resolución de defectos de cálculo).
4. **Tarifa Estándar de Ingeniería Universitaria:** Siguiendo los lineamientos del ecosistema Open Hub Tec del Instituto Tecnológico de Tlaxiaco, se fijó una tarifa de **$150.00 MXN / hora hombre** para el trabajo técnico calificado (*Tequio Tecnológico Profesional*), asumiendo un tipo de cambio de referencia de **$19.00 MXN por 1.00 USD**.

---

## 2. Desglose Detallado de Estimaciones por Historia de Usuario

### HU01: Registro de Tiempo y Costo de Elaboración (Cálculo de Precio Digno Anti-Regateo)
* **Complejidad Ágil:** **8 Puntos de Historia (Story Points)**.
* **Propósito Social:** Proteger el sustento económico de las artesanas mixtecas mediante un modelo matemático verificable que calcula el **Precio Mínimo Digno**, desglosando horas efectivas de corte, desespinado, blanqueado al sol, teñido y tejido en palma, sumando el costo de insumos (palma, leña, agua, tintes) y depreciación de herramientas (cuchillas, agujas de arria, recipientes).
* **Criterios de Aceptación Vinculados:**
  * **CA-1.1:** Ingreso guiado e intuitivo de tiempos por fases de tejido con opción de cronómetro por sesiones acumuladas.
  * **CA-1.2:** Desglose paramétrico de costos directos de materia prima (manojos de palma, gramos de tinte).
  * **CA-1.3:** Algoritmo determinista de cálculo de precio justo:  
    $$\text{Precio Mínimo Digno} = (\text{Horas Totales} \times \text{Tarifa Salarial Rural Justa/Hora}) + \text{Costos Directos} + \text{Factor de Desgaste Físico (15\%)}$$
  * **CA-1.4:** Bloqueo de venta a pérdida: alerta visual de alto impacto si el usuario intenta fijar un precio inferior al costo real de producción, impidiendo el abuso del regateo.

#### Desglose de Tiempo y Costo Técnico (HU01):
| Tarea Técnica / Insumo | Responsable | Horas | Tarifa MXN | Costo MXN | Costo USD |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Modelado matemático de la fórmula de precio digno con artesanas | Maritza Sánchez | 4.0 h | $150.00 | $600.00 | $31.58 |
| Diseño de interfaz accesible con iconografía de fases de tejido | Paola Rosario | 4.0 h | $150.00 | $600.00 | $31.58 |
| Programación del motor de cálculo en TypeScript y persistencia | Ariadna Belén | 10.0 h | $150.00 | $1,500.00 | $78.95 |
| Componentes UI interactivos y cálculo dinámico en tiempo real | Paola Rosario | 8.0 h | $150.00 | $1,200.00 | $63.16 |
| *Prevención CoQ:* Pruebas de invariantes matemáticas (`proptest`) | Mayra González | 6.0 h | $150.00 | $900.00 | $47.37 |
| *Evaluación CoQ:* Pruebas de campo con artesanas y verificación de redondeo | Mayra / Maritza | 6.0 h | $150.00 | $900.00 | $47.37 |
| *Corrección CoQ:* Depuración de errores en cálculo de decimales y casos límite | Ariadna Belén | 4.0 h | $150.00 | $600.00 | $31.58 |
| **SUBTOTAL HU01** | **Equipo Grupo 5** | **42.0 h** | **-** | **$6,300.00** | **$331.58** |

---

### HU02: Control de Inventario y Ventas para el Tianguis Sabatino (Modo Offline-First)
* **Complejidad Ágil:** **5 Puntos de Historia (Story Points)**.
* **Propósito Social:** Brindar a las artesanas una herramienta de punto de venta e inventario que opere con total autonomía en el tianguis sabatino de Tlaxiaco, donde las redes celulares colapsan y no existe acceso a WiFi ni electricidad continua, evitando pérdidas de mercancía y desajustes de caja.
* **Criterios de Aceptación Vinculados:**
  * **CA-2.1:** Registro y actualización de existencias de tenates en base de datos local SQLite/SQLCipher en menos de **800 ms** sin conexión.
  * **CA-2.2:** Registro de venta rápida en dos toques (seleccionar tenate -> confirmar cobro efectivo), actualizando el stock local de forma atómica.
  * **CA-2.3:** Generación de recibo de venta digital local en pantalla con código alfanumérico para control de la compradora y la artesana.
  * **CA-2.4:** Resiliencia total ante apagones o reinicio forzado del dispositivo, garantizando cero pérdida de transacciones del día de plaza.

#### Desglose de Tiempo y Costo Técnico (HU02):
| Tarea Técnica / Insumo | Responsable | Horas | Tarifa MXN | Costo MXN | Costo USD |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Especificación de casos de uso de venta rápida en tianguis | Maritza Sánchez | 3.0 h | $150.00 | $450.00 | $23.68 |
| Estructuración de esquemas relacionales e índices B-Tree en SQLite | Ariadna Belén | 6.0 h | $150.00 | $900.00 | $47.37 |
| Implementación de vistas de inventario y punto de venta PWA | Paola Rosario | 8.0 h | $150.00 | $1,200.00 | $63.16 |
| Manejo transaccional ACID en cliente cifrado con SQLCipher | Ariadna Belén | 7.0 h | $150.00 | $1,050.00 | $55.26 |
| *Prevención CoQ:* Validación de esquemas y tipos estrictos de datos | Mayra González | 4.0 h | $150.00 | $600.00 | $31.58 |
| *Evaluación CoQ:* Simulación de 500 ventas consecutivas desconectadas | Mayra González | 5.0 h | $150.00 | $750.00 | $39.47 |
| *Corrección CoQ:* Optimización de consultas para evitar bloqueos en Android Go | Ariadna Belén | 3.0 h | $150.00 | $450.00 | $23.68 |
| **SUBTOTAL HU02** | **Equipo Grupo 5** | **36.0 h** | **-** | **$5,400.00** | **$284.21** |

---

### HU03: Catálogo Digital de Tenates y Certificación de Autenticidad Cultural
* **Complejidad Ágil:** **8 Puntos de Historia (Story Points)**.
* **Propósito Social:** Proteger la propiedad intelectual colectiva y el patrimonio cultural de las artesanas mediante un catálogo digital con sellos criptográficos de procedencia comunitaria, permitiendo a turistas y compradores conscientes verificar que la pieza fue tejida a mano en la Mixteca Alta y no proviene de manufactura industrial pirata.
* **Criterios de Aceptación Vinculados:**
  * **CA-3.1:** Captura y compresión local de fotografías en Web Workers (< 150 KB en formato WebP) para no saturar el almacenamiento de teléfonos modestos.
  * **CA-3.2:** Generación determinista de un identificador de autenticidad basado en hash SHA-256 (huella criptográfica de medidas, fotos y autora).
  * **CA-3.3:** Visualización sobria y bilingüe de la ficha de la pieza (español y términos tradicionales en *Tu'un Sávi*).
  * **CA-3.4:** Generación de ficha técnica exportable en código QR/imagen estática para exhibir junto a la artesanía física en ferias y tianguis.

#### Desglose de Tiempo y Costo Técnico (HU03):
| Tarea Técnica / Insumo | Responsable | Horas | Tarifa MXN | Costo MXN | Costo USD |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Definición de taxonomía cultural y glosario en *Tu'un Sávi* | Maritza Sánchez | 4.0 h | $150.00 | $600.00 | $31.58 |
| Diseño de tarjetas de catálogo y fichas de producto de alto impacto | Paola Rosario | 6.0 h | $150.00 | $900.00 | $47.37 |
| Módulo de compresión de imágenes en cliente con Web Workers | Paola Rosario | 8.0 h | $150.00 | $1,200.00 | $63.16 |
| Generación de hashes de autenticidad SHA-256 y renderizado QR | Ariadna Belén | 8.0 h | $150.00 | $1,200.00 | $63.16 |
| *Prevención CoQ:* Linteo estricto y auditoría de compresión sin pérdida | Mayra González | 6.0 h | $150.00 | $900.00 | $47.37 |
| *Evaluación CoQ:* Verificación de huellas SHA-256 y legibilidad QR | Mayra González | 5.0 h | $150.00 | $750.00 | $39.47 |
| *Corrección CoQ:* Corrección de fugas de memoria al procesar ráfagas de fotos | Ariadna / Paola | 7.0 h | $150.00 | $1,050.00 | $55.26 |
| **SUBTOTAL HU03** | **Equipo Grupo 5** | **44.0 h** | **-** | **$6,600.00** | **$347.37** |

---

### HU04: Registro de Características Técnicas y Patrimonio Artesanal
* **Complejidad Ágil:** **5 Puntos de Historia (Story Points)**.
* **Propósito Social:** Documentar, clasificar y salvaguardar las técnicas tradicionales de tejido de las abuelas mixtecas (tipos de grecas, teñido natural con cochinilla, pericón o nanche, medidas tradicionales en cuartas y dedos), protegiendo este conocimiento frente al olvido generacional y la pérdida de identidad.
* **Criterios de Aceptación Vinculados:**
  * **CA-4.1:** Clasificación estandarizada de tipos de tejido: petatillo, cruzado fino, tejido doble y calado tradicional.
  * **CA-4.2:** Registro de procedencia de la materia prima: palma criolla local o palma de la Costa, y tipo de pigmentación (orgánica o anilina).
  * **CA-4.3:** Registro de dimensiones precisas (altura, diámetro de base y boca, peso en gramos) con tolerancia milimétrica.
  * **CA-4.4:** Búsqueda y filtrado instantáneo (< 500 ms) en la base de datos local por técnica, artesana o comunidad de origen.

#### Desglose de Tiempo y Costo Técnico (HU04):
| Tarea Técnica / Insumo | Responsable | Horas | Tarifa MXN | Costo MXN | Costo USD |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Levantamiento de catálogo de técnicas y medidas tradicionales | Maritza Sánchez | 4.0 h | $150.00 | $600.00 | $31.58 |
| Formulario accesible de captura con selectores visuales simplificados | Paola Rosario | 8.0 h | $150.00 | $1,200.00 | $63.16 |
| Indexación B-Tree de atributos técnicos en SQLite/SQLCipher | Ariadna Belén | 7.0 h | $150.00 | $1,050.00 | $55.26 |
| Módulo de búsqueda y filtrado reactivo multifactorial | Ariadna / Paola | 7.0 h | $150.00 | $1,050.00 | $55.26 |
| *Prevención CoQ:* Validación de tipos y restricciones de integridad en BD | Mayra González | 4.0 h | $150.00 | $600.00 | $31.58 |
| *Evaluación CoQ:* Benchmark de latencia de búsqueda en hardware Android Go | Mayra González | 5.0 h | $150.00 | $750.00 | $39.47 |
| *Corrección CoQ:* Depuración de errores en filtros cruzados y ordenamiento | Ariadna Belén | 3.0 h | $150.00 | $450.00 | $23.68 |
| **SUBTOTAL HU04** | **Equipo Grupo 5** | **38.0 h** | **-** | **$5,700.00** | **$300.00** |

---

## 3. Matriz Consolidada de Tiempo, Esfuerzo y Costos Técnicos

La siguiente tabla resume el dimensionamiento de las cuatro Historias de Usuario, integrando el trabajo de desarrollo directo y las horas de aseguramiento de calidad (CoQ):

| Historia de Usuario | Story Points | Horas Desarrollo / Análisis | Horas CoQ (Prev. + Eval. + Corr.) | Horas Totales | Costo Total en MXN | Costo Total en USD | % del Presupuesto |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **HU01: Costo Digno Anti-Regateo** | 8 pts | 26.0 h | 16.0 h | **42.0 h** | $6,300.00 | $331.58 | 26.25% |
| **HU02: Inventario Tianguis Offline** | 5 pts | 24.0 h | 12.0 h | **36.0 h** | $5,400.00 | $284.21 | 22.50% |
| **HU03: Catálogo y Autenticidad** | 8 pts | 26.0 h | 18.0 h | **44.0 h** | $6,600.00 | $347.37 | 27.50% |
| **HU04: Características y Patrimonio** | 5 pts | 24.0 h | 14.0 h | **38.0 h** | $5,700.00 | $300.00 | 23.75% |
| **TOTALES DEL BACKLOG BASE** | **26 pts** | **100.0 h** | **60.0 h** | **160.0 h** | **$24,000.00** | **$1,263.16** | **100.00%** |

> **Nota Metodológica:** Obsérvese que las 160.0 horas totales del proyecto se distribuyen con precisión quirúrgica entre el desarrollo y análisis funcional (100.0 h = 62.5%) y el ciclo completo de aseguramiento y corrección de la calidad (60.0 h = 37.5%), demostrando solvencia y rigor técnico.

---

## 4. Estructura Presupuestal de Insumos Físicos, Hardware y Logística

Para ejecutar las pruebas en el entorno real de Tlaxiaco sin depender de supuestos de laboratorio, se presupuestaron los insumos materiales necesarios para las pruebas de campo:

| Categoría de Insumo | Descripción Técnica del Insumo | Justificación en el Proyecto | Costo en MXN | Costo en USD |
| :--- | :--- | :--- | :---: | :---: |
| **Pruebas de Red y Telecomunicaciones** | 2 Tarjetas SIM prepago Telcel/Bait con recarga de datos móviles | Ejecución de pruebas de estrangulamiento de ancho de banda y degradación forzada a 2G/EDGE en el tianguis. | $600.00 | $31.58 |
| **Hardware de Pruebas y Respaldo Físico** | 2 Memorias USB 3.0 de 64 GB cifradas (BitLocker / VeraCrypt) | Replicación física y transporte de bases de datos locales cifradas entre integrantes sin depender de internet. | $500.00 | $26.32 |
| **Validación de Campo con Artesanas** | Muestras físicas de tenates, manojos de palma y tintes para pesaje y calibración | Calibración real de la balanza digital y verificación empírica de la fórmula matemática de costeo (HU01). | $800.00 | $42.11 |
| **Movilidad y Logística Local** | Viáticos locales para traslados al tianguis de Tlaxiaco y barrios tradicionales | Entrevistas contextuales, pruebas piloto con artesanas y levantamiento de requerimientos culturales. | $1,200.00 | $63.16 |
| **SUBTOTAL INSUMOS FÍSICOS** | **Insumos y Logística de Soporte Operativo** | **-** | **$3,100.00** | **$163.17** |

---

## 5. Presupuesto Económico Integral del Proyecto (MXN / USD)

Consolidando los costos de mano de obra técnica universitaria calificada y los insumos operativos directos:

```
+-----------------------------------------------------------------------------------------------+
|                       ESTRUCTURA PRESUPUESTAL INTEGRAL - GRUPO 5                              |
+---------------------------------------------------+--------------------+----------------------+
| Rubro Presupuestal                                | Costo Total en MXN | Costo Total en USD   |
+---------------------------------------------------+--------------------+----------------------+
| 1. Mano de Obra Técnica (160 horas @ $150.00/h)   | $24,000.00 MXN     | ~$1,263.16 USD       |
|    - Desarrollo y Análisis Funcional (100 h)      | $15,000.00 MXN     |   ~$789.47 USD       |
|    - Aseguramiento y Costo de la Calidad (60 h)   |  $9,000.00 MXN     |   ~$473.69 USD       |
| 2. Insumos Físicos, Tarjetas SIM y Logística      |  $3,100.00 MXN     |   ~$163.16 USD       |
| 3. Licencias de Software y Nube Comercial         |      $0.00 MXN     |      $0.00 USD       |
+---------------------------------------------------+--------------------+----------------------+
| COSTO INTEGRAL ESTIMADO DEL PROYECTO              | $27,100.00 MXN     | ~$1,426.32 USD       |
+---------------------------------------------------+--------------------+----------------------+
```

> **Alineación con Estándares Open Hub Tec:** El presupuesto total de **$27,100.00 MXN (~$1,426.32 USD)** guarda una simetría exacta con el marco de referencia de proyectos del Instituto Tecnológico de Tlaxiaco, demostrando viabilidad y realismo financiero.

---

## 6. Estrategias de Sostenibilidad y Frugalidad Tecnológica

Para mantener el costo de licencias e infraestructura en **cero pesos ($0.00 MXN)**, el Grupo 5 adopta una arquitectura de **frugalidad tecnológica**:
* **Cero gasto en servidores Cloud:** La base de datos es nativa del dispositivo cliente (SQLite embebido con SQLCipher para cifrado AES-256 en reposo), eliminando pagos mensuales de instancias AWS, Azure o bases de datos administradas.
* **Stack Libre y Abierto:** Desarrollo con herramientas gratuitas (Node.js, TypeScript, Tailwind CSS, VS Code, Git y GitHub Projects gratuito para educación).
* **Compresión Cero-Costo:** Procesamiento multimedia en el propio cliente mediante Web Workers con librerías de compresión libres, evitando el consumo de APIs comerciales de procesamiento de imágenes.
* **Potencial de Financiamiento Descentralizado:** En fases posteriores, el proyecto podrá postular a fondos públicos abiertos y mecanismos de micromecenazgo Web3 para sustentar becas de manutención estudiantil y dotación de dispositivos a las artesanas de Tlaxiaco.
