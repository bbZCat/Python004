from animal import Animal
from cat import Cat
from dog import Dog

class Zoo(object):
    __animals = {}
    
    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        name = animal.name
        #如果不存在则新增
        if name not in self.__animals:
            self.__animals[name] = animal
            #如果是Cat的实例则设置Cat属性
            if isinstance(animal, Cat):
                #print(animal.__class__)
                self.__setattr__('Cat', True)

    @property
    def animals(self):
        return self.__animals.values()

#=======================================================================
if __name__ == "__main__":
    #实例化动物园
    zoo = Zoo('时光动物园')
    print(f'欢迎来到：{zoo.name}')

    #实例化一只猫
    cat1 = Cat("大花猫", "食肉", "小", "温顺")
    print(f'{cat1.name} 是否合适做宠物：{not(cat1.is_ferocious)}')
    cat1.speak()

    #实例化一只狗
    dog1 = Dog("大狼狗", "食肉", "大", "凶猛")
    print(f'{dog1.name} 是否合适做宠物：{not(dog1.is_ferocious)}')
    dog1.speak()

    #增加一只猫到动物园
    zoo.add_animal(cat1)
    #增加一只狗到动物园
    zoo.add_animal(dog1)
    
    #列举动物园中的所有动物
    animals = zoo.animals
    for animal in animals:
        print(f'动物园里有个：{animal.name}，很{animal.characters}')

    #动物园是否有猫这种动物
    have_cat = hasattr(zoo, 'Cat')
    print(f'动物园中是否有猫：{have_cat}')
