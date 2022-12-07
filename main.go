package main

import (
	"AdventOfCode/Day1"
	"AdventOfCode/Day2"
	"AdventOfCode/Day3"
	"AdventOfCode/Day4"
	"AdventOfCode/Day5"
	"AdventOfCode/Day6"
	"flag"
	"fmt"
	"strconv"
)
func main() {
	var adventDay int

	flag.IntVar(&adventDay, "day", 0, "Day to run")
	flag.Parse()
	switch adventDay {
	case 1:
		part1 := Day1.Part1()
		part2 := Day1.Part2()
		fmt.Println(formatResult(adventDay, part1, part2))
	case 2:
		part1 := Day2.Part1()
		part2 := Day2.Part2()
		fmt.Println(formatResult(adventDay, part1, part2))
	case 3:
		part1 := Day3.Part1()
		part2 := Day3.Part2()
		fmt.Println(formatResult(adventDay, part1, part2))
	case 4:
		part1 := Day4.Part1()
		part2 := Day4.Part2()
		fmt.Println(formatResult(adventDay, part1, part2))
	case 5:
		part1 := Day5.Part1("input.txt")
		part2 := Day5.Part2("input.txt")
		fmt.Println(formatStringResult(adventDay, part1, part2))
	case 6:
		part1 := Day6.Part1()
		part2 := Day6.Part2()
		fmt.Println(formatResult(adventDay, part1, part2))
	default:
		fmt.Println("Please Provide a Day")
	}


}

func formatResult(day int, part1 int, part2 int) string {
	return fmt.Sprintf(
		"Day %s:\n    Part 1: %s\n    Part 2: %s",
		strconv.Itoa(day),
		strconv.Itoa(part1),
		strconv.Itoa(part2),
	)
}

func formatStringResult(day int, part1 string, part2 string) string {
	return fmt.Sprintf(
		"Day %s:\n    Part 1: %s\n    Part 2: %s",
		strconv.Itoa(day),
		part1,
		part2,
	)
}