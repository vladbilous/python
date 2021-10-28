# Inheritance
exec(open("lab_7_2.py").read())

class Market(Building):
    def __init__(self, material, color, price, number=0):
        super().__init__(material, color, number=number)
        self.price = price

    def info(self):
        temp = "Material: {}, color: {}, number: {}, place: {}"
        print(temp.format(self.material, self.color, self.get_number(), self.price))


brick = Market("brick", "white", 85.26, 300)
plank = Market("plank", "brown", 54.49, 20)

brick.info()
plank.info()

brick.plus(50)
plank.minus(3)

brick.info()
plank.info()
