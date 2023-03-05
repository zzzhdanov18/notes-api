from abc import ABC, abstractmethod
from src.service.abstract_crud import AbstractCRUD

class AbstractService(ABC):

    crud: AbstractCRUD

    def __init__(self, crud):
        self.crud = crud

    @abstractmethod
    def get_items_list(*args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def get_item(*args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def create_item(*args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def delete_item(*args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def mark_item_as_completed(*args, **kwargs):
        raise NotImplementedError

        