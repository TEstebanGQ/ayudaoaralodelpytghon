from datetime import datetime, timedelta

def totalDiario(gastos):
    hoy = datetime.now().strftime("%Y-%m-%d")
    return sum(g["cantidad"] for g in gastos if g["fecha"] == hoy)

def totalSemanal(gastos):
    hoy = datetime.now()
    hace7 = hoy - timedelta(days=7)
    return sum(
        g["cantidad"]
        for g in gastos
        if hace7 <= datetime.strptime(g["fecha"], "%Y-%m-%d") <= hoy
    )

def totalMensual(gastos):
    hoy = datetime.now()
    return sum(
        g["cantidad"]
        for g in gastos
        if datetime.strptime(g["fecha"], "%Y-%m-%d").month == hoy.month
    )
