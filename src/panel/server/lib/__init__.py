from .django_cr_sign.signer     import *
from .util.util                 import *
from .search.search             import Search
from .sort.sort                 import *
from .email.v2_email_controller import *
from .email.v1_email_controller import *
from .jwt.libJwT                import *

# development only
from .gen_fake_data import *
# development only

#region the sorting / searching algorithm testing / importing
# built in packages
from random import randint
from timeit import repeat
import time

ARRAY_LENGTH = 1000
array       = [i for i in range(ARRAY_LENGTH)]
rand_val    = randint(0, len(array))

#region making searching as a class
test_search = Search(array,rand_val)
#endregion

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    runTime = f"Algorithm: {algorithm}. Minimum execution time: {min(times)}"

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(runTime)

#region rest sorting algorithms
def test_all_sort():
    # Generate a sorted array of ARRAY_LENGTH items

    # Call each of the functions
    run_sorting_algorithm(algorithm="insertion_sort",  array=array)
    run_sorting_algorithm(algorithm="insertion_sort2", array=array)
    run_sorting_algorithm(algorithm="bubble_sort",     array=array)
    run_sorting_algorithm(algorithm="quick_sort",      array=array)
    run_sorting_algorithm(algorithm="tim_sort",        array=array)
    run_sorting_algorithm(algorithm="merge_sort",      array=array)

def test_insertion():
    run_sorting_algorithm(algorithm="insertion_sort",  array=array)

def test_merge():
    run_sorting_algorithm(algorithm="merge_sort",      array=array)

def test_quickS():
    run_sorting_algorithm(algorithm="quick_sort",      array=array)

def test_tim():
    run_sorting_algorithm(algorithm="tim_sort",        array=array)

def test_bubble():
    run_sorting_algorithm(algorithm="bubble_sort",      array=array)

def test_insertion2():
    run_sorting_algorithm(algorithm="insertion_sort2",  array=array)

#endregion


#region testing the different searching algorithms
def test_all_search():
    start = time.perf_counter()
    test_search_binary()
    test_search_linear()
    test_search_jump()
    test_search_fibonacci()
    test_search_exponential()
    test_search_interpolation()
    end = time.perf_counter()

    print(f"Finished testing all searching Algorithms:\n time: {start-end}\n")

def test_search_binary():
    start = time.perf_counter()

    test_search.Binary_Search()

    end = time.perf_counter()
    print(f"Finished testing binary search:\n time: {start-end}\n")

def test_search_linear():
    start = time.perf_counter()
    
    test_search.Linear_Search()

    end = time.perf_counter()
    print(f"Finished testing linear search:\n time: {start-end}\n")

def test_search_jump():
    start = time.perf_counter()
    
    test_search.Jump_Search()
    
    end = time.perf_counter()
    print(f"Finished testing jump search:\n time: {start-end}\n")

def test_search_fibonacci():
    start = time.perf_counter()
    
    test_search.Fibonacci_Search()
    
    end = time.perf_counter()
    print(f"Finished testing fibonacci search:\n time: {start-end}\n")

def test_search_exponential():
    start = time.perf_counter()

    test_search.Exponential_Search()
    
    end = time.perf_counter()
    print(f"Finished testing exponential search:\n time: {start-end}\n")

def test_search_interpolation():
    start = time.perf_counter()
    
    test_search.Interpolation_Search()
    
    end = time.perf_counter()
    print(f"Finished testing interpolation search:\n time: {start-end}\n")

#endregion

#endregion