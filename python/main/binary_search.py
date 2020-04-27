'''
@challenge: Implement binary search.
Find number in sorted array and return index. Return -1 if number does not exist
@author: Svetlana Klinova
@email: sklinova.home@gmail.com
'''

def get_index_if_number_exist_in_array(nums, number):
    first = 0
    last = len(nums) - 1
    mid = (first + last) // 2

    while first <= last:
        if nums[mid] < number:
            first = mid + 1
        elif nums[mid] > number:
            last = mid - 1
        else:
            return mid

        mid = (first + last) // 2
    return -1



assert (get_index_if_number_exist_in_array([0,1,2,3,4,5,9,120], 0) == 0)
assert (get_index_if_number_exist_in_array([0,1,2,3,4,5,9,120], 3) == 3)
assert (get_index_if_number_exist_in_array([0,4,5,9,120], 120) == 4)
assert (get_index_if_number_exist_in_array([1], 1) == 0)
assert (get_index_if_number_exist_in_array([0,4,5,9,120], -1) == -1)
assert (get_index_if_number_exist_in_array([0,1,2,3,4,5,9,120], 11) == -1)
assert (get_index_if_number_exist_in_array([], 1) == -1)

