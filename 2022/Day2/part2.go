/*
A for Rock Opponent             X for lose
B for Paper Opponent            Y for draw
C for Scissors Opponent         Z for win
score:
  - 1 for rock
  - 2 for paper
  - 3 for scissors
  - 0 for loss
  - 3 for draw
  - 6 for win
*/
package Day2

import (
	"AdventOfCode/Utils"
	"bufio"
	"errors"
	"fmt"
	"strings"
)

 func Part2() int {
	reader := Utils.CreateScanner("input.txt", 2)
	reader.Split(bufio.ScanLines)
	totalScore := 0
	for reader.Scan() {
		text := reader.Text()
		plays := strings.Split(text, " ")
		opponentPlay, errOpp := getPlayFromChar(plays[0])
		outcome, errYou := getOutcomeFromChar(plays[1])
		if (errOpp != nil) {
			fmt.Println(errOpp)
		}
		if (errYou != nil) {
			fmt.Println(errYou)
		}
		yourPlay := getYourPlay(opponentPlay, outcome)
		totalScore += roundScore(opponentPlay, yourPlay)
	}
	return totalScore
}

func getOutcomeFromChar(char string) (Outcome, error) {
	switch char {
	case "X":
		return LOSEo, nil
	case "Y":
		return DRAWo, nil
	case "Z":
		return WINo, nil
	default:
		return DEFAULTo, errors.New("outcome given is not accepted")
	}
}

func getYourPlay(opponentPlay Play, outcome Outcome) Play {
	winCon := map[Play]Play { ROCKs: SCISSORSs, PAPERs: ROCKs, SCISSORSs: PAPERs }
	loseCon := map[Play]Play { ROCKs: PAPERs, PAPERs: SCISSORSs, SCISSORSs: ROCKs }
	var yourPlay Play
	if (outcome == DRAWo) {
		yourPlay = opponentPlay
	} else if (outcome == WINo) {
		yourPlay = loseCon[opponentPlay]
	} else if (outcome == LOSEo) {
		yourPlay = winCon[opponentPlay]
	}
	return yourPlay
}