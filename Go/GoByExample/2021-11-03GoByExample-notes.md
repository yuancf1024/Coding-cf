# 2021-11-03GoByExample-notes

[toc]

## 更新记录

- [x] 2021-11-03 1-Hello World
- [x] 2021-11-04 中午2+3
- [ ] 2021-11-06 4~20

## Readme

Go by Example 是一个通过带注释的示例程序学习 Go 语言的网站。网站包含了从简单的 Hello World 到高级特性 Goroutine、Channel 等一系列示例程序，并附带了注释说明，非常适合 Go 语言初学者。

如果您想学习 Go 语言基础知识，不要犹豫，请直接前往 Go by Example 开始学习！

## 1-Hello World

我们的第一个程序将打印传说中的“hello world”， 右边是完整的程序代码。

```go
package main

import "fmt"

func main() {
	fmt.Println("hello world")
}
```

要运行这个程序，先将将代码放到名为 hello-world.go 的文件中，然后执行 go run。

```shell
PS C:\Users\chenfengyuan\Coding-cf\Go\GoByExample\hello-world> go run hello-world.go
hello world
```

如果我们想将程序编译成二进制文件（Windows 平台是 .exe 可执行文件）， 可以通过 go build 来达到目的。

然后我们可以直接运行这个二进制文件。

现在我们可以运行和编译基础的 Go 程序了， 让我们开始学习更多关于这门语言的知识吧。

```shell
PS C:\Users\chenfengyuan\Coding-cf\Go\GoByExample\hello-world> go build hello-world.go
PS C:\Users\chenfengyuan\Coding-cf\Go\GoByExample\hello-world> ls
    目录: C:\Users\chenfengyuan\Coding-cf\Go\GoByExample\hello-world

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2021/11/4      0:12        1924608 hello-world.exe
-a----         2021/11/4      0:09             77 hello-world.go
PS C:\Users\chenfengyuan\Coding-cf\Go\GoByExample\hello-world> ./hello-world
hello world
```

## 2-值

Go 拥有多种值类型，包括字符串、整型、浮点型、布尔型等。 下面是一些基础的例子。

字符串可以通过 + 连接。

整数和浮点数

布尔型，以及常见的布尔操作。

```go
package main

import "fmt"

func main() {
	fmt.Println("go" + "lang")

	fmt.Println("1+1 = ", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}
```

PS C:\Us> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\values\values.go"
golang
1+1 =  2
7.0/3.0 = 2.3333333333333335
false
true
false

## 3-变量

在 Go 中，*变量* 需要显式声明，并且在函数调用等情况下， 编译器会检查其类型的正确性。

```go
package main

import "fmt"

func main() {
	// var 声明 1 个或者多个变量。
	var a = "initial"
	fmt.Println(a)

	// 你可以一次性声明多个变量。
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go 会自动推断已经有初始值的变量的类型。
	var d = true
	fmt.Println(d)

	// 声明后却没有给出对应的初始值时，变量将会初始化为 零值 。
	// 例如，int 的零值是 0。
	var e int
	fmt.Println(e)

	// := 语法是声明并初始化变量的简写， 
	// 例如 var f string = "short" 
	// 可以简写为右边这样。
	f := "short"
	fmt.Println(f)
}
```

PS C:\Users\chenfengyuan\Coding-cf\Go\GoByExample\hello-world> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\variables\variables.go"
initial
1 2
true
0
short


## 4-常量

Go 支持字符、字符串、布尔和数值 **常量** 。

```go
package main

import (
	"fmt"
	"math"
)

// `const`用于声明一个常量。
const s string = "constant"

func main() {
	fmt.Println(s)

	// `const`语句可以出现在任何var语句可以出现的地方
	const n = 500000000

	// 常数表达式可以执行任意精度的运算
	const d = 3e20 / n
	fmt.Println(d)

	// 数值型常量没有确定的类型，直到被给定某个类型，比如显式类型转化。
	fmt.Println(int64(d))

	// 一个数字可以根据上下文的需要（比如变量赋值、函数调用）自动确定类型。 
	// 举个例子，这里的 math.Sin 函数需要一个 float64 的参数，n 会自动确定类型。
	fmt.Println(math.Sin(n))
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\constant\constant.go"        
constant
6e+11
600000000000
-0.28470407323754404

## 5-For循环

for 是 Go 中唯一的循环结构。这里会展示 for 循环的三种基本使用方式。

```go
package main

import "fmt"

func main() {
	
	// 最基础的方式，单个循环条件
	i := 1
	for i <= 3 {
		fmt.Println(i)
		 i = i + 1
	}

	// 经典的初始/条件/后续 for循环
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// 不带条件的for循环将一直重复执行，直到在循环体内
	// 使用了break或者return跳出循环
	for {
		fmt.Println("loop")
		break
	}

	// 你也可以使用continue直接进入下一次循环
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\for\for.go"    
1
2
3
7
8
9
loop
1
3
5

我们在后续教程中学习 range 语句，channels 以及其他数据结构时， 还会看到一些 for 的其它用法。

## 6-If/Else分支

if 和 else 分支结构在 Go 中非常直接。

```go
package main

import "fmt"

func main() {
	
	// 这里是一个基本的例子
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	// 你可以不要else只用if语句
	if 8%4 == 0 {
		fmt.Println("8 is divisible by 4")
	}

	// 在条件语句之前可以有一个声明语句；在这里声明的变量可以在
	// 这个语句所有的条件分支中使用
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		fmt.Println(num, "has 1 digit")
	} else {
		fmt.Println(num, "has multiple digits")
	}
}
```

> 注意，在 Go 中，条件语句的圆括号不是必需的，但是花括号是必需的。

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\if-else\if-else.go"
7 is odd
8 is divisible by 4
9 has 1 digit

*Go 没有三目运算符， 即使是基本的条件判断，依然需要使用完整的 if 语句。*

## 7-Switch分支结构

switch 是多分支情况时快捷的条件语句。

> 突然发现一个Bug，更新Vscode后，好像不能正常检查Go代码了，这就很无语呀。
> 但是终究不是影响运行的大问题，忍忍吧。😂

```go

```



## 8-数组

## 9-切片

## 10-Map

## 11-Range遍历

## 12-函数

## 13-多返回值

## 14-变参函数

## 15-闭包

## 16-递归

## 17-指针

## 18-结构体

## 19-方法

## 20-接口

## 21-错误处理

## 22-协程

## 23-通道

## 24-通道缓冲

## 25-通道同步

## 26-通道方向

## 27-通道选择器

## 28-超时处理

## 29-非阻塞通道操作

## 30-通道的关闭

## 31-通道遍历

## 32-Timer

## 33-Ticker

## 34-工作池

## 35-WaitGroup

## 36-速率限制

## 37-原子计数器

## 38-互斥锁

## 39-状态协程

## 40-排序

## 41-使用函数自定义排序

## 42-Panic

## 43-Defer

## 44-组合函数

## 45-字符串函数

## 46-字符串格式化

## 47-正则表达式

## 48-JSON

## 49-XML

## 50-时间

## 51-时间戳

## 52-时间的格式化和解析

## 53-随机数

## 54-数字解析

## 55-URL解析

## 56-SHA1哈希

## 57-Base64编码

## 58-读文件

## 59-写文件

## 60-行过滤器

## 61-文件路径

## 62-目录

## 63-临时文件和目录

## 64-单元测试

## 65-命令行参数

## 66-命令行标志

## 67-命令子命令

## 68-环境变量

## 69-HTTP客户端

## 70-Context

## 71-生成进程

## 72-执行进程

## 73-信号

## 74-退出


