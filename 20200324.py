# 删除排序数组中的重复项
class Solution:
    # 双指针
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0: return 0
        tag_1, tag_2 = 0, 0
        while tag_1 < len(nums):
            if nums[tag_1] == nums[tag_2]:
                tag_1 += 1
            elif nums[tag_1] != nums[tag_2]:
                tag_2 += 1
                nums[tag_2] = nums[tag_1]
        return tag_2 + 1

example = Solution()
print(example.removeDuplicates([1, 2, 3]))