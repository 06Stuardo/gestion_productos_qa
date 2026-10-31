import pytest
from productos import GestorProductos


def test_registro():
    gestor = GestorProductos()
    assert gestor.registrar('P1', 'Mouse', 50, 2)['nombre'] == 'Mouse'


def test_busqueda():
    gestor = GestorProductos()
    gestor.registrar('P1', 'Mouse', 50, 2)
    assert gestor.buscar('P1')['precio'] == 50


def test_actualizacion():
    gestor = GestorProductos()
    gestor.registrar('P1', 'Mouse', 50, 2)
    assert gestor.actualizar('P1', 'Mouse nuevo', 60, 3)['cantidad'] == 3


def test_eliminacion():
    gestor = GestorProductos()
    gestor.registrar('P1', 'Mouse', 50, 2)
    assert gestor.eliminar('P1')['codigo'] == 'P1'


def test_validacion_negativos():
    gestor = GestorProductos()
    with pytest.raises(ValueError):
        gestor.registrar('P1', 'Mouse', -1, 2)
    with pytest.raises(ValueError):
        gestor.registrar('P2', 'Mouse', 10, -2)
