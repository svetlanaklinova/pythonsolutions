'''
@challenge: Implement binary search.
Find number in sorted array and return index. Return -1 if number does not exist
@author: Svetlana Klinova
@email: sklinova.home@gmail.com
'''

def get_index_if_number_exist_in_array(arr, number):
    if number == -1:
        return number
    left = 0
    right = len(arr) -1
    total_steps = 0
    result = -1


    while left <= right:
        total_steps += 1
        mid = (left + right)//2

        if arr[mid] < number:
            left = mid + 1
        elif arr[mid] > number:
            right = mid - 1
        else:
            result = mid
            break
    if result > -1:
        print('Found number {} at index {} in {} tries'.format(number, result, total_steps))
    else:
        print("Unable to find number {}".format(number))
    return result



assert (get_index_if_number_exist_in_array([0,1,2,3,4,5,9,120], 0) == 0)
assert (get_index_if_number_exist_in_array([0,1,2,3,4,5,9,120], 3) == 3)
assert (get_index_if_number_exist_in_array([0,4,5,9,120], 120) == 4)
assert (get_index_if_number_exist_in_array([1], 1) == 0)
assert (get_index_if_number_exist_in_array([0,4,5,9,120], -1) == -1)
assert (get_index_if_number_exist_in_array([0,1,2,3,4,5,9,120], 11) == -1)
assert (get_index_if_number_exist_in_array([], 1) == -1)

