# no.1 两数之和
'''
给定 nums = [2, 7, 11, 15], target = 9,返回两数之和为target的下标
'''
import time

nums = [2, 11, 15, 7]
target = 9
# 暴力法
def foo_first(nums, target):
    last_label = len(nums)  # 为下标递增设置一个上限
    for i, value in enumerate(nums):
        diff = target - value
        j = i + 1  # 确保两个数字不相同
        while j < last_label:
            if diff == nums[j]:
                return [i, j]
            else:
                j += 1

# 排列+首尾递进
def foo_second(nums, target):
    sort_id_list = range(len(nums))
    # sort_id_list = sorted(range(len(nums)), key=lambda x: nums[x])  # 排序后按照nums列表的下标返回
    print(sort_id_list)
    left_id = 0  # 左端下标
    right_id = len(nums) - 1
    while left_id < right_id:
        sum = nums[sort_id_list[left_id]] + nums[sort_id_list[right_id]]
        if sum == target:
            return [left_id, right_id]
        elif sum < target:
            left_id += 1
        elif sum > target:
            right_id -= 1

# 哈希表
def foo_third(nums, target):
    hash_dict = {}  # 建立哈希表
    for i, value in enumerate(nums):
        diff = target - value
        while diff in hash_dict:
            return [hash_dict.get(diff), i]
        hash_dict[value] = i  # 以value作为哈希表的键

caculate = foo_third(nums, target)
print(caculate)