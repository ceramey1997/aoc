package Day3

import (
	"AdventOfCode/Utils"
	"strings"
)

func Part2() int {
	input := ReadByLine("input.txt")
	groups := make([][]string, len(input)/3)
	k := 0
	for i := 0; i < len(input)/3; i++ {
		groups[i] = make([]string, 3)
		for j := 0; j < 3; j++ {
			groups[i][j] = input[k]
			k++
		}
	}

	sum := 0
	for i := 0; i < len(input)/3; i++ {
		for j := 0; j < len(groups[i][0]); j++ {
			if strings.Contains(groups[i][1], string(groups[i][0][j])) && strings.Contains(groups[i][2], string(groups[i][0][j])) {
				sum += priorities[string(groups[i][0][j])]
				break
			}
		}
	}
	return sum
}

func ReadByLine(filename string) []string {
	lines := []string{}
	scanner := Utils.CreateScanner(filename, 3)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

var priorities = map[string]int{
	"a": 1,
	"b": 2,
	"c": 3,
	"d": 4,
	"e": 5,
	"f": 6,
	"g": 7,
	"h": 8,
	"i": 9,
	"j": 10,
	"k": 11,
	"l": 12,
	"m": 13,
	"n": 14,
	"o": 15,
	"p": 16,
	"q": 17,
	"r": 18,
	"s": 19,
	"t": 20,
	"u": 21,
	"v": 22,
	"w": 23,
	"x": 24,
	"y": 25,
	"z": 26,

	"A": 27,
	"B": 28,
	"C": 29,
	"D": 30,
	"E": 31,
	"F": 32,
	"G": 33,
	"H": 34,
	"I": 35,
	"J": 36,
	"K": 37,
	"L": 38,
	"M": 39,
	"N": 40,
	"O": 41,
	"P": 42,
	"Q": 43,
	"R": 44,
	"S": 45,
	"T": 46,
	"U": 47,
	"V": 48,
	"W": 49,
	"X": 50,
	"Y": 51,
	"Z": 52,
}