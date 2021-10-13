import string

# Let students generate sets with all lowercase, uppercase symbols and not unique numbers and store it as variable set
set1 = set(string.ascii_letters + string.digits[3:7] + string.digits[:5])
set2 = set(string.ascii_letters + string.digits[3:7] + string.digits[6:])

# print first set and check that all items are unique
print('set1')
print(set1)

# print the tuple that created from two sets intersection
print('set2')
print(set2)

# print the tuple that created from difference first set with second
# make slice of first 3 symbols from first tuple
# Print only symbols with numbers from second tuple
# print reversed tuples
# convert both tuples into list type