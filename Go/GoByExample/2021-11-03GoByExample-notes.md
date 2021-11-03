# 2021-11-03GoByExample-notes

[toc]

## 更新记录

- [ ] 2021-11-03 
- [ ] 

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

