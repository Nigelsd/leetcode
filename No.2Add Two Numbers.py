#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2018 Nigel. All Rights Reserved
#

"""
File: No.2Add Two Numbers.py
Author: jolin132@qq.com
Date: 2018/02/04 000412:44
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _sum = 0
        root = n = ListNode(0)
        while l1 or l2 or _sum:
            if l1:
                _sum += l1.val

                l1 = l1.next

            if l2:
                _sum += l2.val
                l2 = l2.next

            n.next = ListNode(_sum % 10)
            n = n.next
            _sum = _sum / 10

        return root.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # print l1
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    sl = Solution()
    print sl.addTwoNumbers(l1, l2)
