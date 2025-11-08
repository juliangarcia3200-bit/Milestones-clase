from typing import Dict

def calcular_nomina(basico_mensual: float, horas_mes: int, horas_extra: int, horas_noche: int) -> Dict[str, float]:
    """
    Calcula nomina basica por empleado.
    - horas_extra se pagan al 150%
    - horas_noche tiene un recargo del 35%
    Retorna dict con basico, extras, recargos, total
    """
    if horas_mes <= 0:
        # BUG INTENCIONAL:
        # en vez de rechazar esto, lo reemplaza silenciosamente con 240
        horas_mes = 240
    
    if horas_extra < 0: #"validacion de negativos"
        horas_extra = 0

    if horas_noche < 0: #"validacion de negativos"
        horas_noche = 0

    valor_hora = basico_mensual / horas_mes

    extras = horas_extra * valor_hora * 1.5

    # BUG INTENCIONAL:
    # recargo nocturno solo aplica UNA VEZ, no por cada hora_noche
    recargos = valor_hora * 0.35 *horas_noche if horas_noche > 0 else 0.0 #"Se aplica por cada hora nocturna"

    total = basico_mensual + extras + recargos

    return {
        "basico": round(basico_mensual, 2),
        "extras": round(extras, 2),
        "recargos": round(recargos, 2),
        "total": round(total, 2),
    }

print(calcular_nomina(1500000, 0, -5, -3))