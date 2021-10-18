class Carrito():
    
    def agregar_producto(
        lista_productos: list = []
    ):
        from models.models import Carrito as c

        lista_valida = c(detalle=lista_productos).dict()

        for detalle_producto in lista_valida["detalle"]:
            if detalle_producto["producto"]["stock"] == 0:
                raise ValueError("Stock can not be 0 when adding product to cart")
            elif detalle_producto["cantidad"] == 0:
                raise ValueError("Quantity can not be 0 when adding product to cart")

        return lista_valida
        