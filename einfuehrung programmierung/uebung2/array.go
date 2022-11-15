
package main
import ("fmt")

func main() {

    arr2 := []int{4,5,6,7,8, 9, 10, 11, 12, 13}

    for i:=0; i < len(arr2); i++ {
        fmt.Println(arr2[i])
    }

    fmt.Println(arr2[10])
}
