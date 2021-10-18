class Producto():
    
    def create_product(
        name: str = None,
        stock: int = None,
        description: str = None
    ):  
        from models.models import Producto as p

        if type(name) == int:
            raise ValueError("name can not be an integer")
        if name is not None and name.isdigit():
            raise ValueError("name can not be an integer")

        producto_validado = p(
            name=name,
            stock=stock,
            description=description).dict()

        return producto_validado
