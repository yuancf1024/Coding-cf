# 2021-10Go-notes

[toc]

# 学习记录

- [] 2021-11-06


# 命令行安装插件

```shelll
go install golang.org/x/lint/golint@latest
```

## golint报错信息

```shell
PS C:\Users\chenfengyuan\go> go get golang.org/x/lint/golint
go: downloading golang.org/x/lint v0.0.0-20210508222113-6edffad5e616
go: downloading golang.org/x/tools v0.0.0-20200130002326-2f3ba24bd6e7
go get: installing executables with 'go get' in module mode is deprecated.
        Use 'go install pkg@version' instead.
        For more information, see https://golang.org/doc/go-get-install-deprecation
        or run 'go help get' or 'go help install'.
PS C:\Users\chenfengyuan\go> go install golang.org/x/lint/golint
go install: version is required when current directory is not in a module
        Try 'go install golang.org/x/lint/golint@latest' to install the latest version      
PS C:\Users\chenfengyuan\go> go install golang.org/x/lint/golint@latest
```


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

