text = input('input text : ')

print(text)

# print first symbol of text
firstSymbol = text[0]
print(firstSymbol)

# print the last symbol of text
lastSymbol = text[-1]
print(lastSymbol)

# make slice of first 8 symbols
sliceFirst8 = text[0:8]
print(sliceFirst8)

# не зробив
# print only symbols with index, which divides on 3 without remaining
# print(string[int(len(string)/2):int(len(string)/2)+1])
# print('--------1-------')
# numbs = re.findall(r'\d+', text)
# numbs = [int(i) for i in numbs]
#
# print(numbs)
# print(numbs % 3 == 0)
# print('--------2-------')



# just='Standard Price:20000'
# int(just.split(':')[1])

# print the symbol of the middle of the string text

# reverse text using slice
reverse = text[::-1]
print(reverse)
