class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color

        self.number = number

    def get_number(self):
        return self.__number

    def set_number(self, value):
        if type(value) != int:
            raise TypeError("Number value sould integer!")
        self.__number = value
        if value <= 0:
            print("out of stock")
        elif 0 < value < 100:
            print("warehouse")
        else:
            print("Remote warehouse")

    def plus(self, p):
        self.set_number(self.get_number() + p)

    def minus(self, m):
        self.set_number(self.get_number() - m)

    def info(self):
        temp = "Material: {}, color: {}, number: {}"
        print(temp.format(self.material, self.color, self.__number))

    number = property(get_number, set_number)


brick = Building("brick", "white", 300)
plank = Building("plank", "brown", 20)

brick.info()
plank.info()

brick.plus(50)
plank.minus(3)
brick.info()
plank.info()

brick.number -= 50
plank.number += 3
brick.info()
plank.info()