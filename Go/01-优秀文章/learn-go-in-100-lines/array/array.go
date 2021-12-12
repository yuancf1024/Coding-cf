package main

import "fmt"

func main() {
	// 定义一个大小为4的数组，存储可部署的选项
	var DeploymentOptions = [4]string{"R-pi", "AWS", "GCP", "Azure"}

	// 循环遍历可部署选项数组
	for i := 0; i < len(DeploymentOptions); i++ {
		option := DeploymentOptions[i]
		fmt.Println(i, option)
	}
}