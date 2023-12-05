package Day2

import (
	"bufio"
	"errors"
	"fmt"
	"os"
)

func getPlayFromChar(char string) (Play, error) {
	switch char {
	case "A":
		return ROCKs, nil
	case "B":
		return PAPERs, nil
	case "C":
		return SCISSORSs, nil
	case "X":
		return ROCKs, nil
	case "Y":
		return PAPERs, nil
	case "Z":
		return SCISSORSs, nil
	default:
		return DEFAULTs, errors.New("play is not of the correct expected types")
	}
}

func createReader(filename string) *bufio.Scanner {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Print(err)
	}
	return bufio.NewScanner(file)
}

func roundScore(opponentPlay Play, yourPlay Play) int {
	winCon := map[Play]Play { ROCKs: SCISSORSs, PAPERs: ROCKs, SCISSORSs: PAPERs }
	loseCon := map[Play]Play { ROCKs: PAPERs, PAPERs: SCISSORSs, SCISSORSs: ROCKs }
	roundPoints := 0
	if (winCon[yourPlay] == opponentPlay) {
		roundPoints += int(WIN)
	} else if (loseCon[yourPlay] == opponentPlay) {
		roundPoints += int(LOSS)
	} else {
		roundPoints += int(DRAW)
	}

	switch yourPlay {
	case ROCKs:
		roundPoints += int(ROCK)
	case PAPERs:
		roundPoints += int(PAPER)
	case SCISSORSs:
		roundPoints += int(SCISSORS)
	}
	return roundPoints
}