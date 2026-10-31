class GestorProductos:
    def __init__(self):
        self.productos = {}

    def registrar(self, codigo, nombre, precio, cantidad):
        self._validar(codigo, nombre, precio, cantidad)
        if codigo in self.productos:
            raise ValueError('El código ya existe')
        self.productos[codigo] = {'codigo': codigo, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        return self.productos[codigo].copy()

    def buscar(self, codigo):
        if codigo not in self.productos:
            raise KeyError('Producto inexistente')
        return self.productos[codigo].copy()

    def actualizar(self, codigo, nombre, precio, cantidad):
        if codigo not in self.productos:
            raise KeyError('Producto inexistente')
        self._validar(codigo, nombre, precio, cantidad)
        self.productos[codigo] = {'codigo': codigo, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        return self.buscar(codigo)

    def eliminar(self, codigo):
        if codigo not in self.productos:
            raise KeyError('Producto inexistente')
        return self.productos.pop(codigo)

    def listar(self):
        return [producto.copy() for producto in self.productos.values()]

    @staticmethod
    def _validar(codigo, nombre, precio, cantidad):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError('Código obligatorio')
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError('Nombre obligatorio')
        if isinstance(precio, bool) or not isinstance(precio, (int, float)) or not 0 <= precio < float('inf'):
            raise ValueError('Precio inválido')
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError('Cantidad inválida')
