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
         # Validacion de negativos y Excepciones
        producto = it.get("producto", "Desconocido")
        try:
            precio = float(it.get("precio_unitario", 0))
            cantidad = int(it.get("cantidad", 0))
        
            if precio < 0:
                raise ValueError("El precio del producto '{producto}' no puede ser negativo.")
            if cantidad < 0:
                raise ValueError("La cantidad del producto '{producto}' no puede ser negativa.")
                                                
            subtotal += precio * cantidad
    
        except ValueError as e:
            print(f"[AVISO] Producto ignorado: {producto}. No se facturó.")
        except Exception as e:
            print(f"[ERROR] ERROR procesando un producto: {producto}. No se facturó.")

    subtotal_neto = subtotal * (1 - descuento)
        
    iva_calc = round(subtotal_neto * iva, 2)

    # aplica el descuento Antes de sumar IVA.
    
    total_bruto = subtotal_neto + iva_calc
    total_final = round(total_bruto, 2)

    return round(subtotal_neto, 2), iva_calc, total_final

print(calcular_factura([
    {"producto": "Camisa", "precio_unitario": -10000, "cantidad": 2},
    {"producto": "Pantalon", "precio_unitario": 20000, "cantidad": 1},
], iva=0.19, descuento=0.10))