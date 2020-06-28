#!/usr/bin/env python
# coding=utf-8

#################################################################################################
# Leetcode 232 用栈实现队列
#
# 使用栈实现队列的下列操作：
#   push(x) -- 将一个元素放入队列的尾部。
#   pop() -- 从队列首部移除元素。
#   peek() -- 返回队列首部的元素。
#   empty() -- 返回队列是否为空。
#
# 示例:
#   MyQueue queue = new MyQueue();
#
#   queue.push(1);
#   queue.push(2);  
#   queue.peek();  // 返回 1
#   queue.pop();   // 返回 1
#   queue.empty(); // 返回 false
#
# 说明:
#   你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#   你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#   假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
#################################################################################################


class MyQueue:
    """

    (knowledge)

    思路：
    1. 使用两个栈来模拟实现队列，分别为stack1和stack2；
    2. 对于push操作 => 简单将其推到stack1即可；
    3. 对于peek操作 => 判断stack2是否为空，不为空则返回其栈顶元素，为空则将stack1依次弹栈，并依次push进stack2中，然后返回stack2的栈顶元素；
    4. 对于pop操作 => 首先执行peek操作，然后弹出stack2的栈顶元素；
    5. 对于empty操作 => 判断stack1和stack2是否同时为空即可；

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用两个栈来实现一个队列
        self.stack1, self.stack2 = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.peek()
    print(param_2, "= 1")
    param_3 = obj.pop()
    print(param_3, "= 1")
    param_4 = obj.empty()
    print(param_4, "= False")
