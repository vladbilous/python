class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) !=int:
            raise TypeError("Number value sould be integer!")
        self.__number = value
        if value <= 0:
            print("out of stock")
        elif 0 < value < 100:
            print("warehouse")
        else:
            print("Remote warehouse")

    def info(self):
        temp = "Material: {}, color: {}, number: {}"
        print(temp.format(self.material, self.color, self.number))


brick = Building("brick", "white", 300)
plank = Building("plank", "brown", 20)
brick.info()
plank.info()

brick.number += 50
plank.number -= 3
brick.info()
plank.info()

