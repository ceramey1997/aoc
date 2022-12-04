package Day1

import (
	"AdventOfCode/Utils"
	"bufio"
	"fmt"
	"sort"
	"strconv"
)

func Part2() int {
	highestTotals := getAnswer("input.txt")
	highestTotal := 0
	for _, num := range highestTotals {
		highestTotal += num
	}
	return highestTotal
}

func getAnswer(filename string) []int {
	fileScanner := Utils.CreateScanner("input.txt", 1)
	fileScanner.Split(bufio.ScanLines)
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
	sort.Slice(allElfs, func(i, j int) bool {
		return allElfs[i].total > allElfs[j].total
	})
	return []int { allElfs[0].total, allElfs[1].total, allElfs[2].total }
}