# 2021-10-12runoob-go-tutorial

[toc]

# 学习记录

1. - [ ] 2021-10-12 1-
2.  

# 1 Go语言教程

Go 是一个开源的编程语言，它能让构造简单、可靠且高效的软件变得容易。

Go是从2007年末由Robert Griesemer, Rob Pike, Ken Thompson主持开发，后来还加入了Ian Lance Taylor, Russ Cox等人，并最终于2009年11月开源，在2012年早些时候发布了Go 1稳定版本。现在Go的开发已经是完全开放的，并且拥有一个活跃的社区。

**Go 语言特色**

* 简洁、快速、安全

* 并行、有趣、开源

* 内存管理、数组安全、编译迅速

**Go 语言用途**

*Go 语言被设计成一门应用于搭载 Web 服务器，存储集群或类似用途的巨型中央服务器的系统编程语言。*

*对于高性能分布式系统领域而言，Go 语言无疑比大多数其它语言有着更高的开发效率。它提供了***海量并行***的支持，这对于游戏服务端的开发而言是再好不过了。*

**第一个 Go 程序**

接下来我们来编写第一个 Go 程序 hello.go（Go 语言源文件的扩展是 .go），代码如下：

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
	fmt.Println("你好，袁晨峰！")
}
```

要执行 Go 语言代码可以使用 go run 命令。

执行以上代码输出:
PS C:\Users\chenfengyuan\go\src\Runoob\1_tutorial\hello> go run hello.go
Hello, World!

此外我们还可以使用 go build 命令来生成二进制文件：

PS C:\Users\chenfengyuan\go\src\Runoob\1_tutorial\hello> ./hello
Hello, World!
你好，袁晨峰！

# 2 Go语言环境安装

Go 语言支持以下系统：

* Linux
* FreeBSD
* Mac OS X（也称为 Darwin）
* Windows

安装包下载地址为：https://golang.org/dl/。

如果打不开可以使用这个地址：https://golang.google.cn/dl/。

各个系统对应的包名：

| 操作系统 | 包名                           |
| -------- | ------------------------------ |
| Windows  | go1.4.windows-amd64.msi        |
| Linux    | go1.4.linux-amd64.tar.gz       |
| Mac      | go1.4.darwin-amd64-osx10.8.pkg |
| FreeBSD  | go1.4.freebsd-amd64.tar.gz     |

**UNIX/Linux/Mac OS X, 和 FreeBSD 安装**

以下介绍了在UNIX/Linux/Mac OS X, 和 FreeBSD系统下使用源码安装方法：

1、下载二进制包：go1.4.linux-amd64.tar.gz。

2、将下载的二进制包解压至 /usr/local目录。

tar -C /usr/local -xzf go1.4.linux-amd64.tar.gz

3、将 /usr/local/go/bin 目录添加至PATH环境变量：

export PATH=$PATH:/usr/local/go/bin

注意：MAC 系统下你可以使用 .pkg 结尾的安装包直接双击来完成安装，安装目录在 /usr/local/go/ 下。

**Windows 系统下安装**

Windows 下可以使用 .msi 后缀(在下载列表中可以找到该文件，如go1.4.2.windows-amd64.msi)的安装包来安装。

默认情况下 .msi 文件会安装在 c:\Go 目录下。你可以将 c:\Go\bin 目录添加到 Path 环境变量中。添加后你需要重启命令窗口才能生效。

安装测试

创建工作目录 C:\>Go_WorkSpace。

test.go 文件代码：

```go
package main

import "fmt"

func main() {
   fmt.Println("Hello, World!")
}
```

使用 go 命令执行以上代码输出结果如下：

C:\Go_WorkSpace>go run test.go

Hello, World!

# 3 Go语言结构

在我们开始学习 Go 编程语言的基础构建模块前，让我们先来了解 Go 语言最简单程序的结构。

**Go Hello World 实例**

Go 语言的基础组成有以下几个部分：

* 包声明
* 引入包
* 函数
* 变量
* 语句 & 表达式
* 注释

接下来让我们来看下简单的代码，该代码输出了"Hello World!":

**实例**

```go
package main

