# 2021-11-03GoByExample-notes

[toc]

## 更新记录

- [x] 2021-11-03 1-Hello World
- [x] 2021-11-04 中午2+3
- [x] 2021-11-06~23 4~20
- [x] 2021-11-24 21
- [x] 2021-11-25 22~26
- [x] 2021-11-26 27~40 有一些没有完全消化，需要对照相应资料深入理解和思考
- [ ] 

## Readme

Go by Example 是一个通过带注释的示例程序学习 Go 语言的网站。网站包含了从简单的 Hello World 到高级特性 Goroutine、Channel 等一系列示例程序，并附带了注释说明，非常适合 Go 语言初学者。

如果您想学习 Go 语言基础知识，不要犹豫，请直接前往 Go by Example 开始学习！

## notes

1. 指针

\* 解引用指针，从对应地址获取值；

& 取得对象的内存地址，即指向对象的指针。

2. Go 计算程序运行时间

**计算代码块的运行时间**

> 其中time.Since()函数返回字符串类型，例如1h2m3s等，可能还有us等.

```go
start := time.Now()
//some func or operation
cost := time.Since(start)
fmt.Printf("cost=[%s]",cost) 
```

3. Go select使用

Go中的select和channel配合使用，通过select可以监听多个channel的I/O读写事件，当 IO操作发生时，触发相应的动作。

**基本用法**

```go
//select基本用法
select {
case <- chan1:
// 如果chan1成功读到数据，则进行该case处理语句
case chan2 <- 1:
// 如果成功向chan2写入数据，则进行该case处理语句
default:
// 如果上面都没有成功，则进入default处理流程
```

**使用规则**

1. 如果没有default分支,select会阻塞在多个channel上，对多个channel的读/写事件进行监控。
2. 如果有一个或多个IO操作可以完成，则Go运行时系统会随机的选择一个执行，否则的话，如果有default分支，则执行default分支语句，如果连default都没有，则select语句会一直阻塞，直到至少有一个IO操作可以进行。　　　

**计算函数的运行时间**

> 利用defer的作用，可以在函数开始的时候获取一个时间，使用time.Now()在函数结束的时候，获取程序从标记开始的时间段，可以得到函数运行的时间。

```go
func compute() {
    start := time.Now()
    defer func() {
        cost := time.Since(start)
        fmt.Println("cost=", cost)
    }()
    // some computation
}
```

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
package main

import (
	"fmt"
	"time"
)

