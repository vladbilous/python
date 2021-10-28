# Encapsulation
class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.set_number(number)
        self.place(number)

    def place(self, n):
        if n <= 0:
            print("out of stock")
        elif 0 < n < 100:
            print("warehouse")
        else:
            print("Remote warehouse")

    def plus(self, p):
        self.set_number(self.get_number() + p)

    def minus(self, m):
        self.set_number(self.get_number() - m)

    def get_number(self):
        return self.__number

    def set_number(self, value):
        if type(value) != int:
            raise TypeError("Number value sould be integer!")
        self.__number = value
        self.place(self.__number)

    def info(self):
        temp = "Material: {}, color: {}, number: {}"
        print(temp.format(self.material, self.color, self.__number))


brick = Building("brick", "white", 300)
plank = Building("plank", "brown", 20)

brick.info()
plank.info()

brick.plus(50)
plank.minus(3)

brick.info()
plank.info()
