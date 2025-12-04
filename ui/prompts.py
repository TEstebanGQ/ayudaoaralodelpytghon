def inputSeguro(mensaje):
    """
    Maneja inputs con seguridad evitando caídas por CTRL+C o CTRL+Z.
    """
    try:
        valor = input(mensaje).strip()
        if valor == "":
            print(" No puede dejar este campo vacío.")
            return None
        return valor
    except (KeyboardInterrupt, EOFError):
        print("\n Entrada cancelada por el usuario.")
        return None
