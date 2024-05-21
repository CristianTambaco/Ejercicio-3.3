print("Determinar el mejor regalo para comprar por el 14 de Febrero")
presupuesto = float(input("Ingrese su presupuesto para el regalo: "))

def seleccionar_regalo(presupuesto):
    if presupuesto <= 10.00:
        return "Tarjeta"
    elif presupuesto <= 100.00:
        return "Chocolates"
    elif presupuesto <= 250.00:
        return "Flores"
    elif presupuesto > 250.00:
        return "Anillo"
    else:
        return "Presupuesto no válido"

regalo = seleccionar_regalo(presupuesto)
print(f"La mejor opción de regalo para comprar es: {regalo}")
