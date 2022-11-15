package main
import "fmt"
import "unsafe"

func main() {
	var b int
	fmt.Println(unsafe.Sizeof(b))
}
