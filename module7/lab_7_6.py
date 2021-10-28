exec(open("lab_7_2.py").read())
exec(open("lab_7_2_2.py").read())


class MarkerFactory(Building):

    @staticmethod
    def factory(Type, *data):
        return Type(*data)

data_brick = ("brick", "white", 300)
data_plank = ("plank", "brown", 54.49, 20)
brick = MarkerFactory.factory(Building, *data_brick)
plank = MarkerFactory.factory(Market, *data_plank)

brick.info()
plank.info()

brick.plus(50)
plank.minus(3)

brick.info()
plank.info()