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

`&` 前缀生成一个结构体指针。

使用`.`来访问结构体字段。

也可以对结构体指针使用`.` - 指针会被自动解引用。

结构体是*可变(mutable)的*.

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

	fmt.Println(&person{name: "Ann", age: 40})

	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	sp := &s
	fmt.Println(sp.age)

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


