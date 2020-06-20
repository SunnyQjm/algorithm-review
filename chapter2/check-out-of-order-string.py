#!/usr/bin/env python
# coding=utf-8

############################################################################
# 乱序字符串检查
#
# 乱序字符串是指一个字符串只是另一个字符串的重新排列。例如，'heart' 和 'earth' 就是乱序字符串。 
#  'python' 和'typhon' 也是。
# 
# 为了简单起见，我们假设所讨论的两个字符串具有相等的长度，并且他们由26个小写字母集合组成。
#  我们的目标是写一个布尔函数，它将两个字符串做参数并返回它们是不是乱序。
############################################################################


class Solution:
    
    ###################################################
    # 此处省略逐字比较，麻烦性能还差，主要是太多难记2333
    ###################################################

    def anagramSolution(self, s1, s2):
        """
        排序对比法

        思路：
        1. 将两个字符串转为list；
        2. 堆两个list进行排序；
        3. 然后逐一比较对应位置的字符是否相等即可
        """
        # 特判字符串长度不相同的情况
        # 其实这个不是必须的，只是在输入有可能长度不一的情况下，用这个可能可以提高一点性能
        if len(s1) != len(s2):
            return False
        list1 = list(s1)
        list2 = list(s2)
        list1.sort()
        list2.sort()

        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

    def anagramSolution2(self, s1, s2):
        """
        字符统计对比法(Knowledge)

        思路：
        1. 创建两个长度位26的数组；
        2. 各自统计两个字符串中每个字符出现的次数；
        3. 接着对比两个数组即可

        PS: ord => python中的一个内置函数，传入一个字符，会返回其对应的ASCII值
        """
        # 特判字符串长度不相同的情况
        # 其实这个不是必须的，只是在输入有可能长度不一的情况下，用这个可能可以提高一点性能
        if len(s1) != len(s2):
            return False
        
        c1 = [0] * 26
        c2 = [0] * 26

        # 统计字符出现的次数
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1

        # 对比统计结果
        for i in range(26):
            if c1[i] != c2[i]:
                return False

        return True





if __name__ == '__main__':
    solution = Solution()

    print(solution.anagramSolution("heart", "earth"), " == True")
    print(solution.anagramSolution("python", "typhon"), " == True")
    print(solution.anagramSolution("qwert", "qwertg"), " == False")

    print(solution.anagramSolution2("heart", "earth"), " == True")
    print(solution.anagramSolution2("python", "typhon"), " == True")
    print(solution.anagramSolution2("qwert", "qwertg"), " == False")
        
