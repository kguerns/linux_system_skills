# Maximize Array Sum with a Fixed Window
# Given a list of integers and a fixed window size, find the maximum
# sum of a contiguous subarray of size exactly K.
# Accomplished in O(n) time complexity

def max_subarray_sum(nums, k):

    if k > len(nums):
        return 0

    window_sum = sum(nums[0:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    max_sum = max_subarray_sum([4, 2, 1, 7, 8, 1, 2, 8, 3], 3)
    print(f"Max sum is {max_sum}")