package Day9

import (
	"AdventOfCode/Utils"
	"fmt"
	"strings"
)

func Part1(fileName string) int {
	var visitedHead []Coordinate
	var visitedTail []Coordinate
	mostRecentCordHead := Coordinate{0,0}
	mostRecentCordTail := Coordinate{0,0}
	visitedHead = append(visitedHead, mostRecentCordHead) 
	lines := Utils.GetLines(fileName, 9)
	directions := parseDirections(lines)
	fmt.Println(directions)
	for _, d := range directions {
		moreCordsHead, moreCordsTail := d.Execute(mostRecentCordHead, mostRecentCordTail)
		
		visitedHead = append(visitedHead, moreCordsHead...)
		mostRecentCordHead = moreCordsHead[len(moreCordsHead)-1]
		
		visitedTail = append(visitedTail, moreCordsTail...)
		mostRecentCordTail = moreCordsTail[len(moreCordsTail)-1]

	}
	visitedTail = removeDuplicates(visitedTail)

	return len(visitedTail)
}

func parseDirections(lines []string) []Day9Instruction {
	var dirs []Day9Instruction
	for _, line := range lines {
		dirs = append(dirs, parseDirection(line))
	}
	return dirs
}

func parseDirection(line string) Day9Instruction {
	d := strings.Split(line, " ")
	dir, err := CreateDay9Instruction(d[0], d[1])
	if (err != nil) {
		fmt.Println(err)
	}
	return dir
}

func removeDuplicates(cords []Coordinate) []Coordinate {
	keys := make(map[Coordinate]bool)
	ret := []Coordinate{}

	for _, c := range cords {
		if _, hasVal := keys[c]; !hasVal {
			keys[c] = true
			ret = append(ret, c)
		}
	}
	return ret
}
func Part2(fileName string) int {
	return 0
}