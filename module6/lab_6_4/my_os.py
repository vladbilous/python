import os

cwd = os.path.abspath(".")
print("Computer name: {}".format(os.environ['COMPUTERNAME']))
print("Processor architecture: {}".format(os.environ['PROCESSOR_ARCHITECTURE']))
print("Current directory: {}".format(os.getcwd()))

os.chdir("C:/")
print(os.listdir("."))
print([file for file in os.listdir(".") if os.path.isfile(file)])
for item in os.listdir("."):
    if os.path.islink(item):
        print("Link - %s!" % item)

os.chdir(cwd)
os.mkdir("Temp")
input()
os.rmdir("Temp")