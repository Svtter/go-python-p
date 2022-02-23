// 如果需要运行本测试，将 main.c 移动到其他的目录下面
package main

import "testing"

func TestParseJSON(t *testing.T) {
	response := `{"code": 1, "msg": "success", "data": "hello"}`
	res := parseJSON(response)
	if res != "success" {
		t.Errorf("Not correct")
	}
}
