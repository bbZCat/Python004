from abc import abstractmethod, ABCMeta


class Animal(metaclass=ABCMeta):
    # 是否凶猛动物
    __Is_Ferocious = False

    @property
    def is_ferocious(self):
        return self.__Is_Ferocious

    def __init__(self, name, types, shapes, characters):
        self.name = name
        self.types = types
        self.shapes = shapes
        self.characters = characters
        # 含肉食性，体型中或大， 性格凶猛字样为凶猛动物，不适合作为宠物
        if str(self.types).find('肉') != -1\
                and (str(self.shapes).find('中') != -1 or str(self.shapes).find('大') != -1)\
                and str(self.characters).find('凶猛') != -1:
            self.__Is_Ferocious = True

    @abstractmethod
    def speak(self):
        pass
