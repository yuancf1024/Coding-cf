# 2021-10Head-First-Go

[toc]

# 学习记录

1. - [x] 2021-10-12 前言+让我们开始吧：语法基础
2. 

# 1分钟入门

## 1.1 hello,world

go\src\gopl\ch1\helloworld>

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello,世界！")
}

```

终端运行Go程序的方式：
**直接运行** 
PS C:\Users\chenfengyuan\go\src\gopl\ch1\helloworld> go run helloworld.go
Hello,世界！

**先编译后链接**

PS C:\Users\chenfengyuan\go\src\gopl\ch1\helloworld> go build helloworld.go
PS C:\Users\chenfengyuan\go\src\gopl\ch1\helloworld> ./helloworld
Hello,世界！

## 小技巧

1. 安装/更新Go包

需要安装 go 的工具包。在 vscode 中，输入快捷键：`command(ctrl) + shift + p`，

在弹出的窗口中，输入：`go:install/Update Tools`，回车后，选择所有插件(勾一下全选)，点击确认，进行安装（最好翻墙安装）。

2. 设置Golang的代码提示

在项目的 settings.json 文件中添加配置：

```go
"go.autocompleteUnimportedPackages": true,
"go.docsTool": "gogetdoc",
"go.formatTool": "goimports",
```

安装包：

```go
go get -v github.com/zmb3/gogetdoc
go get -v golang.org/x/tools/cmd/goimports
```

# 如何使用这本书：前言

## 元认知：思考“何为思考”

如果你真的想要学习，而且你想学的更快、更深，那就留意你是如何集中注意力的。想想你是如何思考的。学会如何学习。

*诀窍是让你的大脑看到你正在学习的新资料是非常重要的。*对你的健康也是至关重要的。像老虎一样重要。否则，你就会陷入一场持续的战斗，你的大脑会尽其所能阻止新内容的产生。

**如何让你的大脑对待编程就像对待一只饥饿的老虎呢？**

*慢方法是纯粹的重复。*

*快的方法是做任何能增加大脑活动的事情，尤其是不同类型的大脑活动。*

谈话风格很有帮助，因为当人们意识到他们在交谈时往往会更加专注。因为他们希望紧跟并坚持到底。

## 如何做能让你的大脑就范

1. 放慢速度，多去理解，从而减少机械记忆。
2. 做练习，记笔记。
3. 读懂“有问必答”。
4. 将本书作为你的睡前读物，或者至少是最后一个挑战。
5. 大声谈论你学到的知识。
6. 大量喝水。
7. 倾听你的大脑。
8. 感受某些事情。
9.  写大量代码！

# 1 让我们开始吧：语法基础

## 准备好，出发

Google工程师为一门语言勾画了一些目标：

* 快速编译
* 不太笨重的代码
* 自动释放未使用的内存（垃圾收集）
* 易于编写同时执行多个操作的软件（并发）
* 很好地支持多核处理器

Google创建了Go：一种能快速编写代码并生成程序的语言，可以快速编译和运行。

Golang以其简单和强大的功能而迅速流行起来。

Gopher 英文意思是地鼠，也泛指 Golang 开发者。

哈哈哈哈，地鼠Gopher。

## Go Playground

https://play.golang.org

Hello.go

```go
package main // 表示文件中的所有其余代码都属于"main"包

import "fmt"  // 使用"fmt"包中的文本格式代码

func main() { // 程序运行时，首先运行ta
	fmt.Println("Hello, Go!") // 从"fmt"包调用"Println"函数来实现
}
```

## 典型的Go文件布局

1. package子句
2. 任何import语句
3. 实际代码

```go
package main // package子句

import "fmt" // imports部分

func main() {
	fmt.Println("Hello, Go!) // 实际代码
}
```

缺失圆括号：
PS C:\Users\chenfengyuan\go> go run "c:\Users\chenfengyuan\go\src\HeadFirstGo\1_Basics\Hello\Hello.go"
command-line-arguments
src\HeadFirstGo\1_Basics\Hello\Hello.go:6:14: syntax error: unexpected literal "Hello, Go!" at end of statement

## 调用函数

`package.function()`

`fmt.Println()`

## 函数返回值

function_return.go

```go
package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	fmt.Println(math.Floor(2.75))
	fmt.Println(strings.Title("head first go"))
}
```

Output:
2
Head First Go






# 2 接下来运行哪些代码：条件和循环

# 3 调用：函数

# 4 代码集：包

# 5 列表：数组

# 6 追加的问题：切片

# 7 标签数据：映射

# 8 构建存储：struct

# 9 我喜欢的类型：定义类型

# 10 保密：封装和嵌入

# 11 你能做什么：接口

# 12 重新站起来：从失败中恢复

# 13 分享工作：goroutine和channel

# 14 代码的质量保证：自动化测试

# 15 响应请求：Web应用程序

# 16 要遵循的模式：HTML模板

# A 理解os.OpenFile：打开文件

# B 有六件事我们没有涉及：剩下的内容



