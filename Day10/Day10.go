package Day10

import (
	"AdventOfCode/Utils"
	"fmt"
	"strconv"
	"strings"
)

func Part1(inputfile string) int{
	lines := Utils.GetLines(inputfile, 10)
	statements := ParseStatements(lines)
	ticks := 0
	registerx := 1
	signalStrength := 0
	tickIt := func() {
		ticks++
		if (ticks == 20 || ticks == 60 || ticks == 100 || ticks == 140 || ticks == 180 || ticks == 220) {
			fubar := calculateSignalStrength(registerx, ticks)
			fmt.Println(fubar)
			signalStrength = signalStrength + fubar
		}
	}
	for _, statement := range statements {
		tickIt()
		if (statement.ins == ADDX) {
			tickIt()
			registerx += statement.x
		}
	}
	return signalStrength
}

func calculateSignalStrength(regx int, ticks int) int {
	return ticks * regx
}

func Part2(inputfile string) string {
	lines := Utils.GetLines(inputfile, 10)
	finalString := strings.Builder{}
	ticks := 1
	registerx := 1
	var line string
	const screenWidthInPixels = 40
	for len(lines) > 0 {
		pixel := (ticks - 1) % screenWidthInPixels
		if pixel == 0 {
			finalString.WriteString("\n")
		}
		if pixel-1 <= registerx && registerx <= pixel+1 {
			finalString.WriteString("#")
		} else {
			finalString.WriteString(" ")
		}

		if len(line) == 0 {
			line = lines[0]
			if line == "noop" {
				lines = lines[1:]
				line = ""
			}
			ticks++
		} else {
			splitLine := strings.Split(line, " ")
			num, _ := strconv.Atoi(splitLine[1])
			registerx += num
			lines = lines[1:]
			line = ""
			ticks++
		}
	}
	return finalString.String()
}