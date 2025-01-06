from typing import List

class Solution:
    def fourSum_Brute(self, nums: List[int], target: int) -> List[List[int]]:
        final_Res = []
        res_Set = set()

        for ind1 in range(0, len(nums) - 3):
            for ind2 in range(ind1 + 1, len(nums) - 2):
                for ind3 in range(ind2 + 1, len(nums) - 1):
                    for ind4 in range(ind3 + 1, len(nums)):
                        four_sum = nums[ind1] + nums[ind2] + nums[ind3] + nums[ind4]
                        if four_sum == target:
                            res = [nums[ind1], nums[ind2], nums[ind3], nums[ind4]]
                            res.sort()

                            current_res = tuple(res)

                            if current_res not in res_Set:
                                final_Res.append(res)
                            res_Set.add(current_res)

        return final_Res
    

    def fourSum_Better(self, nums: List[int], target: int) -> List[List[int]]:
        final_Res = []
        res_Set = set()
        firstMap = set()

        for i in range(1, len(nums) - 2):
            firstMap.add(nums[i - 1])
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    three_sum = nums[i] + nums[j] + nums[k]
                    ele1 = target - three_sum

                    if ele1 in firstMap:
                        res = [nums[i], nums[j], nums[k], ele1]
                        res.sort()

                        current_res = tuple(res)

                        if current_res not in res_Set:
                            final_Res.append(res)
                        res_Set.add(current_res)


        return final_Res
    

    def fourSum_Optimal(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums)):

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):

                if j != (i + 1) and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = len(nums) - 1

                while (k < l):
                    fourSum = nums[i] + nums[j] + nums[k] + nums[l]

                    if fourSum == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k - 1] == nums[k]:
                            k += 1

                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    elif fourSum < target:
                        k += 1
                        while k < l and nums[k - 1] == nums[k]:
                            k += 1

                    else:
                        l -= 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1


        return res

            





        


S = Solution()
nums = [1,0,-1,0,-2,2]
# nums = [-2,-1,-1,1,1,2,2]
target = 0
print(S.fourSum_Brute(nums=nums, target=target))
print(S.fourSum_Better(nums=nums, target=target))
print(S.fourSum_Optimal(nums=nums, target=target))