import "fmt"

func main() {
   /* 这是我的第一个简单的程序 */
   fmt.Println("Hello, World!")
}
```

让我们来看下以上程序的各个部分：

*第一行代码 package main 定义了包名。*你必须在源文件中非注释的第一行指明这个文件属于哪个包，如：package main。package main表示一个可独立执行的程序，每个 Go 应用程序都包含一个名为 main 的包。

*下一行 import "fmt" 告诉 Go 编译器这个程序需要使用 fmt 包（的函数，或其他元素），fmt 包实现了格式化 IO（输入/输出）的函数。*

*下一行 func main() 是程序开始执行的函数。*main 函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的函数（如果有 init() 函数则会先执行该函数）。

下一行 /*...*/ 是注释，在程序执行时将被忽略。*单行注释是最常见的注释形式，你可以在任何地方使用以 // 开头的单行注释。*多行注释也叫块注释，均已以 /* 开头，并以 */ 结尾，且不可以嵌套使用，多行注释一般用于包的文档描述或注释成块的代码片段。

下一行 fmt.Println(...) 可以将字符串输出到控制台，并在最后自动增加换行字符 \n。

使用 fmt.Print("hello, world\n") 可以得到相同的结果。

Print 和 Println 这两个函数也支持使用变量，如：fmt.Println(arr)。如果没有特别指定，它们会以默认的打印格式将变量 arr 输出到控制台。

*当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头*，如 Group1，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为**导出**（像面向对象语言中的 public）；*标识符如果以小写字母开头，则对包外是不可见的，*但是他们在整个包的内部是可见并且可用的（**像面向对象语言中的 protected**）。

**执行 Go 程序**

让我们来看下如何编写 Go 代码并执行它。步骤如下：

打开编辑器如Sublime2，将以上代码添加到编辑器中。

将以上代码保存为 hello.go

打开命令行，并进入程序文件保存的目录中。

输入命令 go run hello.go 并按回车执行代码。

如果操作正确你将在屏幕上看到 "Hello World!" 字样的输出。

$ go run hello.go
Hello, World!

我们还可以使用 go build 命令来生成二进制文件：

$ go build hello.go 
$ ls
hello    hello.go
$ ./hello 
Hello, World!

**注意**

*需要注意的是 { 不能单独放在一行.*

# 4 Go语言基础语法

上一章节我们已经了解了 Go 语言的基本组成结构，本章节我们将学习 Go 语言的基础语法。

**Go 标记**

Go 程序可以由多个标记组成，可以是关键字，标识符，常量，字符串，符号。如以下 GO 语句由 6 个标记组成：

```go
fmt.Println("Hello, World!")
```

6 个标记是(每行一个)：

```go
1. fmt
2. .
3. Println
4. (
5. "Hello, World!"
6. )
```

**行分隔符**

在 Go 程序中，一行代表一个语句结束。每个语句不需要像 C 家族中的其它语言一样以分号 ; 结尾，因为这些工作都将由 Go 编译器自动完成。

如果你打算将多个语句写在同一行，它们则必须使用 ; 人为区分，但在实际开发中我们并不鼓励这种做法。

以下为两个语句：

```go
fmt.Println("Hello, World!")
fmt.Println("菜鸟教程：runoob.com")
```

**注释**

注释不会被编译，每一个包应该有相关注释。

单行注释是最常见的注释形式，你可以在任何地方使用以 // 开头的单行注释。多行注释也叫块注释，均已以 /* 开头，并以 */ 结尾。如：

```go
// 单行注释
/*
 Author by 菜鸟教程
 我是多行注释
 */
