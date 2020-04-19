#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (64.86%)
# Likes:    445
# Dislikes: 0
# Total Accepted:    78.1K
# Total Submissions: 119.5K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for rows in range(len(grid)):
            for columns in range(len(grid[0])):
                if rows == 0:
                    if columns != 0:
                        grid[rows][columns] += grid[rows][columns - 1]
                else:
                    if columns == 0:
                        grid[rows][columns] += grid[rows - 1][columns]
                    else:
                        grid[rows][columns] += min(grid[rows][columns - 1], grid[rows - 1][columns])
        return grid[-1][-1]


# @lc code=end