func main() {

	i := 2
	fmt.Print("write ", i, " as ")
	// 一个基本的switch
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}
	// 在同一个 case 语句中，你可以使用逗号来分隔多个表达式。 
	// 在这个例子中，我们还使用了可选的 default 分支。
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("It's the weekend")
	default:
		fmt.Println("It's a weekday")
	}

	// 带表达式的 switch 是实现 if/else 逻辑的另一种方式。 
	// 这里还展示了 case 表达式也可以不使用常量。
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("It's before noon")
	default:
		fmt.Println("It's after noon")
	}

	// 类型开关 (type switch) 比较类型而非值。可以用来发现一个接口值的类型。 
	// 在这个例子中，变量 t 在每个分支中会有相应的类型。
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("I'm a bool")
		case int:
			fmt.Println("I'm an int")
		default:
			fmt.Printf("Don't know type %T\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\switch\switch.go"
write 2 as two
It's a weekday
It's after noon
I'm a bool     
I'm an int
Don't know type string

## 8-数组

在 Go 中，**数组** 是一个具有编号且长度固定的元素序列。

```go
package main

import "fmt"

func main() {
	var a[5]int
	fmt.Println("emp:", a)
	// 这里我们创建了一个刚好可以存放 5 个 int 元素的数组 a。 
	// 元素的类型和长度都是数组类型的一部分。 
	// 数组默认值是零值，对于 int 数组来说，元素的零值是 0。

	// 我们可以使用 array[index] = value 语法来设置数组指定位置的值， 
	// 或者用 array[index] 得到值。
	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])

	// 内置函数 len 可以返回数组的长度。
	fmt.Println("len:", len(a))

	// 使用这个语法在一行内声明并初始化一个数组。
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	// 数组类型是一维的，但是你可以组合构造多维的数据结构。
	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d:", twoD)
}
```

> 注意，使用 fmt.Println 打印数组时，会按照 [v1 v2 v3 ...] 的格式打印。

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\arrays\arrays.go"
emp: [0 0 0 0 0]
set: [0 0 0 0 100]
get: 100
len: 5
dcl: [1 2 3 4 5]
2d: [[0 1 2] [1 2 3]]

## 9-切片

在 Go 程序中，相较于数组，用得更多的是 _切片(slice)_。我们接着来看切片。

Slice 是 Go 中一个重要的数据类型，它提供了比数组更强大的序列交互方式。

```go
package main

import "fmt"

func main() {

	// 与数组不同，slice 的类型仅由它所包含的元素的类型决定（与元素个数无关）。 
	// 要创建一个长度不为 0 的空 slice，需要使用内建函数 make。 
	// 这里我们创建了一个长度为 3 的 string 类型的 slice（初始值为零值）。
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// 我们可以和数组一样设置和得到值
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// len 返回 slice 的长度
	fmt.Println("len:", len(s))

	// 除了基本操作外，slice 支持比数组更丰富的操作。
	// 比如 slice 支持内建函数 append， 该函数会返回一个包含了一个或者多个新值的 slice。 
	// 注意由于 append 可能返回一个新的 slice，我们需要接收其返回值。
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// slice 还可以 copy。
	// 这里我们创建一个空的和 s 有相同长度的 slice——c， 然后将 s 复制给 c。
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// slice 支持通过 slice[low:high] 语法进行“切片”操作。 
	// 例如，右边的操作可以得到一个包含元素 s[2]、s[3] 和 s[4] 的 slice。
	l1 := s[2:5] // 含左不含右
	fmt.Println("sl1:", l1)

	// 这个 slice 包含从 s[0] 到 s[5]（不包含 5）的元素。
	l2 := s[:5]
	fmt.Println("sl2:", l2)

	// 这个 slice 包含从 s[2]（包含 2）之后的元素。
	l3 := s[2:]
	fmt.Println("sl3:", l3)

	// 我们可以在一行代码中声明并初始化一个 slice 变量。
	t := []string{"g", "h", "i"}
	fmt.Println("dcl:", t)

	// Slice 可以组成多维数据结构。内部的 slice 长度可以不一致，这一点和多维数组不同。
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d:", twoD)
}
```

> 注意，slice 和数组是不同的类型，但它们通过 fmt.Println 打印的输出结果是类似的。

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\slices\slices.go"
emp: [  ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d: [[0] [1 2] [2 3 4]]

看看这个由 Go 团队撰写的一篇很棒的博文http://blog.golang.org/2011/01/go-slices-usage-and-internals.html ，了解更多关于 Go 中 slice 的设计和实现细节。

## 10-Map

现在，我们已经学习了数组和 slice，接下来我们将学习 Go 中的另一个重要的内建数据类型：map。

**map** 是 Go 内建的关联数据类型 （在一些其他的语言中也被称为 **哈希(hash)** 或者 **字典(dict)** ）。

要创建一个空 map，需要使用内建函数 make：`make(map[key-type]val-type)`。

使用典型的 `name[key] = val` 语法来设置键值对。

打印 map。例如，使用 `fmt.Println` 打印一个 map，会输出它所有的键值对。

使用 `name[key]` 来获取一个键的值。

内建函数 `len` 可以返回一个 map 的键值对数量。

内建函数 `delete` 可以从一个 map 中移除键值对。

当从一个 map 中取值时，还有可以选择是否接收的第二个返回值，该值表明了 map 中是否存在这个键。 这可以用来消除 *键不存在* 和 *键的值为零值* 产生的歧义， 例如 0 和 ""。这里我们不需要值，所以用 *空白标识符(blank identifier) `_`*将其忽略

你也可以通过右边的语法在一行代码中声明并初始化一个新的 map。

注意，使用 `fmt.Println` 打印一个 map 的时候， 是以 `map[k:v k:v]` 的格式输出的。

```go
package main

import "fmt"

func main() {
	m := make(map[string]int)

	m["k1"] = 7
	m["k2"] = 13

	fmt.Println("map:", m)

	v1 := m["k1"]
	fmt.Println("v1:", v1)

	fmt.Println("len:", len(m))

	delete(m, "k2")
	fmt.Println("map:", m)

	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	n:=map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)

}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\maps\maps.go"
map: map[k1:7 k2:13]
v1: 7
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]

## 11-Range遍历

`range` 用于迭代各种各样的数据结构。 让我们来看看如何在我们已经学过的数据结构上使用 `range`。

这里我们使用 `range` 来对 `slice` 中的元素求和。 *数组也可以用这种方法初始化并赋初值*。

`range` 在数组和 `slice` 中提供对每项的索引和值的访问。 上面我们不需要索引，所以我们使用 空白标识符 _ 将其忽略。 实际上，我们有时候是需要这个索引的。

range 在 map 中迭代键值对。

range 也可以只遍历 map 的键。

range 在字符串中迭代 unicode 码点(code point)。 第一个返回值是字符的起始字节位置，然后第二个是字符本身。

```go
package main

import "fmt"

func main() {
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	for k := range kvs {
		fmt.Println("key:", k)
	}

	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\range\range.go"
sum: 9
index: 1
a -> apple
b -> banana
key: a
key: b
0 103
1 111

## 12-函数

**函数** 是 Go 的核心。我们将通过一些不同的例子来进行学习它。

这里是一个函数，接受两个 int 并且以 int 返回它们的和

Go 需要明确的 return，也就是说，它不会自动 return 最后一个表达式的值

当多个连续的参数为同样类型时， 可以仅声明最后一个参数的类型，忽略之前相同类型参数的类型声明。

通过 *函数名(参数列表)* 来调用函数，

Go 函数还有很多其他的特性。 其中一个就是多值返回，它也是我们接下来要接触的。

```go
package main

import "fmt"

func plus(a int, b int) int {
	return a + b
}

func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {
	res := plus(1, 2)
	fmt.Println("1+2 = ", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\functions\functions.go"    
1+2 =  3
1+2+3 = 6

## 13-多返回值

Go 原生支持 _多返回值_。 这个特性在 Go 语言中经常用到，*例如用来同时返回一个函数的结果和错误信息。*

(int, int) 在这个函数中标志着这个函数返回 2 个 int。

这里我们通过 **多赋值** 操作来使用这两个不同的返回值。

如果你仅仅需要返回值的一部分的话，你可以使用空白标识符 _。

```go
package main

import "fmt"

func vals() (int, int) {
	return 3, 7
}

func main() {
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	_, c := vals()
	fmt.Println(c)
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\multiple-return-values\multiple-return-values.go"
3
7
7

## 14-变参函数

我们接下来要学习的是 Go 函数另一个很好的特性：变参函数。

**可变参数函数**。 在调用时可以传递任意数量的参数。 例如，`fmt.Println` 就是一个常见的变参函数。

这个函数接受任意数量的 `int` 作为参数。

变参函数使用常规的调用方式，传入独立的参数。

如果你有一个含有多个值的 `slice`，想把它们作为参数使用， 你需要这样调用 `func(slice...)`。

```go
package main

import "fmt"

func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {
	sum(1, 2)
	sum(1, 2, 3)

	nums := []int{1, 2, 3, 4}
	sum(nums...)
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\variadic-functions\variadic-functions.go"
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

## 15-闭包

接下来我们要看的是 Go 函数的另一个关键特性：闭包。

Go 支持**匿名函数**， 并能用其构造 **闭包**。 *匿名函数在你想定义一个不需要命名的内联函数时是很实用的。*

`intSeq` 函数返回一个在其函数体内定义的匿名函数。 返回的函数使用闭包的方式 **隐藏**变量 `i`。 返回的函数 **隐藏** 变量 `i` 以形成闭包。

我们调用 `intSeq` 函数，将返回值（一个函数）赋给 `nextInt`。 这个函数的值包含了自己的值 `i`，这样在每次调用 `nextInt` 时，都会更新 `i` 的值。

通过多次调用 nextInt 来看看闭包的效果。

为了确认这个状态对于这个特定的函数是唯一的，我们重新创建并测试一下。

```go
package main

import "fmt"

func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {
	nextInt := intSeq()

	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	newInts := intSeq()
	fmt.Println(newInts())
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\closures\closures.go"      
1
2
3
1

## 16-递归

我们马上要学习关于函数的最后一个特性：递归。

Go 支持 **递归**。 这里是一个经典的阶乘示例。

`fact` 函数在到达 `fact(0)` 前一直调用自身。

```go
package main

import "fmt"

func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\recursion\recursion.go"    
5040

## 17-指针

Go 支持 **指针**， 允许在程序中通过 `引用传递` 来传递值和数据结构。

我们将通过两个函数：`zeroval` 和 `zeroptr` 来比较 `指针` 和 `值`。 `zeroval` 有一个 `int` 型参数，所以使用值传递。 `zeroval` 将从调用它的那个函数中得到一个**实参的拷贝**：`ival`。

`zeroptr` 有一个和上面不同的参数：`*int`，这意味着它使用了 `int` 指针。 紧接着，函数体内的 `*iptr` 会 **解引用** 这个指针，*从它的内存地址得到这个地址当前对应的值*。 **对解引用的指针赋值，会改变这个指针引用的真实地址的值。**

通过 `&i` 语法来取得 `i` 的内存地址，即指向 `i` 的指针。

指针也是可以被打印的。

`zeroval` 在 `main` 函数中不能改变 `i` 的值， 但是 `zeroptr` 可以，*因为它有这个变量的内存地址的引用*。

```go
package main

import "fmt"

func zeroval(ival int) {
	ival = 0
}

func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("initial:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	fmt.Println("pointer:", &i)
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\pointers\pointers.go"      
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0xc000012078

## 18-结构体

Go 的**结构体(struct)** 是带类型的字段(fields)集合。 这在组织数据时非常有用。

这里的 `person` 结构体包含了 `name` 和 `age` 两个字段。

使用这个语法创建新的结构体元素。

你可以在初始化一个结构体元素时指定字段名字。

省略的字段将被初始化为零值。

```go
package main

import "fmt"

type person struct {
	name string
	age int
}

func main() {
	fmt.Println(person{"Bob", 20})

	fmt.Println(person{name: "Alice", age: 30})

	fmt.Println(person{name: "Fred"})

	// `&` 前缀生成一个结构体指针。
	fmt.Println(&person{name: "Ann", age: 40})

	// 使用`.`来访问结构体字段。
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// 也可以对结构体指针使用`.` - 指针会被自动解引用。
	sp := &s
	fmt.Println(sp.age)

	// 结构体是可变(mutable)的
	sp.age = 51
	fmt.Println(sp.age)
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\structs\structs.go"        
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
Sean
50
51

## 19-方法

Go 支持为结构体类型定义**方法(methods)** 。

这里的 `area` 是一个拥有 **`*rect` 类型接收器(receiver)**的方法。

可以为值类型或者指针类型的接收者定义方法。 这是一个值类型接收者的例子。

这里我们调用上面为结构体定义的两个方法。

调用方法时，Go 会自动处理值和指针之间的转换。 *想要避免在调用方法时产生一个拷贝，或者想让方法可以修改接受结构体的值， 你都可以使用指针来调用方法。*

```go
package main

import "fmt"

type rect struct {
	width, height int
}

func (r *rect) area() int {
	return r.width * r.height
}

func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	fmt.Println("area: ", r.area())
	fmt.Println("perim: ", r.perim())

	rp := &r // & 取得 r 的地址
	fmt.Println("area: ", rp.area())
	fmt.Println("perim: ", rp.perim())
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\methods\methods.go"        
area:  50
perim:  30
area:  50
perim:  30

## 20-接口

接下来，我们将学习 Go 对方法集进行命名和分组的另一机制：接口。

方法签名的集合叫做：_接口(Interfaces)_。

这是一个几何体的基本接口。

在这个例子中，我们将为 `rect` 和 `circle` 实现该接口。

**要在 Go 中实现一个接口，我们只需要实现接口中的所有方法。** 这里我们为 `rect` 实现了 `geometry` 接口。

`circle` 的实现。

如果一个变量实现了某个接口，我们就可以调用指定接口中的方法。 这儿有一个通用的 `measure` 函数，我们可以通过它来使用所有的 `geometry`。

结构体类型 `circle` 和 `rect` 都实现了 `geometry` 接口， 所以我们可以将其实例作为 `measure` 的参数。

要学习更多关于 Go 接口的知识， 可以看看这篇[很棒的博文](http://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go)。

```go
package main

import (
	"fmt"
	"math"
)

type geometry interface {
	area() float64
	perim() float64
}

type rect struct {
	width, height float64
}

type circle struct {
	radius float64
}

func (r rect) area() float64 {
	return r.width * r.height
}

func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	measure(r)
	measure(c)
}
```

PS C:\Users\chenfengyuan\Coding-cf> go run "c:\Users\chenfengyuan\Coding-cf\Go\GoByExample\interfaces\interfaces.go"  
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

## 21-错误处理 反复思考🤔

*符合 Go 语言习惯的做法是使用一个独立、明确的返回值来传递错误信息*。 这与 Java、Ruby 使用的异常（exception） 以及在 C 语言中有时用到的重载 (overloaded) 的单返回/错误值有着明显的不同。 Go 语言的处理方式能清楚的知道哪个函数返回了错误，并使用跟其他（无异常处理的）语言类似的方式来处理错误。

按照惯例，错误通常是最后一个返回值并且是 `error` 类型，它是一个内建的接口。

`errors.New` 使用给定的错误信息构造一个基本的 `error` 值。

返回错误值为 `nil` 代表没有错误。

你还可以通过实现 `Error()` 方法来自定义 error 类型。 这里使用自定义错误类型来表示上面例子中的参数错误。

在这个例子中，我们使用 `&argError` 语法来建立一个新的结构体， 并提供了 `arg` 和 `prob` 两个字段的值。

下面的两个循环测试了每一个会返回错误的函数。 注意，在 if 的同一行进行错误检查，是 Go 代码中的一种常见用法。

如果你想在程序中使用自定义错误类型的数据， 你需要通过类型断言来得到这个自定义错误类型的实例。

到 Go 官方博客去看这篇[很棒的文章](http://blog.golang.org/2011/07/error-handling-and-go.html)， 以获取更多关于错误处理的信息。

```go
package main

import (
	"errors"
	"fmt"
)

func f1(arg int) (int, error) {
	if arg == 42 {
		// errors.New 使用给定的错误信息构造一个基本的 error 值。
		return -1, errors.New("can't work with 42")
	}
	
	return arg + 3, nil // 返回错误值为 nil 代表没有错误。
}

type argError struct {
	arg int
	prob string
}

// 你还可以通过实现 Error() 方法来自定义 error 类型。 
// 这里使用自定义错误类型来表示上面例子中的参数错误。
func (e *argError) Error() string { // * 解引用指针，从对应地址获取值
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

// 在这个例子中，我们使用 &argError 语法来建立一个新的结构体， 
// 并提供了 arg 和 prob 两个字段的值。
func f2(arg int) (int, error) {
	if arg == 42 {
		return -1, &argError{arg, "can't work with it"}
	}
	return arg + 3, nil
}

func main() {
	// 下面的两个循环测试了每一个会返回错误的函数。 
	// 注意，在 if 的同一行进行错误检查，是 Go 代码中的一种常见用法。
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}

	for _, i := range []int{7, 42} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

// 如果你想在程序中使用自定义错误类型的数据， 
// 你需要通过类型断言来得到这个自定义错误类型的实例。
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
		fmt.Println("***Test***") // test
		fmt.Println(ok) // test
		fmt.Println(e.(*argError))
		fmt.Println(e)
	}
}
```

PS D:\Coding-cf> go run "d:\Coding-cf\Go\GoByExample\errors\errors.go"
f1 worked: 10
f1 failed: can't work with 42
f2 worked: 10
f2 failed: 42 - can't work with it
42
can't work with it
***Test***
true
42 - can't work with it
42 - can't work with it

## 22-协程

**协程(goroutine)**是轻量级的执行线程。

假设我们有一个函数叫做 f(s)。 我们一般会这样 *同步地* 调用它

使用 go f(s) 在一个协程中调用这个函数。 这个新的 Go 协程将会 *并发地* 执行这个函数。

你也可以为匿名函数启动一个协程。

现在两个协程在独立的协程中 *异步地* 运行， 然后等待两个协程完成（更好的方法是使用 [WaitGroup](https://gobyexample-cn.github.io/waitgroups)）。

```go
package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// 假设我们有一个函数叫做 f(s)。 我们一般会这样 同步地 调用它
	f("direct")

	// 使用 go f(s) 在一个协程中调用这个函数。 这个新的 Go 协程将会 并发地 执行这个函数。
	go f("goroutine")

	// 你也可以为匿名函数启动一个协程。
	go func(msg string) {
		fmt.Println(msg)
	} ("going")

	// 现在两个协程在独立的协程中 异步地 运行， 然后等待两个协程完成（更好的方法是使用 WaitGroup）。
	time.Sleep(time.Second)
	fmt.Println("done")
}
```

PS D:\Coding-cf\C\Hello> go run "d:\Coding-cf\Go\GoByExample\goroutines\goroutines.go"
direct : 0
direct : 1
direct : 2
going
goroutine : 0
goroutine : 1
goroutine : 2
done

当我们运行这个程序时，首先会看到阻塞式调用的输出，然后是两个协程的交替输出。 这种*交替的情况表示 Go runtime 是以并发的方式运行协程的*。

## 23-通道

下来我们将学习协程的辅助特性：通道（channels）。

**通道(channels)** 是**连接多个协程**的管道。 你可以*从一个协程将值发送到通道，然后在另一个协程中接收*。

使用 `make(chan val-type)` 创建一个新的通道。 通道类型就是他们需要传递值的类型。

使用 `channel <-` 语法 *发送* 一个新的值到通道中。 这里我们在一个新的协程中发送 `"ping"` 到上面创建的 `messages` 通道中。

使用 `<-channe`l 语法从通道中 *接收* 一个值。 这里我们会收到在上面发送的 `"ping"` 消息并将其打印出来。

```go
package main

import "fmt"

func main() {
	// 使用 make(chan val-type) 创建一个新的通道。 
	// 通道类型就是他们需要传递值的类型。
	messages := make(chan string)

	go func() {
		// 使用 channel <- 语法 发送 一个新的值到通道中。 
		// 这里我们在一个新的协程中发送 "ping" 到上面创建的 messages 通道中。
		messages <- "ping"
	}()

	// 使用 <-channel 语法从通道中 接收 一个值。 
	// 这里我们会收到在上面发送的 "ping" 消息并将其打印出来。

	msg := <- messages
	fmt.Println(msg)
}
```

PS D:\Coding-cf\C\Hello> go run "d:\Coding-cf\Go\GoByExample\channels\channels.go"
ping

我们运行程序时，通过通道， 成功的将消息 "ping" 从一个协程传送到了另一个协程中。

*默认发送和接收操作是阻塞的，直到发送方和接收方都就绪。* 这个特性允许我们，不使用任何其它的同步操作， 就可以在程序结尾处等待消息 "ping"。

## 24-通道缓冲

默认情况下，通道是 *无缓冲* 的，这意味着只有对应的接收（`<- chan`） 通道准备好接收时，才允许进行发送（`chan <-`）。 *有缓冲通道* 允许在没有对应接收者的情况下，缓存一定数量的值。

```go
package main

import "fmt"

func main() {
	// 这里我们 make 了一个字符串通道，最多允许缓存 2 个值。
	messages := make(chan string, 2)

	// 由于此通道是有缓冲的， 因此我们可以将这些值发送到通道中，而无需并发的接收。
	messages <- "buffered"
	messages <- "channel"

	// 然后我们可以正常接收这两个值。
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
```

PS D:\Coding-cf\C\Hello> go run "d:\Coding-cf\Go\GoByExample\channel-buffering\channel-buffering.go"
buffered
channel

## 25-通道同步 思考🤔

我们可以**使用通道来同步协程之间的执行状态**。 这儿有一个例子，*使用阻塞接收的方式，实现了等待另一个协程完成*。 **如果需要等待多个协程，WaitGroup 是一个更好的选择。**

```go
package main

import (
	"fmt"
	"time"
)

func worker(done chan bool) {
	// 我们将要在协程中运行这个函数。 
	// done 通道将被用于通知其他协程这个函数已经完成工作。
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// 发送一个值来通知我们已经完工啦。
	done <- true // 从一个协程将值发送到通道
}

func main() {

	// 运行一个 worker 协程，并给予用于通知的通道。
	done := make(chan bool, 1)
	go worker(done)

	// 程序将一直阻塞，直至收到 worker 使用通道发送的通知。
	<-done // 从通道接受
	// 如果你把 <- done 这行代码从程序中移除， 程序甚至可能在 worker 开始运行前就结束了。
}
```

PS D:\Coding-cf\C\Hello> go run "d:\Coding-cf\Go\GoByExample\channel-synchronization\channel-synchronization.go"
working...done

## 26-通道方向

*当使用通道作为函数的参数时，你可以指定这个通道是否为只读或只写。 该特性可以提升程序的类型安全。*

```go
package main

import "fmt"

// ping 函数定义了一个只能发送数据的（只写）通道。 
// 尝试从这个通道接收数据会是一个编译时错误。
func ping(pings chan<- string, msg string) {
	pings <- msg // 发送数据到管道
}

// pong 函数接收两个通道，pings 仅用于接收数据（只读），
// pongs 仅用于发送数据（只写）。
func pong(pings <-chan string, pongs chan<- string) {
	msg := <- pings // 从管道接收数据
	pongs <- msg // 发送数据到管道
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs) // 从通道接收
}
```

PS D:\Coding-cf\C\Hello> go run "d:\Coding-cf\Go\GoByExample\channel-directions\channel-directions.go"
passed message

> 直接打印通道，会输出通道对应的内存地址

```go
PS D:\Coding-cf\C\Hello> go run "d:\Coding-cf\Go\GoByExample\channel-directions\channel-directions.go"
0xc00006c0c0
```

## 27-通道选择器

Go 的 **选择器（select）** 让你可以同时等待多个通道操作。 **将协程、通道和选择器结合，是 Go 的一个强大特性。**

```GO
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	// 在这个例子中，我们将从两个通道中选择。
	c1 := make(chan string)
	c2 := make(chan string)

	// 各个通道将在一定时间后接收一个值， 
	// 通过这种方式来模拟并行的协程执行（例如，RPC 操作）时造成的阻塞（耗时）。
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	} ()

	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	} ()

	// 我们使用 select 关键字来同时等待这两个值， 
	// 并打印各自接收到的值。
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <- c1:
			fmt.Println("received", msg1)
		case msg2 := <- c2:
			fmt.Println("received", msg2)
		}
	}
	cost := time.Since(start)
	fmt.Printf("cost=[%s]",cost)
}
```

PS D:\Coding-cf\C\Hello> go run "d:\Coding-cf\Go\GoByExample\select\select.go"
received one
received two
cost=[2.0040901s]

跟预期的一样，我们首先接收到值 "one"，然后是 "two"。

注意，程序总共仅运行了两秒左右。因为 1 秒 和 2 秒的 Sleeps 是并发执行的，

## 28-超时处理

**超时** 对于一个需要连接外部资源， 或者有耗时较长的操作的程序而言是很重要的。 得益于通道和 select，在 Go 中实现超时操作是简洁而优雅的。

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	// 在这个例子中，假如我们执行一个外部调用， 
	// 并在 2 秒后使用通道 c1 返回它的执行结果。
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	} ()

	// 这里是使用 select 实现一个超时操作。 
	// res := <- c1 等待结果，<-Time.After 等待超时（1秒钟）以后发送的值。 
	// 由于 select 默认处理第一个已准备好的接收操作，
	// 因此如果操作耗时超过了允许的 1 秒的话，将会执行超时 case。
	select {
	case res := <- c1:
		fmt.Println(res)
	case <- time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	c2 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()

	// 如果我们允许一个长一点的超时时间：3 秒， 
	// 就可以成功的从 c2 接收到值，并且打印出结果。
	select {
	case res := <- c2:
		fmt.Println(res)
	case <- time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}
}
```

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\timeouts\timeouts.go"
timeout 1
result 2

运行这个程序，首先显示运行超时的操作，然后是成功接收的。

## 29-非阻塞通道操作

常规的通过通道发送和接收数据是阻塞的。 然而，我们可以*使用带一个 `default` 子句的 `select` 来实现 **非阻塞** 的发送、接收，甚至是非阻塞的多路 `select`*。

```go
package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// 这是一个非阻塞接收的例子。 
	// 如果在 messages 中存在，然后 select 将这个值带入 <-messages case 中。 
	// 否则，就直接到 default 分支中。
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	// 一个非阻塞发送的例子，代码结构和上面接收的类似。 
	// msg 不能被发送到 message 通道，
	// 因为这是 个无缓冲区通道，并且也没有接收者，
	// 因此， default 会执行。
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	// 我们可以在 default 前使用多个 case 子句来实现一个多路的非阻塞的选择器。 
	// 这里我们试图在 messages 和 signals 上同时使用非阻塞的接收操作。
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("no activity")
	}
}
```

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\non-blocking-channel-operations\non-blocking-channel-operations.go"
no message received
no message sent
no activity

## 30-通道的关闭 Question

> 此部分运行结果和教程中的给出结果不一致，应该是Go版本迭代出现的问题，根据最新Go特性来解释。

**关闭** 一个通道意味着不能再向这个通道发送值了。 该特性可以向通道的接收方传达工作已经完成的信息。

```go
package main

import "fmt"

// 在这个例子中，我们将使用一个 jobs 通道，将工作内容， 
// 从 main() 协程传递到一个工作协程中。 
// 当我们没有更多的任务传递给工作协程时，我们将 close 这个 jobs 通道。

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// 这是工作协程。使用 j, more := <- jobs 循环的从 jobs 接收数据。 
	// 根据接收的第二个值，如果 jobs 已经关闭了， 并且通道中所有的值都已经接收完毕，
	// 那么 more 的值将是 false。 当我们完成所有的任务时，
	// 会使用这个特性通过 done 通道通知 main 协程。
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// 使用 jobs 发送 3 个任务到工作协程中，然后关闭 jobs。
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")
	fmt.Println("Test1")

	// 使用前面学到的通道同步方法等待任务结束。
	<-done // 从通道接受
}
```

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\closing-channels\closing-channels.go"
sent job 1
sent job 2
sent job 3
sent all jobs
Test1
received job 1
received job 2
received job 3
received all jobs

给出的参考结果：
```shell
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs
```

根据**关闭通道**的思想，可以引出我们的下一个示例：遍历通道。

## 31-通道遍历

在前面的例子中， 我们讲过 `for` 和 `range` 为基本的数据结构提供了迭代的功能。 我们也可以使用这个语法来遍历的从通道中取值。

```go
package main

import "fmt"

func main() {

	// 我们将遍历在 queue 通道中的两个值。
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// range 迭代从 queue 中得到每个值。 
	// 因为我们在前面 close 了这个通道，
	// 所以，这个迭代会在接收完 2 个值之后结束。
	for elem := range queue {
		fmt.Println(elem)
	}
}
```

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\range-over-channels\tempCodeRunnerFile.go"
one
two

*这个例子也让我们看到，一个非空的通道也是可以关闭的， 并且，通道中剩下的值仍然可以被接收到。*

## 32-Timer

我们经常需要在未来的某个时间点运行 Go 代码，或者每隔一定时间重复运行代码。 Go 内置的 *定时器* 和 *打点器* 特性让这些变得很简单。 我们会先学习定时器，然后再学习打点器。

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	// 定时器表示在未来某一时刻的独立事件。
	// 你告诉定时器需要等待的时间，
	// 然后它将提供一个用于通知的通道。
	// 这里的定时器将等待 2 秒。
	timer1 := time.NewTimer(2 * time.Second)

	// <-timer1.C 会一直阻塞，
	// 直到定时器的通道 C 明确的发送了定时器失效的值。
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// 如果你需要的仅仅是单纯的等待，使用 time.Sleep 就够了。
	// 使用定时器的原因之一就是，你可以在定时器触发之前将其取消。例如这样。
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}
	// 给 timer2 足够的时间来触发它，以证明它实际上已经停止了。
	time.Sleep(2 * time.Second)

	cost := time.Since(start)
	fmt.Printf("cost=[%s]", cost)
}
```

第一个定时器将在程序开始后大约 2s 触发， 但是第二个定时器还未触发就停止了。

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\timers\timers.go"
Timer 1 fired
Timer 2 stopped
cost=[4.0115602s]

## 33-Ticker

- **定时器** 是当你*想要在未来某一刻执行一次时使用的*
- **打点器** 则是为你*想要以固定的时间间隔重复执行而准备的。* 这里是一个打点器的例子，它将定时的执行，直到我们将它停止。

```go
package main

import (
	"fmt"
	"time"
)

func main() {

	start := time.Now()

	// 打点器和定时器的机制有点相似：使用一个通道来发送数据。
	// 这里我们使用通道内建的 select，等待每 500ms 到达一次的值。
	fmt.Println("Test1") // Test
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	// 打点器可以和定时器一样被停止。
	// 打点器一旦停止，将不能再从它的通道中接收到值。
	// 我们将在运行 1600ms 后停止这个打点器。
	fmt.Println("Test2") // Test
	time.Sleep(1600 * time.Millisecond)
	fmt.Println("Test3") // Test
	ticker.Stop()
	fmt.Println("Test4") // Test
	done <- true
	fmt.Println("Ticker stopped")

	cost := time.Since(start)
	fmt.Printf("cost=[%s]", cost)
}

```

我们运行这个程序时，打点器会在我们停止它前打点 3 次。

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\tickers\tickers.go"
Test1
Test2
Tick at 2021-11-26 14:54:56.7337073 +0800 CST m=+0.514811001
Tick at 2021-11-26 14:54:57.2339533 +0800 CST m=+1.015057001
Tick at 2021-11-26 14:54:57.7348781 +0800 CST m=+1.515981801
Test3
Test4
Ticker stopped
cost=[1.6045433s]

## 34-工作池

在这个例子中，我们将看到如何使用*协程与通道*实现一个**工作池**。

```go
package main

import (
	"fmt"
	"time"
)

// 这是 worker 程序，我们会并发的运行多个 worker。
// worker 将在 jobs 频道上接收工作，并在 results 上发送相应的结果。
// 每个 worker 我们都会 sleep 一秒钟，
// 以模拟一项昂贵的（耗时一秒钟的）任务。
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {

	start := time.Now()

	// 为了使用 worker 工作池并且收集其的结果，我们需要 2 个通道。
	const numJobs = 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// 这里启动了 3 个 worker， 初始是阻塞的，因为还没有传递任务。
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}
	fmt.Println("Test1") // Test
	// 这里我们发送 5 个 jobs，
	// 然后 close 这些通道，表示这些就是所有的任务了。
	for j := 1; j <= numJobs; j++ {
		jobs <- j // 协程输出的地方
	}

	close(jobs)
	fmt.Println("Test2") // Test
	// 最后，我们收集所有这些任务的返回值。
	// 这也确保了所有的 worker 协程都已完成。
	// 另一个等待多个协程的方法是使用WaitGroup。
	for a := 1; a <= numJobs; a++ {
		<-results
	}
	fmt.Println("Test3") // Test

	cost := time.Since(start)
	fmt.Printf("cost=[%s]", cost)
}
```

运行程序，显示 5 个任务被多个 worker 执行。 尽管所有的工作总共要花费 5 秒钟，但该程序只花了 2 秒钟， 因为 3 个 worker 是并行的。

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\worker-pools\worker-pools.go"
Test1
Test2
worker 3 started job 3
worker 1 started job 1
worker 2 started job 2
worker 2 finished job 2
worker 2 started job 4
worker 1 finished job 1
worker 1 started job 5
worker 3 finished job 3
worker 1 finished job 5
worker 2 finished job 4
Test3
cost=[2.0199268s]

## 35-WaitGroup

想要等待多个协程完成，我们可以使用 *wait group*。

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

// 每个协程都会运行该函数。 注意，WaitGroup 必须通过指针传递给函数。
func worker(id int, wg *sync.WaitGroup) {

	// return 时，通知 WaitGroup，当前协程的工作已经完成。
	defer wg.Done()

	fmt.Printf("Worker %d starting\n", id)

	// 睡眠一秒钟，以此来模拟耗时的任务。
	time.Sleep(time.Second)
	fmt.Printf("Worker %d done\n", id)
}

func main() {

	start := time.Now()

	// WaitGroup 用于等待该函数启动的所有协程。
	var wg sync.WaitGroup

	// 启动几个协程，并为其递增 WaitGroup 的计数器
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go worker(i, &wg)
	}

	fmt.Println("Test")

	// 阻塞，直到 WaitGroup 计数器恢复为 0； 即所有协程的工作都已经完成。
	wg.Wait()

	cost := time.Since(start)
	fmt.Printf("cost=[%s]", cost)
}
```

每次运行，各个协程开启和完成的时间可能是不同的。

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\waitgroups\waitgroups.go"
Worker 2 starting
Worker 3 starting
Test
Worker 5 starting
Worker 4 starting
Worker 1 starting
Worker 1 done
Worker 3 done
Worker 4 done
Worker 2 done
Worker 5 done
cost=[1.009809s]

## 36-速率限制

**速率限制** 是控制服务资源利用和质量的重要机制。 *基于协程、通道和打点器，Go 优雅的支持速率限制*。

```go
package main

import (
	"fmt"
	"time"
)

func main() {

	start := time.Now()

	// 首先，我们将看一个基本的速率限制。
	// 假设我们想限制对收到请求的处理，我们可以通过一个通道处理这些请求
	requests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	// limiter 通道每 200ms 接收一个值。 这是我们任务速率限制的调度器。
	limiter := time.Tick(200 * time.Millisecond)

	// 通过在每次请求前阻塞 limiter 通道的一个接收，
	// 可以将频率限制为，每 200ms 执行一次请求。
	for req := range requests {
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	// 有时候我们可能希望在速率限制方案中允许短暂的并发请求，
	// 并同时保留总体速率限制。 我们可以通过缓冲通道来完成此任务。
	// burstyLimiter 通道允许最多 3 个爆发（bursts）事件。
	burstLimiter := make(chan time.Time, 3)

	// 填充通道，表示允许的爆发（bursts）。
	for i := 0; i < 3; i++ {
		burstLimiter <- time.Now()
	}

	// 每 200ms 我们将尝试添加一个新的值到 burstyLimiter中， 直到达到 3 个的限制。
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			burstLimiter <- t
		}
	}()

	// 现在，模拟另外 5 个传入请求。 受益于 burstyLimiter 的爆发（bursts）能力，
	// 前 3 个请求可以快速完成。
	burstRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstRequests <- i
	}
	close(burstRequests)
	for req := range burstRequests {
		<-burstLimiter
		fmt.Println("request", req, time.Now())
	}

	cost := time.Since(start)
	fmt.Printf("cost=[%s]", cost)
}
```

运行程序，我们看到第一批请求意料之中的大约每 200ms 处理一次。

PS D:\Coding-cf\Go\GoByExample\select> go run "d:\Coding-cf\Go\GoByExample\rate-limiting\rate-limiting.go"
request 1 2021-11-26 15:54:52.7125512 +0800 CST m=+0.218740401
request 2 2021-11-26 15:54:52.9143874 +0800 CST m=+0.420576601
request 3 2021-11-26 15:54:53.116389 +0800 CST m=+0.622578201
request 4 2021-11-26 15:54:53.3061452 +0800 CST m=+0.812334401
request 5 2021-11-26 15:54:53.5101447 +0800 CST m=+1.016333901
request 1 2021-11-26 15:54:53.5101447 +0800 CST m=+1.016333901
request 2 2021-11-26 15:54:53.5101447 +0800 CST m=+1.016333901 
request 3 2021-11-26 15:54:53.5101447 +0800 CST m=+1.016333901 
request 4 2021-11-26 15:54:53.7157193 +0800 CST m=+1.221908501
request 5 2021-11-26 15:54:53.9223151 +0800 CST m=+1.428504301
cost=[1.4199199s]

第二批请求，由于爆发（burstable）速率控制，我们直接连续处理了 3 个请求， 然后以大约每 200ms 一次的速度，处理了剩余的 2 个请求。

## 37-原子计数器

Go 中最主要的状态管理机制是依靠通道间的通信来完成的。 我们已经在工作池的例子中看到过，并且，还有一些其他的方法来管理状态。 这里，我们来看看如何使用 `sync/atomic` 包在多个协程中进行 _原子计数_。

```go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

func main() {

	start := time.Now()

	// 我们将使用一个无符号整型（永远是正整数）变量来表示这个计数器。
	var ops uint64

	// WaitGroup 帮助我们等待所有协程完成它们的工作。
	var wg sync.WaitGroup

	// 我们会启动 50 个协程，并且每个协程会将计数器递增 1000 次。
	for i := 0; i < 50; i++ {
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {

				// 使用 AddUint64 来让计数器自动增加，
				// 使用 & 语法给定 ops 的内存地址。
				atomic.AddUint64(&ops, 1)

				// 由于多个协程会互相干扰，运行时值会改变，可能会导致我们得到一个不同的数字
				// ops++
			}
			wg.Done()
		}()
	}

	// 等待，直到所有协程完成。
	wg.Wait()

	// 现在可以安全的访问 ops，因为我们知道，此时没有协程写入 ops， 此外，
	// 还可以使用 atomic.LoadUint64 之类的函数，在原子更新的同时安全地读取它们。
	fmt.Println("ops:", ops)

	cost := time.Since(start)
	fmt.Printf("cost=[%s]", cost)
}
```

PS D:\Coding-cf\Go\GoByExample\atomic-counters> go run "d:\Coding-cf\Go\GoByExample\atomic-counters\atomic-counters.go"
ops: 50000
cost=[1.0355ms]

预计会进行 `50,000` 次操作。如果我们使用非原子的 `ops++` 来增加计数器， 由于多个协程会互相干扰，运行时值会改变，可能会导致我们得到一个不同的数字。 此外，运行程序时带上 `-race` 标志，我们可以获取数据竞争失败的详情

PS D:\Coding-cf\Go\GoByExample\atomic-counters> go run atomic-counters.go -race      
ops: 49157
cost=[0s]

接下来，我们看一下管理状态的另一个工具——互斥锁。

## 38-互斥锁

在前面的例子中，我们看到了如何使用原子操作来管理简单的计数器。 对于更加复杂的情况，我们可以使用一个**互斥锁** 来在 Go 协程间安全的访问数据。

```go
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"sync/atomic"
	"time"
)

