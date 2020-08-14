class Solution(object):
  def makesquare(self, nums):
    if not nums:
        return False
    L = len(nums)
    perimeter = sum(nums)
    possible_side =  perimeter // 4
    if possible_side * 4 != perimeter:
        return False
    nums.sort(reverse=True)
    sums = [0 for _ in range(4)]
    def dfs(index):
        if index == L:
            return sums[0] == sums[1] == sums[2] == possible_side
        for i in range(4):
            if sums[i] + nums[index] <= possible_side:
                sums[i] += nums[index]
                if dfs(index + 1):
                    return True
                sums[i] -= nums[index]
        return False        
    return dfs(0)
val=Solution()
n=int(input())
nums=list(map(int,input().split()))
print(val.makesquare(nums))
