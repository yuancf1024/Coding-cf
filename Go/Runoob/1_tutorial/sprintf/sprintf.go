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