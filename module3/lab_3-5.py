textList = list(input("input text : "))
print(textList)

# print first symbol of list
firstSymbol = textList[0]
print('firstSymbol :')
print(firstSymbol)

# print the last symbol of list
lastSymbol = textList[-1]
print('lastSymbol :')
print(lastSymbol)

# print 3rd from beginning and 3rd from the end symbols
beginning3 = textList[2]
print(beginning3)

end3 = textList[-3]
print(end3)

# make slice of first 10 symbols
firstTenSlice = textList[0:10]
print('firstTenSlice :')
print(firstTenSlice)

# print only symbols with index, which divides on 3 without remaining

# print only integer values from list

# reverse integer list using slice
reverseInteger = textList[::-1]
print('reverseInteger :')
print(reverseInteger)
# convert list into string with “-” separator

listIntoString = '-'.join(textList)
print('listIntoString :')
print(listIntoString)