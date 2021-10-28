# from module7.lab_7_1 import Building

exec(open("lab_7_1_2.py").read())


brick = Building("brick", "yellow", 200)
plank = Building("plank", "red", 10)

print(brick.material, brick.color, brick.number)
print(plank.material, plank.color, plank.number)

brick.plus(1)
plank.minus(2)
