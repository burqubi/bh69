from pydantic import BaseModel, Field, PositiveInt
from pydantic.types import Decimal
from typing import Type, List, TypeVar
from io import TextIOWrapper
from abc import ABC, abstractmethod

class ProductDetail(BaseModel):
    title: str = Field(..., max_length=128)
    descr: str = Field(..., max_length=4096)
    price: Decimal = Field(..., max_digits=8, decimal_places=2)
    count: PositiveInt

Schema = TypeVar('Schema', bound=BaseModel)
Schema: Type[BaseModel]


class Parser(ABC):
    schema: Type[BaseModel]

    @classmethod
    @abstractmethod
    def parse(cls, file: TextIOWrapper, delimiter: str) -> List[Schema]:
        ...

    @classmethod
    @abstractmethod
    def dump(cls, objs: List[Schema], file: TextIOWrapper, delimiter: str) -> None:
        ...

