import pandas as pd
from pathlib import Path
from .ventas import calcular_factura
from .nomina import calcular_nomina
from .reportes import generar_reporte

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"

def demo_ventas():
    print("=== DEMO VENTAS ===")
    df = pd.read_csv(DATA / "ventas.csv")
    items = df.to_dict(orient="records")
    sub, iva, total = calcular_factura(items, iva=0.19, descuento=0.05)
    print("Subtotal:", sub)
    print("IVA:", iva)
    print("Total (c/ descuento):", total)

def demo_nomina():
    print("\n=== DEMO NOMINA ===")
    df = pd.read_csv(DATA / "empleados.csv")
    for _, row in df.iterrows():
        calc = calcular_nomina(
            row["basico_mensual"],
            row["horas_mes"],
            row["horas_extra"],
            row["horas_noche"],
        )
        print(f"{row['nombre']}: total={calc['total']} extras={calc['extras']} recargos={calc['recargos']}")

def demo_reportes():
    print("\n=== DEMO REPORTE GERENCIAL ===")
    resumen_empresa, detalle_nomina = generar_reporte()
    print("Resumen empresa:", resumen_empresa)
    print("Detalle nomina:")
    print(detalle_nomina)

if __name__ == "__main__":
    demo_ventas()
    demo_nomina()
    demo_reportes()
