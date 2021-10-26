# Create list of numbers from 0 to 9
seq1 = list(range(10))
# Create list of numbers from 0 to 9 with step 2
seq2 = list(range(0,10,2))
# Create empty list in global visibility area
res = []

def intersection(seq1, seq2):
    # Start with empty list as local variable
    res = []
    # Scan seq1
    for x in seq1:
        # Common item?
        if x in seq2:
            # Add to end
            res.append(x)
    return res

print(intersection(seq1, seq2))
print("List:", res)
