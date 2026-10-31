import pytest
from productos import GestorProductos


def test_registrar_y_buscar():
    gestor = GestorProductos()
    gestor.registrar('P1', 'Teclado', 100, 5)
    assert gestor.buscar('P1')['nombre'] == 'Teclado'


def test_actualizar_y_verificar():
    gestor = GestorProductos()
    gestor.registrar('P1', 'Teclado', 100, 5)
    gestor.actualizar('P1', 'Teclado', 120, 8)
    assert gestor.buscar('P1')['precio'] == 120


def test_eliminar_y_confirmar():
    gestor = GestorProductos()
    gestor.registrar('P1', 'Teclado', 100, 5)
    gestor.eliminar('P1')
    with pytest.raises(KeyError):
        gestor.buscar('P1')


def test_operar_producto_inexistente():
    gestor = GestorProductos()
    with pytest.raises(KeyError):
        gestor.actualizar('NOEXISTE', 'Nuevo', 10, 1)
    with pytest.raises(KeyError):
        gestor.eliminar('NOEXISTE')


def test_codigo_duplicado():
    gestor = GestorProductos()
    gestor.registrar('P1', 'Teclado', 100, 5)
    with pytest.raises(ValueError):
        gestor.registrar('P1', 'Otro', 200, 3)
