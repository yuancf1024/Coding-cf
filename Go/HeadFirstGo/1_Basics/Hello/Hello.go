package main // 表示文件中的所有其余代码都属于"main"包

import "fmt"  // 使用"fmt"包中的文本格式代码

func main() { // 程序运行时，首先运行ta
	fmt.Println("Hello, Go!") // 从"fmt"包调用"Println"函数来实现
}