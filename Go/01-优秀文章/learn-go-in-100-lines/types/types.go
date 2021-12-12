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