package main

import "fmt"
import "math"

const PI = 3.14

func main() {
	fmt.Println(PI)
	intyPI := int32(math.Ceil(PI)) // Runden ist subjektiv
	fmt.Println(intyPI)
}
