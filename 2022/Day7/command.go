package Day7

import (
	"errors"
	"strings"
)
type Action string
const (
	LS Action = "ls"
	CD Action = "cd"
)

type Command struct {
	Command Action
	Location string
	AssociatedLines []string
}

func CreateCommand(line string) (Command, error) {
	if (strings.Split(line, "")[0] != "$") {
		return Command{}, errors.New("Error: Instruction does not start with $. It's probably not an instruction")
	}
	line = strings.ReplaceAll(line, "$", "")
	line = strings.TrimSpace(line)
	ins := strings.Split(line, " ")

	var location string
	command := getAction(ins[0])
	if (len(ins) == 1) {
		// instruction is ls
		location = ""
	} else if (len(ins) == 2) {
		location =ins[1]
	}
	return Command{ command, location, []string{} }, nil
}

func getAction(s string) Action {
	if (s == "ls") {
		return LS
	}
	return CD
}