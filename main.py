import importlib
from TK_1 import input_data_from_console
from TK_2 import tuple_min_and_max
from TK_3 import devision_avg
from TK_4 import multipication_on_avg

arr = input_data_from_console(5)
print("Your array:", arr)
min_and_max = tuple_min_and_max(arr)
print("Min and max tuple:", min_and_max)
devision_array = devision_avg(arr)
print("Devision array on avg:", devision_array)
multiplication_array = multipication_on_avg(arr)
print("Multiplication array on avg:", multiplication_array)
sqrt_array = importlib.import_module('TK-5').sqrt_arr(arr)
print("Sqrt array:", sqrt_array)