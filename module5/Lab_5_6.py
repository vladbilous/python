# 1. Create list with 5 elements of string data
string_list = ['string1', 'string2', 'string3', 'string4', 'string5']
# 2. Create empty config.data file
# 4. Create simple python decorator were:
# a. Created file object with path – “config.data” and mode “r+”
# b. writeConfig function called
# c. close file object
def simpleDecor(func):
    def decor(item):
        file = open("config.data", "r+")
        func(file, item)
        file.close()
    return decor

# 3. Create function “writeConfig” that will do:
# a. Take two arguments (file object and string data)
# b. Read data from file and if in config.data lines -
# “Configuration file! Do not modify!”, skip step else write above line.
# c. Write second argument (string data) from new line, ex. - “string_data;”
@simpleDecor
def writeConfig(file, stringData):
    if "Configuration file! Do not modify!" in file.read():
        file.write("%s\n"%(stringData))
    else:
        file.write("Configuration file! Do not modify!\n"+\
                   "%s;\n"%(stringData))
# 5. Use for loop for write each item from list created before
for item in string_list:
    writeConfig(item)
# 6. Use breakpoint after every iteration and check config.data file content