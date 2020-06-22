#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 208 实现 Trie (前缀树)
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#   Trie trie = new Trie();
#
#   trie.insert("apple");
#   trie.search("apple");   // 返回 true
#   trie.search("app");     // 返回 false
#   trie.startsWith("app"); // 返回 true
#   trie.insert("app");   
#   trie.search("app");     // 返回# true
#
# 说明:
#   - 你可以假设所有的输入都是由小写字母 a-z 构成的。
#   - 保证所有输入均为非空字符串。
#######################################################################################

class TreeNode:
    def __init__(self):
        self.word = False       # 表示当前节点是否是一个曾经插入的单词
        self.children = {}      # 子节点列表

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # 从根节点出发
        node = self.root
        for char in word:
            if char not in node.children:           # 判断当前字符是否在当前节点的子节点里面，不在，则创建一个子节点
                node.children[char] = TreeNode()
            node = node.children[char]              # 跳到对应的子节点
        node.word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple"), "= True")
    print(obj.search("app"), "= False")
    print(obj.startsWith("app"), "= True")
    obj.insert("app")
    print(obj.search("app"), "= True")