```

**标识符**

标识符用来命名变量、类型等程序实体。一个标识符实际上就是一个或是多个字母(A~Z和a~z)数字(0~9)、下划线_组成的序列，但是第一个字符必须是字母或下划线而不能是数字。

以下是有效的标识符：

```go
mahesh   kumar   abc   move_name   a_123
myname50   _temp   j   a23b9   retVal
```

以下是无效的标识符：

```go
1ab（以数字开头）
case（Go 语言的关键字）
a+b（运算符是不允许的）
```

**字符串连接**

Go 语言的字符串可以通过 + 实现：

实例
```go
package main
import "fmt"
func main() {
    fmt.Println("Google" + "Runoob")
}
```

以上实例输出结果为：

GoogleRunoob

**关键字**

下面列举了 Go 代码中会使用到的 25 个关键字或保留字：

```go
break	default	func	interface	select
case	defer	go	map	struct
chan	else	goto	package	switch
const	fallthrough	if	range	type
continue	for	import	return	var
```

除了以上介绍的这些关键字，Go 语言还有 36 个预定义标识符：

```go
append	bool	byte	cap	close	complex	complex64	complex128	uint16
copy	false	float32	float64	imag	int	int8	int16	uint32
int32	int64	iota	len	make	new	nil	panic	uint64
print	println	real	recover	string	true	uint	uint8	uintptr
```

*程序一般由关键字、常量、变量、运算符、类型和函数组成。*

程序中可能会使用到这些分隔符：括号 ()，中括号 [] 和大括号 {}。

程序中可能会使用到这些标点符号：.、,、;、: 和 …。

**Go 语言的空格**
*Go 语言中变量的声明必须使用空格隔开*，如：

```go
var age int;
```

语句中适当使用空格能让程序更易阅读。

无空格：

```go
fruit=apples+oranges;
```

在变量与运算符间加入空格，程序看起来更加美观，如：

```go
fruit = apples + oranges; 
```

**格式化字符串**

Go 语言中使用 `fmt.Sprintf` 格式化字符串并赋值给新串：

实例

```go
package main

import (
	"fmt"
)

func main() {
	// %d 表示整数， %s 表示字符串
	var stockcode = 123
	var enddate = "2021-10-18"
	var url = "Code=%d&endDate=%s"
	var target_url = fmt.Sprintf(url, stockcode, enddate)
	fmt.Println(target_url)
}
```

输出结果为：
Code=123&endDate=2021-10-18

更多内容参见：Go fmt.Sprintf 格式化字符串

# 5 Go语言数据类型

在 Go 编程语言中，数据类型用于声明函数和变量。

数据类型的出现是为了把数据分成所需内存大小不同的数据，编程的时候需要用大数据的时候才需要申请大内存，就可以充分利用内存。

Go 语言按类别有以下几种数据类型：

| 序号 | 类型和描述                                                                                                                                                         |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | **布尔型** 布尔型的值只可以是常量 true 或者 false。一个简单的例子：var b bool = true。                                                                             |
| 2    | **数字类型** 整型 int 和浮点型 float32、float64，Go 语言支持整型和浮点型数字，并且支持复数，*其中位的运算采用补码。*                                               |
| 3    | **字符串类型:** 字符串就是一串固定长度的字符连接起来的字符序列。Go 的字符串是由单个字节连接起来的。Go 语言的字符串的字节使用 UTF-8 编码标识 Unicode 文本。         |
| 4    | **派生类型:** 包括： (a) 指针类型（Pointer） (b) 数组类型 (c) 结构化类型(struct) (d) Channel 类型 (e) 函数类型 (f) 切片类型 (g) 接口类型（interface） (h) Map 类型 |

**数字类型**

*Go 也有基于架构的类型*，例如：int、uint 和 uintptr。

| 序号 | 类型和描述                                                           |
| ---- | -------------------------------------------------------------------- |
| 1    | uint8 无符号 8 位整型 (0 到 255)                                     |
| 2    | uint16 无符号 16 位整型 (0 到 65535)                                 |
| 3    | uint32 无符号 32 位整型 (0 到 4294967295)                            |
| 4    | uint64 无符号 64 位整型 (0 到 18446744073709551615)                  |
| 5    | int8 有符号 8 位整型 (-128 到 127)                                   |
| 6    | int16 有符号 16 位整型 (-32768 到 32767)                             |
| 7    | int32 有符号 32 位整型 (-2147483648 到 2147483647)                   |
| 8    | int64 有符号 64 位整型 (-9223372036854775808 到 9223372036854775807) |

**浮点型**

| 序号 | 类型和描述                    |
| ---- | ----------------------------- |
| 1    | float32 IEEE-754 32位浮点型数 |
| 2    | float64 IEEE-754 64位浮点型数 |
| 3    | complex64 32 位实数和虚数     |
| 4    | complex128 64 位实数和虚数    |

**其他数字类型**

以下列出了其他更多的数字类型：

| 序号 | 类型和描述                           |
| ---- | ------------------------------------ |
| 1    | byte 类似 uint8                      |
| 2    | rune 类似 int32                      |
| 3    | uint 32 或 64 位                     |
| 4    | int 与 uint 一样大小                 |
| 5    | uintptr 无符号整型，用于存放一个指针 |

# 6 Go语言变量

变量来源于数学，是计算机语言中能储存计算结果或能表示值抽象概念。

变量可以通过变量名访问。

Go 语言变量名由字母、数字、下划线组成，其中首个字符不能为数字。

声明变量的一般形式是使用 var 关键字：

```go
var identifier type
```

可以一次声明多个变量：

```go
var identifier1, identifier2 type
```

实例 test1.go

```go
package main

