package main
import ("fmt")

func main() {

    type Person struct {
        username string
        passwd string
    }

    arr2 := map[string]string {"Dieter": "Hildegard", "admin": "admin", "testuser": "Test123", "Niklas": "Schmitz", "hewwo": "bwybwy"}

    username := fmt.Scanln("Name: ")
    password := fmt.Scanln("Password:")

    for i, x := range arr2 {
        if user == x["username"] && password == x["password"] {
            fmt.Println("willkommen, Meister!")
        }
        else {
            fmt.Println("Nnnnnnnö!")
        }
    }

}
