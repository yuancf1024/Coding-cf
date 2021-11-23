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

首先要注意的是，每个 Go 程序都组织在一个包中。包只是同一目录中的源文件的集合，允许变量、类型和函数在同一包内的其他源文件中可见。对于可执行程序入口文件，包名为 main，但文件名由程序员决定。

接下来，我们导入实现格式化 I/O 的包 "fmt"，并使用 fmt.Println() 函数将默认格式写入标准输出，以及针对需要更大灵活性时的 fmt.Printf() 函数。

最后，在main函数体中，我们调用fmt.Println() 输出传递给它的参数，即 Hello, world。请注意，main 函数不接受任何参数且不返回任何值。与main包类似，main 函数是可执行程序必须的。

要运行该程序，我们需要将源代码及其依赖项编译为可执行的二进制文件。我们通过在包目录中打开命令行终端并运行 go build，后跟源文件的名称进行编译。

## 03 100行代码基础知识



## 04 超越基础知识

