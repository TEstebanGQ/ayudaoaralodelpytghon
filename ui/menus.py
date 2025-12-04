from ui.prompts import inputSeguro
from utils.screenControllers import limpiarPantalla, pausarPantalla
from core.gastoManager import registrarGasto
from core.storage import loadData
from core.filtros import filtrarCategoria, filtrarRangoFechas
from core.reportes import totalDiario, totalSemanal, totalMensual
from tabulate import tabulate
from utils.validators import validarFecha

def menuPrincipal():
    while True:
        limpiarPantalla()
        print("""
=============================================
        Simulador de Gasto Diario
=============================================
1. Registrar nuevo gasto
2. Listar gastos
3. Calcular totales
4. Salir
=============================================
""")

        opcion = inputSeguro("Seleccione una opción: ")

        if opcion == "1":
            registrarGasto()
        elif opcion == "2":
            listarGastosMenu()
        elif opcion == "3":
            calcularTotalesMenu()
        elif opcion == "4":
            salir = inputSeguro("¿Desea salir? (S/N): ")
            if salir and salir.upper() == "S":
                break
        else:
            print("Opción inválida.")
            pausarPantalla()

def listarGastosMenu():
    data = loadData()
    gastos = data["gastos"]

    while True:
        limpiarPantalla()
        print("""
=============================================
                Listar Gastos
=============================================
1. Ver todos los gastos
2. Filtrar por categoría
3. Filtrar por rango de fechas
4. Volver
=============================================
""")

        opcion = inputSeguro("Seleccione una opción: ")

        if opcion == "1":
            mostrarTabla(gastos)

        elif opcion == "2":
            cat = inputSeguro("Categoría: ")
            lista = filtrarCategoria(gastos, cat)
            mostrarTabla(lista)

        elif opcion == "3":
            inicio = inputSeguro("Fecha inicio (YYYY-MM-DD): ")
            fin = inputSeguro("Fecha fin (YYYY-MM-DD): ")
            if validarFecha(inicio) and validarFecha(fin):
                lista = filtrarRangoFechas(gastos, inicio, fin)
                mostrarTabla(lista)
            else:
                print("Fechas inválidas.")
                pausarPantalla()

        elif opcion == "4":
            break
        else:
            print(" Opción inválida.")
            pausarPantalla()

def mostrarTabla(lista):
    if not lista:
        print(" No hay registros.")
        return pausarPantalla()

    tabla = [
        [g["id"], g["fecha"], g["categoria"], g["cantidad"], g["descripcion"]]
        for g in lista
    ]

    print(tabulate(tabla, headers=["ID", "Fecha", "Categoría", "Monto", "Descripción"]))
    pausarPantalla()

def calcularTotalesMenu():
    data = loadData()
    gastos = data["gastos"]

    limpiarPantalla()
    print("""
=============================================
            Totales de Gastos
=============================================
""")

    print(f"Total diario: ${totalDiario(gastos):.2f}")
    print(f"Total semanal: ${totalSemanal(gastos):.2f}")
    print(f"Total mensual: ${totalMensual(gastos):.2f}")

    pausarPantalla()
