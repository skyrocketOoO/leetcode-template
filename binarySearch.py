# return -1 if not found
def find_target(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

# return -1 if not found
def find_biggest_num_smaller_than_target(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return r

# return -1 if not found
def find_smallest_num_bigger_than_target(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l if l < len(nums) else -1

if __name__ == '__main__':
    print(find_smallest_num_bigger_than_target([1,3,4], 5))