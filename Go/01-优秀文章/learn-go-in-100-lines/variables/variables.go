package main

import "fmt"

/*声明单个变量*/

var a int

/*声明一组变量*/

// var (
// 	b bool
// 	c float32
// 	d string
// )

// func main() {
// 	a = 42            // 单个变量赋值
// 	b, c = true, 32.0 // 多个变量赋值
// 	d = "string"      // 字符串必须包含双引号
// 	fmt.Println(a, b, c, d) // 42 true 32 string
// }

// 重构后的版本，短变量声明使代码更加简洁

func main() {
	a := 42
	b, c := true, 32.0
	d := "string"
	fmt.Println(a, b, c, d)
}