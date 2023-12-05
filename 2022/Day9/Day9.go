package Day9

import (
	"AdventOfCode/Utils"
	"fmt"
	"math"
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
	moves := map[Direction9]int{UP: 1, DOWN: -1, RIGHT: 1, LEFT: -1}
	knots := make(map[int][]Coordinate)
	for i:=0; i<10; i++ {
		knots[i] = []Coordinate{{X:0, Y:0}}
	}
	lines := Utils.GetLines(fileName, 9)
	directions := parseDirections(lines)
	for _, d := range directions {
		for i:=0; i<d.moveUnits; i++ {
			h := knots[0][len(knots[0])-1]
			hx := h.X
			hy := h.Y
			if (d.direction == RIGHT || d.direction == LEFT) {
				hx += moves[d.direction]
			} else if (d.direction == UP || d.direction == DOWN) {
				hy += moves[d.direction]
			}
			knots[0] = append(knots[0], Coordinate{X:hx, Y:hy})
			for k:=1; k<10; k++ {
				th := knots[k][len(knots[k])-1]
				t := knots[k-1][len(knots[k-1])-1]
				tCord := part2Calculation(float64(t.X), float64(t.Y), float64(th.X), float64(th.Y))
				knots[k] = append(knots[k], tCord)
			}
		}
	}
	k9 := removeDuplicates(knots[9])
	return len(k9)
}

func part2Calculation(p1x float64, p1y float64, p2x float64, p2y float64) Coordinate {
	distance := math.Abs(p1x - p2x) + math.Abs(p1y - p2y)
	if (p1x == p2x && distance >= 2) {
		if (p1y > p2y) {
			return Coordinate{X: int(p2x), Y: int(p1y - 1)}
		}
		return Coordinate{X: int(p2x), Y: int(p1y + 1)}
	}
	if (p1y == p2y && distance >= 2) {
		if (p1x > p2x) {
			return Coordinate{X: int(p1x - 1), Y: int(p2y)}
		}
		return Coordinate{X: int(p1x + 1), Y: int(p2y)}
	}
	if (distance > 2) {
		if (p1x > p2x) {
			if (p1y > p2y) {
				return Coordinate{X: int(p2x + 1), Y: int(p2y + 1)}
			}
			return Coordinate{X: int(p2x + 1), Y: int(p2y - 1)}
		}
		if (p1x < p2x) {
			if (p1y > p2y) {
				return Coordinate{X: int(p2x - 1), Y: int(p2y + 1)}
			}
			return Coordinate{X: int(p2x - 1), Y: int(p2y - 1)}
		}
	}
	return Coordinate{X: int(p2x), Y: int(p2y)}
}