from abc import ABC, abstractmethod


class AbstractCRUD(ABC):

    def __init__(self, db):
        self.db = db

    @abstractmethod
    def get_detail(*args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def get_list(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def create(*args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def delete(*args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def mark_as_completed(*args, **kwargs):
        raise NotImplementedError
    


    


