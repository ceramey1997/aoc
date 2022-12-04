package Day1

import (
	"AdventOfCode/Utils"
	"fmt"
	"strconv"
)

func Part1() int {
	fileScanner := Utils.CreateScanner("input.txt", 1)
	elfTotal := 0
	position := 0
	var allElfs []ElfDay1
	for fileScanner.Scan() {
		text := fileScanner.Text()
		if (text == "") {
			allElfs = append(allElfs, ElfDay1{
				position: position,
				total: elfTotal,
			})
			elfTotal = 0
		} else {
			cal, err := strconv.Atoi(text)
			if (err != nil) {
				fmt.Printf("error: %x -- line coudl not be processed into int %x", err, text)
			}
			elfTotal += cal
		}
	}
	highestTotal := 0
	for _, elfy := range allElfs {
		if (elfy.total > highestTotal) {
			highestTotal = elfy.total
		}
	}
	return highestTotal
}
