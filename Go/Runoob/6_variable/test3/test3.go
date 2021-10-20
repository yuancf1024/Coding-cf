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