import "fmt"

func main() {
	var a string = "Runoob"
	fmt.Println(a)

	var b, c int = 1, 2
	fmt.Println(b, c)
}
```

以上实例输出结果为：
Runoob
1 2

**变量声明**

*第一种，指定变量类型，如果没有初始化，则变量默认为零值。*

```go
var v_name v_type
v_name = value
```

零值就是变量没有做初始化时系统默认设置的值。

实例 test2.go

```go
package main

import "fmt"

func main() {
	
	// 声明一个变量并初始化
	var a = "RUNOOB"
	fmt.Println(a)

	// 没有初始化就为零值
	var b int
	fmt.Println(b)

	// bool 零值为false
	var c bool
	fmt.Println(c)
}
```

以上实例执行结果为：
RUNOOB
0
false

* 数值类型（包括complex64/128）为 0

* 布尔类型为 false

* 字符串为 ""（空字符串）

以下几种类型为 nil：

```go
var a *int
var a []int
var a map[string] int
var a chan int
var a func(string) int
var a error // error 是接口
```

实例 test3.go

```go
package main

import "fmt"

func main() {
	var i int
	var f float64
	var b bool
	var s string
	// 
	var m *int
	var n []int
	var o map[string] int
	var p chan int
	var q func(string) int
	var r error

	fmt.Println("%v %v %v %q\n", i, f, b, s)
	fmt.Println(m, n, o, p, q, r)
}
```

输出结果是：
%v %v %v %q
 0 0 false
<nil> [] map[] <nil> <nil> <nil>

*第二种，根据值自行判定变量类型。*

var v_name = value

**实例** test4.go

```go
package main

import "fmt"

func main() {
	var d = true
	fmt.Println(d)
}
```

输出结果是：

true

*第三种，如果变量已经使用 var 声明过了，再使用 := 声明变量，就产生编译错误*，格式：

```go
v_name := value
```

例如：

```go
var intVal int 
intVal :=1 // 这时候会产生编译错误，因为 intVal 已经声明，不需要重新声明
```

直接使用下面的语句即可：

```go
intVal := 1 // 此时不会产生编译错误，因为有声明新的变量，因为 := 是一个声明语句
```

`intVal := 1` 相等于：

```go
var intVal int 
intVal =1 
```

可以将 var f string = "Runoob" 简写为 f := "Runoob"：

实例 test5.go

```go
package main

import "fmt"

func main() {
	f := "Runoob" // var f string = "Runoob"

	fmt.Println(f)
}
```

输出结果是：
Runoob

**多变量声明**

```go
//类型相同多个变量, 非全局变量
var vname1, vname2, vname3 type
vname1, vname2, vname3 = v1, v2, v3

