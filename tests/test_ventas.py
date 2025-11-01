from src.ventas import calcular_factura

def test_ventas_smoke():
    items = [
        {"producto": "A", "precio_unitario": 1000, "cantidad": 2},
        {"producto": "B", "precio_unitario": 500, "cantidad": 1},
    ]
    sub, iva, total = calcular_factura(items, iva=0.19, descuento=0.0)
    assert sub == 2500.0
    assert iva > 0
    assert total >= sub
