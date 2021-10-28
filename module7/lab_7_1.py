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
            print("Remove warehouse")

obl1 = Building('wood', 'brown', 200)
obl2 = Building('stone', 'gray', 10)
