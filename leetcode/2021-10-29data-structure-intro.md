# 2021-10-29data-structure-intro

[toc]

## 打卡记录

1. [x] 2021-10-29 217-存在重复元素 + 53-最大子序和  （题目不简单，道阻且长呀😂）
2. [ ] 

## Readme

leetcode官网展示的数据结构教程，主要包括栈、数组、链表和字符串。

实现语言：Java、Python、Go等。

该教程中简单题28道，中等题5道，难题0道，算得上是最简单得教程了吧。😂

Talk is cheap, show me the code. 废话少说，上代码吧！

**数据结构**

力扣 (LeetCode)

在计算机科学中，数据结构是计算机中存储、组织数据的方式。

正确的数据结构选择可以提高算法的效率。在计算机程序设计的过程中，选择适当的数据结构是一项重要工作。许多大型系统的编写经验显示，程序设计的困难程度与最终成果的质量与表现，取决于是否选择了最适合的数据结构。

## 第1天 数组

### 217.存在重复元素

给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

**自己写的代码**

```Python
# 自己的暴力求解算法：2个for循环遍历
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        target = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    target = True
                    break

        return target
```

### 官方题解

**方法一：排序**

*在对数字从小到大排序之后，数组的重复元素一定出现在相邻位置中。*因此，我们可以扫描已排序的数组，每次判断相邻的两个元素是否相等，如果相等则说明存在重复的元素。

```java
class Solution {
    pubilc boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 0; i < n-1; i++) {
            if (nums[i] == nums[i+1]) {
                return true;
            }
        }
        return false;
    }
}
```

```go
func containsDuplicate(nums []int) bool {
    sort.Ints(nums)
    for i := 1; i < len(nums); i++ {
        if nums[i] == nums[i-1] {
            return true
        }
    }
    return false
}
```

**复杂度分析**

时间复杂度：$O(NlogN)$，其中 N 为数组的长度。需要对数组进行排序。

空间复杂度：$O(logN)$，其中 N 为数组的长度。注意我们在这里应当考虑递归调用栈的深度。

**方法二：哈希表**

*对于数组中每个元素，我们将它插入到哈希表中。如果插入一个元素时发现该元素已经存在于哈希表中，则说明存在重复的元素。*

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for (int x : nums) {
            if (!set.add(x)) {
                return true;
            }
        }
        return false;
    }
}
```

```go
func containsDuplicate(nums []int) bool {
    set := map[int]struct{}{}
    for _, v := range nums {
        if _, has := set[v]; has {
            return true // 如果成功插入到hash表，返回true，说明 --### 
        }
        set[v] = struct{}{}
    }
    return false
}
```

*Go实现的这段代码不是很理解，也许是对go语言还不熟悉造成的，但是可以理解上面那段Java代码的逻辑。*

**复杂度分析**

时间复杂度：$O(N)$，其中 N 为数组的长度。

空间复杂度：$O(N)$，其中 N 为数组的长度。

**奇技淫巧**

```python
class Solution:
    def containsDuplicate(self, nums : List[int]) -> bool:
        return len(nums) != len(set(nums)) 
        # 利用了Python集合中不包含重复元素的特性
```

```java
public boolean containsDuplicate(int[] nums) {
    return Arrays.stream(nums).distinct().count() < nums.length;
}
```

### 53.最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000
 
提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
 
*进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。*

**自己写的代码**

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
...
```

```java
...
```

leetcode 真的emo了，数据结构入门教程，你直接上分治和动态规划。。。

*妙啊，简直就是妙蛙种子吃了妙脆角走进了米奇妙妙屋，妙到家了*

*这就是简单题吗？ai了ai了*

### 官方题解

**方法一：动态规划**

思路和算法

假设 $\textit{nums}$ 数组的长度是 n，下标从 0 到 n-1。

我们用 $f(i)$ 代表以第 $i$ 个数结尾的「连续子数组的最大和」，那么很显然我们要求的答案就是：

$\max_{0 \leq i \leq n-1} \{ f(i) \}$

