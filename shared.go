package main

import "C"
import (
	"encoding/json"
	"fmt"
	"sync"
)

var mtx sync.Mutex

//export add
func add(a, b int) int {
	return a + b
}

//export append_str
func append_str(a, b *C.char) *C.char {
	merge := C.GoString(a) + C.GoString(b)
	return C.CString(merge)
}

type Response struct {
	Code int    `json:"code"`
	Msg  string `json:"msg"`
	Data string `json:"data"`
}

//export parseJSON
func parseJSON(a []byte) string {
	var r Response
	if err := json.Unmarshal(a, &r); err != nil {
		fmt.Printf("meet error: %s\n", err.Error())
	}
	return r.Msg
}

// go build -buildmode=c-shared -o demo.so shared.go
func main() {
}
