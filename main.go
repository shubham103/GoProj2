package main

import (
	"fmt"
	"time"
)

func main() {
	ticker := time.Tick(time.Second)
	
	fmt.Printf("Collecting pods info")
	for i := 1; i <= 10; i++ {
		<-ticker
        fmt.Printf("\rContainer status :  %d/10", i) // escape sequence is different in this environment
	}
	fmt.Println("\nAll pods up and running...")
}
