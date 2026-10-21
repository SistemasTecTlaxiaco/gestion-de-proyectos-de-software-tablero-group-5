#!/usr/bin/env python3
import json
import re

json_path = 'docs/tablero_backlog_items.json'
md_path = 'docs/04_operatividad_tablero_github_projects.md'

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

md_table = []
md_table.append('| ID Tarea | Título de la Tarea en el Tablero | Historia | Responsable Asignada | Perfil Técnico | Horas | Clasificación CoQ / Tipo | Columna Tablero | Criterios CA |')
md_table.append('| :---: | :--- | :---: | :--- | :--- | :---: | :--- | :---: | :--- |')
for t in data['tareas']:
    ca_str = ', '.join(t['criterios'])
    md_table.append(f"| `{t['id']}` | {t['titulo']} | {t['historia']} | {t['responsable']} | {t['perfil']} | {t['horas']:.1f} h | `{t['clasificacion_coq']}` | **{t['columna']}** | {ca_str} |")
md_table.append('| **TOTAL** | **Consolidación General de Tareas Sprint 3** | **-** | **4 Integrantes** | **Grupo 5** | **160.0 h** | **100% Carga Cubierta** | **4 Columnas** | **CA-1.1 a CA-4.4** |')

table_content = '\n'.join(md_table)

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(## 4\. Catálogo Maestro de Tareas del Sprint 3 \(Mapeo Completo de 160 Horas\)\n\nA continuación se detalla la totalidad de las \*\*.*?\*\* que conforman el tablero del Sprint 3, totalizando exactamente \*\*160\.0 horas de trabajo\*\*:\n\n)(?:\|.*?\n)+(?=\n---|\n## 5\.)'

replacement = f"\\g<1>{table_content}\n"

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Documento {md_path} sincronizado exitosamente con {len(data['tareas'])} tareas.")
