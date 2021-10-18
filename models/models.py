from pydantic import BaseModel , validator
from pydantic.fields import Field

class Producto(BaseModel):
    name: str = Field(max_length=10)
    stock: int = Field(gt=-1)
    description: str 
    
class DetalleProducto(BaseModel):
    cantidad: int
    producto: Producto

    @validator("cantidad", allow_reuse=True)
    def can_not_be_none(cls, v):
        if v is None:
            raise ValueError(f"cantidad can not be None")
        elif v <0:
            raise ValueError("cantidad can not be less than 0")
        elif v == 0:
            raise ValueError("cantidad can not be 0")
        return v

class Carrito(BaseModel):
    detalle: list[DetalleProducto]
