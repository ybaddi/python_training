# import random

# print(random.random())

# import  my_functions as functions

# import example_2_1.my_functions as functions1
# import example_2_2.my_functions as functions2

# my_res = functions.table_de_multiplication_4()
# functions1.table_de_multiplication_3()
# functions2.table_de_multiplication_3()
# print(my_res)

#  ================================
from  my_functions import table_de_multiplication_4 as f_4

from example_2_1.my_functions import table_de_multiplication_3 as f_3
from example_2_2.my_functions import table_de_multiplication_3 as f2_3

my_res = f_4()
f_3()
f2_3()
print(my_res)