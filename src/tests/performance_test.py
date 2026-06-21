"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from recursion.recursive_floyd import recursive_floyd_warshall
# from iterative.iterative_floyd import iterative_floyd
from recursive_floyd import *
from iterative_floyd import *
from time import process_time


def performance_test(function_handle):

    """
    A function that performs a simple performance test
    function_handle -> The function which is being tested.
                       It must take no parameters

    Please complete this function
    """


    start_time = process_time()
    print (f"{start_time:.8f} seconds")
    function_handle()
    end_time = process_time()
    print (f"{end_time:.8f} seconds")


    execution_time = end_time - start_time

    print(f"{execution_time:.8f} seconds")

    return execution_time


print ("Recursion Test Time")
performance_test(
lambda: recursive_floyd_warshall(outer_loop=MIN_LEVEL,middle_loop=MIN_LEVEL,inner_loop=MIN_LEVEL )

)

print ("Iterative Test Time")
performance_test(iterative_floyd)




