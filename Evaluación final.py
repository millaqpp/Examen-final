productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
}

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}


def validar_texto(valor):
    return isinstance(valor, str) and valor.strip() != ""


def validar_nombre(nombre):
    return validar_texto(nombre)


def validar_categoria(categoria):
    return validar_texto(categoria)


def validar_marca(marca):
    return validar_texto(marca)


def validar_peso(peso_kg):
    try:
        return float(peso_kg) > 0
    except (ValueError, TypeError):
        return False


def validar_si_no(valor):
    return isinstance(valor, str) and valor.strip().lower() in ('s', 'n')


def validar_precio(precio):
    try:
        return int(precio) > 0
    except (ValueError, TypeError):
        return False


def validar_unidades(unidades):
    try:
        return int(unidades) >= 0
    except (ValueError, TypeError):
        return False


def validar_codigo_nuevo(codigo):
    if not validar_texto(codigo):
        return False
    codigo = codigo.strip().upper()
    return codigo not in productos and codigo not in stock


def unidades_categoria(categoria):
    total = 0
    categoria = categoria.lower()
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria:
            if codigo in stock:
                total += stock[codigo][1]
    print(f"El total de unidades disponibles es: {total}")


def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos_stock in stock.items():
        precio, unidades = datos_stock
        if p_min <= precio <= p_max and unidades != 0:
            nombre = productos[codigo][0]
            resultados.append(f"{nombre}--{codigo}")

    resultados.sort()

    if resultados:
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.strip().upper()
    if codigo not in stock:
        return False
    stock[codigo][0] = nuevo_precio
    return True


def agregar_producto(codigo, nombre, categoria, marca, peso_kg,
                      es_importado, es_para_cachorro, precio, unidades):
    codigo = codigo.strip().upper()
    if codigo in productos or codigo in stock:
        return False

    productos[codigo] = [nombre, categoria, marca, peso_kg,
                          es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True


def eliminar_producto(codigo):
    codigo = codigo.strip().upper()
    if codigo not in productos and codigo not in stock:
        return False
    productos.pop(codigo, None)
    stock.pop(codigo, None)
    return True


def mostrar_menu():
    print("                  ")
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")


def pedir_entero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Debe ingresar valores enteros")


def opcion_1():
    categoria = input("Ingrese categoría a consultar: ")
    unidades_categoria(categoria)


def opcion_2():
    while True:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue

        if p_min < 0 or p_max < 0 or p_min > p_max:
            print("Debe ingresar valores enteros")
            continue

        busqueda_precio(p_min, p_max)
        break


def opcion_3():
    while True:
        codigo = input("Ingrese código del producto: ")

        while True:
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if nuevo_precio <= 0:
                    print("Debe ingresar valores enteros")
                    continue
                break
            except ValueError:
                print("Debe ingresar valores enteros")

        if actualizar_precio(codigo, nuevo_precio):
            print("Precio actualizado")
        else:
            print("El código no existe")

        respuesta = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
        if respuesta != 's':
            break


def opcion_4():
    codigo = input("Ingrese código del producto: ")
    if not validar_codigo_nuevo(codigo):
        print("El código no existe o ya está en uso")
        return

    nombre = input("Ingrese nombre: ")
    if not validar_nombre(nombre):
        print("El nombre no es válido")
        return

    categoria = input("Ingrese categoría: ")
    if not validar_categoria(categoria):
        print("La categoría no es válida")
        return

    marca = input("Ingrese marca: ")
    if not validar_marca(marca):
        print("La marca no es válida")
        return

    peso_kg = input("Ingrese peso (kg): ")
    if not validar_peso(peso_kg):
        print("El peso no es válido")
        return
    peso_kg = float(peso_kg)

    es_importado_str = input("¿Es importado? (s/n): ")
    if not validar_si_no(es_importado_str):
        print("Debe responder 's' o 'n'")
        return
    es_importado = es_importado_str.strip().lower() == 's'

    es_cachorro_str = input("¿Es para cachorro? (s/n): ")
    if not validar_si_no(es_cachorro_str):
        print("Debe responder 's' o 'n'")
        return
    es_para_cachorro = es_cachorro_str.strip().lower() == 's'

    precio = input("Ingrese precio: ")
    if not validar_precio(precio):
        print("El precio no es válido")
        return
    precio = int(precio)

    unidades = input("Ingrese unidades: ")
    if not validar_unidades(unidades):
        print("Las unidades no son válidas")
        return
    unidades = int(unidades)

    if agregar_producto(codigo, nombre, categoria, marca, peso_kg,
                         es_importado, es_para_cachorro, precio, unidades):
        print("Producto agregado")
    else:
        print("El código ya existe")


def opcion_5():
    codigo = input("Ingrese código del producto: ")
    if eliminar_producto(codigo):
        print("Producto eliminado")
    else:
        print("El código no existe")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ")

        if opcion == '1':
            opcion_1()
        elif opcion == '2':
            opcion_2()
        elif opcion == '3':
            opcion_3()
        elif opcion == '4':
            opcion_4()
        elif opcion == '5':
            opcion_5()
        elif opcion == '6':
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida")


if __name__ == "__main__":
    main()
