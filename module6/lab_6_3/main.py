# Не завершив лабораторну не знаю як
# Import data from definitions.py as defs

import definitions as defs

# Create variable – main_var with some string value
main_var = 'some string value'

# if __name__ == "__main__":
#     defs.function_two(main_var)
# else:
#     print("Execution module:{}".format(__file__))

if __name__ == "__main__":
    defs.function_two(main_var)
else:
    print("Execution module: {}".format(__file__))