var vname1, vname2, vname3 = v1, v2, v3 // 和 python 很像,不需要显示声明类型，自动推断

vname1, vname2, vname3 := v1, v2, v3 // 出现在 := 左侧的变量不应该是已经被声明过的，否则会导致编译错误

// 这种因式分解关键字的写法一般用于声明全局变量
var (
    vname1 v_type1
    vname2 v_type2
)
```

实例

```go
package main

var x, y int

var( // 这种因式分解关键字的写法一般用于声明全局变量
	a int
	b bool
)

var c, d int = 1, 2
var e, f = 123, "hello"

// 这种不带声明格式的只能在函数体中出现
// g, h = 123, "hello"

func main() {
	g, h := 123, "hello"
	println(x, y, a, b, c, d, e, f, g, h)
}
```

以上实例执行结果为：
0 0 0 false 1 2 123 hello 123 hello

**值类型和引用类型**

所有像 int、float、bool 和 string 这些基本类型都属于值类型，使用这些类型的变量直接指向存在内存中的值：

![](.\Figure\4.4.2_fig4.1.jpg)

当使用等号 = 将一个变量的值赋值给另一个变量时，如：j = i，实际上是在内存中将 i 的值进行了拷贝：

![](.\Figure/4.4.2_fig4.2.jpg)

你可以通过 &i 来获取变量 i 的内存地址，例如：0xf840000040（每次的地址都可能不一样）。*值类型的变量的值存储在栈中。*

内存地址会根据机器的不同而有所不同，甚至相同的程序在不同的机器上执行后也会有不同的内存地址。因为每台机器可能有不同的存储器布局，并且位置分配也可能不同。

更复杂的数据通常会需要使用多个字，这些数据一般使用引用类型保存。

一个引用类型的变量 r1 存储的是 r1 的值所在的内存地址（数字），或内存地址中第一个字所在的位置。

4.4.2_fig4.3

这个内存地址称之为指针，这个指针实际上也被存在另外的某一个值中。

同一个引用类型的指针指向的多个字可以是在连续的内存地址中（内存布局是连续的），这也是计算效率最高的一种存储形式；也可以将这些字分散存放在内存中，每个字都指示了下一个字所在的内存地址。

当使用赋值语句 r2 = r1 时，只有引用（地址）被复制。

如果 r1 的值被改变了，那么这个值的所有引用都会指向被修改后的内容，在这个例子中，r2 也会受到影响。

简短形式，使用 := 赋值操作符
我们知道可以在变量的初始化时省略变量的类型而由系统自动推断，声明语句写上 var 关键字其实是显得有些多余了，因此我们可以将它们简写为 a := 50 或 b := false。

a 和 b 的类型（int 和 bool）将由编译器自动推断。

这是使用变量的首选形式，但是它只能被用在函数体内，而不可以用于全局变量的声明与赋值。使用操作符 := 可以高效地创建一个新的变量，称之为初始化声明。

注意事项
如果在相同的代码块中，我们不可以再次对于相同名称的变量使用初始化声明，例如：a := 20 就是不被允许的，编译器会提示错误 no new variables on left side of :=，但是 a = 20 是可以的，因为这是给相同的变量赋予一个新的值。

如果你在定义变量 a 之前使用它，则会得到编译错误 undefined: a。

如果你声明了一个局部变量却没有在相同的代码块中使用它，同样会得到编译错误，例如下面这个例子当中的变量 a：

实例

# 7 Go语言常量

# 8 Go语言运算符

# 9 Go语言条件语句

# 10 Go语言循环条件

# 11 Go语言函数

# 12 Go语言变量作用域

# 13 Go语言数组

# 14 Go语言指针

# 15 Go语言结构体

# 16 Go语言切片（Slice）

# 17 Go语言范围（Range）

# 18 Go语言Map（集合）

# 19 Go语言递归函数

# 20 Go语言类型转换

# 21 Go语言接口

# 22 Go错误处理

# 23 GO并发

# 24 Go语言开发工具

