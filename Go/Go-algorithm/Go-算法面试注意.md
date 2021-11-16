# Go-算法面试注意

## 算法思维

* 进入函数优先考虑边界
* 如果出现循环，进入循环时考虑`break`条件和`continue`条件
* 使用下标计算长度时，优先考虑区间的开闭
* 我们应该在做算法的过程中不断的思考和总结共性

## 面试注意

一定要记得常用的函数，现场是没有办法可以查的

* 字符串去左右空格
* 字符串切割
* 随机数种子，随机数生成
* 内置排序函数
* int最小值最大值怎么取

**以Go为例**

```go
s = strings.TrimSpace(s)
arr := strings.Spilt(s, "")

rand.Seed(time.Now().UnixNano())
rand.Int()

sort.Int()
sort.Slice(x, func(i, j int)bool {
    // 降序
    return x[i]>x[j]
})

math.MaxInt32
math.MinInt32
```

## 牛客网面试注意

牛客网比较坑，一切输入输出都要自己实现

还要劳记**链表创建代码**，[完整代码](https://github.com/coding3min/interview-leetcode/tree/5cb2e5224e55a017aa569f71ee31714371f1a8cd/LeetCode/all/0.%e5%88%9b%e5%bb%ba%e9%93%be%e8%a1%a8.go)

```go
package main

import "fmt"

type LinkNode struct {
    val int
    Next *LinkNode
}

func createNode(a []int) *LinkNode {
    head := &LinkNode{
        0,
        nil,
    }
}
```

## 常用排序算法



Reference：
1. https://leetcode.coding3min.com/leetcode/suan-fa-mian-shi-zhu-yi/
2. 