func main() {

	start := time.Now()

	// 在这个例子中，state 是一个 map。
	var state = make(map[int]int)

	// mutex 将同步对 state 的访问。
	var mutex = &sync.Mutex{}

	// 我们会持续追踪读写操作的数量。
	var readOps uint64
	var writeOps uint64

	// 这里我们启动 100 个协程， 每个协程以每 1ms 一次的频率来重复读取 state。
	for r := 0; r < 100; r++ {
		go func() {
			total := 0
			for {
				// 每次循环读取，我们使用一个键来进行访问，
				// Lock() 这个 mutex 来确保对 state 的独占访问，
				// 读取选定的键的值，Unlock() 这个 mutex，
				// 并将 ops 值加 1。
				key := rand.Intn(5)
				mutex.Lock()
				total += state[key]
				mutex.Unlock()
				atomic.AddUint64(&readOps, 1)

				// 在下次读取前等待片刻。
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 同样的，我们启动 10 个协程来模拟写入操作， 使用和读取相同的模式。

	for w := 0; w < 10; w++ {
		go func() {
			for {
				key := rand.Intn(5)
				val := rand.Intn(100)
				mutex.Lock()
				state[key] = val
				mutex.Unlock()
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 让这 10 个协程对 state 和 mutex 的操作持续 1 s。
	time.Sleep(time.Second)

	// 获取并输出最终的操作计数。
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)

	// 对 state 使用一个最终的锁，展示它是如何结束的。
	mutex.Lock()
	fmt.Println("state:", state)
	mutex.Unlock()

	cost := time.Since(start)
	fmt.Printf("cost=[%s]", cost)
}
```

**Question**：*导致教程、PC、The Go Playground运行结果不一致的原因？*

> GoByExample 教程中的运行结果

运行这个程序，显示我们进行了大约 90,000 次 mutex 同步的 state 操作。

```shell
$ go run mutexes.go
readOps: 83285
writeOps: 8320
state: map[1:97 4:53 0:33 2:15 3:2]
```

> PC运行结果

PS D:\Coding-cf\Go\GoByExample\atomic-counters> go run "d:\Coding-cf\Go\GoByExample\mutexes\mutexes.go"
readOps: 6557
writeOps: 660
state: map[0:28 1:8 2:50 3:78 4:9]
cost=[1.0066632s]

> The Go Playground运行结果

readOps: 100001
writeOps: 10000
state: map[0:94 1:87 2:53 3:90 4:8]
cost=[1s]

接下来我们将看一下，*只使用协程和通道， 如何实现相同的任务状态管理*。

## 39-状态协程 思考🤔

在前面的例子中，我们用 互斥锁 进行了明确的锁定， 来让共享的 state 跨多个 Go 协程同步访问。 另一个选择是，*使用内建协程和通道的同步特性来达到同样的效果*。 **Go 共享内存的思想是**，*通过通信使每个数据仅被单个协程所拥有，即**通过通信实现共享内存***。 基于通道的方法与该思想完全一致！

```go
package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// 在这个例子中，state 将被一个单独的协程拥有。
// 这能保证数据在并行读取时不会混乱。 为了对 state 进行读取或者写入，
// 其它的协程将发送一条数据到目前拥有数据的协程中，
// 然后等待接收对应的回复。 结构体 readOp 和 writeOp 封装了这些请求，
// 并提供了响应协程的方法。

type readOp struct {
	key  int
	resp chan int
}

type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	start := time.Now()

	// 和前面的例子一样，我们会计算操作执行的次数。
	var readOps uint64
	var writeOps uint64

	// 其他协程将通过 reads 和 writes 通道来发布 读 和 写 请求。
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// 这就是拥有 state 的那个协程， 和前面例子中的 map 一样，
	// 不过这里的 state 是被这个状态协程私有的。
	// 这个协程不断地在 reads 和 writes 通道上进行选择，
	// 并在请求到达时做出响应。 首先，执行请求的操作；然后，执行响应，
	// 在响应通道 resp 上发送一个值，
	// 表明请求成功（reads 的值则为 state 对应的值）。
	go func() { // 此协程的运行机制是什么？
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// 启动 100 个协程通过 reads 通道向拥有 state 的协程发起读取请求。
	// 每个读取请求需要构造一个 readOp，发送它到 reads 通道中，
	// 并通过给定的 resp 通道接收结果。

	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int),
				}
				reads <- read // 发送数据
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 用相同的方法启动 10 个写操作。
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool),
				}
				writes <- write
				<-write.resp
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 让协程们跑 1s。
	time.Sleep(time.Second)

	// 最后，获取并报告 ops 值。
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)

	cost := time.Since(start)
	fmt.Printf("cost=[%s]", cost)
}
```

运行这个程序显示这个基于协程的状态管理的例子 达到了每秒大约 80,000 次操作。

> GoByExample 教程中的运行结果

```shell
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177
```

> PC运行结果

PS D:\Coding-cf\Go\GoByExample\atomic-counters> go run "d:\Coding-cf\Go\GoByExample\stateful-goroutines\stateful-goroutines.go"
readOps: 6589
writeOps: 660

> The Go Playground运行结果

readOps: 100099
writeOps: 10010
cost=[1s]

通过这个例子我们可以看到，**基于协程的方法比基于互斥锁的方法要复杂得多**。 但是，在某些情况下它可能很有用， 例如，当你涉及其他通道，或者管理多个同类互斥锁时，会很容易出错。 *您应该使用最自然的方法，尤其是在理解程序正确性方面。*

## 40-排序

Go 的 sort 包实现了内建及用户自定义数据类型的排序功能。 我们先来看看内建数据类型的排序。

```go
package main

import (
	"fmt"
	"sort"
)

func main() {

	// 排序方法是针对内置数据类型的； 这是一个字符串排序的例子。
	// 注意，它是原地排序的，所以他会直接改变给定的切片，
	// 而不是返回一个新切片。
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	// 一个 int 排序的例子。
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints: ", ints)

	// 我们也可以使用 sort 来检查一个切片是否为有序的。
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted: ", s)
}
```

运行程序，打印排序好的字符串和整型切片， 以及数组是否有序的检查结果：true。

PS D:\Coding-cf\Go\GoByExample\atomic-counters> go run "d:\Coding-cf\Go\GoByExample\sorting\sorting.go"
Strings: [a b c]
Ints:  [2 4 7]
Sorted:  true

## 41-使用函数自定义排序

有时候，我们可能想根据自然顺序以外的方式来对集合进行排序。 例如，假设我们要按字符串的长度而不是按字母顺序对它们进行排序。 这儿有一个在 Go 中自定义排序的示例。



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


