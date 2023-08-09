from pydantic import BaseModel, Field, PositiveInt
from pydantic.types import Decimal
class ProductDetail(BaseModel):
    title: str = Field(..., max_length=128)
    descr: str = Field(..., max_length=4096)
    price: Decimal = Field(..., max_digits=8, decimal_places=2)
    count: PositiveInt