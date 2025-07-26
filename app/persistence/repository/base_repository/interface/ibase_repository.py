from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)
ID = TypeVar('ID')

class IBaseRepository(ABC, Generic[T, ID]):
    @abstractmethod
    def get(self, id: ID) -> Optional[T]:
        pass
    
    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        pass
    
    @abstractmethod
    def create(self, obj_in: T) -> T:
        pass
    
    @abstractmethod
    def update(self, id: ID, obj_in: T) -> Optional[T]:
        pass
    
    @abstractmethod
    def delete(self, id: ID) -> bool:
        pass
