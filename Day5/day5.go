package Day5

import (
	"AdventOfCode/Utils"
	"fmt"
	"strconv"
	"strings"
)

type Instruction struct {
	numToMove int
	fromCol int
	toCol int
}
func Part1(inputfile string) string{
	stacks, endShipRow := getShip(inputfile)

	instructionScanner := Utils.CreateScanner(inputfile, 5)
	idx := 0
	for instructionScanner.Scan() {
		idx++
		if (idx <= endShipRow) {
			continue
		}
		text := instructionScanner.Text()
		instruction, err := parseInstruction(text)
		if (err != nil) {
			fmt.Println(err)
		}
		stacks = executeInstuction(instruction, stacks)
	}
	return TopCrates(stacks)
}

func Part2(inputfile string) string{
	stacks, endShipRow := getShip(inputfile)

	instructionScanner := Utils.CreateScanner(inputfile, 5)
	idx := 0
	for instructionScanner.Scan() {
		idx++
		if (idx <= endShipRow) {
			continue
		}
		text := instructionScanner.Text()
		instruction, err := parseInstruction(text)
		if (err != nil) {
			fmt.Println(err)
		}
		stacks = executePart2Instruction(instruction, stacks)
	}
	return TopCrates(stacks)
}

func positionallyAlign(lines []string) []map[int]string {
	var maps []map[int]string
	for _, line := range lines {
		maps = append(maps, alignRow(strings.Split(line, "")))
	}
	return maps
}

func alignRow(line []string) map[int]string {
	m := make(map[int]string)
	j := 1
	for i:=1; i < len(line); i+=4 {
		char := strings.ReplaceAll(line[i], "[", "")
		char = strings.ReplaceAll(char, "]", "")
		m[j] = char
		j++
	}
	return m
}

func createStacks(mp []map[int]string, countStacks int) []Stack {
	var stackObjs []Stack
	var stacks []map[int]string
	currentStack := make(map[int]string)
	j := 0
	for column:=1; column<=countStacks+1; column++ {
		for row:=0; row<=len(mp)-1; row++ {
			currentStack[row] = mp[row][column]
		}
		j++
		stacks = append(stacks, currentStack)
		currentStack = map[int]string{}
	}
	for idx, stack := range stacks {
		stackObj := NewStack(stack, idx + 1)
		stackObjs = append(stackObjs, stackObj)
	}
	return stackObjs
}

func getShip(inputfile string) ([]Stack, int) {
	var numStacks int
	var lines []string
	idx := 0
	scanner := Utils.CreateScanner(inputfile, 5)
	for scanner.Scan() {
		idx++
		text := scanner.Text()
		if (text == "") {
			break
		}
		numStacks++
		lines = append(lines, text)
	}
	maps := positionallyAlign(lines[:len(lines)-1])
	return createStacks(maps, len(maps)), idx
}

func parseInstruction(instruction string) (Instruction, error) {
	instruction = strings.ReplaceAll(instruction, "move ", "")
	instruction = strings.ReplaceAll(instruction, "from ", "")
	instruction = strings.ReplaceAll(instruction, "to ", "")
	strs := strings.Split(instruction, " ")
	var in Instruction
	for idx, i := range strs {
		tmp, err := strconv.Atoi(i)
		if (err != nil) {
			return Instruction{}, err
		}
		if (idx == 0) {
			in.numToMove = tmp
		} else if (idx == 1) {
			in.fromCol = tmp - 1
		} else if (idx == 2) {
			in.toCol = tmp - 1
		}
	}
	return in, nil
}

func executeInstuction(instruction Instruction, stacks []Stack) []Stack {
	for i:=1; i<= instruction.numToMove; i++ {
		crateToMove := stacks[instruction.fromCol].crates[0]
		//newCrate := NewCrate(crateToMove.char, )
		//crates := removeElement(stacks[instruction.fromCol].crates, 0)
		crates := stacks[instruction.fromCol].crates[1:]
		stacks[instruction.fromCol].crates = crates
		stacks[instruction.toCol].crates = append([]Crate{crateToMove}, stacks[instruction.toCol].crates...)
	}
	return stacks
}

func removeElement[T string | int | Crate](slice []T, s int) []T{
	return append(slice[:s], slice[s+1:]...)
}

func executePart2Instruction(instruction Instruction, stacks []Stack) []Stack {
	var tmpStackToMove []Crate
	for i:=1; i <= instruction.numToMove; i++ {
		crateToMove := stacks[instruction.fromCol].crates[0]
		crates := stacks[instruction.fromCol].crates[1:]
		stacks[instruction.fromCol].crates = crates
		tmpStackToMove = append(tmpStackToMove, crateToMove)
	}
	stacks[instruction.toCol].crates = append(tmpStackToMove, stacks[instruction.toCol].crates...)
	return stacks
}