package Day4

import (
	"AdventOfCode/Utils"
	"errors"
	"fmt"
	"strconv"
	"strings"
)

func Part1() int {
	lines := Utils.GetLines("input.txt", 4)
	totalOverlapPairs := 0
	for _, pair := range lines {
		if(parseAssignment(pair, 1)) {
			totalOverlapPairs += 1
		}
	}
	return totalOverlapPairs
}

func Part2() int {
	lines := Utils.GetLines("input.txt", 4)
	totalOverlapPairs := 0
	for _, pair := range lines {
		if(parseAssignment(pair, 2)) {
			totalOverlapPairs += 1
		}
	}
	return totalOverlapPairs
}

func parseAssignment(pair string, part int) bool {
	firstAssignment, secondAssignment := getAssignments(pair)
	expandedFirst, errFirst := expandAssignment(firstAssignment)
	expandedSecond, errSecond := expandAssignment(secondAssignment)
	if (errFirst != nil) {
		fmt.Println("error first")
	}
	if (errSecond != nil) {
		fmt.Println("error second")
	}
	if (part == 1) {
		if (doesFullyContain(expandedFirst, expandedSecond)) {
			return true
		}
	} else {
		if (doesContain(expandedFirst, expandedSecond)) {
			return true
		}
	}
	
	return false

	
}

func getAssignments(pair string) (string, string) {
	assignments := strings.Split(pair, ",")
	firstAssignment := strings.TrimSpace(assignments[0])
	secondAssignment := strings.TrimSpace(assignments[1])
	return firstAssignment, secondAssignment
}

func expandAssignment(assignment string) ([]int, error) {
	startEnd := strings.Split(assignment, "-")
	start, errStart := strconv.Atoi(startEnd[0])
	var rng []int
	end, errEnd := strconv.Atoi(startEnd[1])
	if (errStart != nil) {
		return make([]int, 0), errors.New(fmt.Sprint("Parsing start failed: %s", errStart.Error()))
	}
	if (errEnd != nil) {
		return make([]int, 0), errors.New(fmt.Sprint("Parsing end failed: %s", errEnd.Error()))
	}
	for i := start; i<=end; i++ {
		rng = append(rng, i)
	}
	return rng, nil
}

func getLongestThenShortest(first []int, second []int) ([]int, []int) {
	var rng []int
	var other []int
	if (len(first) > len(second)) {
		rng = first
		other = second
	} else {
		rng = second
		other = first
	}
	return rng, other
}

func doesFullyContain(first []int, second []int) bool {
	rng, other := getLongestThenShortest(first, second)
	if (Utils.Contains(rng, other[0])) {
		if (Utils.Contains(rng, other[len(other)-1])) {
			return true
		}
	}
	return false
}

func doesContain(first []int, second []int) bool {
	rng, other := getLongestThenShortest(first, second)
	for _, num := range rng {
		if (Utils.Contains(other, num)) {
			return true
		}
	}
	return false
}