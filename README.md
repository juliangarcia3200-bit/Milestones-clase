# Milestones Practice

Este repositorio es para practicar:
- Milestones
- Issues
- Pull Requests
- Trabajo en equipo por entregas / sprints

IMPORTANTE:
- El codigo TIENE errores intencionales.
- Ustedes deben detectar problemas, crear Issues, asignarlos a un Milestone y luego arreglarlos con un Pull Request.
- Cada Issue debe estar dentro de un Milestone.
- Cada Pull Request debe cerrar un Issue usando `Closes #N`.

## Objetivo general
Vamos a simular un sistema muy sencillo con:
1. ventas (cobro con IVA y descuentos)
2. nomina (horas extra y recargo nocturno)
3. reportes (consolidar informacion de ventas y nomina)

## Flujo de trabajo que vamos a practicar
1. Crear Milestones (Sprint 1, Sprint 2, Sprint 3).
2. Abrir Issues con titulo claro, descripcion, labels y responsable.
3. Asignar cada Issue a un Milestone.
4. Hacer una rama, corregir el problema, subir Pull Request.
5. Cerrar el Issue con `Closes #N` en el Pull Request.

## Milestones que deben crear

### Milestone: `Sprint 1 - Ventas y descuentos`
Descripcion sugerida:
Arreglar el modulo de ventas para que calcule correctamente subtotal, IVA y total con descuento, y manejar entradas invalidas.
Fecha limite sugerida: 7 dias despues de iniciar el ejercicio.

Este Milestone debe contener al menos estos Issues:
- Calculo del descuento (revisar si se esta aplicando en el orden correcto).
- Validacion de cantidades (no deberia aceptar numeros negativos).
- Pruebas con multiples productos.

### Milestone: `Sprint 2 - Nomina basica`
Descripcion sugerida:
Calcular horas extra y recargo nocturno de forma correcta y valida.
Fecha limite sugerida: 14 dias despues de iniciar el ejercicio.

Este Milestone debe contener al menos estos Issues:
- Recargo nocturno (esta incompleto).
- Manejo de horas negativas o cero.
- Documentacion del modulo (explicar formulas en comentarios/docstring).

### Milestone: `Sprint 3 - Reportes y cierre`
Descripcion sugerida:
Generar un reporte combinado de ventas y nomina, y exportarlo en CSV limpio.
Fecha limite sugerida: 21 dias despues de iniciar el ejercicio.

Este Milestone debe contener al menos estos Issues:
- Revisar el reporte final (hay columnas faltantes / calculos raros).
- Limpiar el formato del total (formato dinero).
- Actualizar README final con instrucciones paso a paso.

## Reglas para el equipo
- Cada estudiante debe:
  - Crear minimo 2 Issues.
  - Hacer minimo 1 Pull Request real que arregle algo.
  - Asignar su PR a un Issue y a un Milestone.
- No se debe trabajar directo en `main`. Siempre crear rama:
  `fix/...`, `feat/...`, `docs/...`, etc.

## Como correr el proyecto
```bash
pip install -r requirements.txt
python -m src.main
```

## Archivos principales
- src/ventas.py      -> logica de ventas (contiene errores)
- src/nomina.py      -> calculo de nomina (contiene errores)
- src/reportes.py    -> genera un mini "reporte gerencial" (contiene errores)
- src/main.py        -> script de demostracion
- data/ventas.csv    -> datos de ventas de ejemplo
- data/empleados.csv -> datos de nomina de ejemplo
- tests/             -> pruebas basicas (algunas pasaran, otras no)
- .github/ISSUE_TEMPLATE/ -> plantillas para Issues

## Entrega final esperada
- Milestones creados con descripcion y fecha.
- Issues creados, etiquetados y asignados a cada Milestone.
- Pull Requests que cierran Issues.
- Captura de pantalla del progreso de cada Milestone (porcentaje de completado).
