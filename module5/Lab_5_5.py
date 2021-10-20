foo = [1, 2, 3, 4, 5]

# Define own enumerate function
def enumerate(lst):
    # Loop for generation objects with yield
    for item in lst:
        # Return tuple with 2 items - item index +1 and item value
        yield lst.index(item)+1, item


for item in enumerate(foo):
    print(item)