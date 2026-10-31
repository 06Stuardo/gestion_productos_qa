from productos import GestorProductos


def leer_datos():
    nombre = input('Nombre: ').strip()
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    return nombre, precio, cantidad


def main():
    gestor = GestorProductos()
    while True:
        print('\n=== SISTEMA DE GESTIÓN DE PRODUCTOS ===')
        print('1. Registrar\n2. Buscar\n3. Actualizar\n4. Eliminar\n5. Listar\n6. Salir')
        opcion = input('Seleccione una opción: ').strip()
        if opcion == '6':
            print('Hasta pronto')
            break
        try:
            if opcion == '1':
                codigo = input('Código: ').strip()
                nombre, precio, cantidad = leer_datos()
                print('Registrado:', gestor.registrar(codigo, nombre, precio, cantidad))
            elif opcion == '2':
                print('Encontrado:', gestor.buscar(input('Código: ').strip()))
            elif opcion == '3':
                codigo = input('Código: ').strip()
                nombre, precio, cantidad = leer_datos()
                print('Actualizado:', gestor.actualizar(codigo, nombre, precio, cantidad))
            elif opcion == '4':
                print('Eliminado:', gestor.eliminar(input('Código: ').strip()))
            elif opcion == '5':
                for producto in gestor.listar():
                    print(producto)
            else:
                print('Opción inválida')
        except (ValueError, KeyError) as error:
            print('Error:', error)


if __name__ == '__main__':
    main()