因此我们只需要求出每个位置的 $f(i)$，然后返回 $f$ 数组中的最大值即可。那么我们如何求 $f(i)$ 呢？我们可以考虑 $\textit{nums}[i]$ 单独成为一段还是加入 $f(i−1)$ 对应的那一段，这取决于 $\textit{nums}[i]$ 和 $f(i-1) + \textit{nums}[i]$ 的大小，我们希望获得一个比较大的，于是可以写出这样的*动态规划转移方程*：

$f(i) = \max \{ f(i-1) + \textit{nums}[i], \textit{nums}[i] \}$

不难给出一个时间复杂度 $O(n)$、空间复杂度 $O(n)$ 的实现，即用一个 $f$ 数组来保存 $f(i)$ 的值，用一个循环求出所有 $f(i)$。考虑到 $f(i)$ 只和 $f(i−1)$ 相关，于是我们可以只用一个变量 $\textit{pre}$ 来维护对于当前 $f(i)$ 的 $f(i-1)$ 的值是多少，从而让空间复杂度降低到 $O(1)$，**这有点类似「滚动数组」的思想。**

代码

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int pre = 0, maxAns = nums[0];
        for (int x : nums) {
            pre = Math.max(pre + x, x);
            maxAns = Math.max(maxAns, pre);
        }
        return maxAns;
    }
}
```

```go
func maxSubArray(nums []int) int {
    max := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] + nums[i-1] > nums[i] {
            nums[i] += nums[i-1]
        }
        if nums[i] > max {
            max = nums[i]
        }
    }
    return max
}
```

**复杂度**

时间复杂度：$O(n)$，其中 n 为 $\textit{nums}$ 数组的长度。我们只需要遍历一遍数组即可求得答案。
空间复杂度：$O(1)$。我们只需要常数空间存放若干变量。

**方法二：分治**

思路和算法

这个分治方法类似于**「线段树求解最长公共上升子序列问题」**的 `pushUp` 操作。 也许读者还没有接触过线段树，没有关系，方法二的内容假设你没有任何线段树的基础。当然，如果读者有兴趣的话，推荐阅读线段树区间合并法解决多次询问的「区间最长连续上升序列问题」和「区间最大子段和问题」，还是非常有趣的。

我们定义一个操作 `get(a, l, r)` 表示查询 $a$ 序列 $[l,r]$ 区间内的最大子段和，那么最终我们要求的答案就是 `get(nums, 0, nums.size() - 1)`。如何分治实现这个操作呢？对于一个区间 $[l,r]$，我们取 $m = \lfloor \frac{l + r}{2}⌋$，对区间 $[l,m]$ 和 $[m+1,r]$ 分治求解。当递归逐层深入直到区间长度缩小为 1 的时候，递归「开始回升」。这个时候我们考虑如何通过 $[l,m]$ 区间的信息和 $[m+1,r]$ 区间的信息合并成区间 $[l,r]$ 的信息。最关键的两个问题是：

* 我们要维护区间的哪些信息呢？
* 我们如何合并这些信息呢？

对于一个区间 $[l,r]$，我们可以维护四个量：

* $\textit{lSum}$ 表示 $[l,r]$ 内以 $l$ 为左端点的最大子段和
* $\textit{rSum}$ 表示 $[l,r]$ 内以 $r$ 为右端点的最大子段和
* $\textit{mSum}$ 表示 $[l,r]$内的最大子段和
* $\textit{iSum}$ 表示 $[l,r]$的区间和

以下简称 $[l,m]$ 为 $[l,r]$ 的「左子区间」，$[m+1,r]$ 为 $[l,r]$ 的「右子区间」。我们考虑如何维护这些量呢（如何通过左右子区间的信息合并得到 $[l,r]$的信息）？*对于长度为 $1$ 的区间 $[i, i]$ ，四个量的值都和 $\textit{nums}[i]$ 相等*。对于长度大于 $1$ 的区间：

* 首先最好维护的是 $\textit{iSum}$，区间 $[l,r]$ 的 $\textit{iSum}$ 就等于「左子区间」的 $\textit{iSum}$ 加上「右子区间」的 $\textit{iSum}$。
* 对于 $[l,r]$ 的 $\textit{lSum}$，存在两种可能，它要么等于「左子区间」的 $\textit{lSum}$，要么等于「左子区间」的 $\textit{iSum}$ 加上「右子区间」的 $\textit{lSum}$，二者取大。
* 对于 $[l,r]$ 的 $\textit{rSum}$，同理，它要么等于「右子区间」的 $\textit{rSum}$，要么等于「右子区间」的 $\textit{iSum}$ 加上「左子区间」的 $\textit{rSum}$，二者取大。
* 当计算好上面的三个量之后，就很好计算 $[l,r]$ 的 $\textit{mSum}$ 了。我们可以考虑 $[l,r]$ 的 $\textit{mSum}$ 对应的区间是否跨越 $m$——它可能不跨越 $m$，也就是说 $[l,r]$ 的 $\textit{mSum}$ 可能是「左子区间」的 $\textit{mSum}$ 和 「右子区间」的 $\textit{mSum}$ 中的一个；它也可能跨越 $m$，可能是「左子区间」的 $\textit{rSum}$ 和 「右子区间」的 $\textit{lSum}$ 求和。三者取大。

这样问题就得到了解决。

代码

```java
class Solution {
    public class Status {
        public int lSum, rSum, mSum, iSum;

