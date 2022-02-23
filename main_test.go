package main

import "testing"

func TestMain(t *testing.T) {
	response := `{"code": 1, "msg": "success", "data": "hello"}`
	b := []byte(response)
	res := parseJSON(b)
	if res != "success" {
		t.Errorf("Not correct")
	}
}
