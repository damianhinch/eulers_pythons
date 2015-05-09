package main

import "fmt"

func main() {
	sum := 0
	upperBound := 1000
	lowerBound := 0
	for i := lowerBound; i < upperBound; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	fmt.Println("Answer:", sum)
}
