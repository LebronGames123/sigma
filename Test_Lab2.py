import Lab2
import pytest

def test_find_min_max():
    test_arr = [2, 3, 4, 6, 92, 940, 190, 5]
    min_excepted_result = 2
    max_excepted_result = 940
    result1 = Lab2.calc_min(test_arr)
    result2 = Lab2.calc_max(test_arr)
    assert(min_excepted_result == result1)
    assert(max_excepted_result == result2)

def test_calc_average():
    test_arr = [2,3,4,5,7,8,9,0,10,32,4]
    result = Lab2.calc_avg(test_arr)
    expected_result = sum(test_arr)/len(test_arr)
    assert (result==expected_result)

def test_calc_median_temperature():
    test_arr = [2,33,44,25,62,7,123,323,45,6]
    sorted_array=sorted(test_arr)
    median = 38.50
    n = len(sorted_array)
    if n%2 == 1:
        expected_median=sorted_array[n//2]
        formatted_median = float("{:.2f}".format(expected_median))
    else:
        midvalue1 =sorted_array[n//2]
        midvalue2 =sorted_array[n//2-1]
        expected_median= (midvalue1+midvalue2)/2
        formatted_median = float("{:.2f}".format(expected_median))

    assert(median == formatted_median)