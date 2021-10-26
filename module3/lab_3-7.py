import string

# Let students generate sets with all lowercase, uppercase symbols and not unique numbers and store it as variable set
set1 = set(string.ascii_letters + string.digits[3:7] + string.digits[:5])
set2 = set(string.ascii_letters + string.digits[3:7] + string.digits[6:])

# print first set and check that all items are unique
print('\n set1:')
print(set1)

# print the tuple that created from two sets intersection
print('\n set2:')
print(set2)

tupleIntersection = tuple(set1.intersection(set2))
print('\n tupleIntersection:')
print(tupleIntersection)

# print the tuple that created from difference first set with second
tupleDifference = tuple(set1.difference(set2))
print('\n tupleDifference:')
print(tupleDifference)

# make slice of first 3 symbols from first tuple
sliceFirstTuple = tupleIntersection[:3]
print('\n sliceFirstTuple')
print(sliceFirstTuple)

# Print only symbols with numbers from second tuple
numbersFromSecondTuple = tuple(set(string.digits).intersection(set2))
print('\n numbersFromSecondTuple')
print(numbersFromSecondTuple)

# print reversed tuples
reverserTuples = tupleIntersection[::-1]
print('\n reverserTuples')
print(reverserTuples)

# convert both tuples into list type
# преобразовать оба кортежа в тип списка
tuple1List = list(tupleIntersection)
tuple2List = list(tupleDifference)

print('\n tuple1List, tuple2List')
print(tuple1List, tuple2List)