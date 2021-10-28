# Polymorphism
exec(open("lab_7_2.py").read())


class Shop(Building):

    def plus(self, p):
        self.set_number(self.get_number() + p//2)

    def minus(self, m):
        self.set_number(self.get_number() - m//2)


brick = Shop("brick", "white", 300)
plank = Shop("plank", "brown", 20)
brick.info()
plank.info()

brick.plus(50)
plank.minus(3)
brick.info()
plank.info()