        public Status(int lSum, int rSum, int mSum, int iSum) {
            this.lSum = lSum;
            this.rSum = rSum;
            this.mSum = mSum;
            this.iSum = iSum;
        }
    }

    public int maxSubArray(int[] nums) {
        return getInfo(nums, 0, nums.length - 1).mSum;
    }

    public Status getInfo(int[] a, int l, int r) {
        if (l == r) {
            return new Status(a[l], a[l], a[l], a[l]);
        }
        int m = (l + r) >> 1;
        Status lSub = getInfo(a, l, m);
        Status rSub = getInfo(a, m+1, r);
        return pushUp(lSub, rSub);
    }

    public Status pushUp(Status l, Status r) {
        int iSum = l.iSum + r.iSum;
        int lSum = Math.max(l.lSum, l.iSum + r.lSum);
        int rSum = Math.max(r.rSum, r.iSum + l.rSum);
        int mSum = Math.max(Math.max(l.mSum, r.mSum), l.rSum + r.lSum);
        return new Status(lSum, rSum, mSum, iSum);
    }
}
```

```go
func maxSubArray(nums []int) int {
    return get(nums, 0, len(nums)-1).mSum
}

func pushUp(l, r Status) Status {
    iSum := l.iSum + r.iSum
    lSum := max(l.lSum, l.iSum + r.lSum)
    rSum := max(r.rSum, r.iSum + l.rSum)
    mSum := max(max(l.mSum, r.mSum), l.rSum + r.lSum)
    return Status{lSum, rSum, mSum, iSum}
}

func get(nums []int, l, r int) Status {
    if (l == r) {
        return Status{nums[l], nums[l], nums[l], nums[l]}
    }
    m := (l + r) >> 1
    lSub := get(nums, l, m)
    rSub := get(nums, m+1, r)
    return pushUp(lSub, rSub)
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

type Status struct {
    lSum, rSum, mSum, iSum int
}
```

**奇技淫巧**

```python
class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)
```

**代码解释**：你可以理解为思想是动态规划，nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和。如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和。

大佬，你的代码很棒但是讲的似乎有一点问题，“而是到前一项为止的最大子序和”这句话，因为如果遍历到的该项为负，就不是最大子序和啦！这句话应该改成“*而是到前一项为止的最大子序和或者最大子序和与该项的和*”，该项若是负，就是最大子序和和该项的和，若是正，就是最大子序和。

## 第2天 数组

## 第3天 数组

## 第4天 数组

## 第5天 数组

## 第6天 字符串

## 第7天 链表

## 第8天 链表

## 第9天 栈/队列

## 第10天树

## 第11天树

## 第12天树

## 第13天树

## 第14天树

