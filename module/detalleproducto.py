class DetalleProducto:

    def crear_detalle(
        cantidad: int,
        producto: dict
    ):
        from models.models import Producto as p, DetalleProducto as dp

        producto_validado = p(**producto).dict()

        if cantidad>producto_validado["stock"]:
            raise ValueError("Can't add more products than avaliable in stock")
        else:
            producto_validado["stock"] = producto_validado["stock"]-cantidad
            
        detalle_validado = dp(
            cantidad=cantidad,
            producto=producto_validado).dict()

        return detalle_validado
        
