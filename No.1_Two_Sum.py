#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2018 Nigel. All Rights Reserved
#

"""
File: No.1_Two_Sum.py
Author: jolin132@qq.com
Date: 2018/02/03 000320:27
"""
class Solution(object):
    """
    leetcode problems no.1
    """
    def twosum(self, nums, target):
        """

        :param nums: type list int
        :param target: type int
        :return: list int
        """
        if not len(nums):
            return None

        else:
            hash_dic={}

            for i in xrange(len(nums)):
                if nums[i] in hash_dic:
                    res = [hash_dic[nums[i]],i]
                    return res
                else:
                    hash_dic[target-nums[i]] = i


if __name__ == "__main__":
    sl = Solution()
    nums=[3,4,5,6,7,15,19,8,9,15]
    nums = [-3,4,3,90]
    target = 0
    print sl.twosum(nums,target)