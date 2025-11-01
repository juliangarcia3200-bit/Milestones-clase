import pandas as pd
from pathlib import Path
from .ventas import calcular_factura
from .nomina import calcular_nomina

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"

def generar_reporte():
    """
    Genera un "reporte gerencial" con 2 partes:
    - resumen de ventas (subtotal, iva, total)
    - resumen de nomina por empleado

    BUGS INTENCIONALES:
    - usa nombres de columnas duros y asume que siempre existen
    - mezcla totales sin formateo de moneda
    - no valida datos negativos / raros
    """
    # Ventas
    df_v = pd.read_csv(DATA / "ventas.csv")
    items = df_v.to_dict(orient="records")
    sub, iva, total = calcular_factura(items, iva=0.19, descuento=0.05)

    # Nomina
    df_n = pd.read_csv(DATA / "empleados.csv")
    nominas = []
    for idx, row in df_n.iterrows():
        calc = calcular_nomina(
            row["basico_mensual"],
            row["horas_mes"],
            row["horas_extra"],
            row["horas_noche"],
        )
        nominas.append({
            "nombre": row["nombre"],
            "total_nomina": calc["total"],
            "extras": calc["extras"],
            "recargos": calc["recargos"],
        })

    resumen_nomina = pd.DataFrame(nominas)

    # Reporte final combinado
    reporte = {
        "ventas_subtotal": sub,
        "ventas_iva": iva,
        "ventas_total": total,
        "nomina_total_empresa": resumen_nomina["total_nomina"].sum(),  # sin formato COP
    }

    return reporte, resumen_nomina
