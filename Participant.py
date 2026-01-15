class Participant():
    def __init__(self,  name: str, stamina: int):
        self.name = name
        self.stamina = stamina

    
    # ********** property foo - (getter only) ***********
    @property 
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        if(isinstance(value,str) and value.strip() != ""):
            self.__name = value
        else:
            raise("invalid name")
    
    @property
    def stamina(self) -> int:
        return self.__stamina
    
    @stamina.setter
    def stamina(self, value: int) -> None:
        if(isinstance(value,int) and value > 0):
            self.__stamina = value
        else:
            raise("invalid stamina")
    

    def is_exhausted(self) -> bool:
        if(self.stamina <= 0):
            return True
        else:
            return False
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.name == other.name

    
    def __str__(self) -> str:
        return f"{self.name} (stamina: {self.stamina})"


    def __repr__(self) -> str:
         return self.name
