from ui.prompts import inputSeguro
from utils.validators import validarFecha, validarCantidad
from utils.screenControllers import pausarPantalla
from core.storage import loadData, saveData, nextId

def registrarGasto():
    print("""
=============================================
            Registrar Nuevo Gasto
=============================================
""")

    data = loadData()

    fecha = inputSeguro("Fecha (YYYY-MM-DD): ")
    if not fecha or not validarFecha(fecha):
        print(" Fecha inválida.")
        return pausarPantalla()

    cantidad = inputSeguro("Monto: ")
    if not cantidad or not validarCantidad(cantidad):
        print("Monto inválido.")
        return pausarPantalla()

    print("\nCategorías disponibles:")
    if data["categorias"]:
        for idx, cat in enumerate(data["categorias"], start=1):
            print(f"{idx}. {cat}")
    else:
        print(" No hay categorías guardadas aún.")

    print("\nEscriba una categoría existente o una nueva:")

    categoria = inputSeguro("Categoría: ")
    if not categoria:
        print(" Categoría inválida.")
        return pausarPantalla()

    categoria = categoria.lower()

    if categoria not in data["categorias"]:
        print(f" Nueva categoría detectada: '{categoria}'. Guardando...")
        data["categorias"].append(categoria)

    descripcion = inputSeguro("Descripción (opcional): ")
    if descripcion is None:
        descripcion = ""

    confirmar = inputSeguro("¿Guardar gasto? (S/N): ")
    if not confirmar or confirmar.upper() != "S":
        print("❌ Operación cancelada.")
        return pausarPantalla()

    gastoId = nextId(data)

    gasto = {
        "id": gastoId,
        "fecha": fecha,
        "categoria": categoria,
        "cantidad": float(cantidad),
        "descripcion": descripcion
    }

    data["gastos"].append(gasto)
    saveData(data)

    print("Gasto registrado correctamente.")
    pausarPantalla()
