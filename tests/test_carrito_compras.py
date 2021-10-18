import pytest
skip_test = pytest.mark.skipif(False, reason="skip")

#3
@skip_test
def test_create_carrito_quantity_is_cero():
    from module.producto import Producto
    from module.detalleproducto import DetalleProducto
    from module.carrito import Carrito

    name = "producto 1"
    stock= 5
    description= "description"

    producto_valido = Producto.create_product(
        name=name, 
        stock=stock, 
        description=description)
            
    assert producto_valido["name"] == name
    assert producto_valido["stock"] == stock
    assert producto_valido["description"] == description

    cantidad = 0
    with pytest.raises(ValueError, match="cantidad can not be 0"):
        detalle_producto = DetalleProducto.crear_detalle(
            cantidad=cantidad,
            producto= producto_valido
        )

#5
@skip_test
def test_create_carrito():
    from module.producto import Producto
    from module.detalleproducto import DetalleProducto
    from module.carrito import Carrito

    name = "producto 1"
    stock=10
    description= "description"

    producto_valido = Producto.create_product(
        name=name, 
        stock=stock, 
        description=description)
    
    assert producto_valido["name"] == name
    assert producto_valido["stock"] == stock
    assert producto_valido["description"] == description

    producto_valido_2 = Producto.create_product(
        name=name, 
        stock=stock, 
        description=description)
    
    assert producto_valido_2["name"] == name
    assert producto_valido_2["stock"] == stock
    assert producto_valido_2["description"] == description

    cantidad = 1
    detalle_producto = DetalleProducto.crear_detalle(
        cantidad=cantidad,
        producto= producto_valido
    )

    assert detalle_producto["cantidad"] == cantidad

    detalle_producto_2 = DetalleProducto.crear_detalle(
        cantidad=cantidad,
        producto= producto_valido
    )

    assert detalle_producto_2["cantidad"] == cantidad

    lista_detalles =[detalle_producto, detalle_producto_2]

    carrito = Carrito.agregar_producto(lista_productos=lista_detalles)

    assert len(carrito) > 0

    #6
@skip_test
def test_nombre_producto_distinto_null():
    from module.producto import Producto

    with pytest.raises(ValueError, match="none is not an allowed value"):
        crear_producto = Producto.create_product(
            name=None, 
            stock=1, 
            description="descripcion")

#7
@skip_test
def test_nombre_producto_numerico():
    from module.producto import Producto

    with pytest.raises(ValueError, match="name can not be an integer"):
        crear_producto = Producto.create_product(
            name=11111, 
            stock=1, 
            description="descripcion")

#8
@skip_test
def test_nombre_producto_name_too_long():
    from module.producto import Producto
    from random import choice
    from string import ascii_uppercase

    name = ''.join(choice(ascii_uppercase) for i in range(11))
    with pytest.raises(ValueError, match="ensure this value has at most 10 characters"):
        crear_producto = Producto.create_product(
            name=name, 
            stock=1, 
            description="descripcion")

#15
@skip_test
def test_stock_producto_distinto_null():
    from module.producto import Producto

    with pytest.raises(ValueError, match="none is not an allowed value"):
        crear_producto = Producto.create_product(
            name="juan", 
            stock=None, 
            description="descripcion")

#17
@skip_test
def test_stock_valido_name_nulo_descripcion_nula():
    from module.producto import Producto

    with pytest.raises(ValueError, match="none is not an allowed value"):
        crear_producto = Producto.create_product(
            name=None, 
            stock=0, 
            description=None)


#18
@skip_test
def test_descripcion_valido_name_nulo_stock_nulo():
    from module.producto import Producto

    with pytest.raises(ValueError, match="none is not an allowed value"):
        crear_producto = Producto.create_product(
            name=None, 
            stock=None, 
            description="descripcion")

#19
@skip_test
def test_create_detalle_producto():
    from module.producto import Producto
    from module.detalleproducto import DetalleProducto

    name = "producto 1"
    stock=10
    description= "description"

    producto_valido = Producto.create_product(
        name=name, 
        stock=stock, 
        description=description)
    
    assert producto_valido["name"] == name
    assert producto_valido["stock"] == stock
    assert producto_valido["description"] == description

    cantidad = 1
    detalle_producto = DetalleProducto.crear_detalle(
        cantidad=cantidad,
        producto= producto_valido
    )

    assert detalle_producto["cantidad"] == cantidad
    assert detalle_producto["producto"]["stock"] == stock-cantidad

    #20
    @skip_test
def test_create_detalle_producto_cantidad_negativa():
    from module.producto import Producto
    from module.detalleproducto import DetalleProducto

    name = "producto 1"
    stock=10
    description= "description"

    producto_valido = Producto.create_product(
        name=name, 
        stock=stock, 
        description=description)
    
    assert producto_valido["name"] == name
    assert producto_valido["stock"] == stock
    assert producto_valido["description"] == description

    cantidad = 0
    with pytest.raises(ValueError, match="cantidad can not be 0"):

        detalle_producto = DetalleProducto.crear_detalle(
            cantidad=cantidad,
            producto=producto_valido
        )
