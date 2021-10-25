# leetcode刷题笔记

[toc]

## 打卡记录

- [ ] 2021-07-05
- [ ] 2021-07-06

## Readme

今天是2021年7月5日，到目前为止，我已经学习过基本的C语言和Python，完整看完过《算法图解》，《漫画算法Python》的部分了。理论上来说，我已经具备了初步的算法知识，可以开始动手学leetcode上面刷题了，但是很遗憾，我的算法功底还是比较弱，一些基本的数据结构和编程语言的糅合还不是很熟。

编程，终究是一门动手的实践学科。想要学会编程，就得动手开始编程，所以，我在leetcode上报名了算法基础的学习计划，一共20天，每天2-3道题，基本上是简单和中等的难度。希望自己可以坚持着，花一些时间认真做一些事情。

知易行难，行胜于言。加油💪好运🤞

主要实现语言：Java，Python

**************

在数学和计算机科学之中，算法是一个被定义好的、计算机可施行之指示的有限步骤或次序，常用于计算、数据处理和自动推理。作为一个有效方法，算法被用于计算函数，它包含了一系列定义清晰的指令，并可于有限的时间及空间内清楚的表述出来。

## leetcode算法基础-21天计划

### 第1天-二分查找2021-07-05

***二分查找的一个基准程序***

> 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

***官方解答***

java解答

```java
class Solution {
    public int search(int[] nums, int target) {
        int pivot, left = 0, right = nums.length - 1;
        while (left <= right) {
            pivot = left + (right - left) / 2;
            if (nums[pivot] == target) return pivot;
            if (target < nums[pivot]) right = pivot - 1;
            else left = pivot + 1;
        }
        return -1;
    }
}
```

Python解答

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
```

***我的程序***

```java
class Solution {
    public int search(int[] nums, int target) {
        // int res = -1;
        int left = 0, right = nums.length - 1, mid;
        while(left <= right) {
            mid = left + (right - left) / 2;
            if (target <= nums[mid]) // bug
                right = mid - 1;
            else if (target > nums[mid])
                left = mid + 1;
            else if (target == nums[mid]){
                return mid; // bug
            }
        }
        return -1;
    }
}
```

**犯错误的地方**：1. 二分查找时，应该首先判断target 是否等于数组中间值的特殊情况；
2. Java if-else语法不熟悉。废话，是还没学。

***网友的分享***

```java
class Solution {
    public static int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        int mid = 0;
        while (start <= end) {
            mid = start + (end - start) / 2;
            if (nums[mid] < target) {
                start = mid + 1;
            } else if (nums[mid] > target) {
                end = mid - 1;
            } else if (nums[mid] == target) {
                return mid;
            }
        }
        return -1;
    }
}
```

如何完整运行一个Java程序？😂 还是基本功不到位，处处受限。

```java
public class YourClassNameHere {
    public static void main(String[] args) {
        int [] nums = {-1,0,3,5,9,12};
        int target = 9;
        search(nums, target);
    }
}

class Solution {
    public int search(int[] nums, int target) {
        // int res = -1;
        int left = 0, right = nums.length - 1, mid;
        while(left <= right) {
            mid = left + (right - left) / 2;
            if (target <= nums[mid])
                right = mid - 1;
            else if (target > nums[mid])
                left = mid + 1;
            else if (target == nums[mid]){
                return mid;
            }
        }
        return -1;
    }
}
```

#### 模板1

模板 #1 是二分查找的最基础和最基本的形式。这是一个标准的二分查找模板，大多数高中或大学会在他们第一次教学生计算机科学时使用。模板 #1 用于查找可以通过访问数组中的单个索引来确定的元素或条件。

Java实现

```Java
int binarySearch(int[] nums, int target) {
    if (nums == null || nums.length == 0)
        return -1;

    int left = 0, right = nums.length - 1;
    while (left <= right) {
        // 阻止(left + right)溢出
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) { return mid;}
        else if (nums[mid] < target) { left = mid + 1;}
        else {right = mid - 1;}
    }
    // 结束循环的条件：left > right
    return -1;
}
```

Python实现

```Python
from typing import List
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nmus[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # 循环终止条件：left > right
    return -1
```

#### x 的平方根

> 实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

```Python
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, -1
        while left <= right:
            pivot = left + (right - left) // 2
            if pivot * pivot <= x :
                ans = pivot
                left = pivot + 1
            else:
                right = pivot - 1   
        return ans
```

#### 34. 在排序数组中查找元素的第一个和最后一个位置

> 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。如果数组中不存在目标值 target，返回 [-1, -1]。

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：

输入：nums = [], target = 0
输出：[-1,-1]

提示：

0 <= nums.length <= 105

-109 <= nums[i] <= 109

nums 是一个非递减数组

-109 <= target <= 109

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[] {-1, -1};
        res[0] = binarySearch(nums, target, true);
        res[1] = binarySearch(nums, target, false);
        return res;
    }
    //leftOrRight为true找左边界 false找右边界
    public int binarySearch(int[] nums, int target, boolean leftOrRight) {
        int res = -1;
        int left = 0, right = nums.length - 1, mid;
        while(left <= right) {
            mid = left + (right - left) / 2;
            if(target < nums[mid])
                right = mid - 1;
            else if(target > nums[mid])
                left = mid + 1;
            else {
                res = mid;
                //处理target == nums[mid]
                if(leftOrRight)
                    right = mid - 1; // 查找元素第一个位置时，要让right变成中间的数-1
                else
                    left = mid + 1;
            }
        }
        return res;
    }
}
```

#### 33. 搜索旋转排序数组

> 整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：

输入：nums = [1], target = 0
输出：-1

提示：

1 <= nums.length <= 5000

-10^4 <= nums[i] <= 10^4

nums 中的每个值都 独一无二

题目数据保证 nums 在预先未知的某个下标上进行了旋转

-10^4 <= target <= 10^4

```java
class Solution {
    public int search(int[] nums, int target) {
        int len = nums.length;
        int left = 0, right = len-1;
        while(left <= right){
            int mid = (left + right) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < nums[right]){
                if(nums[mid] < target && target <= nums[right])
                    left = mid+1;
                else
                    right = mid-1;
            }
            else{
                if(nums[left] <= target && target < nums[mid])
                    right = mid-1;
                else
                    left = mid+1;
            }
        }
        return -1;
    }
}
```

思路：思路：如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的，我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，这样就可以确定保留哪半边了。

#### 74. 搜索二维矩阵

> 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1：

![mat](2021-07-05leetcode-notes.assets/mat.jpg)

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

提示：

m == matrix.length

n == matrix[i].length

1 <= m, n <= 100

-104 <= matrix[i][j], target <= 104

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return false;
        int begin, mid, end;
        begin = mid = 0;
        int len1 = matrix.length, len2 = matrix[0].length;
        end = len1 * len2 - 1;
        while (begin < end) {
            mid = (begin + end) / 2;
            if (matrix[mid / len2][mid % len2] < target)
                begin = mid + 1;
            else
                end = mid;
        }
        return matrix[begin / len2][begin % len2] == target;
    }
}
```

### 第2天-二分查找

#### 153. 寻找旋转排序数组中的最小值

> 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

***Python实现***

```Python
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]
```

***Java实现***

```Java
class Solution:
    public int findMin(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        while (low < high) {
            int pivot = low + (high - low) / 2;
            if (nums[pivot] < nums[high]) {
                high = pivot;
            } else {
                low = pivot + 1;
            }
        }
        return nums[low];
    }
