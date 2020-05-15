'''
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
'''


def replaceElements(arr):
    m = -1

    for i in range(len(arr))[::-1]:
        arr[i], m = m, max(m, arr[i])
    return arr



assert replaceElements([17,18,5,4,6,1]) == [18, 6, 6, 6, 1, -1]
