from Participant import Participant

class Player(Participant):
    def __init__(self, name, stamina, skill: int):
        super().__init__(name, stamina)
        self.skill = skill

    @property
    def skill(self) -> int:
        return self.__skill
    
    @skill.setter
    def skill(self, value: int) -> None:
        if(isinstance(value,int) and value > 0 and value <= 100):
            self.__skill = value
    
    def __lt__(self, value) -> bool:
        if not isinstance(self,value):
            return NotImplemented
        return self.skill < value.skill
