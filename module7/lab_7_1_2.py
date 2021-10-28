class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number
        self.place(number)

    def place(self, n):
        if n <= 0:
            print("out of stock")
        elif 0 < n < 100:
            print("warehouse")
        else:
            print("Remote warehouse")

    def plus(self, p):
        self.number = self.number + p
        self.place(self.number)

    def minus(self, m):
        self.number = self.number - m
        self.place(self.number)


brick = Building("brick", "white", 300)
plank = Building("plank", "brown", 20)

print(brick.material, brick.color, brick.number)
print(plank.material, plank.color, plank.number)

brick.plus(50)
plank.minus(3)