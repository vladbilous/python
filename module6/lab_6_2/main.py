# 1. Create module with name – main.py were define next:
# a. Import data from definitions.py as defs

import definitions as defs

# b. Create variable – main_var with some string value
main_var = 'string value'

if __name__ == "__main__":
    defs.function_two(main_var)
else:
    print("Execution module:{}".format(__file__))
