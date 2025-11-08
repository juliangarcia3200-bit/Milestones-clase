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
    productos_facturados = []
    
    print("\n=== Detalle de Factura ===")
    print("{:<20} {:>10} {:>10} {:>10}".format("Producto", "Precio U.", "Cantidad", "Total"))
    print("-" * 60)
    
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
            
            # Calculo del subtotal por item                                   
            subtotal_item = precio * cantidad
            subtotal += subtotal_item
            productos_facturados.append((producto, precio, cantidad, subtotal_item))
            print("{:<20} {:>10.2f} {:>10} {:>10.2f}".format(producto, precio, cantidad, subtotal_item))
            
        except ValueError as e:
            print(f"[AVISO] Producto ignorado: {producto}. No se facturó.")
        except Exception as e:
            print(f"[ERROR] ERROR procesando un producto: {producto}. No se facturó.")
    
    print("-" * 60)

    subtotal_neto = subtotal * (1 - descuento)
    iva_calc = round(subtotal_neto * iva, 2)
    total_bruto = subtotal_neto + iva_calc
    total_final = round(total_bruto, 2)
    
    print(f"{'Subtotal:':>43} {subtotal:>10.2f}")
    print(f"{'Descuento:':>43} {subtotal - subtotal_neto:>10.2f}")
    print(f"{'Subtotal Neto:':>43} {subtotal_neto:>10.2f}")
    print(f"{'IVA:':>43} {iva_calc:>10.2f}")
    print(f"{'Total:':>43} {total_final:>10.2f}")

    return round(subtotal_neto, 2), iva_calc, total_final

calcular_factura([
    {"producto": "Camisa", "precio_unitario": -10000, "cantidad": 2},
    {"producto": "Pantalon", "precio_unitario": 20000, "cantidad": 1},
    {"producto": "Zapatos", "precio_unitario": 50000, "cantidad": 1},
    {"producto": "Corbata", "precio_unitario": 15000, "cantidad": -1},
], iva=0.19, descuento=0.10)