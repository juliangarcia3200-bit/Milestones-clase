from src.nomina import calcular_nomina

def test_nomina_smoke():
    calc = calcular_nomina(1000000, 240, 5, 2)
    assert calc["basico"] == 1000000
    assert calc["total"] >= calc["basico"]
