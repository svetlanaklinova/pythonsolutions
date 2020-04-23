'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''



def findShortestSubArray(nums):
        ar = [int(i) for i in nums if i.isdigit()]
        print('debug: {}'.format(ar))
        left,right, count = {}, {}, {}
        for i,x in enumerate(ar):
            if x not in left:
                left[x] = i
            right[x] = count.get(x,0) + 1
            count[x] = count.get(x,0) + 1
        ans = len(ar)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans,right[x] - left[x] +1)
        return ans




data = '1 2 2 3 1'
assert findShortestSubArray(data) == 2