```

#### 162. 寻找峰值

> 峰值元素是指其值大于左右相邻值的元素。
给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞ 。

***方法一：线性扫描***

```Python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 1):
            if nums[i] >  nums[i+1]:
                return i
            i += 1
        return len(nums) - 1
```

```Java
public class Solution {
    public int findPeakElement(int[] nums) {
        for (int i = 0; i <nums.length - 1; i++) {
            if (nums[i] > nums[i+1])
                return i;
        }
        return nums.length - 1;
    }
}
```

**复杂度分析：**

时间复杂度 : O(n)。 我们对长度为 n 的数组 nums 只进行一次遍历。

空间复杂度 : O(1)。 只使用了常数空间。

***方法二：递归二分查找***

**算法**

我们可以将 numsnums 数组中的任何给定序列视为交替的升序和降序序列。通过利用这一点，以及“可以返回任何一个峰作为结果”的要求，我们可以利用二分查找来找到所需的峰值元素。

在简单的二分查找中，我们处理的是一个有序数列，并通过在每一步减少搜索空间来找到所需要的数字。在本例中，我们对二分查找进行一点修改。首先从数组 numsnums 中找到中间的元素 midmid。若该元素恰好位于降序序列或者一个局部下降坡度中（通过将 nums[i]nums[i] 与右侧比较判断)，则说明峰值会在本元素的左边。于是，我们将搜索空间缩小为 midmid 的左边(包括其本身)，并在左侧子数组上重复上述过程。

若该元素恰好位于升序序列或者一个局部上升坡度中（通过将 nums[i]nums[i] 与右侧比较判断)，则说明峰值会在本元素的右边。于是，我们将搜索空间缩小为 midmid 的右边，并在右侧子数组上重复上述过程。

就这样，我们不断地缩小搜索空间，直到搜索空间中只有一个元素，该元素即为峰值元素。

```Python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return search(nums, 0, len(nums) - 1) # bug: TypeError: unhashable type: 'list'

    def search(nums: List[int],l: int, r: int):
        if (l == r): return l
        mid = l + (r - l) // 2
        if nums[mid] > nums[mid+1]:
            return search(nums, l, mid)
        return search(nums, mid + 1, r)
```

```Java
public class Solution {
    public int findPeakElement(int[] nums) {
        return search(nums, 0, nums.length - 1);
    }
    
    public int search(int[] nums, int l, int r) {
        if (l == r) return l;
        int mid = l + (r - l) / 2;
        if (nums[mid] > nums[mid+1])
            return search(nums, l, mid);
        return search(nums, mid + 1, r)；
    }
}
```

复杂度分析

时间复杂度 : O(log_2(n)。每一步都将搜索空间减半。因此，总的搜索空间只需要 O(log_2(n))步。其中 n 为 nums 数组的长度。
空间复杂度: O(log_2(n))。每一步都将搜索空间减半。因此，总的搜索空间只需要 log_2(n) 步。于是，递归树的深度为 log_2(n)。

**方法三：迭代二分查找**

算法: 上述二分查找方法使用了递归。我们可以通过迭代达到同样的效果。本方法即为迭代实现二分查找.

```Java
public class Solution {
    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[mid + 1])
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
}
```

复杂度分析

时间复杂度 : O(log_2(n))。 每一步都将搜索空间减半。因此，总的搜索空间只需要 log_2(n) 步。其中 n 为 nums 数组的长度。
空间复杂度 : O(1)。 只使用了常数空间。
