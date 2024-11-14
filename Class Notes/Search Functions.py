"""
    mkp
    Week 12: Search Functions

"""

def bin_search(x, nums):
    low = 0
    high = len(nums) - 1
    while (low <= high ):
        mid = (low + high) // 2
        item = nums[mid]
        if ( x == item ):
            return mid
        elif ( x < item ):
            high = mid - 1
        else:
            low = mid + 1
    return -1


def linear_search(x, nums):
    for i in range(len(nums)):
        if( nums[i] == x ):
            return i
    return -1

def bin_search_rec(x, low, high, nums):
    if( low == high ):
        if ( nums[low] == x ):
            return low
        else:
            return -1
    else:
        mid = (low + high) // 2
        if( nums[mid] < x ):
            return binSearch(x, mid, high, nums)
        else:
            return binSearch(x, low, mid, nums)


