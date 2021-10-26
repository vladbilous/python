import sys

print(sys.platform)
print(sys.version)
print(sys.getsizeof("abc"))

try:
    name, n = sys.argv
except IndexError:
    n = 11

list_var = list(range(0, int(n)))

for item in list_var:
    sys.stdout.write(str(item))
if int(n) % 2 == 0:
    sys.exit(n)