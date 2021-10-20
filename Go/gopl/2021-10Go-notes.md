# 2021-10Go-notes

[toc]

# 学习记录

# ch1-入门

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

## 1.2 命令行参数

