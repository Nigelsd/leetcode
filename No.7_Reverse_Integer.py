#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2018 Nigel. All Rights Reserved
#

"""
File: No.7_Reverse_Integer.py
Author: jolin132@qq.com
Date: 2018/02/03 000318:09
"""
class Solution(object):
    """
    leetcode Problems no.7 reverse integer solution
    """
    def revers(self,x):
        """

        :param x: type int
        :return: type int
        """
        if x > 2147483647 or x < -2147483647 or x == 0:
            return 0
        else:
            str_lis = []
            str_num = str(abs(x))
            for i in xrange(1, len(str_num) + 1):
                str_lis.append(str_num[-i])
            res = int(''.join(str_lis))

            if x < 0:
                res = -res
            else:
                res = res
            return res if abs(res) < 2147483647 else 0

if __name__ == "__main__":
    sl=Solution()
    str_num=[-123424000,1232400,8919823829382313,12320]
    for i in str_num:
        print sl.revers(i)