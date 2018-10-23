# 组合:一个对象的属性值是另外一个类的对象


class Dog:
    def __init__(self,name,aggr,hp,kind):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.kind = kind

    def bite(self,obj):
        obj.hp -= self.aggr


class Persion:
    def __init__(self,name,aggr,hp,sex):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.kind = sex
        self.money = 100
        self.weapon = None

    def attach(self,obj):
        obj.hp -= self.aggr

    def get_weapon(self,weapon):
        if self.money >= weapon.price:
            self.money -= weapon.price
            self.weapon = weapon
            self.aggr += weapon.aggr
        else:
            print('金币不足，无法获取武器')


class Weapon:
    def __init__(self,name,aggr,njd,price):
        self.name = name
        self.aggr = aggr
        self.njd = njd
        self.price = price

    def ult(self,obj):
        if self.njd > 0:
            obj.hp -= self.aggr * 2
            self.njd -= 1


dog = Dog('阿黄',20,500,'中华田园犬')
persion = Persion('小明',10,200,'男')
print(dog.hp,persion.hp)
print('======')
# 人狗各攻击对方一次
persion.attach(dog)
dog.bite(persion)
print(dog.hp,persion.hp)
print('======')
# 人使用武器,人狗再次各攻击对方一次
w = Weapon('打狗棒',100,3,100)
persion.get_weapon(w)
persion.attach(dog)
dog.bite(persion)
print(dog.hp,persion.hp)
print('======')
# 人使用武器的大招，人狗再次各攻击对方一次
persion.weapon.ult(dog)
dog.bite(persion)
print(dog.hp,persion.hp)
print('======')