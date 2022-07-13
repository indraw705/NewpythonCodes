temp_str = "INDRAJIT"
print("reverse of :"+temp_str+" is "+temp_str[::-1])

import sys

my_list = [i for i in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list),"Bytes")
# Make list in tuples to use less memory

my_list = (i for i in range(10000))
print(sum(my_list))
print(sys.getsizeof(my_list),"Bytes")

i = 10
print(f'square of {i} is {i*i}')