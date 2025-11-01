from src.reportes import generar_reporte

def test_reportes_smoke():
    resumen_empresa, detalle_nomina = generar_reporte()
    assert "ventas_total" in resumen_empresa
    assert "nomina_total_empresa" in resumen_empresa
    assert not detalle_nomina.empty
