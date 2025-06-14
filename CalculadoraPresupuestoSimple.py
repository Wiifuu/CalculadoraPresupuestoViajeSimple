# Leer README.md si estas aprendiendo

def comprobar(valor, cadena, flag):
    while True:
        try:
            if flag == 1 and valor.strip() != "": return valor.title()
            elif flag == 2 and int(valor) > 0: return int(valor)
            elif flag == 3 and float(valor) > 0: return float(valor)
            elif flag == 4 and valor.strip().lower() in ("si", "no"): return valor.strip().lower()
            else: raise ValueError
        except ValueError:
            print(f"Entrada inválida. Ingrese {cadena}")
            if flag == 1: valor = input("Ingrese su nombre: ")
            elif flag == 2: valor = input("Ingrese número de días de viaje: ")
            elif flag == 3: valor = input("Ingrese el gasto diario estimado: ")
            elif flag == 4: valor = input("¿Desea incluir el tour adicional por $45000? (sí/no): ")

def ingresar_datos():
    nombre = comprobar(input("\nIngrese su nombre: "),"un nombre que no esté vacío.", 1)
    dias  = comprobar(input("\nIngrese número de días de viaje: "), "un número de días mayor a 0.", 2)
    gasto_diario = comprobar(input("\nIngrese el gasto diario estimado: "), "un valor para gastos diarios mayor a 0.", 3)
    tour = comprobar(input("\n¿Desea incluir el tour adicional por $45000? (sí/no): "), "explícitamente 'si' o 'no'.", 4)
    return nombre, dias, gasto_diario, tour

def calcular_total(dias, gasto_diario, tour):
    return dias * gasto_diario if tour == 'no' else dias * gasto_diario + 45000

def mostrar(nombre, dias, gasto_diario, tour, total):
    print (f"""
           ------ PRESUPUESTO DE VIAJE ------
           Nombre: {nombre}
           Días de viaje: {dias}
           Gasto diario: ${gasto_diario:,.2f}
           Tour adicional: {'Sí' if tour == 'si' else 'No'}
           Total estimado: ${total:,.2f}
    """)

# Main
nombre, dias, gasto_diario, tour = ingresar_datos()
total = calcular_total(dias, gasto_diario, tour)
mostrar(nombre, dias, gasto_diario, tour, total)