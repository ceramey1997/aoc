package Day6

import (
	"AdventOfCode/Utils"
	"errors"
	"fmt"
	"strings"
)

func Part1() int {
	lines := Utils.GetLines("input.txt", 6)
	chars := strings.Split(lines[0], "")
	startingPosition, err :=  findUniquePart1(chars)
	if (err != nil) {
		fmt.Println(err)
	}
	return startingPosition + 4
}

func Part2() int {
	lines := Utils.GetLines("input.txt", 6)
	chars := strings.Split(lines[0], "")
	startingPosition, err :=  findUniquePart2(chars)
	if (err != nil) {
		fmt.Println(err)
	}
	return startingPosition + 14
}

func findUniquePart2(chars []string) (int, error) {
	var uniqueList []string
	for i:=0; i<len(chars); i++ {
		if (i + 13 > len(chars) -1) {
			break
		}
		for j:=i;j<i+14;j++ {
			uniqueList = append(uniqueList, chars[j])
		}
		isUnique := unique(uniqueList)
		if (isUnique == true) {
			return i, nil
		}
		uniqueList = []string{}
	}
	return 0, errors.New("bad never found unique")
}
func findUniquePart1(chars []string) (int, error){
	var uniqueList []string
	for i:=0; i<len(chars); i++ {
		if (i + 3 > len(chars) -1) {
			break
		}
		for j:=i;j<i+4;j++ {
			uniqueList = append(uniqueList, chars[j])
		}
		isUnique := unique(uniqueList)
		if (isUnique == true) {
			return i, nil
		}
		uniqueList = []string{}
	}
	return 0, errors.New("bad never found unique")
}

func unique(chars []string) bool {
	for i:=0; i<len(chars); i++ {
		for j:=i+1; j<len(chars); j++ {
			if (chars[i] == chars[j]) {
				return false
			}
		}
	}
	return true
}