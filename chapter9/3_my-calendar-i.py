#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 729 我的日程安排表 I
#
# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内没有其他安排，则可以存储这个新的日程安排。
# MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。
# 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生重复预订。
# 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。
# 请按照以下步骤调用 MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
#
# 示例 1:
#   MyCalendar();
#   MyCalendar.book(10, 20); // returns true
#   MyCalendar.book(15, 25); // returns false
#   MyCalendar.book(20, 30); // returns true
#   解释: 
#   第一个日程安排可以添加到日历中.  第二个日程安排不能添加到日历中，因为时间 15 已经被第一个日程安排预定了。
#   第三个日程安排可以添加到日历中，因为第一个日程安排并不包含时间 20 。
#
# 说明:
#   - 每个测试用例，调用 MyCalendar.book 函数最多不超过 100次。
#   - 调用函数 MyCalendar.book(start, end)时， start 和 end 的取值范围为 [0, 10^9]。
#######################################################################################


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

class MyCalendar:
    
    def __init__(self):
        # 定义一个数组，用于记录行程
        self.calendar = []

    
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype bool

        (knowledge)

        思路：
        1. 用一个数组记录行程安排，其中每个元素为一个二元组，表示左闭又开的行程安排；
        2. 每次插入之前判断当前行程是否与既定行程重叠，重叠则返回False;
        3. 如果不重叠，则在适当位置插入行程，保证整体有序；
        """

        # 处理行程安排为空的情况
        if len(self.calendar) == 0:
            self.calendar.append((start, end))
            return True

        # 处理当前要插入的行程，比所有之前插入的行程安排都要早，且不重叠的情况
        if self.calendar[0][0] >= end:
            self.calendar.insert(0, (start, end))
            return True

        # 处理当前要插入的行程，比所有之前插入的行程安排都要迟，且不重叠的情况
        if self.calendar[-1][1] <= start:
            self.calendar.append((start, end))
            return True

        for i in range(1, len(self.calendar)):
            # 找到合适的位置，插入新的行程
            if self.calendar[i][0] >= end:
                if self.calendar[i - 1][1] <= start:
                    self.calendar.insert(i, (start, end))
                    return True
                else:
                    return False

        return False


if __name__ == '__main__':
    obj = MyCalendar()
    print(obj.book(10, 20), "= True")
    print(obj.book(15, 25), "= False")
    print(obj.book(20, 30), "= True")
