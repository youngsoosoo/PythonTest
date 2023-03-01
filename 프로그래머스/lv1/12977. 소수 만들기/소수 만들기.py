def isprime(a) :
    if a < 2:
        return False
    for i in range(2, int(a**0.5)+1):
        if a%i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if isprime(nums[i]+nums[j]+nums[k]):
                    answer+=1

    return answer