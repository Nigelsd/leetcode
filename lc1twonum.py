#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2018 Nigel. All Rights Reserved
#

"""
File: lc1twonum.py
Author: jolin132@qq.com
Date: 2018/02/03  17:56
"""
class Solution(object):
    """
    leetcode problems 1 two sum solution script
    """
    def twosum(self,nums,target):
        """

        :param nums: type list[int]
        :param target: type int
        :return:type list[int]
        """
        sum = 0
        for i in xrange(len(nums)):
            for j in xrange(0,i):
                sum = nums[i]+nums[j]
                if sum == target:

                    return [j,i]
                    break


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10,11,13]
    target = 7
    sl = Solution()
    print sl.twosum(nums,target)
