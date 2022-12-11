package main

import (
	"AdventOfCode/Day1"
	"AdventOfCode/Day10"
	"AdventOfCode/Day2"
	"AdventOfCode/Day3"
	"AdventOfCode/Day4"
	"AdventOfCode/Day5"
	"AdventOfCode/Day6"
	"AdventOfCode/Day7"
	"AdventOfCode/Day8"
	"AdventOfCode/Day9"
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
	case 7:
		part1 := Day7.Part1("input.txt")
		part2 := Day7.Part2("input.txt")
		fmt.Println(formatResult(adventDay, part1, part2))
	case 8:
		part1, part2 := Day8.Parts("input.txt")
		fmt.Println(formatResult(adventDay, part1, part2))
	case 9:
		part1 := Day9.Part1("input.txt")
		part2 := Day9.Part2("input.txt")
		fmt.Println(formatResult(adventDay, part1, part2))
	case 10:
		part1 := Day10.Part1("input.txt")
		part2 := Day10.Part2("input.txt")
		fmt.Println(formatIntAndString(adventDay, part1, part2))
	default:
		fmt.Println("Please Provide a Day")
	}
}

func formatResult[T int | int64, V int | int64](day int, part1 T, part2 V) string {
	return fmt.Sprintf(
		"Day %v:\n    Part 1: %v\n    Part 2: %v",
		day,
		part1,
		part2,
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

func formatIntAndString(day int, part1 int, part2 string) string {
	return fmt.Sprintf(
		"Day %s:\n    Part 1: %v\n    Part 2: %s",
		strconv.Itoa(day),
		part1,
		part2,
	)
}