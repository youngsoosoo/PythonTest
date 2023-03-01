def solution(nums):
    answer = len(nums)
    nums = set(nums)
    a = len(nums)
    if len(nums) > answer//2:
        a=answer//2
    return a