from abc import ABC, abstractmethod
from typing import Type, TypeVar
from pydantic import BaseModel
from io import TextIOWrapper
class Parser(ABC):
    schema: Type[BaseModel]

    @classmethod
    @abstractmethod
    def parse(cls, file: TextIOWrapper, delimiter: str) -> List[Schema]:
        ...

    @classmethod
    @abstractmethod
    def dump(cls, objs: list, file: TextIOWrapper, delimiter: str) -> None:
        ...
