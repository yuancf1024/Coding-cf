# 2021-11-20learn-go-in-100-lines

[toc]

## Readme

这是一篇标准的博客文章&公众号文章的写法，值得学习其框架和写法，博客就应该这么写。

[通过100行代码入门Go](https://mp.weixin.qq.com/s?__biz=MzkyMTI5MTgzNg==&mid=2247484103&idx=1&sn=cd0004ba5d7d8a4d3a970785335dd6e5&chksm=c1849f94f6f316821a2e5a28bca05214bd4259b0d43ceabcaab186e94cf78face001384d349e&mpshare=1&scene=24&srcid=1119MXvdOxOHZxPT1zyI5Drv&sharer_sharetime=1637298105345&sharer_shareid=dcf89ae72d7836db172b3c061cfb5a73#rd)

原文链接：https://fireship.io/lessons/learn-go-in-100-lines/

 ---

大家好，我是程序员幽鬼。

本文适合 Go 新手或想学习 Go 的朋友，通过 100 行代码学习 Go 知识。

## 01 介绍

Go 是由 Robert Griesemer、Rob Pike 和 Ken Thompson 在 Google 开发的一种开源编程语言。它通常被描述为“21 世纪的 C”，然而，它借鉴了其他几种语言的重要思想，如 ALGOL、Pascal、Modula-2、Oberon、CSP 等。*Go 的核心是依靠简单性、可靠性和效率来克服其先辈的缺点*。**Go 具有垃圾回收、包系统、一等公民函数、词法作用域、基于 UTF-8 的不可变字符串以及超棒的并发模型**。

作为一种编译型语言，Go 通常比解释性语言更快，并且由于其内置的类型系统而更安全。话虽如此，Go 在*表达性和安全性*之间有一个很好的平衡，它*为程序员提供了强类型系统的好处，而没有复杂工作流程的负担*。

该语言的**使用场景**从*网络服务器和分布式系统到 CLI、Web 和移动开发、可扩展数据库和云原生应用程序*等。

## 02 Hello World

在开始之前，请查看 [Go 安装指南](https://golang.org/doc/install) 在你的机器上安装好 Go。我们将从经典的“hello world”开始。尽管只是一个简单的例子，但它已经说明了许多中心思想。

hello_world.go

```go
package main // 一个独立的可执行文件所需

import "fmt" // fmt 包实现了格式化的输入输出

/*执行此程序时，执行运行的第一个函数是main.main（）*/
func main() {
	fmt.Println("Hello, world") // 从 fmt 包中调用 Println() 函数
}
```

PS D:\Coding-cf> go run "d:\Coding-cf\Go\01-优秀文章\learn-go-in-100-lines\hello_world\hello_world.go"
Hello, world

首先要注意的是，每个 Go 程序都组织在一个包中。包只是同一目录中的源文件的集合，允许变量、类型和函数在同一包内的其他源文件中可见。对于可执行程序入口文件，包名为 `main`，但文件名由程序员决定。

接下来，我们导入实现格式化 I/O 的包 `"fmt"`，并使用 `fmt.Println()` 函数将默认格式写入标准输出，以及针对需要更大灵活性时的 `fmt.Printf()` 函数。

最后，在`main`函数体中，我们调用`fmt.Println()` 输出传递给它的参数，即 Hello, world。请注意，`main` 函数不接受任何参数且不返回任何值。与`main`包类似，`main` 函数是可执行程序必须的。

要运行该程序，我们需要将源代码及其依赖项编译为可执行的二进制文件。我们通过在包目录中打开命令行终端并运行 `go build`，后跟源文件的名称进行编译。

$ go build hello_world.go

要执行二进制文件，请键入 ./ 后跟二进制文件的名称。

$ ./hello_world

// output
Hello, world

另一种选择是 `go run`  后跟源文件的名称。这将结合上面概述的两个步骤并产生相同的结果，*但是，不会在工作目录中保存任何可执行文件。这种方法主要用于一次性代码片段和将来不太可能需要的实验代码。*

## 03 100行代码基础知识

在接下来的 100 行代码中，我们将通过几个示例来说明 Go 的特性。我们将介绍*如何声明变量、了解 Go 的内置类型、处理数组和切片、介绍 map 以及控制流*。此外，会用额外的代码行介绍*指针、结构体和 Go 对并发*的内置支持。

### 变量

*在编写 Go 程序时，必须先声明变量，然后才能使用它们*。下面的示例显示了如何声明单个变量或一组变量。为了节省空间，输出显示为行内注释。

```go
package main

import "fmt"

/*声明单个变量*/

var a int

/*声明一组变量*/

var (
	b bool
	c float32
	d string
)

func main() {
	a = 42            // 单个变量赋值
	b, c = true, 32.0 // 多个变量赋值
	d = "string"      // 字符串必须包含双引号
	fmt.Println(a, b, c, d) // 42 true 32 string
}
```

请注意每个变量声明后是如何跟随该变量的类型。在下一节介绍类型之前，请注意，当需要在代码中引入常量时，需要将 `var` 关键字替换为 `const`。

在声明变量时，另一种选择是使用 `:= `*运算符一次性初始化和分配变量*。这称为*短变量声明*。让我们重构上面的代码来说明这一点。

```go
package main

import "fmt"

func main() {
 a := 42            // Initialize and assign to a single variable
 b, c := true, 32.0 // Initialize and assign to multiple variables
 d := "string"
 fmt.Println(a, b, c, d) // 42 true 32 string
}
```

简短的变量声明使我们的代码更简洁，因此我们将在本文中再次看到它。

### 类型

Go 提供了丰富的类型集合，包括数字、布尔值、字符串、error 以及创建自定义类型的能力。字符串是用双引号括起来的一系列 UTF-8 字符。数字类型是最多的，有符号 (  `int` ) 和无符号 (  `uint` ) 整数的 8、16、32和 64 位变体。

`byte` 是 `uint8` 的别名。`rune` 是 `int32` 的别名。`float`（浮点数）是 `float32` 或 `float64`。也支持复数，可以表示为 `complex128` 或 `complex64`。

当声明一个变量而未赋值时，会自动分配一个该类型的零值。例如，`var k int`，`k` 的值为 0。`var s string`，`s` 的值为 `""`。下面的示例显示了用户指定的类型与使用短变量声明分配的默认类型之间的区别。

```go
package main

import "fmt"

func main() {
	// 用户自定义类型
	const a int32 = 12 // 32位整数
	const b float32 = 20.5 // 32位浮点数
	var c complex128 = 1 + 4i // 128位复数
	var d uint16 = 14 // 16位无符号整数

	// 默认类型
	n := 42 // 整数
	pi := 3.14 // 浮点数
	x, y := true, false // 布尔类型
	z := "Go is awesome" // 字符串

	fmt.Printf("user-specified types:\n %T %T %T %T\n", a, b, c, d)
	fmt.Printf("default types:\n %T %T %T %T %T\n", n, pi, x, y, z)
}
```

注意 `fmt.Printf()` 第一个参数中的占位符 `%T`。在 Go 中，这称为动词，它代表传递的变量的类型。`\n` 在输出的末尾引入一个新行。`fmt.Printf()` 有许多其他动词，包括 `%d` 十进制整数、`%s` 字符串、`%f` 浮点数、`%t` 布尔、`%v` 值以及类型的任何自然值。

另一件要注意的事情是， `int` 占用空间到底是 `int32` 还是 `int64`，取决于底层系统。运行代码示例以查看正在运行的类型和格式动词。

PS D:\Coding-cf\Go\01-优秀文章\learn-go-in-100-lines\hello_world> go run "d:\Coding-cf\Go\01-优秀文章\learn-go-in-100-lines\types\types.go"
user-specified types:
 int32 float32 complex128 uint16
default types:
 int float64 bool bool string

### 数组

使用数组、切片和 map（Go 版本的 hashmap）可以实现在列表中存储多个元素。我们将在下面的示例中考虑这三个类型。*数组由它们的固定大小和所有元素的通用数据类型定义。*有趣的是，*数组的大小是类型的一部分，这意味着数组不能增长或缩小，否则它们将具有不同的类型。使用方括号访问数组元素*。下面的例子展示了如何声明一个包含字符串的数组以及循环遍历它的元素。

```go
package main

import "fmt"

func main() {
	// 定义一个大小为4的数组，存储可部署的选项
	var DeploymentOptions = [4]string{"R-pi", "AWS", "GCP", "Azure"}

	// 循环遍历可部署选项数组
	for i := 0; i < len(DeploymentOptions); i++ {
		option := DeploymentOptions[i]
		fmt.Println(i, option)
	}
}
```

请注意循环条件没有括号。在这个例子中，我们遍历数组输出当前索引和存储在该索引处的值。运行代码会产生以下输出。

PS D:\Coding-cf\Go\01-优秀文章\learn-go-in-100-lines\hello_world> go run "d:\Coding-cf\Go\01-优秀文章\learn-go-in-100-lines\array\array.go"
0 R-pi
1 AWS
2 GCP
3 Azure



## 04 超越基础知识

