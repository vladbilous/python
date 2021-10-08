# lab work 3-3
import math
import random

# generate sequence of 5 random integers from range (0, 100), store them in int_seq variable
int_seq = [random.randint(0,100) for _ in range(5)]

# generate fandom float number, store it as float_random variable
float_random = random.uniform(0, 100)

# print both these variables
print(int_seq)
print(float_random)

# find maximum element of int_seq variable and store it in variable int_seq_max
int_seq_max = max(int_seq)


