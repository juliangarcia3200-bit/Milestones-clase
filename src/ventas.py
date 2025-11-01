from typing import List, Dict, Tuple

def calcular_factura(items: List[Dict], iva: float = 0.19, descuento: float = 0.0) -> Tuple[float, float, float]:
    """
    Calcula subtotal, iva y total.
    items: [{"producto": str, "precio_unitario": float, "cantidad": int}, ...]
    iva: 0.19 = 19%
    descuento: 0.10 = 10%

    Retorna (subtotal, iva_calculado, total_final)
    """
    subtotal = 0.0
    for it in items:
        precio = float(it.get("precio_unitario", 0))
        cantidad = int(it.get("cantidad", 0))
        # No valida negativos
        subtotal += precio * cantidad

    iva_calc = round(subtotal * iva, 2)

    # BUG INTENCIONAL:
    # aplica el descuento DESPUES de sumar IVA.
    total_bruto = subtotal + iva_calc
    total_final = round(total_bruto * (1 - descuento), 2)

    return round(subtotal, 2), iva_calc, total_final
