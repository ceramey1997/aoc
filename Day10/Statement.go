package Day10

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

type Instruction10 string
const (
	ADDX Instruction10 = "addx"
	NOOP Instruction10 = "noop"
)

type Statement struct {
	ins Instruction10
	x int
}

func ParseStatements(lines []string) []Statement {
	var statements []Statement
	var err error
	for _, line := range lines {
		splitLine := strings.Split(line, " ")
		instruction, _ := GetInstruction(splitLine[0])
		num := 0
		if (instruction == ADDX) {
			num, err = strconv.Atoi(splitLine[1])
			if (err != nil) {
				fmt.Println(err)
			}
		}
		statements = append(statements, Statement{ins: instruction, x: num})
	}
	return statements
}

func GetInstruction(ins string) (Instruction10, error) {
	switch ins {
	case "addx":
		return ADDX, nil
	case "noop":
		return NOOP, nil
	default:
		return ADDX, errors.New("bad instruction given")
	}
}